# Ve slovníku zde najdeš Morseovu abecedu, kde jako klíč slouží znak v klasické abecedě a jako hodnota zápis znaku v Morseově abecedě.

# Napiš program, který se uživatele zeptá na text, který chce zapsat v Morseově abecedě. Uvažuj disciplinovaného uživatele, který zadává pouze znaky bez diakritiky, malá písmena atd. Na začátku uvažuj i to, že uživatel nezadává mezery.
# Projdi řetězec zadaný uživatelem. Najdi každý znak ve slovníku a vypiš ho na obrazovku v Morseově abecedě.
# Abychom měli celý kód vypsaný na jedné řádce, požádáme funkci print(), aby na konci výpisu nevkládala znak pro konec řádku, ale mezeru. To uděláme tak, že jako druhý argument funkce dáme argument end=" ".
# Nyní přidáme mezery. Uvažuj, že uživatel může zadat mezeru. Před tím, než budeš hledat znak ve slovníku, zkontroluj, zda znak není mezera. Pokud ano, vypiš znak lomítka /.

morse_code = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-",
}

morse_code[" "] = "/"

textkprekladu = input("Zadejte text pro preklad do morseovy abecedy:")

morse = []

isValid = ()

for letter in textkprekladu:
  letter = letter.lower()
  isValid = False
  for key, value in morse_code.items():
    if letter == key:
      morse.append(value)
      isValid = True
  if isValid == False:
    print("Neplatne zadani.")
    break

if isValid == True:
  for character in morse:
    print(character, end=" ")
