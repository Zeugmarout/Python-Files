# OD&D with Chainmail Character Generator
# see https://www.statuscake.com/blog/creating-a-character-in-python/


#%%

# imports
import random
import numpy as np
import json

# ask the user how many characters to generate
num_chars_str = input("No. of characters to generate: ")
num_chars = int(num_chars_str)




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
gnome_last_names = ["", "", ""]



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

#%%

# definition of rolling ability scores

def __getAbilityScores__():
    abilScores = []
    for x in range(6):  # outer loop, all 6 scores

        abilScore = []
        for x in range(3): # inner loop, summing 3 dice
            abilScore.append(random.randint(1,6))
            
        abilScores.append(sum(abilScore))

    unsortedScores = {'STR':0, 'INT':0, 'WIS':0, 'DEX':0, 'CON':0, 'CHA':0}

    unsortedScores["STR"] = abilScores[0]
    unsortedScores["INT"] = abilScores[1]
    unsortedScores["WIS"] = abilScores[2]
    unsortedScores["DEX"] = abilScores[3]
    unsortedScores["CON"] = abilScores[4]
    unsortedScores["CHA"] = abilScores[5]

    return unsortedScores # unsortedScores included just in case another method is selected, such as swap any 2 





#%%

def __getClass__( attributes ):

    # default class
    character_class = "Fighting-Man"

    # redundant set of attributes for doing >= with later
    strength = attributes.get("STR")
    intelligence = attributes.get("INT")
    wisdom = attributes.get("WIS")
    dexterity = attributes.get("DEX")
    constitution = attributes.get("CON")
    charisma = attributes.get("CHA")

    # set of attributes JUST for setting parent class through Prime Requisite
    # otherwise odd errors will turn up where if CON or CHA is highest score,
    # character class will stay Fighter no matter if others (e.g. DEX) are higher than STR
    PRattributes = {}
    PRattributes["STR"] = strength
    PRattributes["INT"] = intelligence
    PRattributes["WIS"] = wisdom
    PRattributes["DEX"] = dexterity

    highest_attribute = max(PRattributes, key=PRattributes.get)

    # Assigns character class based on the highest attribute.

    # Some messy code has been added in to deal with tiebreakers because highest_attribute gets 
    # confused in case of duplicate scores. 

    # For now, these are all running on the stringent Strategic Revue/Greyhawk etc. 
    # ability score requirements, rather than a more lenient dual-PR system. 
    # Retainers are not allowed to swap ability scores (in this code.)
    # Exceptions so far being the Ranger (int, wis and con requirements all dropped by 3.)

    # These many subclasses will have a function later that turns them 'off',
    # ie. back into their parent class, if the user did not selected against them.
    # Even if you play purist OD&D, the subclasses can still inform the character's concept.

    # Just for fun and symmetry we are adding OSE's Necromancer and an adapted Gazeteer Shaman (plus ACKS),
    # the Paladin/Anti-Paladin, the Illusionist, Druid, Ranger...

    # Final note on the multiplicity of classes: we are here assuming that CONAN THE BARBARIAN
    # was a multi-classed F-M/Thief, rather than creating a Barbarian subclass, but a Barbarian could
    # easily be created (FM who can run up walls, etc.) who selects for high STR and CON.
    # Later note: code added to support Barbarian selection, though I doubt I'll use it.

    # Races will apply their own ability score requirements (as per BX) later on, given class.

    # Alignment is here generated within the function to determine whether a cleric is 
    # one of the other types, based on a distribution of law 3 in 6, neutral 2 in 6, chaotic 1 in 6. 
    # later on an actual function will use class and race to determine alignment.
    tempALN = random.randint(1,6)
    # Where 1 to 3 is Lawful, 4 or 5 is Neutral and 6 is Chaotic.

    tempChoose = random.randint(1,6)
    # this is one more just for deciding on tiebreakers between classes.

    # In descending order of qualifying for the class:

    # FM Subclasses and Monk block
    if (highest_attribute == "STR" and charisma >= 17) or (strength >= 9 and charisma >= 17):
        if tempALN <= 5:
            character_class = "Paladin"
        elif tempALN == 6:
            character_class = "Anti-Paladin" # only a 1 in 6 chance of returning a Chaotic Paladin.
    
    elif highest_attribute == "STR" and intelligence >= 9 and wisdom >= 9 and constitution >= 15:
        # note the change in attribute requirements. Because more lenient, only 66% chance of returning Ranger.
        if tempChoose >= 3:
            character_class = "Ranger" 
        else:
            character_class = "Barbarian"
    
    # and now the backup chance yielding Barbarian in case int or wis are under 9.
    elif highest_attribute == "STR" and constitution >= 15:
        character_class = "Barbarian"
    
    # extremely unlikely, as written, so changed to lower requirements:
    elif highest_attribute == "WIS" and dexterity >= 12:
        if tempChoose >= 3:
            character_class = "Monk"
        else:
            character_class = "Cleric"

    # Thief and Assassin block
    elif highest_attribute == "DEX" and strength >= 12 and intelligence >= 12 and dexterity >= 12:
        character_class = "Assassin"
    elif (dexterity == wisdom and dexterity >= strength and dexterity > intelligence):
        character_class = "Thief" 
        # this was added because the max function iterates in order of insertion. The only tiebreaker
        # I'm concerned with is that a high-dex and wis character be a Thief rather than a Cleric.
    elif highest_attribute == "DEX" and intelligence >= 12:
        if tempChoose <= 2:
            character_class = "Illusionist"
        else:
            character_class = "Thief"
    elif highest_attribute == "DEX":
        character_class = "Thief"

    # Magic-User and Illusionist block
    elif highest_attribute == "INT" and dexterity >= 15:
        character_class = "Illusionist"
    # taking incredible liberties here to add in the Necromancer:
    elif highest_attribute == "INT" and wisdom >= 9 and tempALN >= 4:
        character_class = "Necromancer"
    elif highest_attribute == "INT":
        character_class = "Magic-User" 

    # Cleric, Anti-Cleric, Druid and Shaman block
    elif highest_attribute == "WIS": 
        if tempALN <= 3:
            character_class = "Cleric"
        elif tempALN == 4:
            character_class = "Shaman"
        elif tempALN == 5:
            character_class = "Druid"
        elif tempALN == 6:
            character_class = "Anti-Cleric"
    else:
        character_class = "Fighting-Man"

    
    return character_class


