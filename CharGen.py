# OD&D with Chainmail Character Generator
# see https://www.statuscake.com/blog/creating-a-character-in-python/


#%%

# imports
import random
import numpy as np
import json

# dictionary

# declarations of basic variables

races = ["Human", "Dwarf", "Halfling"]
subraces = ["Aquilonian", "Border Kingdom", "Skandaharian", "Stygian", "Wood Elf"]

classes = ["Fighting-Man", "Magic-User", "Cleric", "Thief"]
FMSubclasses = ["Ranger", "Paladin", "Death Knight"]
MUSubclasses = ["Illusionist", "Necromancer"]
CLRSubclasses = ["Anti-Cleric", "Druid", "Shaman", "Monk"]

sexes = ["Male", "Female"]

PRBonus = ["-20%", "-10%", "+0%", "+5%", "+10%"]

human_male_names = ["A", "B", "C"]
human_female_names = ["A", "B", "C"]
human_last_names = ["x", "y", "z"]

dwarf_male_names = ["A", "B", "C"]
dwarf_female_names = ["A", "B", "C"]
dwarf_last_names = ["x", "y", "z"]

elf_male_names = ["A", "B", "C"]
elf_female_names = ["A", "B", "C"]
elf_last_names = ["x", "y", "z"]

halfling_male_names = ["A", "B", "C"]
halfling_female_names = ["A", "B", "C"]
halfling_last_names = ["x", "y", "z"]


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

    #### unorderedscores = [strength, intelligence, wisdom, dexterity, constitution, charisma]

    # Find the attribute with the highest value
    # highest_attribute = max(attributes, key=attributes.get)

    # Assign character class based on the highest attribute
    # For now, these are all running on the stringent Strategic Revue/Greyhawk etc. 
    # ability score requirements, rather than a more lenient dual-PR system.

    # These many subclasses will have a function later that turns them 'off',
    # ie. back into their parent class, if the user did not selected against them.
    # Even if you play purist OD&D, the subclasses can still inform the character's concept.

    # Just for fun and symmetry we are adding OSE's Necromancer and an adapted Gazeteer Shaman (plus ACKS),

    # Final note on the multiplicity of classes: we are here assuming that CONAN THE BARBARIAN
    # was a multi-classed F-M/Thief, rather than creating a Barbarian subclass, but a Barbarian could
    # easily be created (FM who can run up walls, etc.) who selects for high STR and CON.

    # Races will apply their own ability score requirements (as per BX) later on, given class.

    # Alignment is here generated within the function to determine whether a cleric is 
    # one of the other types, based on a distribution of law 3 in 6, neutral 2 in 6, chaotic 1 in 6. 
    # later on an actual function will use class and race to determine alignment.
    tempALN = random.randint(1,6)
    # Where 1 to 3 is Lawful, 4 or 5 is Neutral and 6 is Chaotic.

    # In descending order of qualifying for the class:

    # FM Subclasses and Monk block
    if (highest_attribute == "STR" and charisma >= 17) or (strength >= 9 and charisma >= 17):
        if tempALN <= 5:
            character_class = "Paladin"
        elif tempALN == 6:
            character_class = "Death Knight"
    elif highest_attribute == "STR" and intelligence >= 12 and wisdom >= 12 and constitution >= 15:
        character_class = "Ranger" # will almost certainly change, that's ludicrous
    elif wisdom >= 15 and dexterity >= 15 and strength >= 12:
        character_class = "Monk"

    # Thief and Assassin block
    elif highest_attribute == "DEX" and strength >= 12 and intelligence >= 12 and dexterity >= 12:
        character_class = "Assassin"
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
        
        # redundant blocks for subclasses, all Human only.
        case "Paladin":      
            result = "Human"
        case "Death Knight":
            result = "Human"
        case "Ranger":      
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
                halflingchance = 0.65
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

# Test block

testscores = __getAbilityScores__()

