elements = {"Ac":"Actinium","Ag":"Silver","Al":"Aluminum","Am":"Americium",
"Ar":"Argon","As":"Arsenic","At":"Astatine","Au":"Gold","B":"Boron","Ba":"Barium",
"Be":"Beryllium","Bh":"Bohrium","Bi":"Bismuth","Bk":"Berkelium","Br":"Bromine",
"C":"Carbon","Ca":"Calcium","Cd":"Cadmium","Ce":"Cerium","Cf":"Californium",
"Cl":"Chlorine","Cm":"Curium","Cn":"Copernicium","Co":"Cobalt","Cr":"Chromium",
"Cs":"Cesium","Cu":"Copper","Db":"Dubnium","Ds":"Darmstadtium","Dy":"Dysprosium",
"Er":"Erbium","Es":"Einsteinium","Eu":"Europium","F":"Fluorine","Fe":"Iron",
"Fl":"Flerovium","Fm":"Fermium","Fr":"Francium","Ga":"Gallium","Gd":"Gadolinium",
"Ge":"Germanium","H":"Hydrogen","He":"Helium","Hf":"Hafnium","Hg":"Mercury",
"Ho":"Holmium","Hs":"Hassium","I":"Iodine","In":"Indium","Ir":"Iridium",
"K":"Potassium","Kr":"Krypton","La":"Lanthanum","Li":"Lithium","Lr":"Lawrencium",
"Lu":"Lutetium","Lv":"Livermorium","Mc":"Moscovium","Md":"Mendelevium",
"Mg":"Magnesium","Mn":"Manganese","Mo":"Molybdenum","Mt":"Meitnerium",
"N":"Nitrogen","Na":"Sodium","Nb":"Niobium","Nd":"Neodymium","Ne":"Neon",
"Nh":"Nihonium","Ni":"Nickel","No":"Nobelium","Np":"Neptunium","O":"Oxygen",
"Og":"Oganesson","Os":"Osmium","P":"Phosphorus","Pa":"Protactinium","Pb":"Lead",
"Pd":"Palladium","Pm":"Promethium","Po":"Polonium","Pr":"Praseodymium",
"Pt":"Platinum","Pu":"Plutonium","Ra":"Radium","Rb":"Rubidium","Re":"Rhenium",
"Rf":"Rutherfordium","Rg":"Roentgenium","Rh":"Rhodium","Rn":"Radon",
"Ru":"Ruthenium","S":"Sulfur","Sb":"Antimony","Sc":"Scandium","Se":"Selenium",
"Sg":"Seaborgium","Si":"Silicon","Sm":"Samarium","Sn":"Tin","Sr":"Strontium",
"Ta":"Tantalum","Tb":"Terbium","Tc":"Technetium","Te":"Tellurium","Th":"Thorium",
"Ti":"Titanium","Tl":"Thallium","Tm":"Thulium","Ts":"Tennessine","U":"Uranium",
"V":"Vanadium","W":"Tungsten","Xe":"Xenon","Y":"Yttrium","Yb":"Ytterbium",
"Zn":"Zinc","Zr":"Zirconium"}


def dedup(list):
    seen = set()
    sv = 1
    for a in list:
        if a in seen:
            list[list.index(a)] = a + str(sv)
            if sv != 9:
                sv += 1
            else:
                sv = 1
        seen.add(a)


letters = []
fs = []
fel = []
x = 5
skip = ""
done = False


sentence = input("Enter a sentence: ")

for character in sentence:
    letters.append(character)

for item in letters:
    if item == " ":
        letters.remove(item)

dedup(letters)

print(letters)

for letter in letters:
    if skip != letter:
        for element in elements:
            if not done:
                if letters.index(letter) + 1 < len(letters):
                    if str(letter[0].capitalize() + letters[letters.index(letter) + 1][0]) == element:
                        fs.append(element)
                        skip = letters[letters.index(letter) + 1]
                        done = True
        for element in elements:
            if not done:
                if letter[0].capitalize() == element:
                    fs.append(element)
                    done = True
    done = False

print(fs)
for item in fs:
    fel.append(elements.get(item))
print(fel)
