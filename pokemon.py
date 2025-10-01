#class to define pokemon
class Pokemon:
    def __init__(self, name, lifePoint, attackP, type):
        self.name = name
        self.lifePoint = lifePoint
        self.attackP = attackP
        self.type = type

# function for calculating the attack effectivness
def calculateAttackEffectivness(type1, type2):
    if type1 == "FIRE" and type2 == "GRASS":
        return 2
    else:
        return 0

# function for calculating the result of the fight
def calculateResult(lifePoint, attackPoint, attackEffectivness):
    return lifePoint - (attackPoint * attackEffectivness)

carizard = Pokemon("Carizard", 160, 70, "FIRE")
bulbusar = Pokemon("Bulbusar", 70, 20, "GRASS")

attackEffectivness = calculateAttackEffectivness(carizard.type, bulbusar.type)
resultOfTheAttack = calculateResult(bulbusar.lifePoint, carizard.attackP, attackEffectivness)

print(f"lifepoint:  {bulbusar.lifePoint}  attack:  {carizard.attackP}  result:  {resultOfTheAttack}")
