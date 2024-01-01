import sys
import json
import folium
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView

# 全国のGeoJSONファイルの読み込み
with open('N03-21_210101.json', 'r', encoding='utf-8') as file:
    japan_geojson = json.load(file)

# 特定の地域のデータを抽出して地図に適用する関数
def apply_area_boundary(map, prefecture_name, area_name, color):
    area_data = next((feature for feature in japan_geojson['features']
                      if feature['properties']['N03_001'] == prefecture_name and
                         feature['properties']['N03_004'] == area_name), None)
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
def create_map():
    map = folium.Map(location=[35.6895, 139.6917], zoom_start=5, tiles='CartoDB dark_matter')
    # ここで特定の地区を選択して色を適用
    apply_area_boundary(map, '東京都', '港区', 'blue')
    apply_area_boundary(map, '長野県', '長野市', 'red')  # 例: 北海道札幌市中央区
    
    # 他の地区も同様に追加
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
        self.setWindowTitle('複数地区の境界線に色を適用 - ダークテーマ')
        self.show()

# アプリケーションを実行
app = QApplication(sys.argv)
ex = MapApp()
sys.exit(app.exec_())
