# [2022/11/6 11:34:26 +08:00] 
# AES
# Key: Opathon2022-Group1
# IV: 111111aabbccwwww
# Encoded Data: Gw/nFRnw85c0/n4WlEv1nUspG1BRUC3Q2q3rhCpm0yewIf3xwGWt0z7XfK9T9XHF

# You have to create a WebAPI to decode Encoded Data, and create a page in WeChat MiniProgram to let users to input other Encoded Data to get the result.

# Good luck!

import hashlib
import base64
i_type = "AES"
i_key = "Opathon2022-Group1"
i_iv = "111111aabbccwwww"
i_encoded_data = "Gw/nFRnw85c0/n4WlEv1nUspG1BRUC3Q2q3rhCpm0yewIf3xwGWt0z7XfK9T9XHF"
from Crypto.Cipher import AES
# 密钥（key）, 密斯偏移量（iv） CBC模式加密
  
def AES_Encrypt(key, data):
    vi = i_iv
    pad = lambda s: s + (16 - len(s)%16) * chr(16 - len(s)%16)
    data = pad(data)
    # 字符串补位
    cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, vi.encode('utf8'))
    encryptedbytes = cipher.encrypt(data.encode('utf8'))
    # 加密后得到的是bytes类型的数据
    encodestrs = base64.b64encode(encryptedbytes)
    # 使用Base64进行编码,返回byte字符串
    enctext = encodestrs.decode('utf8')
    # 对byte字符串按utf-8进行解码
    return enctext
  
def AES_Decrypt(key, data):
    vi = i_iv
    data = data.encode('utf8')
    encodebytes = base64.decodebytes(data)
    # 将加密数据转换位bytes类型数据
    cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, vi.encode('utf8'))
    text_decrypted = cipher.decrypt(encodebytes)
    unpad = lambda s: s[0:-s[-1]]
    text_decrypted = unpad(text_decrypted)
    # 去补位
    text_decrypted = text_decrypted.decode('utf8')
    return text_decrypted
  

b64_str = base64.b64encode(i_encoded_data.encode("utf8"))
out_key = hashlib.md5(i_key.encode(encoding='UTF-8')).hexdigest()
out_key = out_key[8:24]
b64_str = b64_str.decode("utf8")
print(b64_str)
test_content = """
IP: 52.184.83.145:3389
PWD(Base64ed): c0RoYzc2VEdzOEpk
"""
out_test = AES_Encrypt(out_key,test_content)
print(out_test)
out_test_out = AES_Decrypt(out_key,out_test)
print(out_test_out)

out_test_out = AES_Decrypt(out_key,b64_str)
print(out_test_out)


