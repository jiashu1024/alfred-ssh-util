import sys
import os
from encryptUtil import decrypt_aes

password = sys.argv[1]
password = decrypt_aes(password, os.environ['AES'])
sys.stdout.write(password)