##### MANUAL TEST 
# Creating an empty dictionary
## my_dict = {}
## my_dict['STR'] = 11
## my_dict['INT'] = 12
## my_dict['WIS'] = 13
## my_dict['DEX'] = 10
## my_dict['CON'] = 9
## my_dict['CHA'] = 16

## testclass = __getClass__(my_dict)
testclass = __getClass__(testscores)
testrace = __getRace__(testclass,testscores)
#  
#  print(testscores)
### print(my_dict)
#  print(testclass)
#  print(testrace)

# The chances of nonhuman retainers is fairly rare, which fits well the 
# assumptions of OD&D generally. Special envoys can always be made to elfland 
# or dwarfland, after all.

# A similar function to determine subrace probabilistically
# E.g. elven druid will be wood elf 100%
# Human F-M might be any of the subraces (Aquilonian etc.)



#%%

    # getAlignment takes in the class and race to pick an alignment.

def __getAlignment__( charclass, race ):
    result = ""
    return result 
#%%

def __getSex__( race , charclass, attributes ):

    strength = attributes.get("STR")
    intelligence = attributes.get("INT")
    wisdom = attributes.get("WIS")
    dexterity = attributes.get("DEX")
    constitution = attributes.get("CON")
    charisma = attributes.get("CHA")

    # setting up a variable to contain a % chance of character being female
    femmechance = 0

    if race == "Dwarf":
        femmechance = 0
    elif race == "Gnome":
        femmechance = 0
    elif race == "Halfing":
        femmechance = 33
    elif race == "Human" and (charclass == "Fighting-Man" or charclass == "Ranger"):
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

testsex = __getSex__(testrace, testclass, testscores)
# print(testsex)

#%%

def __getRandomName__( race, gender ):

    name = ""

    if race == "Human" and gender == "Male":
            name = human_male_names[random.randint(0,len(human_male_names)-1)]
        
    if race == "Human" and gender == "Female":
        name = human_female_names[random.randint(0,len(human_female_names)-1)]
        
    if race == "Dwarf" and gender == "Male":
        name = dwarf_male_names[random.randint(0,len(dwarf_male_names)-1)]

    if race == "Dwarf" and gender == "Female":
        name = dwarf_female_names[random.randint(0,len(dwarf_female_names)-1)]

    if race == "Halfling" and gender == "Male":
        name = halfling_male_names[random.randint(0,len(halfling_male_names)-1)]

    if race == "Halfling" and gender == "Female":
        name = halfling_female_names[random.randint(0,len(halfling_female_names)-1)]

    match race:
        case "Human": name += f' {human_last_names[random.randint(0,len(human_last_names)-1)]}'
        case "Dwarf": name += f' {dwarf_last_names[random.randint(0,len(dwarf_last_names)-1)]}'
        case "Halfling": name += f' {halfling_last_names[random.randint(0,len(halfling_last_names)-1)]}'
    
    return name





#%%

# definition of character object

class myCharacter:
    def __init__(self) :
        self.abilityScores = __getAbilityScores__()
        self.characterClass = __getClass__(self.abilityScores)
        
        self.race = __getRace__(self.characterClass, self.abilityScores)
        self.sex = __getSex__(self.race, self.characterClass, self.abilityScores)
        self.name = ""
        
        self.prBonus = ""
        self.hitDice = ""
        self.hitPoints = ""
        self.classFeatures = ""
        self.spellsperday = ""

newCharacter = myCharacter()

print(json.dumps(newCharacter.__dict__))
# need to print it in a different order than it's generated in 
# ie name first, so on and so forth

#%%

# alternate method of saving a character as a dict.
## char_one = dict({
##     "Sex": sexes[random.randint(0,len(sexes)-1)],
##     "Race": races[random.randint(0,len(races)-1)],
##     "Name": [""],
##     "AbilityScores": [_getAbilityScores_()]
## })

## char_one.Name = __getRandomName__(char_one.Race,char_one.Sex)

## import pandas as pd
## test = pd.DataFrame(char_one)
## test.Name
# actually printing a character

#### print(vars(newCharacter))






# %%
