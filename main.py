import sys
import folium
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView

# 地図を生成する関数
def create_map():
    # 日本の地理的中心の緯度と経度
    latitude = 36.2048
    longitude = 138.2529

    # 地図を作成
    map_japan = folium.Map(location=[latitude, longitude], zoom_start=5)

    # 地図をHTMLデータとして保存
    map_html = map_japan._repr_html_()
    return map_html

# アプリケーションウィンドウを作成するクラス
class MapApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # レイアウトの設定
        layout = QVBoxLayout()
        self.setLayout(layout)

        # 地図を表示するためのWebビュー
        map_view = QWebEngineView()

        # 地図データを取得し、ビューに設定
        map_html = create_map()
        map_view.setHtml(map_html)

        # レイアウトにWebビューを追加
        layout.addWidget(map_view)

        # ウィンドウの設定
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('日本地図')
        self.show()

# アプリケーションを実行
app = QApplication(sys.argv)
ex = MapApp()
sys.exit(app.exec_())
