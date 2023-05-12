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
    cursor.execute("select * from sshTable")
    datas = cursor.fetchall()
    res = {}
    dicts = []
    for data in datas:
        dict = {}
        dict['uid'] = data["id"]
        dict['type'] = 'file'
        dict['title'] = data["hostname"]
        dict['subtitle'] = data["user"]
        
        user = data["user"]
        password = data["password"]
        ip = data["ip"]
         
        args = {}
        args['user'] = user
        args['password'] = password
        args['ip'] = ip
        args_str = f"{ip} {user} {password}"
        dict['arg'] = args_str
        dict['arg'] = json.dumps(args_str)
        dict['autocomplete'] = "true"
        dict['icon'] = {
            'type': 'fileicon',
        }
        dicts.append(dict)

    res['items'] = dicts
    res_str = json.dumps(res)
    db.close()

    sys.stdout.write(res_str)

if __name__ == "__main__":
    main()

