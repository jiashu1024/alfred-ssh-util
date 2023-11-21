## 复制密码时进行解密
import sys
import os
from encryptUtil import decrypt_aes

password = sys.argv[1]
if password.startswith('*&*'):
		password = password[3:]
		password = decrypt_aes(password, os.environ['AES'])

sys.stdout.write(password)