# testscores = __getAbilityScores__()

##### MANUAL TEST 
## Creating an empty dictionary
## my_dict = {}
## my_dict['STR'] = 11
## my_dict['INT'] = 12
## my_dict['WIS'] = 13
## my_dict['DEX'] = 10
## my_dict['CON'] = 9
## my_dict['CHA'] = 16

## testclass = __getClass__(my_dict)
# testclass = __getClass__(testscores)

# print(testscores)
## print(my_dict)
# print(testclass)

#%%

    # getRace applies probabilities to the class to spit out a race.

def __getRace__( charclass, attributes ):

    # This function applies a probabilistic distribution that varies by class.
    # Before the probabities are applied, we check to see if the race can be qualified for
    # according to BX ability score minimums. (with an additional Dex reqt for Elves.)
    # (9 Int and Dex for Elves, 9 Con for Dwarves, 9 Dex and Con for Halflings.) 

    # redundant declaration
    # race = "Human"
    result = "Human"

    # redundant set of attributes for doing >= with later
    strength = attributes.get("STR")
    intelligence = attributes.get("INT")
    wisdom = attributes.get("WIS")
    dexterity = attributes.get("DEX")
    constitution = attributes.get("CON")
    charisma = attributes.get("CHA")

    # Define possible outcomes
    outcomes = ["Elf", "Dwarf", "Halfling", "Gnome", "Human"]
    
    # setting up variables 
    elfchance = 0
    dwarfchance = 0
    halflingchance = 0
    gnomechance = 0

    match charclass:
        case "Fighting-Man":
            if intelligence >= 9 and dexterity >= 9:
                elfchance = 0.55
            #elif constitution >= 9 and dexterity >= 9:
                #halflingchance = 0.05
            elif constitution >= 9:
                dwarfchance = 0.55
                #gnomechance = 0.15 
        
        case "Ranger": # allowing Rangers to be (wood-)elves too
             if intelligence >= 9 and dexterity >= 9:
                elfchance = 0.55       

        # redundant blocks for subclasses, all Human only.
        case "Paladin":      
            result = "Human"
        case "Anti-Paladin":
            result = "Human"
        case "Monk":
            result = "Human"
        case "Asassin":
            result = "Human"
        case "Necromancer":
            result = "Human"

        # Cleric block. GH does introduce chances to be demihuman cleric...
        # For now only humans may be Clerics and Anti-Clerics.
        case "Cleric":
            result = "Human"
        case "Anti-Cleric":
            result = "Human"
        
        # Thief chances. Pretty high for non-Humans.
        case "Thief":
            if intelligence >= 9 and dexterity >= 9:
                elfchance = 0.45
            elif constitution >= 9 and dexterity >= 9:
                halflingchance = 0.75
                dwarfchance = 0.15
            elif constitution >= 9:     # this is an extreme edge case
                dwarfchance = 0.45       # so chances are much higher
                gnomechance = 0.45       # for demi-humans, to yield interesting results
            
        case "Illusionist":
            if constitution >= 9:
                gnomechance = 0.65
        
        case "Magic-User":
            if intelligence >= 9 and dexterity >= 9:
                elfchance = 0.55
            elif constitution >= 9:
                gnomechance = 0.25

        case "Druid":
            if intelligence >= 9 and dexterity >= 9:
                elfchance = 0.55

        case "Shaman":
            if constitution >= 9:
                dwarfchance = 0.55 
            
    # Define the probabilities for each outcome
    humanchance = 1-(elfchance + dwarfchance + halflingchance + gnomechance)
    probabilities = [elfchance, dwarfchance, halflingchance, gnomechance, humanchance]
    # Sample from the distribution
    result = np.random.choice(outcomes, p=probabilities)

    return result

