import time
import os

with open("hosts.txt") as file:
    dump = file.read()
    dump = dump.splitlines()
    for ip in dump:
        print("Verificando o ip: ", ip)
        print("-=-" * 25)
        os.system('ping -n 2 {}'.format(ip))
        print("-=-" * 25)
        time.sleep(5)