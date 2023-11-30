from PKCS5 import addPadding, delPadding
from DES import DES
from functools import reduce

def des_ecb_enc(plain, key):
    m = addPadding(plain)
    m = [m[x: x + 8] for x in range(0, len(m), 8)]

    c = [DES(int.from_bytes(x, 'big'),
             int.from_bytes(key, 'big'),
             'encrypt') for x in m]

    c = [x.to_bytes(8, 'big') for x in c]

    return reduce(lambda x, y: x + y, c)


def des_ecb_dec(enc, key):
    assert len(enc) % 8 == 0

    c = [enc[x: x + 8] for x in range(0, len(enc), 8)]

    c = [DES(int.from_bytes(x, 'big'),
             int.from_bytes(key, 'big'),
             'decrypt') for x in c]

    c = [x.to_bytes(8, 'big') for x in c]

    return delPadding(reduce(lambda x, y: x + y, c))

if __name__ == '__main__':
    m = b'helloQAQwww'
    key = b'lilac666'

    c = des_ecb_enc(m, key)
    print(c)
    # b'w\xb4\n\xccM\xd6\xd1\xcd4\xe6aQ\x0c\x88\x826'

    p = des_ecb_dec(c, key)
    print(p)