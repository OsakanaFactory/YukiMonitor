import sys
import json
import folium
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView

# GeoJSONファイルの読み込み
with open('N03-21_13_210101.json', 'r', encoding='utf-8') as file:
    tokyo_geojson = json.load(file)

# 特定の地域のデータを抽出して地図に適用する関数
def apply_area_boundary(map, area_name, color):
    area_data = next((feature for feature in tokyo_geojson['features']
                      if feature['properties']['N03_004'] == area_name), None)
    if area_data:
        folium.GeoJson(
            area_data,
            style_function=lambda feature: {
                'fillColor': color,
                'color': color,
                'weight': 2,
                'fillOpacity': 0.5
            }
        ).add_to(map)

# 地図を生成する関数
def create_map(area_name, color):
    map = folium.Map(location=[35.6895, 139.6917], zoom_start=12, tiles='CartoDB dark_matter')
    apply_area_boundary(map, area_name, color)
    return map._repr_html_()

# アプリケーションウィンドウを作成するクラス
class MapApp(QWidget):
    def __init__(self, area_name, color):
        super().__init__()
        self.area_name = area_name
        self.color = color
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        map_view = QWebEngineView()
        map_html = create_map(self.area_name, self.color)
        map_view.setHtml(map_html)
        layout.addWidget(map_view)

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle(f'{self.area_name}の境界線に色を適用 - ダークテーマ')
        self.show()

# アプリケーションを実行
app = QApplication(sys.argv)
ex = MapApp('港区', 'blue')  # ここで地域名と色を指定
sys.exit(app.exec_())
