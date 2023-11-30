from PKCS5 import addPadding, delPadding
from DES import DES
from functools import reduce

def des_cbc_enc(plain, key, iv):
    key = int.from_bytes(key, 'big')
    iv = int.from_bytes(iv, 'big')

    m = addPadding(plain)
    m = [int.from_bytes(m[x: x + 8], 'big') for x in range(0, len(m), 8)]

    c = []

    for i in range(len(m)):
        r = iv ^ m[i]
        iv = DES(r, key, 'encrypt')
        c.append(iv)

    c = [x.to_bytes(8, 'big') for x in c]

    return reduce(lambda x, y: x + y, c)


def des_cbc_dec(enc, key, iv):
    key = int.from_bytes(key, 'big')
    iv = int.from_bytes(iv, 'big')

    c = [int.from_bytes(enc[x: x + 8], 'big') for x in range(0, len(enc), 8)]

    m = []

    for i in range(len(c)):
        p = DES(c[i], key, 'decrypt')

        m.append(p ^ iv)
        iv = c[i]

    m = [x.to_bytes(8, 'big') for x in m]

    return delPadding(reduce(lambda x, y: x + y, m))


if __name__ == '__main__':
    m = b'helloQAQwww'
    key = b'lilac666'
    iv = b'ruan1234'

    c = des_cbc_enc(m, key, iv)
    print(c)
    # b'\x93W\xb7\xf5\x93\xd2?\n\xe2\x9bR\x179\x94\xa1\x00'

    p = des_cbc_dec(c, key, iv)
    print(p)
    # b'helloQAQwww'
