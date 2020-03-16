from Crypto.Cipher import DES

chave = "12345678"

des = DES.new(chave, DES.MODE_ECB)

texto_claro = "Hellow world    "

texto_cifrado = des.encrypt(texto_claro)

print('[+] cifrado %s' % texto_cifrado)
print("[+] decifrado: %s" % des.decrypt(texto_cifrado))



print("okay!")
