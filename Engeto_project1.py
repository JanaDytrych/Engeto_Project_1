'''
author =
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

# promenne
prihlaseni = {
    "bob" : "123",
    "ann":"pass123",
    "mike":"password123",
    "lizz":"pass123"
}
oddelovac = "-" * 45
print(f"{'WELCOME!':^45}")
print(f"{'- For registered users only -': ^45}")
print(oddelovac)

user = input("Jmeno: ")
heslo = input("Heslo: ")
pocet_textu = len(TEXTS)

# zjistim, jestli udaje patri nasim uzivatelum
if prihlaseni.get(user) != heslo:
    print(oddelovac)
    print("Sorry, wrong user's name or password.")
    quit()
else:
    print(oddelovac)
    print("Welcome to the app,", user, "!")

print(f"We have {pocet_textu} texts to be analyzed.")
print(oddelovac)

cislo_textu = input("Enter a number between 1 and 3 to select: ")

if not cislo_textu.isnumeric() or int(cislo_textu) > int(pocet_textu):
    print("Your input is not correct, this is the end:(")
    print(oddelovac)
    quit()
else:
    print(oddelovac)

# pocet slov
slova_text = []

for slovo in TEXTS[int(cislo_textu)-1].split():
    slova_text.append(slovo.strip(",:;."))

pocet_slov = len(slova_text)

# pocitani prvku v textu
prvni_velke = 0
velke_pismena = 0
male_pismena = 0
pocet_cisel = 0
cisla_text = []

for slovo in slova_text:
    if slovo.istitle():
        prvni_velke += 1
    elif slovo.isupper() and slovo.isalpha():
        velke_pismena += 1
    elif slovo.islower():
        male_pismena += 1
    elif slovo.isnumeric():
        pocet_cisel += 1
        cisla_text.append(int(slovo))

suma_cisel = sum(cisla_text)

# printy na vysledky pocitani prvku a cisel v textu
print(f"""
There are {pocet_slov} words in the selected text.
There are {prvni_velke} titlecase words.
There are {velke_pismena} uppercase words.
There are {male_pismena} lowercase words.
There are {pocet_cisel} numeric strings.
The sum of all the numbers is {suma_cisel}.
{oddelovac}
""")

#delka slov
delka_slov = dict()

for slovo in slova_text:
    delka = len(slovo)
    if delka not in delka_slov:
        delka_slov[delka] = 1
    else:
        delka_slov[delka] += 1

#serazeni podle delky slov
poradi = sorted(list(delka_slov.items()))[:]

#print(poradi)
print(f"{'LEN':>2} | {'OCCURENCES':^17}  |{'NR.':<2}")
# vypis slova
for i, dvojice in enumerate(sorted(poradi)):
    hvezda = "*" * int(dvojice[1])
    print(
        f"{dvojice[0]:>4}|{hvezda: <20}|{dvojice[1]:<2}",
        sep="\n",
        )
print(oddelovac)
print("Thank you for using our Text analysis Tool!")