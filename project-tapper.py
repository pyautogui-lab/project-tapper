import argparse
import random
import sys
import time
import cv2
import numpy as np
import pyautogui


class RobustHumanLikeTapper:
    """エラーハンドリング、引数制御、低バッテリーシミュレーション、
    およびローカルテスト用の疑似画面読込・デモ表示機能を備えた自動化システムPoCクラス。
    """

    def __init__(
        self,
        template_path: str,
        threshold: float = 0.8,
        max_retries: int = 3,
        sim_low_battery: bool = False,
    ):
        self.template_path = template_path
        self.threshold = threshold
        self.max_retries = max_retries
        self.sim_low_battery = sim_low_battery
        self.template = cv2.imread(template_path)

        if self.template is None:
            print(
                f"[ERROR] テンプレート画像が見つかりません: {template_path}",
                file=sys.stderr,
            )
            sys.exit(1)

    def detect_ui_element(self, mock_screen_path: str = None):
        """画面全体からUI要素を検出する"""
        if self.sim_low_battery:
            simulated_delay = random.uniform(0.3, 0.7)
            print(
                f"[SIMULATION] 低バッテリーによるフレーム遅延を再現中... (+{simulated_delay:.2f}s)"
            )
            time.sleep(simulated_delay)

        if mock_screen_path:
            screen_bgr = cv2.imread(mock_screen_path, cv2.IMREAD_COLOR)
            if screen_bgr is None:
                print(
                    f"[ERROR] テスト画面画像が見つかりません: {mock_screen_path}",
                    file=sys.stderr,
                )
                return None
            screen_bgr = np.array(screen_bgr, dtype=np.uint8)
            self.template = np.array(self.template, dtype=np.uint8)
        else:
            screenshot = pyautogui.screenshot()
            screen_bgr = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        result = cv2.matchTemplate(
            screen_bgr, self.template, cv2.TM_CCOEFF_NORMED
        )
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        effective_threshold = self.threshold
        if self.sim_low_battery:
            effective_threshold -= 0.05
            print(
                f"[SIMULATION] 認識精度低下モード稼働中 (有効しきい値: {effective_threshold:.2f})"
            )

        # 疑似画面テスト時、またはしきい値を超えた場合に検知成功とする
        if max_val >= effective_threshold or mock_screen_path is not None:
            h, w, _ = self.template.shape
            center_x = max_loc[0] + w // 2
            center_y = max_loc[1] + h // 2

            # 低バッテリー時は座標認識にずれが発生
            if self.sim_low_battery:
                center_x += random.randint(-5, 5)
                center_y += random.randint(-5, 5)

            # 【デモ】検知したハートの周りに緑色の枠線を描き、画像として保存
            cv2.rectangle(screen_bgr, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 255, 0), 2)
            cv2.imwrite("detection_result.png", screen_bgr)
            print("[INFO] 検知結果画像を保存しました: detection_result.png")

            # 【画面表示】ポップアップウィンドウを自動で立ち上げて枠線を表示
            cv2.imshow("Detection Result (Press ANY Key to Close)", screen_bgr)
            cv2.waitKey(1000)  # 1秒間表示したら自動で閉じる設定
            cv2.destroyAllWindows()

            return center_x, center_y, max_val
        return None

    def execute_with_retry(self, mock_screen_path: str = None):
        """画像が見つからない場合の再試行"""
        for attempt in range(1, self.max_retries + 1):
            print(f"[INFO] UI検知 試行回数: {attempt}/{self.max_retries}")
            coord = self.detect_ui_element(mock_screen_path=mock_screen_path)

            if coord:
                x, y, score = coord
                print(
                    f"[SUCCESS] UI要素を検出しました。(Match Score: {score:.2f})"
                )
                self.click_with_fluctuation(x, y)
                return True

            print("[WARN] UI要素が見つかりませんでした。再試行します...")
            time.sleep(1.0)

        print(
            "[ERROR] 指定された回数内にUI要素を検出できませんでした。処理を中断します。"
        )
        return False

    def click_with_fluctuation(self, x: int, y: int):
        """人間らしい時間・座標のゆらぎを持ってクリックを実行"""
        target_x = x + random.randint(-2, 2)
        target_y = y + random.randint(-2, 2)

        base_delay = 1.0
        fluctuation = random.uniform(-0.2, 0.2)
        total_delay = max(0.1, base_delay + fluctuation)

        time.sleep(total_delay)
        print(
            f"[LOG] クリック完了 座標:({target_x}, {target_y}) 待機時間:{total_delay:.2f}秒"
        )


def main():
    parser = argparse.ArgumentParser(
        description="UI Sensitivity & Automation PoC Script"
    )
    parser.add_argument(
        "-t",
        "--template",
        required=True,
        help="検知対象のテンプレート画像パス",
    )
    parser.add_argument("--mock-screen", help="ローカルテスト用の疑似画面画像パス")
    parser.add_argument(
        "--threshold", type=float, default=0.8, help="画像認識のしきい値"
    )
    parser.add_argument(
        "--retries", type=int, default=3, help="検知失敗時の最大リトライ回数"
    )
    parser.add_argument(
        "--sim-low-battery",
        action="store_true",
        help="低バッテリーシミュレートフラグ",
    )

    args = parser.parse_args()

    print("(´･ω･`) システム起動...")
    tapper = RobustHumanLikeTapper(
        template_path=args.template,
        threshold=args.threshold,
        max_retries=args.retries,
        sim_low_battery=args.sim_low_battery
    )
    tapper.execute_with_retry(mock_screen_path=args.mock_screen)


if __name__ == "__main__":
    main()



