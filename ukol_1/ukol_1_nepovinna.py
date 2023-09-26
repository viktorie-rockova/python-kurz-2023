print('Zadej jmeno a prijmeni')

jmeno_a_prijmeni = input()

#kapitalky
print(jmeno_a_prijmeni.upper())

#mala pismena
print(jmeno_a_prijmeni.lower())

#prvni pismeno velke, ostatni mala (jak u jmena, tak u prijmeni)
rozdelene_jmeno = jmeno_a_prijmeni.split(" ")
print(rozdelene_jmeno[0].capitalize() + ' ' + rozdelene_jmeno[1].capitalize())

#inicialy
print(rozdelene_jmeno[0][0:1].upper() + '. ' + rozdelene_jmeno[1][0:1].upper() + '.')

#křestní jméno zkrácené na první písmeno a příjmení, pokud je křestní jméno delší než 5 znaků. Jinak vypíše standardní variantu, tj. první písmeno velké, další malá (u vstupu Jarmila Malá by došlo ke zkrácení křestního jména, zatímco u vstupu Jana Malá nikoliv)
if len(rozdelene_jmeno[0]) > 5:
  print(rozdelene_jmeno[0][0:1].upper() + '. ' + rozdelene_jmeno[1].capitalize())
else:
  print(rozdelene_jmeno[0].capitalize() + ' ' + rozdelene_jmeno[1].capitalize())