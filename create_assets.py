import cv2
import numpy as np

# ==============================================================================
# Project Tapper - Assets Generator
# 
# 【概要】
# OpenCV画像認識（テンプレートマッチング）の動作検証用スクリプト。
# 数式を用いて描画した赤いハートを含む疑似画面と、それを1ビットの狂いもなく
# 完全型抜きしたテンプレート画像をローカル環境に自動生成します。
# ==============================================================================

def draw_heart(image, center, size, color):
    """NumPy配列上に数式を使って綺麗なハートマークを描画する関数"""
    cx, cy = center
    for y in range(cy - size, cy + size):
        for x in range(cx - size, cx + size):
            # 座標を正規化 (-1.5 から 1.5 の範囲に収める調整)
            nx = (x - cx) / (size * 0.7)
            ny = -(y - cy) / (size * 0.7) - 0.3
            
            # ハートの代数曲線方程式: (x^2 + y^2 - 1)^3 - x^2 * y^3 <= 0
            if (nx**2 + ny**2 - 1)**3 - (nx**2) * (ny**3) <= 0:
                if 0 <= y < image.shape[0] and 0 <= x < image.shape[1]:
                    image[y, x] = color

def create_assets():
    print("(´･ω･`) テスト用ダミー画像をローカルに生成中...")

    # 1. 最初にベースとなる擬似画面（800x600 ピクセル、ライトグレー背景 180）を作成
    mock_screen = np.full((600, 800, 3), 180, dtype=np.uint8)
    
    # 画面上のターゲット位置（400, 300）に赤いハートを配置
    screen_cx, screen_cy = 400, 300
    draw_heart(mock_screen, (screen_cx, screen_cy), 20, (0, 0, 255))
    
    # ノイズとして他の図形やテキストを配置
    cv2.rectangle(mock_screen, (100, 100), (200, 150), (255, 0, 0), -1)
    cv2.putText(mock_screen, "UI Test Screen", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    
    cv2.imwrite("mock_screen.png", mock_screen)
    print("[SUCCESS] 擬似画面画像を保存しました: mock_screen.png")

    # 2. 【重要】疑似画面のハートがある部分（50x50の範囲）をそのまま「型抜き」してテンプレートにする
    # これにより、背景色（180）も含めて1ビットの狂いもなく完全一致させます
    start_y = screen_cy - 25
    start_x = screen_cx - 25
    template = mock_screen[start_y:start_y+50, start_x:start_x+50]
    
    cv2.imwrite("heart_red.png", template)
    print("[SUCCESS] テンプレート画像を完全型抜きで保存しました: heart_red.png")

if __name__ == "__main__":
    create_assets()
