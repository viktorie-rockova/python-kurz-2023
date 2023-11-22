# OOP
# Objektově orientované programování je způsob, jak strukturovat a napsat programy pomocí konceptů zvaných "objekty". Objekty jsou základní stavební kameny OOP a reprezentují reálné nebo abstraktní entity.

# Zde jsou klíčové pojmy objektově orientovaného programování:

# Třída (Class): Třída je jakýsi "návod" nebo "šablona" pro vytváření objektů. Obsahuje atributy (vlastnosti) a metody (funkce), které popisují, co může objekt dělat.

# Objekt (Object): Objekt je instance třídy. To znamená, že je vytvořen podle specifikací dané třídy. Každý objekt má svůj vlastní stav (hodnoty atributů) a může provádět akce (metody).

# Atributy (Attributes): Atributy jsou vlastnosti objektu, které popisují jeho stav. Například, když mluvíme o třídě "Auto", atributy mohou být "barva", "rychlost", atd.

# Metody (Methods): Metody jsou funkce, které jsou součástí třídy a mohou být volány na objektech této třídy. Tyto metody popisují chování objektu. Například, metoda "start" pro třídu "Auto" by mohla spustit motor auta.

# Dědičnost (Inheritance): Dědičnost umožňuje vytvářet nové třídy na základě existujících. Nová třída může zdědit vlastnosti a metody existující třídy a může je rozšířit nebo přepsat.

# Polymorfismus: Polymorfismus umožňuje objektům jedné třídy používat metody jiné třídy. To znamená, že objekty mohou mít více podob (mohou být používány více způsoby).

# Zapouzdření (Encapsulation): Zapouzdření se týká skrývání vnitřního stavu objektu a omezení přístupu k němu. To pomáhá udržovat konzistentní stav objektu a minimalizuje přímý přístup k jeho atributům.

# V praxi je objektově orientované programování často používáno pro modelování skutečných situací nebo systémů, což vede k lepšímu návrhu a snazšímu údržbě kódu. OOP může zjednodušit programování, zlepšit přehlednost a znovupoužitelnost kódu. Je široce využíváno v jazyce jako je Java, Python, C++, a mnoha dalších.

# Uvažuj, že navrhuješ software pro zásilkovou společnost.

# Vytvoř třídu Package, která bude mít tři atributy - address, weight a state. Vytvoř metodu __init__, která uloží hodnoty parametrů metody do atributů.
# Přidej metodu get_info(), která vrátí informace o balíku jako řetězec. Uvažuj například větu "Balík na adresu Václavské Náměstí 12, Praha má hmotnost 0.25 kg je ve stavu nedoručen".
# Zkus si vytvořit alespoň dva objekty ze třídy Balik. U address uvažujeme typ řetězec (str), u weight desetinné číslo. U atributu state zadávej pro zjednodušení pouze dva stavy: doručen a nedoručen.
# Vypiš informace, které generuje metoda get_info(), na obrazovku, a ověř, že je vše v pořádku.

class Package:
  def __init__(self, address, weight, state):
    self.address = address
    self.weight = weight
    self.state = state

  def __str__(self):
    return f"Balik na adresu {self.address} ma hmotnost {self.weight} kg je ve stavu {self.state}."

  def deliver(self):
    if self.state == "dorucen":
      return "Balicek byl jiz dorucen."
    else:
      self.state = "dorucen"
      return "Doruceni ulozeno"

balicek1 = Package("Rimska 22, Praha 2", 3, "nedorucen")
balicek2 = Package("Videnska 1083, Praha 4", 12, "nedorucen")

# print(balicek1)
# print(balicek2)

doruceni_balicku_vysledek = balicek1.deliver()
print(doruceni_balicku_vysledek)
print(balicek1)


