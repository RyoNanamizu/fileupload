from Crypto.Signature import pss
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256

keySize = 2048
msg = b'test'

hash = SHA256.new(msg)
key = RSA.generate(keySize)
pub_pss = pss.new(key).sign(hash)


privateKey = key.export_key('PEM', pkcs=8).decode('utf-8')
publicKey = key.publickey().export_key().decode('utf-8')


print(privateKey)
print(publicKey)