# Napiš program, který se zeptá uživatele na jeho přihlašovací jméno, e-mailovou adresu a heslo.
# Po každém zadaném údaji program ověří jeho správnost podle následujících pravidel:
# uživatelské jméno smí obsahovat malá a velká písmena (nesmí obsahovat žádné jiné znaky),
# jeho minimálná délka je 6 znaků a jeho maximální délka je 10 znaků.

# heslo smí obsahovat malá a velká písmena, číslice, a následující speciální znaky: _, -, ., +, =.
# Jeho minimálná délka je 12 znaků a jeho maximální délka je 30 znaků.
# e-mail by měl být validním e-mailem 🙂 Tady jsou nějaké testovací příklady

import re

def overeni_login(login):
    return re.fullmatch(r'[A-Ža-ž]{6,10}', login) is not None

def overeni_email(email):
    return re.fullmatch(r'^[a-zA-Z0-9_"]+[a-zA-Z0-9"_\.\[\]%+-]+[a-zA-Z0-9_"]+@([a-zA-Z0-9]+[a-zA-Z0-9.-]?[a-zA-Z0-9-]+\.[a-zA-Z]{2,})$', email) is not None

def overeni_heslo(heslo):
    return re.fullmatch(r'[a-zA-Z0-9_\-+.=]{12,30}', heslo) is not None

login = input("Zadejte prihlasovaci jmeno: ")   
while not overeni_login(login):
    print("Zadali jste neplatne prihlasovaci jmeno. Prihlasovaci jmeno musi obsahovat pouze velka ci mala pismena a skladat se z min. 6 a max. 10 znaku.")
    login = input("Zadejte prihlasovaci jmeno: ")

email = input("Zadejte email: ")
while not overeni_email(email):
    print("Zadali jste neplatny format emailu.")
    email = input("Zadejte email: ")

heslo = input("Zadejte heslo: ")
while not overeni_heslo(heslo):
    print("Zadali jste neplatny format hesla. Heslo smi obsahovat mala a velka pismena, cislice a znaky _, -, ., +, =. Zaroven musi byt min. 12 a max. 30 znaku dlouhe.")
    heslo = input("Zadejte heslo: ")

print("Prihlaseni probehlo uspesne.")