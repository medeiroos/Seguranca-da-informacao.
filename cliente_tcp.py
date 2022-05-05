import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou!!!")
        print("Erro: {}".format(e))
        sys.exit()
    print("Socket criado com sucesso!.")

    hostAlvo = input("Digite o HOST ou o IP a ser conectado: ")
    portaAlvo = input("Digite a porta a ser conectada: ")
    try:
        s.connect((hostAlvo, int(portaAlvo)))
        print("Cliente TCP conectado com sucesso no Host: "+hostAlvo+ "e na Porta:"+portaAlvo)
        s.shutdown(2)
    except socket.error as e:
        print("A conexão no Host: "+hostAlvo+ "falhou, e na porta:"+portaAlvo+" tambem falhou.")
        print("Erro: {}".format(e))
        sys.exit()

if __name__ == "__main__":
    main()
