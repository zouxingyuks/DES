from ECB import *
# 主函数
if __name__ == '__main__':
    # # 读取明文
    # plain = input('请输入明文：')
    # # 读取密钥
    # key = input('请输入密钥：')
    # # 读取加密方式
    # method = input('请输入加密方式（ECB/CBC）：')
    #
    # # 加密
    # cipher = DES(plain, key, 'encrypt')
    # print('密文：', cipher)
    # # 解密
    # plain = DES(cipher, key,'decrypt')
    # print('明文：', plain)
    # cipher = DES(0x2973a7e54ec730a3, 0xcafababedeadbeaf, 'encrypt')
    # print(cipher)
    # # 0x2973a7e54ec730a3
    # print(hex(DES(cipher, 0xcafababedeadbeaf, 'decrypt')))
    m = b'helloQAQwww'
    key = b'lilac666'

    c = des_ecb_enc(m, key)
    print(c)
    # b'w\xb4\n\xccM\xd6\xd1\xcd4\xe6aQ\x0c\x88\x826'

    p = des_ecb_dec(c, key)
    print(p)
    # b'helloQAQwww'