# The chances of nonhuman retainers is fairly rare, which fits well the 
# assumptions of OD&D generally. Special envoys can always be made to elfland 
# or dwarfland, after all.

# A similar function to determine subrace probabilistically
# E.g. elven druid will be wood elf 100%
# Human F-M might be any of the subraces (Aquilonian etc.)

def __getSubRace__(charclass, race):

    # this is very dumb and finicky, and highly campaign-specific.  However:

    # set up variables
    subrace = ""
    
    # Define possible human outcomes
    outcomes = ["Aquilonian", "Zingaran", "Skandaharian", "Turanian", "Stygian", "Cimmerian", "Hyrkanian", "Khitai", "Vendyan", "Border Kingdom"]

    AquilChance = 0
    ZingarChance = 0
    SkandaChance = 0
    TuraChance = 0
    StygiChance = 0
    CimmerChance = 0
    HyrkanChance = 0
    KhitChance = 0      # It's a little heavy on the Hyborian Age stuff... maybe cut them down to just a few?
    VendyChance = 0


    roll = random.randint(1,6)
    result = ""

    match race:
        case "Human":
            if charclass == "Fighting-Man":
                AquilChance = 0.20
                ZingarChance = 0.20
                SkandaChance = 0.10
            elif charclass == "Barbarian":
                CimmerChance = 1.00
            elif charclass == "Ranger":
                AquilChance = 0.30
                ZingarChance = 0.10
                HyrkanChance = 0.10
            elif charclass == "Paladin":
                TuraChance = 0.15
                AquilChance = 0.85
            elif charclass == "Anti-Paladin":
                HyrkanChance = 0.33
                AquilChance = 0.33
                ZingarChance = 0.34
            elif charclass == "Magic-User":
                AquilChance = 0.20
                ZingarChance = 0.20
                StygiChance = 0.20
            elif charclass == "Illusionist":
                AquilChance == 0.80
            elif charclass == "Necromancer":
                StygiChance = 0.50
                ZingarChance = 0.50
            elif charclass == "Thief":
                AquilChance = 0.10
                ZingarChance = 0.30
                HyrkanChance = 0.30
            elif charclass == "Assassin":
                ZingarChance = 0.50
                AquilChance = 0.25
                KhitChance = 0.25
            elif charclass == "Cleric":
                AquilChance = 0.60
            elif charclass == "Anti-Cleric":
                AquilChance = 0.60
            elif charclass == "Shaman":
                HyrkanChance = 0.60
            elif charclass == "Monk":
                # VendyChance = 0.30
                KhitChance = 0.60
            else:
                AquilChance = 0.15
                ZingarChance = 0.15
                SkandaChance = 0.05
                TuraChance = 0
                StygiChance = 0
                CimmerChance = 0
                HyrkanChance = 0
                KhitChance = 0
                VendyChance = 0


            # Define the probabilities for each Human outcome
            BorderKingdom = 1-(AquilChance + ZingarChance + SkandaChance + TuraChance + StygiChance + CimmerChance + HyrkanChance + KhitChance + VendyChance)
            probabilities = [AquilChance, ZingarChance, SkandaChance, TuraChance, StygiChance, CimmerChance, HyrkanChance, KhitChance, VendyChance, BorderKingdom]
            # Sample from the distribution
            result = np.random.choice(outcomes, p=probabilities)

            return result
        
        case "Dwarf":
            result = "Dwarf"
            return result
        
        case "Halfling":
            result = "Halfling"
            return result
        
        case "Gnome":
            result = "Gnome"
            return result
        
        case "Elf":
            if charclass == "Ranger":
                result = "Wood Elf"
            elif charclass == "Druid":
                result = "Wood Elf"
            elif charclass == "Fighting-Man":
                result = "Elf"
            elif charclass == "Magic-User":
                result = "Elf"
            else:
                if roll <= 3:
                    result = "Wood Elf"
                else:
                    result = "Elf"

            return result
                

    
            



    
    



