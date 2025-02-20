#lon lat name

#
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# 输入txt文件路径和输出shp文件路径
txt_file = 'input_data.txt'
shp_file = 'output_data.shp'

# 读取txt文件，假设文件以空格或制表符分隔
df = pd.read_csv(txt_file, delim_whitespace=True, header=None, names=['Longitude', 'Latitude', 'Name'])

# 创建geometry列，包含经纬度的点
df['geometry'] = df.apply(lambda row: Point(row['Longitude'], row['Latitude']), axis=1)

# 转换为GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry='geometry')

# 设置坐标参考系统为WGS84（经纬度坐标）
gdf.set_crs('EPSG:4326', inplace=True)

# 保存为shp文件
gdf.to_file(shp_file)

print(f"转换完成！shp文件保存在：{shp_file}")
