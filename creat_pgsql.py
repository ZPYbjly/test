import psycopg2
import os
import json

# modis
def creat_modis_pgsql(inputpath):
    conn=psycopg2.connect(database="WEBGIS",user="postgres",password="235661",host="localhost",port="5432")
    cur=conn.cursor() #创建游标对象
    
    #创建数据库
    cur.execute("drop table if exists modisACF;")
    
    # 创建一个序列为 id 服务
    cur.execute('DROP SEQUENCE if exists modisacf_vendorcode_id_seq ')
    cur.execute('CREATE SEQUENCE modisacf_vendorcode_id_seq START 1;')
     
    cur.execute("CREATE TABLE if not exists modisACF(id integer DEFAULT nextval('modisacf_vendorcode_id_seq'::regclass) primary key,file json, date date);")
    jsonfiles=os.listdir(inputpath)
    print(jsonfiles)
    
     #插入数据   
    for jsonfile in jsonfiles:
        with open(inputpath+'/'+jsonfile,'r',encoding='utf8') as fp:
            json_data = json.load(fp)
            features = json_data['features'][0]['properties']['acq_date']
            print(features,'geojson_data finish !!!')
            date=features
            jsondata = json.dumps(json_data)
            cur.execute("INSERT INTO modisACF(file,date)VALUES(%s,%s)",(jsondata,date))
    conn.commit()
    cur.close()
    conn.close()


def creat_suomiviirs_pgsql(inputpath):
    conn=psycopg2.connect(database="WEBGIS",user="postgres",password="235661",host="localhost",port="5432")
    cur=conn.cursor() #创建游标对象
    #创建数据库
    cur.execute("drop table if exists suomiviirs;")
    # 创建一个序列为 id 服务
    cur.execute('DROP SEQUENCE if exists suomiviirs_vendorcode_id_seq ')
    cur.execute('CREATE SEQUENCE suomiviirs_vendorcode_id_seq START 1;')  

    cur.execute("CREATE TABLE if not exists suomiviirs(id integer DEFAULT nextval('suomiviirs_vendorcode_id_seq'::regclass) primary key,file json, date date);")
    jsonfiles=os.listdir(inputpath)
    print(jsonfiles)
    
     #插入数据   
    for jsonfile in jsonfiles:
        with open(inputpath+'/'+jsonfile,'r',encoding='utf8') as fp:
            json_data = json.load(fp)
            features = json_data['features'][0]['properties']['acq_date']
            print(features,'geojson_data finish !!!')
            date=features
            jsondata = json.dumps(json_data)
            cur.execute("INSERT INTO suomiviirs(file,date)VALUES(%s,%s)",(jsondata,date))
    conn.commit()
    cur.close()
    conn.close()

def creat_j1viirs_pgsql(inputpath):
    conn=psycopg2.connect(database="WEBGIS",user="postgres",password="235661",host="localhost",port="5432")
    cur=conn.cursor() #创建游标对象
    #创建数据库
    cur.execute("drop table if exists j1viirs;")
    # 创建一个序列为 id 服务
    cur.execute('DROP SEQUENCE if exists j1viirs_vendorcode_id_seq ')
    cur.execute('CREATE SEQUENCE j1viirs_vendorcode_id_seq START 1;')  
    cur.execute("CREATE TABLE if not exists j1viirs(id integer DEFAULT nextval('j1viirs_vendorcode_id_seq'::regclass) primary key,file json, date date);")
    jsonfiles=os.listdir(inputpath)
    print(jsonfiles)
    
     #插入数据   
    for jsonfile in jsonfiles:
        with open(inputpath+'/'+jsonfile,'r',encoding='utf8') as fp:
            json_data = json.load(fp)
            features = json_data['features'][0]['properties']['acq_date']
            print(features,'geojson_data finish !!!')
            date=features
            jsondata = json.dumps(json_data)
            cur.execute("INSERT INTO j1viirs(file,date)VALUES(%s,%s)",(jsondata,date))
    conn.commit()
    cur.close()
    conn.close()





    
creat_modis_pgsql('E:/OneDrive/桌面/历史火点数据/MODIS_C6_1_Global_24h/json')
creat_suomiviirs_pgsql('E:/OneDrive/桌面/历史火点数据/SUOMI_VIIRS_C2_Global_24h/json')
creat_j1viirs_pgsql('E:/OneDrive/桌面/历史火点数据/J1_VIIRS_C2_Global_24h/json')