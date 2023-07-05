# 火点下载地址
# https://firms.modaps.eosdis.nasa.gov/active_fire/#firms-shapefile
# 火点参数说明地址
# https://www.earthdata.nasa.gov/learn/find-data/near-real-time/firms/mcd14dl-nrt#ed-firms-attributes
# https://www.earthdata.nasa.gov/learn/find-data/near-real-time/firms/vnp14imgtdlnrt#ed-viirs-375m-attributes

import requests
import time
import os
from zip import zip_shp
from csv_json import csvtoGeojson
from insert_pgsql import insertfirejson
# time data example
# print (time.strftime("%H:%M:%S"))
# print (time.strftime("%I:%M:%S"))
# print (time.strftime("%Y/%m/%d"))
def data_replace(savepath):
  # 火点实时更新数据网址
  url_csv = ['https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_Global_24h.csv',
  'https://firms.modaps.eosdis.nasa.gov/data/active_fire/suomi-npp-viirs-c2/csv/SUOMI_VIIRS_C2_Global_24h.csv',
  'https://firms.modaps.eosdis.nasa.gov/data/active_fire/noaa-20-viirs-c2/csv/J1_VIIRS_C2_Global_24h.csv',

  ]
  url_shp = ['https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/shapes/zips/MODIS_C6_1_Global_24h.zip',
  'https://firms.modaps.eosdis.nasa.gov/data/active_fire/suomi-npp-viirs-c2/shapes/zips/SUOMI_VIIRS_C2_Global_24h.zip',
  'https://firms.modaps.eosdis.nasa.gov/data/active_fire/noaa-20-viirs-c2/shapes/zips/J1_VIIRS_C2_Global_24h.zip'
  ]
  # 更新程序 ACF 三种类型循环爬取（modis suomi-npp-viirs noaa-20-viirs）
  for datatype in range(3):  
  # 文件名称创建

  # 1.文件名截取
    csvname = url_csv[datatype].rsplit("/",1)[1]
    zipname = url_shp[datatype].rsplit('/',1)[1]
    csvpathname = csvname.rsplit(".")[0]
    zippathname = zipname.rsplit(".")[0]
    shppathname = zippathname
    date = time.strftime("%Y_%m_%d_")
  # 2.文件存储路径创建
    
    path_csv = savepath +'/'+csvpathname+'/'+'csv'+'/'+date+'csv'
    path_shp = savepath +'/'+zippathname+'/'+'zip'+'/'+date+'zip'
    path_realshp = savepath+'/'+shppathname +'/'+'shp'+'/'+date+'shp'
    path_json = savepath +'/' +shppathname +'/' +'json'+'/'+date+'json' 
    folder1 = os.path.exists(path_csv)
    if not folder1:                   
      os.makedirs(path_csv) 
    folder2 = os.path.exists(path_shp)    
    if not folder2:                   
      os.makedirs(path_shp)       
    print('start',zipname,csvname)
    savepath_csv = path_csv+'/'+date+csvname
    savepath_shp = path_shp+'/'+date+zipname
    savepath_json = path_json 

    # 爬取数据
    # 1. 爬取shp的zip文件
    resp = requests.get(url_shp[datatype])
    with open(savepath_shp,mode='wb') as f:
      f.write(resp.content)
    # 2. 爬取csv文件
    resp = requests.get(url_csv[datatype])
    with open(savepath_csv,mode='wb') as f:
      f.write(resp.content)
    # csv 数据转换为 geojson 并导入数据库
    csvtoGeojson(path_csv,savepath_json)
    if csvpathname == 'MODIS_C6_1_Global_24h':
      insertfirejson(savepath_json,'modisACF')
    if csvpathname == 'J1_VIIRS_C2_Global_24h':
      insertfirejson(savepath_json,'j1viirs')
    if csvpathname == 'SUOMI_VIIRS_C2_Global_24h':  
      insertfirejson(savepath_json,'suomiviirs')
    # 解压 shp 文件
    zip_shp(path_shp,path_realshp)


if __name__ == "__main__":
  # zip_shp()  
  data_replace('X:/pyzhang/test2')
  # X:\pyzhang\火点数据\实时更新火点数据
  print("all over!!!")
