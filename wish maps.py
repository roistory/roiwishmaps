import folium
import pandas as pd
from folium.plugins import MarkerCluster
from folium import CustomIcon
from branca.element import Figure

fig = Figure(width=50, height=50)

# 맵 기본값 설정
map_center = [37.3525, 126.5943]
zoom_level = 0.5
min_zoom = 2
initial_zoom = 3

# 맵 설정
m = folium.Map(location=map_center, zoom_start=initial_zoom, min_zoom=min_zoom)
fig.add_child(m)

# CSS 파일을 추가
css_link = '<link rel="stylesheet" href="styles.css">'
m.get_root().html.add_child(folium.Element(css_link))
    
# CSV 읽어 들이는 코드
df = pd.read_csv("wishimapslist.csv")

# MarkerCluster 객체 생성
mc = MarkerCluster()  
for index, row in df.iterrows():
    location_name = row['도시']
    latitude = row['Latitude']
    longitude = row['Longitude']
    icon_path = row['icon']
    
    # 아이콘을 사용하여 마커를 생성
    custom_icon = CustomIcon(
        icon_image=icon_path,
        icon_size=(30, 30)
    )

    # HTML 및 CSS를 포함한 IFrame을 사용하여 Popup에 스타일 적용
    popup_content = f'<div class="popup-text popup-background">{location_name}</div>'
    iframe = folium.IFrame(html=popup_content,
                           width=150, height=50,)
    
    popup = folium.Popup(iframe, max_width=500)
    
    # 마커 생성
    marker = folium.Marker(
        location=[latitude, longitude],
        icon=custom_icon,
        popup=popup
    )
    
    marker.add_to(mc)

# MarkerCluster에 마커들을 추가
mc.add_to(m)

# 맵을 저장
m.save('index.html')