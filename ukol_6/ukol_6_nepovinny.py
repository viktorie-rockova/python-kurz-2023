# Přidej třídě Auto metodu vrat_auto(), která bude mít (krom obligátního self) 2 parametry, a to je stav tachometru při
# vrácení a počet dní, po které zákazník auto používal. Ulož stav tachometru do atributu objektu. Nastav vozidlo jako volné.

# Dále ve funkci vypočti cenu za půjčení. Cena je 400 Kč na den, pokud měl zákazník celkem auto méně než týden, a 300 Kč na den,
# pokud měl zákazník auto déle. Cena je stejná pro obě auta. Vlož cenu do nějakého informativního textu a ten vrať pomocí
# klíčového slova return.

class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, pocet_najetych_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.pocet_najetych_km = pocet_najetych_km
        self.dostupnost = True

    def pujceni_auta(self):
        if self.dostupnost:
            self.dostupnost = False
            return "Potvrzuji úspešnou zápujčku vozidla."
        else:
            return "Vozidlo bohužel není k dispozici."  

    def get_info(self):
        return f"Auto typu {self.typ_vozidla} má registrační značku {self.registracni_znacka}."

    def vrat_auto(self, stav_tachometru, pocet_dni):
        self.dostupnost = True
        najete_km = int(stav_tachometru) - self.pocet_najetych_km
        self.pocet_najetych_km = stav_tachometru
        if int(pocet_dni) <= 7:
            cena_pronajmu = int(pocet_dni) * 400
        else:
            cena_pronajmu = int(pocet_dni) * 300
        return f"Zákazník najel {najete_km} během {pocet_dni}. Cena pronájmu bude {cena_pronajmu} Kč."
        


auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
auto2 = Auto("1P3 4747", "Škoda Octavia", 41253)

pokracuj = True

while  pokracuj:
    vyber_funkce = input("Pro pronájem vozidla zadejte jeho značku " \
                       "(Peugeot nebo Škoda). Pro vrácení vozidla zadejte 'Vratit' a ukončete program zadáním 'Konec': ")

    if vyber_funkce.lower() == "konec":
        print("Ukončili jste program.")
        pokracuj = False
    
    elif vyber_funkce.lower() == "vratit":
        vyber_auta = input("Zadejte značku vraceného auta: ")
        stav_tachometru = input("Zadejte stav tachometru: ")
        pocet_dni = input("Zadejte počet dní zápůjčky: ")
        
        if vyber_auta.lower() == "peugeot":
            if auto1.dostupnost == False:
                print(auto1.vrat_auto(stav_tachometru, pocet_dni))
            else:
                print("Toto auto nebylo zapůjčeno.")

        elif vyber_auta.lower() == "škoda":
            if auto2.dostupnost == False:
                print(auto2.vrat_auto(stav_tachometru, pocet_dni))
            else:
                print("Toto auto nebylo zapůjčeno.")

        else:
            print("Neplatná volba značky vozidla.")

    
    elif vyber_funkce.lower() == "peugeot":
        print(auto1.get_info())
        print(auto1.pujceni_auta())

    elif vyber_funkce.lower() == "škoda":
        print(auto2.get_info())
        print(auto2.pujceni_auta())

    else:
        print("Neplatná volba značky vozidla.")