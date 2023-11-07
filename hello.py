from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# ユーザのデスクトップのディレクトリを取得
file = "sample.pdf"
file_path = os.path.expanduser("~") + "/Desktop/" + file

# A4の新規PDFファイルを作成
page = canvas.Canvas(file_path, pagesize=portrait(A4))

# フォントの読み込み
pdfmetrics.registerFont(TTFont("HGRGE", "C:/Windows/Fonts/HGRGE.TTC"))
pdfmetrics.registerFont(TTFont("HGRME", "C:/Windows/Fonts/HGRME.TTC"))

# フォントの設定(第1引数：フォント、第2引数：サイズ)
page.setFont("HGRGE", 20)

# 指定座標が左端となるように文字を挿入
page.drawString(200, 300, "Hello World!")

# 指定座標が中心となるように文字を挿入
page.drawCentredString(200, 200, "Hello World!")

# 指定座標が右端となるように文字を挿入
page.drawRightString(200, 100, "Hello World!")

# PDFファイルとして保存
page.save()
