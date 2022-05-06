import ctypes

pasta = input("Digite o diretorio da pasta ou o arquivo que deseja ocultar:")

ocultar = 0x02

objeto =  ctypes.windll.kernel32.SetFileAttributesW(pasta, ocultar)

if objeto:
    print("Arquivo ocultado.")
else:
    print("Arquivo não ocultado.")