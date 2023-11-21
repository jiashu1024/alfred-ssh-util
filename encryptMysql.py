# 用于对数据库所有密码进行加密
import pymysql
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def encrypt_aes(plaintext, key):
    # 创建AES加密器对象（使用ECB模式）
    # 对密钥进行填充
    key = key.encode('utf-8')
    if len(key) % 16 != 0:
        key = pad(key, AES.block_size)
    cipher = AES.new(key, AES.MODE_ECB)

    # 对明文进行填充
    plaintext = plaintext.encode('utf-8')
    if len(plaintext) % 16 != 0:
        padded_data = pad(plaintext, AES.block_size)

    # 加密明文
    ciphertext = cipher.encrypt(padded_data)
    return ciphertext.hex()

def main():  
    host = os.environ['host']
    port = os.environ['port']
    username = os.environ['username']
    password = os.environ['password']
    database = os.environ['database']
    key = os.environ['AES']
    port = int(port)
    db = pymysql.connect(host=host,
                         port=port,
                         user=username,
                         password=password,
                         database=database)
    
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select * from servers")
    datas = cursor.fetchall()
    for data in datas:
        encryptBool = data["encrypt"]
        if encryptBool == 0:
            password = data["password"]
            password = encrypt_aes(password, key)
            sql = "update servers set password = '%s',encrypt = 1 where id = %d" % ( password, data["id"])
            print(sql)
            # 执行 sql 语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
    cursor.close()
    # 关闭数据库连接
    db.close()

if __name__ == "__main__":
    main()

