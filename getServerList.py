# 用于获取服务器列表
import sys
import json
import pymysql
import os

def main():  
    host = os.environ['host']
    port = os.environ['port']
    username = os.environ['username']
    password = os.environ['password']
    database = os.environ['database']
    port = int(port)
    db = pymysql.connect(host=host,
                         port=port,
                         user=username,
                         password=password,
                         database=database)
    
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select * from servers")
    datas = cursor.fetchall()
    res = {}
    items = []
    for data in datas:
        item = {}
        item['uid'] = data["id"]
        item['type'] = 'file'
        item['title'] = data["hostname"]
        item['subtitle'] = data["user"]
        
        user = data["user"]
        serverPort = data["port"]
        password = data["password"]
        ip = data["ip"]
        encrypt = data["encrypt"]
         
        server = {}
        server['user'] = user
        server['password'] = password
        server['ip'] = ip
        server['port'] = serverPort
        server['encrypt'] = encrypt
        item['arg'] = json.dumps(server)
        item['autocomplete'] = "true"
        item['icon'] = {
            'type': 'fileicon',
        }
        mods = {}
        if encrypt == 1:
            copyPassword = '*&*' + password

        mods['alt'] = {
            'valid': 'true',
            'subtitle': 'press enter to copy password',
            'arg': copyPassword,
        }
        mods['cmd'] = {
            'valid': 'true',
            'subtitle': 'press enter to copy server ip',
            'arg': ip,
        }
        item['mods'] = mods
        items.append(item)
    res['items'] = items
    res_str = json.dumps(res)
    db.close()

    sys.stdout.write(res_str)

if __name__ == "__main__":
    main()

