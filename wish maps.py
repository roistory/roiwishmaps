import folium
import pandas as pd
from folium.plugins import MarkerCluster  # MarkerCluster 추가
from folium import CustomIcon  # CustomIcon을 추가
from branca.element import Figure

fig = Figure(width=50, height=50)
m = folium.Map(
    location=[37.3525, 126.5943],
    zoom_start=2.5,
)
fig.add_child(m)

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
    
    marker = folium.Marker(
        location=[latitude, longitude],
        popup=location_name,
        icon=custom_icon
    )
    
    marker.add_to(mc)

m.get_root().html.add_child(folium.Element("""
<style>
.folium-popup {
  max-width: 1000px;
}
</style>
"""))

# MarkerCluster를 지도에 추가
mc.add_to(m)  
m
m.save('index.html')