#%%

    # getAlignment takes in the class and race to pick an alignment.

def __getAlignment__( charclass, race ):
    result = "Neutral"
    roll = random.randint(1,6)

    # Demi-human block  (Elves and Gnomes assumed more likely to be Neutral)
    if race == "Elf":
        if roll >= 5:
            result = "Lawful"
    elif race == "Dwarf":
        if roll >= 3:
            result = "Lawful"
    elif race == "Gnome":
        if roll >= 5:
            result = "Lawful"
    elif race == "Halfling":
        if roll >= 3:
            result = "Lawful"
    
    # Lawful Class Block
    elif charclass == "Paladin":
            result = "Lawful"
    elif charclass == "Ranger":
            result = "Lawful"

    # Leans heavily towards Law Block
    elif charclass == "Cleric":
        if roll <= 4:
            result = "Lawful"
        else:
            result = "Neutral"

    # Neutral Block
    elif charclass == "Druid":
            result = "Neutral"
    elif charclass == "Assassin":
            result = "Neutral"
    elif charclass == "Barbarian":
            if roll >= 5:
                result = "Chaotic"
    elif charclass == "Thief":
            if roll >= 5:
                result = "Chaotic"

    # Chaotic Block
    elif charclass == "Anti-Paladin":
        result = "Chaotic"
    elif charclass == "Anti-Cleric":
        if roll >= 3:
            result = "Chaotic"

    # Less-likely to be Lawful Block
    elif charclass == "Magic-User":
        if roll >= 5:
            result = "Chaotic"
    elif charclass == "Necromancer":
        if roll >= 3:
            result = "Chaotic"

    # Catch-all Block that assumes campaign dist. of alignments 
    # Where 1 to 2 is Lawful, 3 4 or 5 is Neutral and 6 is Chaotic...

    else: 
        if roll <= 2:
            result = "Lawful"
        elif roll <= 5:
            result = "Neutral"
        else:
            result = "Chaotic"

    
    return result 
