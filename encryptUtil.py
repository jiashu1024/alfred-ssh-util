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

def decrypt_aes(ciphertext, key):
    # 创建AES解密器对象（使用ECB模式）
    # 对密钥进行填充
    key = key.encode('utf-8')
    if len(key) % 16 != 0:
        key = pad(key, AES.block_size)
    cipher = AES.new(key, AES.MODE_ECB)

    # 解密密文
    decrypted_data = unpad(cipher.decrypt(bytes.fromhex(ciphertext)), AES.block_size)
    return decrypted_data.decode('utf-8')

# # # 示例使用
# plaintext = "hello"
# encryption_key = "zhangjiashu"  # 注意：密钥的长度必须符合AES算法要求

# # # 加密
# encrypted_text = encrypt_aes(plaintext, encryption_key)
# print("Encrypted Text:", encrypted_text)

# # 解密
# decrypted_text = decrypt_aes(encrypted_text, encryption_key)
# print("Decrypted Text:", decrypted_text)
