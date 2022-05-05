import hashlib, time

print("-=-"*30)
print("                      Bem-vindo ao criptografador de texto!")
print("-=-"*30)
time.sleep(0.5)
print("Nesta versão temos disponiveis algumas hashes como: MD5(1), SHA1(2), SHA256(3) e SHA512(4)")
print("-=-"*30)
valor = input("Digite o número da hash que você deseja usar:")
print("-=-"*30)
print("                              Analisando o número...")
print("-=-"*30)
time.sleep(1)
if valor == "1":
    string = input("Digite o texto que queria criptografar em MD5:")
    resultado = hashlib.md5(string.encode("utf-8"))
    print("O seu texto criptografado da MD5 é:", resultado.hexdigest())
if valor == "2":
    string2 = input("Digite o texto que queira criptografar em SHA1:")
    resultado2 = hashlib.sha1(string2.encode("utf-8"))
    print("O seu texto criptografado em SHA1 é:", resultado2.hexdigest())
if valor == "3":
    string3 = input("Digite o texto que queira criptografar em SHA256:")
    resultado3 = hashlib.sha256(string3.encode("utf-8"))
    print("O seu texto criptografado em SHA256 é:", resultado3.hexdigest())
if valor == "4":
    string4 = input("Digite o texto que queira criptografar em SHA512:")
    resultado4 = hashlib.sha512(string4.encode("utf-8"))
    print("O seu texto criptografado em SHA512 é:", resultado4.hexdigest())