#%%

def __getSex__( race , charclass, attributes ):

    # setting up a variable to contain a % chance of character being female
    femmechance = 0

    isMartial = False

    match charclass:
        case "Fighting-Man":
            isMartial = True
        case "Paladin":
            isMartial = True
        case "Anti-Paladin":
            isMartial = True
        case "Ranger":
            isMartial = True
        case "Barbarian":
            isMartial = True

    if race == "Dwarf":
        femmechance = 0
    elif race == "Gnome":
        femmechance = 33
    elif race == "Halfing":
        femmechance = 33
    elif race == "Human" and isMartial:
        femmechance = 10
    elif race == "Human":
        femmechance = 40
    elif race == "Elf":
        femmechance = 50

    # random percentile roll-under that will change adventurer to female

    randRoll = random.randint(1,100)
    if randRoll <= femmechance:
        sex = "Female"
    else:
        sex = "Male"

    return sex



#%%

def __getRandomName__( race, gender ):

    name = ""

    if race == "Human" and gender == "Male":
        name = human_male_names[random.randint(0,len(human_male_names)-1)]
        
    if race == "Human" and gender == "Female":
        name = human_female_names[random.randint(0,len(human_female_names)-1)]

    if race == "Aquilonian" and gender == "Male":
        name = aquilonian_male_names[random.randint(0,len(aquilonian_male_names)-1)]
        
    if race == "Aquilonian" and gender == "Female":
        name = aquilonian_female_names[random.randint(0,len(aquilonian_female_names)-1)]

    if race == "Zingaran" and gender == "Male":
        name = zingaran_male_names[random.randint(0,len(zingaran_male_names)-1)]
        
    if race == "Zingaran" and gender == "Female":
        name = zingaran_female_names[random.randint(0,len(zingaran_female_names)-1)]

    if race == "Border Kingdom" and gender == "Male":
        name = borderking_male_names[random.randint(0,len(borderking_male_names)-1)]
        
    if race == "Border Kingdom" and gender == "Female":
        name = borderking_female_names[random.randint(0,len(borderking_female_names)-1)]

    if race == "Skandaharian" and gender == "Male":
        name = skanda_male_names[random.randint(0,len(skanda_male_names)-1)]
        
    if race == "Skandaharian" and gender == "Female":
        name = skanda_female_names[random.randint(0,len(skanda_female_names)-1)]

    if race == "Cimmerian" and gender == "Male":
        name = cimmmerian_male_names[random.randint(0,len(cimmmerian_male_names)-1)]
        
    if race == "Cimmerian" and gender == "Female":
        name = cimmmerian_female_names[random.randint(0,len(cimmmerian_female_names)-1)]

    if race == "Hyrkanian" and gender == "Male":
        name = hyrkanian_male_names[random.randint(0,len(hyrkanian_male_names)-1)]
        
    if race == "Hyrkanian" and gender == "Female":
        name = hyrkanian_female_names[random.randint(0,len(hyrkanian_female_names)-1)]

    if race == "Stygian" and gender == "Male":
        name = stygian_male_names[random.randint(0,len(stygian_male_names)-1)]
        
    if race == "Stygian" and gender == "Female":
        name = stygian_female_names[random.randint(0,len(stygian_female_names)-1)]

    if race == "Turanian" and gender == "Male":
        name = turanian_male_names[random.randint(0,len(turanian_male_names)-1)]
        
    if race == "Turanian" and gender == "Female":
        name = turanian_female_names[random.randint(0,len(turanian_female_names)-1)]

    if race == "Khitai" and gender == "Male":
        name = khitian_male_names[random.randint(0,len(khitian_male_names)-1)]
        
    if race == "Khitai" and gender == "Female":
        name = khitian_female_names[random.randint(0,len(khitian_female_names)-1)]

    if race == "Dwarf" and gender == "Male":
        name = dwarf_male_names[random.randint(0,len(dwarf_male_names)-1)]

    if race == "Dwarf" and gender == "Female":
        name = dwarf_female_names[random.randint(0,len(dwarf_female_names)-1)]

    if race == "Halfling" and gender == "Male":
        name = halfling_male_names[random.randint(0,len(halfling_male_names)-1)]

    if race == "Halfling" and gender == "Female":
        name = halfling_female_names[random.randint(0,len(halfling_female_names)-1)]

    if race == "Elf" and gender == "Male":
        name = elf_male_names[random.randint(0,len(elf_male_names)-1)]

    if race == "Elf" and gender == "Female":
        name = elf_female_names[random.randint(0,len(elf_female_names)-1)]

    if race == "Wood Elf" and gender == "Male":
        name = woodelf_male_names[random.randint(0,len(woodelf_male_names)-1)]

    if race == "Wood Elf" and gender == "Female":
        name = woodelf_female_names[random.randint(0,len(woodelf_female_names)-1)]

    if race == "Gnome" and gender == "Male":
        name = gnome_male_names[random.randint(0,len(gnome_male_names)-1)]

    if race == "Gnome" and gender == "Female":
        name = gnome_female_names[random.randint(0,len(gnome_female_names)-1)]

    match race:
        case "Human": 
            if human_last_names != [""]:
                name += f' {human_last_names[random.randint(0,len(human_last_names)-1)]}'
        case "Aquilonian": 
            if aquilonian_last_names != [""]:
                name += f' {aquilonian_last_names[random.randint(0,len(aquilonian_last_names)-1)]}'
        case "Border Kingdom": 
            if borderking_last_names != [""]:
                name += f' {borderking_last_names[random.randint(0,len(borderking_last_names)-1)]}'
        case "Zingaran": 
            if zingaran_last_names != [""]:
                name += f' {zingaran_last_names[random.randint(0,len(zingaran_last_names)-1)]}'
        case "Skandaharian": 
            if skanda_last_names != [""]:
                name += f' {skanda_last_names[random.randint(0,len(skanda_last_names)-1)]}'
        case "Cimmerian": 
            if cimmmerian_last_names != [""]:
                name += f' {cimmmerian_last_names[random.randint(0,len(cimmmerian_last_names)-1)]}'
        case "Stygian": 
            if stygian_last_names != [""]:
                name += f' {stygian_last_names[random.randint(0,len(stygian_last_names)-1)]}'
        case "Hyrkanian": 
            if hyrkanian_last_names != [""]:
                name += f' {hyrkanian_last_names[random.randint(0,len(hyrkanian_last_names)-1)]}'
        case "Turanian": 
            if turanian_last_names != [""]:
                name += f' {turanian_last_names[random.randint(0,len(turanian_last_names)-1)]}'
        case "Khitai": 
            if khitian_last_names != [""]:
                name += f' {khitian_last_names[random.randint(0,len(khitian_last_names)-1)]}'
        case "Elf": 
            if elf_last_names != [""]:
                name += f' {elf_last_names[random.randint(0,len(elf_last_names)-1)]}'
        case "Wood Elf": 
            if woodelf_last_names != [""]:
                name += f' {woodelf_last_names[random.randint(0,len(woodelf_last_names)-1)]}'
        case "Dwarf": 
            if dwarf_last_names != [""]:
                name += f' {dwarf_last_names[random.randint(0,len(dwarf_last_names)-1)]}'
        case "Halfling": 
            if halfling_last_names != [""]:
                name += f' {halfling_last_names[random.randint(0,len(halfling_last_names)-1)]}'
        case "Gnome": 
            if gnome_last_names != [""]:
                name += f' {gnome_last_names[random.randint(0,len(gnome_last_names)-1)]}'
    
    return name




