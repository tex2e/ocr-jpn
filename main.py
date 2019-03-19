
import sys
import pyocr
import pyocr.builders

from PIL import Image


# OCRの設定
tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
tool = tools[0]

# 画像から文字を抽出する
def extract_string(filename):
    txt = tool.image_to_string(
        Image.open(filename),
        lang='jpn',
        builder=pyocr.builders.TextBuilder())
    return txt


string = extract_string('img/test2.png')
print(string)
