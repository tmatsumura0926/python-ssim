# pythonのOpenCVでSSIMを測定するツールです

## 動作環境
- python 3.10.6
- OpenCV 4.6

## 使い方
### 画像を比較したい場合
- pyフォルダに比較したい画像（aaa.jpg/bbb.jpg）を格納して以下のコマンドを実施してください
- 画素数が異なる場合はエラーを出します
- 結果はCSVにも格納します

python3 ssim-jpg.py aaa.jpg bbb.jpg

### 動画を比較したい場合
- pyフォルダに比較したい動画（aaa.mp4/bbb.mp4）を格納して以下のコマンドを実施してください
- フレームレートや秒数が異なる場合はエラーを出します
- 結果はCSVにも格納します

python3 ssim-movie.py aaa.mp4 bbb.mp4