def __getHitPoints__( characterClass, attributes ):
    # This returns as a string rather than an int just for the purpose of printing
    # may cause problems later.

    hp_at_first = 0
    conBonus = 0

    con = attributes.get("CON")
    if con >= 15:
        conBonus = 1
    elif con <= 6:
       conBonus = -1
    else:
       conBonus = 0

    rollone = random.randint(1,6)
    rolltwo = random.randint(1,6)

    base_hp = rollone + conBonus
    second_HD = rolltwo + conBonus

    if base_hp == 0:
        base_hp = 1
    if second_HD == 0:
        second_HD = 1

    hp_at_first = base_hp

    match characterClass:
        case "Fighting-Man":
            hp_at_first = base_hp + 1
        case "Paladin": 
            hp_at_first = base_hp + 1
        case "Anti-Paladin":
            hp_at_first = base_hp + 1
        case "Ranger": 
            hp_at_first = (base_hp + second_HD) - 2
        case "Barbarian":
            hp_at_first = (base_hp + second_HD) - 2
        case "Cleric":
            hp_at_first = base_hp
        case "Anti-Cleric":
            hp_at_first = base_hp
        case "Druid":
            hp_at_first = base_hp
        case "Shaman":
            hp_at_first = base_hp
        case "Magic-User":
            hp_at_first = base_hp
        case "Illusionist":
            hp_at_first = base_hp
        case "Necromancer":
            hp_at_first = base_hp
        case "Thief":
            hp_at_first = base_hp
        case "Assassin":
            hp_at_first = base_hp
        case "Monk":
            hp_at_first = base_hp

    if hp_at_first == 0 and characterClass == "Ranger":
        hp_at_first = 2
    if hp_at_first == 0 and characterClass == "Barbarian": # redundant?
        hp_at_first = 2
    elif hp_at_first == 0:
        hp_at_first = 1

    hp_string = str(hp_at_first)

    return hp_string
    
