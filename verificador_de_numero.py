import phonenumbers
from phonenumbers import geocoder
print("(no formato +55 com o DD)")
numero = input("Digite o número de telefone:")
phone_number = phonenumbers.parse(numero)
print(geocoder.description_for_number(phone_number, "pt"))



