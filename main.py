import sys
import json
import folium
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView

# GeoJSONファイルの読み込み
with open('/mnt/data/N03-21_13_210101.json', 'r', encoding='utf-8') as file:
    tokyo_geojson = json.load(file)

# 特定の地域のデータを抽出する関数
def extract_area_data(geojson, area_name):
    return next((feature for feature in geojson['features']
                 if feature['properties']['N03_004'] == area_name), None)

# 地図を生成する関数
def create_map():
    map = folium.Map(location=[35.6895, 139.6917], zoom_start=12, tiles='CartoDB dark_matter')
    
    # 新宿区のデータを抽出して地図に適用
    shinjuku_data = extract_area_data(tokyo_geojson, '新宿区')
    if shinjuku_data:
        folium.GeoJson(
            shinjuku_data,
            style_function=lambda feature: {
                'fillColor': 'red',
                'color': 'red',
                'weight': 2,
                'fillOpacity': 0.5
            }
        ).add_to(map)

    return map._repr_html_()

# アプリケーションウィンドウを作成するクラス
class MapApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        map_view = QWebEngineView()
        map_html = create_map()
        map_view.setHtml(map_html)
        layout.addWidget(map_view)

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('新宿区の境界線に色を適用 - ダークテーマ')
        self.show()

# アプリケーションを実行
app = QApplication(sys.argv)
ex = MapApp()
sys.exit(app.exec_())