def __getStrMods__( strength ):
    
    statement = ""

    if strength <= 6:
        statement = "-1 to hit and damage in Single Combat melee. -1 to Force Doors. "
    elif strength <= 8:
        statement = "-1 to hit and damage in Single Combat melee. "
    elif strength > 12 and strength < 15:
        statement = "+1 to hit and damage in Single Combat melee. " 
    elif strength >= 15:
        statement = "+1 to hit and damage in Single Combat melee. +1 to Force Doors. "

    return statement

def __getWisMods__( wisdom ):
    
    statement = ""

    if wisdom <= 6:
        statement = "-2 to Saves vs magical effects. "
    elif strength >= 15:
        statement = "+2 to Saves vs magical effects. "

    return statement

def __getIntMods__( intelligence, charclass ):
    
    statement = ""
    statement2 = ""

    isArcane = False

    match charclass:
        case "Magic-User":
            isArcane = True
        case "Illusionist":
            isArcane = True
        case "Necromancer":
            isArcane = True

    over10 = intelligence - 10

    if intelligence >= 11:
        statement = f"Can speak {over10} additional languages. "

    if isArcane and intelligence >= 14:
        statement2 = statement + "One additional starting spell. "
        statement = statement2

    return statement

def __getDexMods__( dexterity ):
    
    statement = ""

    if dexterity <= 6:
        statement = "-1 to hit with any missile in Single Combat. -1 to Initiative. "
    elif dexterity <= 8:
        statement = "-1 to hit with any missile in Single Combat. "
    elif dexterity > 12 and dexterity < 15:
        statement = "+1 to hit and damage in Single Combat. " 
    elif dexterity >= 15:
        statement = "+1 to hit with any missile in Single Combat. +1 to Initiative. "

    return statement

