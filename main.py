import sys
import folium
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView

# 地名と地理的位置のマッピング
locations = {
    '新宿区': {'lat': 35.6938, 'lng': 139.7036},
    '渋谷区': {'lat': 35.6620, 'lng': 139.7036},
    # 他の地名と位置もここに追加
}

# 特定の地名の色を変更する関数
def change_color(map, place_name, color):
    if place_name in locations:
        lat_lng = locations[place_name]
        folium.Circle(
            location=[lat_lng['lat'], lat_lng['lng']],
            radius=1000,  # 半径
            color=color,
            fill=True,
            fill_color=color
        ).add_to(map)

# 地図を作成
map_japan = folium.Map(location=[35.6895, 139.6917], zoom_start=10)

# 新宿区を赤色に変更する例
change_color(map_japan, '新宿区', 'red')

# 地図をHTMLファイルとして保存
map_japan.save('map_of_japan.html')

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
