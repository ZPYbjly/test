# 此程序可以将csv文件转化为geojson
# csvtoGeojson(inputpath.outputpath)
# 参数1  inputpath 为输入csv文件路径，程序可以自动读取数据
# 参数2  outputpath  为输出geojson文件路径  geojson文件名称自动获取读取到的csv文件名称
import os
import csv
import json 
def csvtoGeojson(inputpath,outputpath):
    print('csv to geojson begining... !!! ')
    csv_files = os.listdir(inputpath)
    flag = os.path.exists(outputpath)
    if not flag:                   
      os.makedirs(outputpath) 
    for csvfile in csv_files:
        csv_file = open(inputpath+'/'+csvfile, encoding='utf8')
        jsonname = csvfile.rsplit('.')[0]
        csv_reader = csv.reader(csv_file)
        
        geojson = '{"type":"FeatureCollection","features":['
        
        lon_index = 0
        lat_index = 1
        for index, row in enumerate(csv_reader):
            if index == 0:
                header = row
                continue
        
            property_dict = {}
            for indexJ, j in enumerate(row):
                if indexJ == lon_index or indexJ == lat_index:
                    continue
                property_dict[header[indexJ]] = j
        
            geojson += '{"geometry":{"coordinates":[%f,%f],"type":"Point"},"properties":%s,"type":"Feature"},' \
                    % (float(row[lat_index]), float(row[lon_index]), json.dumps(property_dict, ensure_ascii=False))
        
        outputjson = outputpath+'/'+jsonname+'.geojson'
        geojson = geojson[:-1] + ']}'
        links_file = open(outputjson, 'w', encoding='utf8')
        links_file.write(geojson)
        print(outputjson,'  over!')


        
# csvtoGeojson('E:/OneDrive/桌面/历史火点数据/MODIS_C6_1_Global_24h/csv','E:/OneDrive/桌面/历史火点数据/MODIS_C6_1_Global_24h/json')
# print('all over!')