def __getConMods__( constitution ):
    
    statement = ""

    if constitution <= 6:
        statement = "-1 hp on each Hit Die (minimum: 1). "
    elif constitution >= 15:
        statement = "+1 hp on each Hit Die. "

    return statement


#%%

# definition of character object

class myCharacter:
    def __init__(self) :
        self.abilityScores = __getAbilityScores__()
        self.characterClass = __getClass__(self.abilityScores)
        
        self.race = __getRace__(self.characterClass, self.abilityScores)
        self.subrace = __getSubRace__(self.characterClass, self.race)
        self.sex = __getSex__(self.race, self.characterClass, self.abilityScores)
        self.align = __getAlignment__(self.characterClass, self.race)
        self.name = __getRandomName__(self.subrace, self.sex)
        
        self.prBonus = ""
        self.hitDice = ""
        self.hitPoints = __getHitPoints__(self.characterClass, self.abilityScores)
        self.classFeatures = ""
        self.spellsperday = ""

if num_chars == 1:
    newCharacter = myCharacter()

    # print(json.dumps(newCharacter.__dict__))
    # need to print it in a different order than it's generated in 
    # ie name first, so on and so forth

    # redundant(?) block here so that I can write out the attributes print functions 
    # as readable code
    strength = newCharacter.abilityScores.get("STR")
    intelligence = newCharacter.abilityScores.get("INT")
    wisdom = newCharacter.abilityScores.get("WIS")
    dexterity = newCharacter.abilityScores.get("DEX")
    constitution = newCharacter.abilityScores.get("CON")
    charisma = newCharacter.abilityScores.get("CHA")

    str_text = __getStrMods__(strength)
    int_text = __getIntMods__(intelligence, newCharacter.characterClass)
    wis_text = __getWisMods__(wisdom)
    dex_text = __getDexMods__(dexterity)
    con_text = __getConMods__(constitution)

    abil_text = str_text + int_text + wis_text + dex_text + con_text

    print("")
    print(newCharacter.name)
    print(newCharacter.align, " ", newCharacter.subrace, " ", newCharacter.characterClass, ", ", newCharacter.sex, sep="")
    print(newCharacter.hitPoints + " hp")
    print("Strength:", strength)
    print("Intelligence:", intelligence)
    print("Wisdom:", wisdom)
    print("Dexterity:", dexterity)
    print("Constitution:", constitution)
    print("Charisma:", charisma)
    print(abil_text)
    print("")

else: 

    print("") # just as a spacer in the terminal

    for number in range(1, num_chars):

        newCharacter = myCharacter()

        print(newCharacter.name + ", " + newCharacter.hitPoints + " hp")
        print(newCharacter.align, " ", newCharacter.subrace, " ", newCharacter.characterClass, ", ", newCharacter.sex, sep="")
        print(newCharacter.abilityScores)
        print("") # just as a spacer in the terminal



#%%



# Test block


##### MANUAL TEST 
##     # Creating an empty dictionary
##     my_dict = {}
##     my_dict['STR'] = 14
##     my_dict['INT'] = 12
##     my_dict['WIS'] = 13
##     my_dict['DEX'] = 10
##     my_dict['CON'] = 15
##     my_dict['CHA'] = 16
##     testscores = my_dict
##     
##     ## RANDOM METHOD
##     # testscores = __getAbilityScores__()
##     
##     testclass = __getClass__(testscores)
##     testrace = __getRace__(testclass,testscores)
##     testhp = __getHitPoints__(testclass, testscores)
##     hp_string = str(testhp)
##     testsex = __getSex__(testrace, testclass, testscores) 
##     print(testscores)
##     print(testsex, testrace, testclass)
##     print(hp_string + " hp")



#%%
