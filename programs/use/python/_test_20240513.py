# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-05-13 17:58:14 UTC+8
"""
import geopandas as gpd

# shp_file_path = 'data/任隆镇/任隆镇_乡镇边界.shp'
# shp_file_path = 'data/任隆镇/任隆镇_县界.shp'
shp_file_path = 'data/黄泥乡边界_10541_Shapefile/10541.shp'
shp_file_path = 'data/蓬溪县/蓬溪县_乡镇边界.shp'
data = gpd.read_file(shp_file_path, encoding='GBK')

# csv_output_path = 'output_data.csv'
# data.to_csv(csv_output_path, index=False)

# json_output_path = 'data/任隆镇_乡镇边界.json'
# json_output_path = 'data/任隆镇_县界.json'
# json_output_path = 'data/黄泥乡边界.json'
json_output_path = 'data/蓬溪县_乡镇边界.json'
# data.to_file(json_output_path, driver='GeoJSON', encoding="UTF-8")
data.to_file(json_output_path, driver='GeoJSON', encoding="GBK")
