from ECB import *
# 主函数
if __name__ == '__main__':
    text = input ("请输入文本：")
    key = input ("请输入密钥：")
    mode = input ("请输入模式：")
    method = input ("请输入方法：")
    character = input ("请输入字符集：")
    # 加密
    if method == 'encrypt':
        # 读取明文
        plain = text
        plain = plain.encode(character)
        # 读取密钥
        key = key
        key = key.encode(character)
        # 加密
        cipher = ''
        if mode == 'ECB':
            cipher = des_ecb_enc(plain, key)
        elif mode == 'CBC':
            cipher = des_cbc_enc(plain, key)
        else:
            print('DES模式错误')
            exit(1)
        print('密文：', cipher)
    # 解密
    elif method == 'decrypt':
        # 读取密文
        cipher = text
        cipher = cipher.encode(character)
        # 读取密钥
        key = key
        key = key.encode(character)
        # 解密
        plain =''
        if mode == 'ECB':
            plain = des_ecb_dec(cipher, key)
        elif mode == 'CBC':
            plain = des_cbc_dec(cipher, key)
        else:
            print('DES模式错误')
            exit(1)
        print('明文：', plain)
    else:
        print('DES方法错误')
        exit(1)