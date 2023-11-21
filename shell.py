import sys
import json
import os
from encryptUtil import decrypt_aes


infpJson = sys.argv[1]
infp = json.loads(infpJson)
ip = infp['ip']
username = infp['user']
password = infp['password']
port = infp['port']
encryptBool = infp['encrypt']
if encryptBool >= 1:
		password = decrypt_aes(password, os.environ['AES'])
# expect脚本
with open('connect.sh', 'r') as f:
		res = f.read()

# 替换ip
res = res.replace('#ip', ip)
# 替换username
res = res.replace('#username', username)
# 替换password
res = res.replace('#password', password)
# 替换port
res = res.replace('#port', port)
# 将 res 写入到文件中
with open('/tmp/ssh.sh', 'w') as f:
		f.write(res)