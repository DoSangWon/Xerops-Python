import psutil
import cpuinfo
import datetime
import socket
import json
import sys
import http.client
from collections import OrderedDict
cpuinfo = cpuinfo.get_cpu_info()

#connection = http.client.HTTPConnection('')
while 1:
    headers = {'Content-type':'application/json'}
    cpuinfo_data = OrderedDict()
    cpuinfo_data['cpu_name'] = cpuinfo['brand']
    cpuinfo_data['men_size'] = psutil.virtual_memory().total
    cpuinfo_data['hostname'] = socket.gethostname()
    with open('/opt/was/tomcat9/webapps/Xerops/data/cpu_info.json' ,'w',encoding='utf-8')as make_file:
        json.dump(cpuinfo_data,make_file,ensure_ascii=False,indent="\t")
        #json_cpuinfo = json.dumps(cpuinfo_data,ensure_ascii=False)
    #connection.request('POST','/test.do',json_cpuinfo,headers) # 전송
    now = datetime.datetime.now()
    nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
    cpu_percent = psutil.cpu_percent(interval=1)
    meminfo = psutil.virtual_memory()
    mem_total = meminfo.percent
    usage_info = OrderedDict()
    usage_info['cpu_usage'] = cpu_percent
    usage_info['mem_usage'] = mem_total
    usage_info['date'] = nowDatetime
    with open('/opt/was/tomcat9/webapps/Xerops/data/cpu_usage.json', 'w', encoding='utf-8')as make_file:
        json.dump(usage_info, make_file, ensure_ascii=False, indent="\t")
        #json_usage = json.dumps(usage_info,ensure_ascii=False)
    #connection.request('POST','/test.do',json_usage,headers) # 전송
