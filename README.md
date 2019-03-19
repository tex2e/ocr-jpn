
# OCRで日本語抽出

```
brew install tesseract
pip install pyocr
```

OCRの日本語の学習データを取ってくる。
正直なところ、日本語読み取り精度はイマイチ。

```
wget https://github.com/tesseract-ocr/tessdata/raw/master/jpn.traineddata
mv jpn.traineddata /usr/local/share/tessdata
```
