# OD&D with Chainmail Character Generator
# see https://www.statuscake.com/blog/creating-a-character-in-python/

# imports
import random

# dictionary

# declarations of basic variables

races = ["Human", "Dwarf", "Elf", "Halfling"]
classes = ["Fighting-Man", "Magic-User", "Cleric", "Thief"]
FMSubclasses = ["Ranger", "Paladin", "Barbarian", "Death Knight"]
MUSubclasses = ["Illusionist", "Necromancer"]
CLRSubclasses = ["Anti-Cleric", "Druid", "Shaman"]
PRBonus = ["-20%", "-10%", "+0%", "+5%", "+10%"]



# definition of rolling ability scores

def _getAbilityScores_():
    abilScores = []
    for x in range(6):  # outer loop, all 6 scores

        abilScore = []
        for x in range(3): # inner loop, summing 3 dice
            abilScore.append(random.randint(1,6))
            
        abilScores.append(sum(abilScore))

    unsortedScores = {'STR':0, 'INT':0, 'WIS':0, 'DEX':0, 'CON':0, 'CHA':0}

    unsortedScores["STR"] = abilScores(0)
    unsortedScores["INT"] = abilScores(1)
    unsortedScores["WIS"] = abilScores(2)
    unsortedScores["DEX"] = abilScores(3)
    unsortedScores["CON"] = abilScores(4)
    unsortedScores["CHA"] = abilScores(5)

    return unsortedScores # unsortedScores included just in case another method is selected, such as swap any 2 



print(_getAbilityScores_())

# definition of character object

class myCharacter:
    def __init__(self) :
        self.race = ""
        self.characterClass = ""
        self.sex = ""
        self.name = ""
        self.abilityScores = _getAbilityScores
        self.prBonus = ""
        self.hitDice = ""
        self.hitPoints = ""

newCharacter = myCharacter

# actually printing a character

print(vars(newCharacter))





