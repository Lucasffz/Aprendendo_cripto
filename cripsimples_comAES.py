from Crypto.Cipher import AES

chave = "123456789abcdefg"
aes = AES.new(chave, AES.MODE_ECB)

texto = input("Digite o texto para criptografar:")

# texto_claro = "Uniao-HackBrasil" 

texto = texto + '#'*(16-len(texto)%16) ## Preenche com # caso não seja multiplo de 16
texto_cifrado = aes.encrypt(texto)

print('Seu texto cifrado cifrado %s' % texto_cifrado)




print("okay!")
