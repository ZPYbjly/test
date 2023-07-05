import psycopg2
import json
import os


def insertfirejson(inputpath,sqlname):
    conn=psycopg2.connect(database="WEBGIS",user="postgres",password="235661",host="localhost",port="5432")
    cur = conn.cursor()
    jsonfiles=os.listdir(inputpath)
    for jsonfile in jsonfiles:
         with open(inputpath+'/'+jsonfile,'r',encoding='utf8') as fp:
            json_data = json.load(fp)
            features = json_data['features'][0]['properties']['acq_date']
            date = features
            print(date,"json——data input finish!!!  ")
            jsondata = json.dumps(json_data)
            cur.execute("INSERT INTO "+sqlname+"(file,date)VALUES(%s,%s)",(jsondata,date))
    conn.commit()
    cur.close()
    conn.close()
#posstgresqlname:  'suomiviirs'   'modisACF'   'j1viirs'    

# insertfirejson('E:/OneDrive/桌面/json','firepoint')

# insertfirejson('E:/OneDrive/桌面/json','j1viirs')
# insertfirejson('E:/OneDrive/桌面/json','modisACF')
# insertfirejson('E:/OneDrive/桌面/json','suomiviirs')
