# print("Bukik!")

import math

# cd .. returns to a previous (parent) folder 

# def hello_user(name):
#   print("Hello, " + name)

# def get_name():
#   name = input("Name: ")
#   print("Ahoj uzivateli: " + name)

def znamky(seznam):
  novy_seznam = []

  for znamka in seznam:
    if znamka == 1:
      novy_seznam.append("vyborny")
    elif znamka == 2:
      novy_seznam.append("chvalitebny")
    elif znamka == 3:
      novy_seznam.append("dobry")
    elif znamka == 4:
      novy_seznam.append("dostatecny")
    elif znamka == 5:
      novy_seznam.append("nedostatecny")
    else:
      novy_seznam.append("ERROR")

  return novy_seznam

hodnoceni = [1, 2, 3, 3, 2, 1, 5]

print(znamky(hodnoceni))
print(znamky([1, 2, 3, 3, 2, 1, 5]))

nezaokrouhlene_cislo = 3.5
print(round(nezaokrouhlene_cislo))
