# Constants to inform DND character generation

races = ["Human", "Dwarf", "Halfling", "Elf"]
subraces = ["Aquilonian", "Border Kingdom", "Skandaharian", "Stygian", "Wood Elf"]

classes = ["Fighting-Man", "Magic-User", "Cleric", "Thief"]
FMSubclasses = ["Ranger", "Barbarian", "Paladin", "Anti-Paladin"]
MUSubclasses = ["Illusionist", "Necromancer"]
CLRSubclasses = ["Anti-Cleric", "Druid", "Shaman", "Monk"]

sexes = ["Male", "Female"]
PRBonus = ["-20%", "-10%", "+0%", "+5%", "+10%"]


# declarations of basic variables

# redundant, just in case subraces is turned OFF.
human_male_names = ["Guiscard", "Sciodin", "Hollin", "Gwalon", "Faelan", "Loic", "Barald", "Agbeorn", "Darnvith", "Balthus", "Tiberias", "Cossos", "Flavius", "Attius", "Ascalante", "Dionus", "Epimetreus", "Pelias", "Trinculo", "Nabonidas", "Horatio", "Chiron", "Lucius", "Claudio", "Mercutio", "Tybalt", "Strato", "Martius", "Mycaenas", "Alastor"]
human_female_names = ["Maerbina", "Natala", "Vateesa", "Yasmela", "Khorala", "Myshalla", "Cymoril", "Hippolyta", "Octavia", "Wyldora", "Linaeya", "Valhame", "Isgar", "Domla", "Wenhild", "Iwohd", "Lychorida", "Dionyza", "Sylvia", "Cymbeline", "Calphurnia", "Cressida", "Innogen", "Coryda"]
human_last_names = [""]

# roman-sounding male names, howard's female names
aquilonian_male_names = ["Tiberias", "Cossos", "Flavius", "Attius", "Ascalante", "Dionus", "Epimetreus", "Pelias", "Trinculo", "Nabonidas"]
aquilonian_female_names = ["Maerbina", "Natala", "Vateesa", "Yasmela", "Khorala", "Myshalla", "Cymoril", "Hippolyta", "Octavia"]
aquilonian_last_names = [""]

borderking_male_names = ["Guiscard", "Sciodin", "Hollin", "Gwalon", "Faelan", "Loic", "Barald", "Agbeorn", "Darnvith", "Balthus"]
borderking_female_names = ["Wyldora", "Linaeya", "Valhame", "Isgar", "Domla", "Wenhild", "Iwohd"]
borderking_last_names = [""]

skanda_male_names = ["Yorn", "Throf", "Vigtham", "Hyrrad", "Soleigr", "Sigferth", "Bjorgulf", "Thorred", "Harrek", "Halvdan"]
skanda_female_names = ["Hildrid", "Aestrid", "Thorlja", "Thorve", "Ashild", "Halla", "Holmfrid"]
skanda_last_names = [""]

# zingarans are spanish(esque) but here I've taken mostly names from the Shakespearean generator
# for a tone of elegance and aristocracy fallen into decay.
zingaran_male_names = ["Horatio", "Chiron", "Lucius", "Claudio", "Mercutio", "Tybalt", "Strato", "Martius", "Mycaenas", "Alastor"]
zingaran_female_names = ["Lychorida", "Dionyza", "Sylvia", "Cymbeline", "Calphurnia", "Cressida", "Innogen", "Coryda"] 
zingaran_last_names = ["Pedrerro", "Zamorano", "Coronel", "Morterero", "Zaragoza", "Ascaso", "Orellana", "Valderas", "del Mallen", "del Ocana", "del Villareal"]

turanian_male_names = ["Bircan", "Nuri", "Akman", "Kai", "Yasam", "Armagan", "Aydolun", "Tozun", "Ertas", "Arif"]
turanian_female_names = ["Ediz", "Hazret", "Aysu", "Icten", "Latife", "Elsin", "Eylul", "Nehir"] 
turanian_last_names = [""]

# Ancient Egyptian (obviously) with female first names as last names too. Matrilinial.
stygian_male_names = ["Shak-amen", "Aker", "Asychis", "Ka-met-ef", "Psamtic", "Mesocris", "Met-su-aut", "Sebekem", "Quas-shi", "Amun-ra"]
stygian_female_names = ["Khata", "Umaya", "Zesiro", "Renenet", "Rashida", "Menai-rata", "Nefertiri", "Heqet"] 
stygian_last_names = ["Akela", "Hap-tek", "Karo-amat", "Meshkenet", "Sa-khana", "Nebt-nehi", "Ta-ba-ret", "Maat-amanset"]

# I thought a Celtic type might work, but went with Barbarian fantasy generator and some Old High German
cimmmerian_male_names = ["Conn", "Vetur", "Jotmon", "Yinderd", "Ipror", "Jagfend", "Gholnen", "Llasild", "Khurmen", "Aulfwic", "Heffric", "Saeldrid", "Thobald", "Siegnan"]
cimmmerian_female_names = ["Faya", "Reha", "Agnis", "Sonja", "Shisha", "Dolma", "Gihlfe", "Wedlash", "Alwyn", "Gerhild"] 
cimmmerian_last_names = [""]

hyrkanian_male_names = ["Sayanov", "Kurchin", "Kulik", "Suslyakov", "Surikov", "Ilyushin", "Moryakov", "Yuzkov", "Rozovsky", "Viktor", "Damirov"]
hyrkanian_female_names = ["Talanova", "Silestrova", "Alena", "Amalia", "Kalantaya", "Inessa", "Ryheakova", "Allesia"] 
hyrkanian_last_names = ["Ilyich", "Artonovich", "Vadimovich", "Olegovich", "Artemovich", "Ulyanov", "Kulyanov", "Sigalov", "Astanokov", "Zinovich", "Vilanova"]

