import os
print("-=-" * 25)
ip_ou_host = input("        Digite o IP ou HOST a ser verificado:")
print("-=-" * 25)
os.system('ping -n 6 {}'.format(ip_ou_host))
print("-=-"* 25)