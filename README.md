# # Project Tapper (PC & Mobile Automation PoC)


[Switch to English Version](#english) / [日本語版はこちら](#japanese)



👉 Portfolio Documents📄 [Project Portfolio PDF](docs/project-tapper-portfolio.pdf)



🖼️ [Detection Result Sample](assets/detection_result.png)


## Detection Example

![Detection Result](assets/detection_result.png)

## 📖 Project Tapper (PC & Mobile Automation PoC) - 日本語

## Overview
OpenCVによる画像認識と、人間の操作リズムのゆらぎを組み合わせ、環境変化に強いUI自動化の仕組みを検証したプロジェクトです。

##  動作デモ（UI検知結果）
プログラムを実行すると、画面内のターゲット（赤いハート）を正確にロックオンし、緑色の枠線で視覚化します。

![UI Detection Result](detection_result.png)

##  本プロジェクトの原点（開発の動機と研究背景）

私のエンジニアリングとしての原点は、**「Pythonを用いたPyAutoGUIによる、ターゲットの自動クリック技術への興味」**から始まりました。

当時は完全なプログラミング初心者であり、環境構築の壁や変数の概念といった基礎的な部分からすべて**独学**でスタートしました。エラーに直面するたびに公式ドキュメントやログを読み解き、自力で解決する中で「自走力」の基盤を養いました。

この独学での経験を通じて「自らの手でシステムを構築するおもしろさと可能性」に強く突き動かされ、技術をより体系的に学ぶため、大学では「ICT副専攻」のカリキュラムを全課程修了。さらに、国が認定する数理・データサイエンス・AI教育プログラムである「MDASH」の資格も取得しました。

###  精神医学研究とエンジニアリングの融合（学際的アプローチ）
私は現在、東海大学健康学部において、**精神科医の指導教授のもと、「睡眠の質と幸福度の関係性」についての研究**を行っています。この学術研究における大規模なデータ統計・分析の現場においても、自身でPythonを活用したデータサイエンスを実践してきました。

この研究の中で、私は一つの重要な仮説を立てました。
> 「人間が一定の機械的なリズムや、絶対的な中心座標への正確すぎる入力を強制されるとき、そこには認知的な不調和と精神的ストレス（負荷）が生じる。これはシステム自動化においても同様であり、機械的すぎる一定の挙動は、対象システムに不自然な歪み（エラーや検知リスク）を生むのではないか」

本プロジェクト（Project Tapper）は、私の原点である「PyAutoGUIによる自動化技術」に対し、この**「精神医学・ウェルネス研究の知見」**と、副専攻・MDASHで培った**「データ駆動型アプローチ（1/fゆらぎアルゴリズム等による制御）」**を融合させた、私にしか構築できない集大成（学際的PoC）として開発されました。

##  概要
本プロジェクトは、従来の「座標固定」「機械的一定周期」の自動化が抱える課題（解像度変更によるズレ、単調リズムによるシステムエラー）を解決するための検証コードです。
実業務や特定製品のコードは一切含まれておらず、ポートフォリオ用の汎用的なロジックのみを実装しています。

## 主な機能と技術的アプローチ
- **堅牢なUI検知（OpenCV / NumPy）**: 画面全体のテンプレートマッチングにより、ボタンの形状や色を正確に検出。
- **人間的なリズムゆらぎ**: 実験データに基づいた「ランダムな時間ゆらぎ（±0.2秒）」と「座標の微小なゆらぎ」を再現。
- **堅牢なエラーハンドリング**: 対象が見つからない場合の再試行（リトライ）ロジックを搭載。
- **環境シミュレーション（低バッテリーモード）**: デバイスの高負荷や低電圧時に発生する「フレーム遅延」や「認識精度の低下」を擬似的に再現し、過酷な環境下でのシステムの堅牢性を検証可能。

##  セットアップと実行方法
外部画像を用意することなく、以下の手順だけで手軽にローカルテストが可能です。

### 1. 依存ライブラリのインストール
```bash
pip install opencv-python numpy pyautogui
```
### 2. テスト用ダミー画像の自動生成 ── 📄 [ソースコードを見る](create_assets.py)

数式を用いたハート描画による、1ビットの狂いもない検証用画像をローカルに生成します。
（コードの詳細は [create_assets.py](create_assets.py) を参照してください）

```bash
python create_assets.py

### 3. 通常デモの実行（自動検知＆ポップアップ表示）
```bash
python ui_tapper_poc.py -t heart_red.png --mock-screen mock_screen.png
```

### 4. 低バッテリー（高負荷環境）のシミュレーション実行
```bash
python ui_tapper_poc.py -t heart_red.png --mock-screen mock_screen.png --sim-low-battery
```

##  動作環境
- Python 3.x
- Windows / macOS / Linux

## 免責事項 (Disclaimer)
本リポジトリは、自動化アルゴリズムの研究および概念実証を目的としたオープンソースコードです。不正なアクセスや規約に違反するスクレイピング等を助長するものではありません。

---

<a id="english"></a>）
## Project Tapper (PC & Mobile Automation PoC) - English

This repository is a Proof of Concept (PoC) for a high-precision UI automation system that combines OpenCV image recognition with human-like behavioral ripples (timing fluctuations).

###  UI Detection Demo
When the program runs, it locks onto the target (red heart) on the screen and visualizes it with a green bounding box.

##  Core Motivation & Research Background

My journey into software engineering began with a simple yet profound curiosity: **"How can I use Python and PyAutoGUI to automate target-based click operations?"**

As a complete beginner at the time, I started entirely through **self-directed learning**, tackling fundamental challenges from configuring development environments to mastering variable concepts. Navigating through errors by analyzing official documentation and debugging logs allowed me to build a strong foundation of self-reliance and autonomous problem-solving from day one.

Driven by the thrill and immense potential of building systems with my own hands, I sought to contextualize this practical experience through structured academic discipline. This led me to complete the entire **Minor in ICT (Information and Communication Technology)** curriculum at my university, alongside earning the **MDASH** certification—a government-approved national program for Mathematics, Data Science, and AI Education.

### 📊 Intersection of Psychiatry Research and Engineering (Interdisciplinary Approach)
Currently, as a student in the School of Wellness Studies at Tokai University, I am a member of a **psychiatry-focused research seminar** supervised by a licensed psychiatrist. My academic research centers on **"The Relationship Between Sleep Quality and Well-being,"** a domain where I have actively applied Python for large-scale statistical data analysis and data science pipelines.

Through this specialized research, I formulated a core hypothesis:
> "When humans are forced to adapt to rigid, mechanical rhythms or highly repetitive, pixel-perfect inputs, it induces cognitive dissonance and psychological stress. This principle translates directly to automated systems; excessively rigid and deterministic automation patterns create artificial friction and unnatural anomalies within the target system, increasing the risk of detection and operational errors."

Project Tapper was born as a proof-of-concept (PoC) to bridge my roots in PyAutoGUI automation with these **insights from psychiatry and wellness studies**, controlled dynamically via the **data-driven approaches (such as the 1/f noise latency algorithm)** acquired through my minor and MDASH studies. It represents a highly unique, interdisciplinary synthesis of domain research and robust engineering that only I could build.

###  Overview
This project validates solutions for common issues in traditional automation, such as resolution mismatches and rigid click intervals. It contains only generic logic built for a portfolio, with no actual business or product code.

### Key Features
- **Robust UI Detection (OpenCV / NumPy)**: Accurately detects buttons via template matching.
- **Human-like Timing Fluctuations**: Simulates natural random delays ($\pm0.2$ seconds) and minor coordinate shifts.
- **Robust Error Handling**: Built-in retry logic when target UIs are missing.
- **Low-Battery Simulation**: Simulates frame drops and reduced accuracy under high device load to test system resilience.

### Setup & Execution
```bash
pip install opencv-python numpy pyautogui
python create_dummy_assets.py
python ui_tapper_poc.py -t heart_red.png --mock-screen mock_screen.png

