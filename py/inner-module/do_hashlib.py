import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
res = md5.hexdigest()
print(res)

# 数据量非常大的时候，可以分段update
md52 = hashlib.md5()
md52.update('how to use md5 in '.encode('utf-8'))
md52.update('python hashlib?'.encode('utf-8'))
print(md52.hexdigest())

# sha
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

sha_256 = hashlib.sha256()
sha_256.update('how to use sha1 in '.encode('utf-8'))
sha_256.update('python hashlib?'.encode('utf-8'))
print(sha_256.hexdigest())

sha_512 = hashlib.sha512()
sha_512.update('how to use sha1 in '.encode('utf-8'))
sha_512.update('python hashlib?'.encode('utf-8'))
print(sha_512.hexdigest())


def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()


db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


def login(user, password):
    p = db.get(user, None)
    if p == None:
        return False
    if calc_md5(password) == p:
        return True
    else:
        return False


assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
assert not login('jane', 'Alice2008')
print('ok')
