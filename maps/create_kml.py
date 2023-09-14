import pandas as pd
import numpy as np

dataset = "dataset_pisa.csv"
df = pd.read_csv(dataset)

long = df["lon"]
lat = df["lat"]
img = df["link"]
size = len(df)
n_layers = size//2000 + 1
start = '''<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <name>Teste</name>
    <description/>
    <Style id="icon-1899-0288D1-normal">
      <IconStyle>
        <color>ffd18802</color>
        <scale>1</scale>
        <Icon>
          <href>https://www.gstatic.com/mapspro/images/stock/503-wht-blank_maps.png</href>
        </Icon>
        <hotSpot x="32" xunits="pixels" y="64" yunits="insetPixels"/>
      </IconStyle>
      <LabelStyle>
        <scale>0</scale>
      </LabelStyle>
    </Style>
    <Style id="icon-1899-0288D1-highlight">
      <IconStyle>
        <color>ffd18802</color>
        <scale>1</scale>
        <Icon>
          <href>https://www.gstatic.com/mapspro/images/stock/503-wht-blank_maps.png</href>
        </Icon>
        <hotSpot x="32" xunits="pixels" y="64" yunits="insetPixels"/>
      </IconStyle>
      <LabelStyle>
        <scale>1</scale>
      </LabelStyle>
    </Style>
    <StyleMap id="icon-1899-0288D1">
      <Pair>
        <key>normal</key>
        <styleUrl>#icon-1899-0288D1-normal</styleUrl>
      </Pair>
      <Pair>
        <key>highlight</key>
        <styleUrl>#icon-1899-0288D1-highlight</styleUrl>
      </Pair>
    </StyleMap>
    <Folder>
      <name>Layer {}</name>
'''
item ='''      <Placemark>
        <name>Foto {}</name>
        <description><![CDATA[<img src="{}" height="200" width="auto" /><br><br>]]></description>
        <styleUrl>#icon-1899-0288D1</styleUrl>
        <Point>
          <coordinates>
            {},{},0
          </coordinates>
        </Point>
      </Placemark>
'''
end = '''    </Folder>
  </Document>
</kml>

'''
for i in range(n_layers):
    with open(f'KMLs/layer_{i}.kml', 'w') as f:
      f.write(start.format(i))
      # Google My Maps has a limit of 2000 items per layer
      for j in range(2000):
        if i*2000 + j >= size:
          break
        print(f"Layer {i}, item {j}")
        img_n = i*2000 + j
        f.write(item.format(img_n, img[img_n], long[img_n], lat[img_n]))
      f.write(end)