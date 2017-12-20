import subprocess
import datetime
import json
import pymysql
from collections import OrderedDict
now = datetime.datetime.now()
nowDatetime = now.strftime('%Y%m%d%H%M')

f = open('/etc/xerops/log/report_xerops_'+nowDatetime+'.txt','r',1,'utf-8')
#f = open('report_xerops_201712120104.txt','r',1,'utf-8')
line = f.readline()
conn = pymysql.connect(host='localhost', port=3306, user='snort', password='', database='snort',charset='utf8mb4')
cursor = conn.cursor(pymysql.cursors.SSCursor)
truncate_query = "TRUNCATE chk"
cursor.execute(truncate_query)
conn.commit()
while line:
    line = line.replace("\n","")
    result = line.split(";")
    line = f.readline()
    name = result[0]
    result2 = result[1]
    importance = result[2]
    #print(name+result2+importance)
    insert_query = "insert into chk VALUES ('"+name+"','"+result2+"','"+importance+"')"
    cursor.execute(insert_query)
    conn.commit()
conn.close()

