import itertools

string = input("Digite a palavra a ser permutada:")
resultado = itertools.permutations(string, len(string))
for i in resultado:
    print("".join(i))