# went with Chinese rather than Japanese. Japanese could be added in as "Ainu" or something.
khitian_male_names = ["Lang", "Qin", "Liao", "Zhuan", "Jia", "Xiang", "Fen", "Tian", "Zhou", "Li", "Qiao"]
khitian_female_names = ["Xi", "Zou", "Shi", "Xun", "Sun", "Lho", "Xia", "Tan", "Su", "Yi", "Yu"] 
khitian_last_names = ["Peng", "Feng", "Xuefeng", "Zheng", "Jian", "Xieren", "Cai", "Yong", "Yuhong", "Hai"]

# unused
vendyan_male_names = ["Horatio", "Chiron", "Lucius", "Claudio", "Mercutio", "Tybalt", "Strato", "Martius", "Mycaenas", "Alastor"]
vendyan_female_names = ["Lychorida", "Dionyza", "Sylvia", "Cymbeline", "Calphurnia", "Cressida", "Innogen", "Coryda"] 
vendyan_last_names = [""]

# unused
juman_male_names = ["Horatio", "Chiron", "Lucius", "Claudio", "Mercutio", "Tybalt", "Strato", "Martius", "Mycaenas", "Alastor"]
juman_female_names = ["Lychorida", "Dionyza", "Sylvia", "Cymbeline", "Calphurnia", "Cressida", "Innogen", "Coryda"] 
juman_last_names = [""]



dwarf_male_names = ["Dolmec", "Thrastil", "Vasdrad", "Sindur", "Lodur", "Baffur", "Vuldan", "Glifon", "Thafur", "Thurbur", "Glirvun", "Nendar", "Floto", "Throlim"]
dwarf_female_names = ["Jozithra", "Elzulin", "Hethika", "Koteline", "Nufelda"]
dwarf_last_names = [""]

elf_male_names = ["Amarthedir", "Harthedir", "Lledon", "Ninthalor", "Vesryn", "Tarathiel", "Lysanthir"]
elf_female_names = ["Lithoniel", "Tialha", "Nuala", "Alasse", "Eshryneth", "Aerith", "Lindis", "Deulara"]
elf_last_names = ["tir Glioscarnach", "tir Fuar", "tir Airgid"]

woodelf_male_names = ["Gwaelben", "Yrchanar", "Triven", "Galaspen", "Maethor", "Aelchanar", "Gwilithien"]
woodelf_female_names = ["Liriel", "Achariel", "Malanil", "Nirnith", "Cabedis", "Teliadis", "Naerhel", "Uaneth"]
woodelf_last_names = ["na Scaethanna", "na Cogarnach", "na n-Iontas"]

halfling_male_names = ["Alberic", "Audomar", "Godobald", "Halfred", "Hlodver", "Cosimo"]
halfling_female_names = ["Verbena", "Rosa", "Cercis", "Beryl", "Selwyn", "Tabita"]
halfling_last_names = ["Potts", "Mugwort", "Brockhouse", "Sandshank", "Goodbody", "Townsend"]

# made up silly sounding dwarvish names
gnome_male_names = ["Bombi", "Medden", "Flifur", "Eltas", "Jeleson", "Granwe", "Elmin", "Elkan", "Rimmi", "Urdur", "Pinka", "Nebi", "Tebi", "Yebi"]
gnome_female_names = ["Sella", "Flyfa", "Heccati", "Kafa", "Wynni"]
gnome_last_names = [""]


# Equipment.
# I am here assuming that retainers need not roll for 30-180 GP and spend it on equipment, but rather
# just pick (probabilistically) from the basic options afforded them. I am not anticipating that 
# misc. gear (rope and spikes and so on) need be enumerated.

eqt_mu = ["Dagger"]
eqt_simple = ["Spear", "Mace"]
eqt_sidearms = ["Dagger", "Sword"]
eqt_blunt = ["Mace", "Quarterstaff", "Warhammer"]
eqt_misc_big = ["Battleax", "Morningstar", "Flail", "Polearm"]
eqt_big_blades = ["Broadsword", "Two-Handed Sword"]
eqt_knightly = ["Lance"]
eqt_horse = ["Draft Horse", "Light Horse", "Heavy Warhorse"]

eqt_simple_ranged = ["Shortbow", "Sling"]
eqt_expert_ranged = ["Horsebow", "Longbow", "Composite Bow"]
eqt_exotic_ranged = ["Light Crossbow", "Heavy Crossbow"]

eqt_unarmored = ["Robes", "Aristocratic Clothes", "Stained Travel Clothes"]
eqt_light_armor = ["Leather"]
eqt_mid_armor = ["Chain Mail"]
eqt_heavy_armor = ["Chain Mail", "Plate"]
eqt_barbaric_armor = ["Unarmored", "Leather", "Chain Mail"]
eqt_shield = ["Shield"]

eqt_holysymbol = ["Holy Symbol", "Silvered Holy Symbol"]
eqt_thievestools = ["Thieves' Tools"]
eqt_spellbook = ["Spellbook"]

eqt_gear = ["Holy Water"]

eqt_accessories = ["Silken Breeches", "Fine Leather Boots", "Wide-brimmed Hat"]
eqt_barbaric_accessories = ["Furs", "Horned Helm", "Antlered Helm"]


# spells
mu_first_level_spells = ["Detect Magic", "Hold Portal", "Magic Missile", "Read Languages", "Shield", "Light", "Charm Person", "Sleep"]
ill_first_level_spells = [""]
necro_first_level_spells = [""]

cantrips = ["Gust of Wind", "Spark from Nothing", "Control Flame", "Ray of Frost", "Lighten Load", "Prestidigitate", "Minor Telekinesis", "Trick of the Voice", "Puff of Smoke", "Weigh Down"]