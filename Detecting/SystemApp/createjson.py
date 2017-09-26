import json
import MySQLdb
import collections
import socket

#def createJson():
IP = socket.gethostbyname(socket.gethostname())

db = MySQLdb.connect("localhost", "root", "", "detect")
cursor = db.cursor()

cursor.execute("""SELECT * 
    FROM details""")
rows = cursor.fetchall()
# result = rows


cursor.execute("""SELECT * 
        FROM local_pc""")
local_pcs = cursor.fetchall()

arr_pcs = []
for pcs in local_pcs:
    arr_pcs.append(pcs[0])



data_array = []
nodeID = "n"
number = 1

for data in rows:
    jData = collections.OrderedDict()
    if  data[3] == "Online":
        if data[0] in arr_pcs:
            jData['color'] = "green"

        else:
            jData['color'] = "red"

    elif data[3] == "Offline" :
                jData['color'] = "gray"

    if IP == data[0]:
        jData['size'] = "4"
    elif IP != data[0]:
        jData['size'] = "2"

    jData['label'] = data[2]
    jData['id'] = data[0]
    number += 1

    data_array.append(jData)


edges_array = []
num = 1
edge = "e"
for ip in rows:
    ipData = collections.OrderedDict()
    ipData['source'] = ip[0]
    ipData['id'] = edge + str(num)
    ipData['target'] = "146.64.204.48"
    num += 1
    edges_array.append(ipData)

with open('C:\\Users\\MTshiololi\\Documents\\CSIR PROJECT\\Detecting\\SystemApp\\static\\SystemApp\\js\\results.json', 'wb+') as f:
    jsonData = {
        'nodes': data_array,
        'edges': edges_array
    }
    json.dump(jsonData, f, rows, indent=2)