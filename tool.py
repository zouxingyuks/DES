import argparse
import datetime
from CBC import *
from ECB import *

parser = argparse.ArgumentParser(description='DES加密工具')
parser.add_argument('-t', '--text',required=True, type=str, help='明文/密文')
parser.add_argument('-m', '--mode', type=str, default='ECB', help='加密模式（ECB/CBC）')
parser.add_argument('-e', '--encrypt', nargs='?', const='encrypt', type=str, help='加密')
parser.add_argument('-d', '--decrypt', nargs='?', const='decrypt', type=str, help='解密')
parser.add_argument('-k', '--key',required=True, type=str, help='密钥')
# 字符集
parser.add_argument('-c','--character',type=str,default='utf-8',help='字符集')

args = parser.parse_args()

# 加密
if args.encrypt is not None:
    # 读取明文
    character =args.character
    plain = args.text
    plain = plain.encode(character)
    # 读取密钥
    key = args.key
    key = key.encode(character)
    # 加密
    cipher = ''
    if args.mode == 'ECB':
        cipher = des_ecb_enc(plain, key)
    elif args.mode == 'CBC':
        cipher = des_cbc_enc(plain, key)
    else:
        print('DES模式错误')
        exit(1)
    print('密文：', cipher)

# 解密
elif args.decrypt is not None:
    # 读取密文
    character =args.character

    cipher = args.text
    cipher = cipher.encode(character)
    # 读取密钥
    key = args.key
    key = key.encode(character)
    # 解密
    plain =''
    if args.mode == 'ECB':
        plain = des_ecb_dec(cipher, key)
    elif args.mode == 'CBC':
        plain = des_cbc_dec(cipher, key)
    else:
        print('DES模式错误')
        exit(1)
    print('明文：', plain)