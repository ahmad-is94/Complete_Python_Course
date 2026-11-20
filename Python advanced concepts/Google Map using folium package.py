import folium
from geopy.geocoders import ArcGIS
from geopy.exc import GeocoderServiceError
from pathlib import Path
import webbrowser

geo_locator = ArcGIS(timeout=10)
place_1 = "Yemen"
output_file = Path("Yemen_Map.html")

try:
    location_1 = geo_locator.geocode(place_1)

    if location_1 is None:
        print(f"Location '{place_1}' not found!")
    else:
        coords = [location_1.latitude, location_1.longitude]

        # Use Esri World Street Map (free, no API key required)
        user_map1 = folium.Map(
            location=coords,
            zoom_start=6,
            tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}",
            attr="Tiles © Esri"
        )

        folium.Marker(
            location=coords,
            popup=location_1.address,
            tooltip=place_1,
        ).add_to(user_map1)

        user_map1.save(output_file)
        webbrowser.open(output_file.resolve().as_uri())

except GeocoderServiceError as e:
    print("Geocoding service error:", e)



 #i am using the reverse geocoding to map lahore
import folium
from geopy.geocoders import ArcGIS
from geopy.exc import GeocoderServiceError
from pathlib import Path
import webbrowser

geo_locator = ArcGIS(timeout=10)

# 1. Place change karein
place_1 = "Lahore, Pakistan"

# 2. File ka naam change karein
output_file = Path("Lahore_Map.html")

try:
    location_1 = geo_locator.geocode(place_1)

    if location_1 is None:
        print(f"Location '{place_1}' not found!")
    else:
        coords = [location_1.latitude, location_1.longitude]

        # 3. zoom_start ko 12 karein city view ke liye
        user_map1 = folium.Map(
            location=coords,
            zoom_start=12,
            tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}",
            attr="Tiles © Esri"
        )

        folium.Marker(
            location=coords,
            popup=location_1.address,
            tooltip=place_1,
        ).add_to(user_map1)

        user_map1.save(output_file)
        webbrowser.open(output_file.resolve().as_uri())

except GeocoderServiceError as e:
    print("Geocoding service error:", e)