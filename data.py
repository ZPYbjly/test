# 火点下载地址
# https://firms.modaps.eosdis.nasa.gov/active_fire/#firms-shapefile

import requests
import time
import os
from zip import unzip_file
from csv_json import csvtoGeojson
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
    path_json = savepath +'/' +shppathname +'/' +'json' 
    # E:\OneDrive\桌面\火点数据5
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
    resp = requests.get(url_shp[datatype])
    with open(savepath_shp,mode='wb') as f:
      f.write(resp.content)
      
    resp = requests.get(url_csv[datatype])
    with open(savepath_csv,mode='wb') as f:
      f.write(resp.content)
    csvtoGeojson(path_csv,savepath_json)
    print(savepath_csv)
    print(savepath_shp)
    print(path_shp)
    zip_shp(path_shp,path_realshp)
def zip_shp(inputpath,savepath):
  # path_zip = ('E:/OneDrive/桌面/火点数据/zip')
  folder1 = os.path.exists(savepath)
  if not folder1:                   
    os.makedirs(savepath) 
  zipfiles=os.listdir(inputpath) 
  for zipFile in zipfiles:
    print(zipFile)
    zippath = inputpath+'/'+zipFile
    print(zippath)  
    unzip_file(zippath,savepath)    
if __name__ == "__main__":
  # zip_shp()  
  data_replace('E:/OneDrive/桌面/火点数据')
  print("all over!!!")
