#File: RPG.py
#Description: HW 2
#Student's Name: Lisa Chu
#Student's UT EID: tc29328
#Course Name: CS 313E
#Unique Number: 50739
#
#Date Created: 2/12/19
#Date Last Modified: 2/15/19

#Defining Weapon class
class Weapon:
    def __init__(self, weaponType):
        self.weaponType = weaponType

        #Dictionary to hold weapons and respective damage
        Weapon.weapons = {'dagger':4, 'axe':6, 'staff':6, 'sword':10, 'none':1}

    def __str__(self):
        return str(self.weaponType)

#Defining Armor class
class Armor:
    def __init__(self, armorType):
        self.armorType = armorType

        #Dictionary to hold armors and respective armor class
        Armor.armors = {'plate':2, 'chain':5, 'leather':8, 'none':10}

    def __str__(self):
        return str(self.armorType)

#Defining RPGCharacter class
class RPGCharacter:
    def __init__(self, name):
        self.name = name
        self.weapon = 'none'
        self.armor = 'none'

    def __str__(self):
        return self.name + \
               '\n   Current Health: ' + str(self.health) + \
               '\n   Current Spell Points: ' + str(self.spellPoints) + \
               '\n   Wielding: ' + str(self.weapon) 

    #Wield method to change weapons
    def wield(self, newWeapon):
        self.weapon = newWeapon

        print(self.name + ' is now wielding a(n) ' + str(self.weapon))

    #Unwield method to change weapon to none
    def unwield(self):
        self.weapon = 'none'

        print(self.name + ' is no longer wielding anything.')

    #putOnArmor method to change armor and set armor class
    def putOnArmor(self, newArmor):
        self.armor = newArmor
        self.armorClass = Armor.armors[str(self.armor)]

        print(self.name + ' is now wearing ' + str(self.armor))

    #takeOffArmor method to change armor to none
    def takeOffArmor(self):
        self.armor = 'none'

        print(self.name + ' is no longer wearing anything.')

    #fight method to reference damage from weapon dictionary, take damage, and
        #check for defeat
    def fight(self, target):
        #Calling damage from weapon dictionary
        self.damage = Weapon.weapons[str(self.weapon)]

        print(self.name + ' attacks ' + target.name + \
              ' with a(n) ' + str(self.weapon))

        target.health = target.health - self.damage

        print(self.name + ' does ' + str(self.damage) + ' damage to ' + \
              target.name)
            
        print(target.name + ' is now down to ' + str(target.health) + \
              ' health')

        target.checkForDefeat(target)

    #checkForDefeat method to check if character health falls to zero
    def checkForDefeat(self, character):
        if character.health <= 0:
            print(character.name + ' has been defeated!')

#Defining Fighter subclass 
class Fighter(RPGCharacter):
    maxHealth = 40
    maxSpellPoints = 0
    
    def __init__(self, name):
        super().__init__(name)
        #Setting starting health and spell points
        self.health = Fighter.maxHealth
        self.spellPoints = Fighter.maxSpellPoints

    def __str__(self):
        return '\n' + \
               RPGCharacter.__str__(self) + \
               '\n   Wearing: ' + str(self.armor) + \
               '\n   Armor class: ' + str(self.armorClass) + \
               '\n'


#Defining Wizard subclass
class Wizard(RPGCharacter):
    maxHealth = 16
    maxSpellPoints = 20
    
    def __init__(self, name):
        super().__init__(name)
        #Setting starting health and spell points
        self.health = Wizard.maxHealth
        self.spellPoints = Wizard.maxSpellPoints
        #Referencing armor class from armor dictionary
        self.armorClass = Armor.armors[str(self.armor)]
        
    def __str__(self):
        return '\n' + \
               RPGCharacter.__str__(self) + \
               '\n   Wearing: ' + str(self.armor) + \
               '\n   Armor class: ' + str(self.armorClass) + \
               '\n'

    #Defining castSpell method
    def castSpell(self, spellName, target):
        self.spellName = spellName
        self.target = target

        #Dictionary to hold spells and respective cost and effect
        spells = {'Fireball':[3, 5], 'Lightning Bolt':[10, 10], 'Heal':[6, -6]}
        #Assigning called spell's effect and cost to variable
        spellEffect = spells[self.spellName][1]
        spellCost = spells[self.spellName][0]

        #Testing if spell exists in spells dictionary
        if self.spellName == 'Fireball' or self.spellName == 'Lightning Bolt' \
           or self.spellName == 'Heal':
            print(self.name + ' casts ' + self.spellName + ' at ' + \
                  self.target.name)

            #Testing if caster has enough spell points for to cast spell
            if self.spellPoints < spellCost:
                print('Insufficient spell points.')
            else:
                #If exists and enough spell points present, action taken
                target.health = target.health - spellEffect
                self.spellPoints = self.spellPoints - spellCost

                #Testing if spell casted is heal
                if self.spellName == 'Heal':
                    #Change in message for heal spell
                    print(self.name + ' heals ' + self.name + ' for ' + \
                          str(abs(spellEffect)) + ' health points.')
                    print(target.name + ' is now at ' + str(target.health) + \
                          ' health')
                else:
                    print(self.name + ' does ' + str(spellEffect) + ' damage to ' + \
                          target.name)
            
                    print(target.name + ' is now down to ' + str(target.health) + \
                          ' health')

                #Checking for defeat after casting spell
                target.checkForDefeat(target)
            
        else:
            print('Unknown spell name. Spell failed.')

    #Restricting Wizard from wearing anything
    def putOnArmor(self, newArmor):
        self.armor = 'none'

        print('Armor not allowed for this character class')

def main():

    plateMail = Armor("plate")
    chainMail = Armor("chain")
    sword = Weapon("sword")
    staff = Weapon("staff")
    axe = Weapon("axe")

    gandalf = Wizard("Gandalf the Grey")
    gandalf.wield(staff)
    
    aragorn = Fighter("Aragorn")
    aragorn.putOnArmor(plateMail)
    aragorn.wield(axe)
    
    print(gandalf)
    print(aragorn)

    gandalf.castSpell("Fireball",aragorn)
    aragorn.fight(gandalf)

    print(gandalf)
    print(aragorn)
    
    gandalf.castSpell("Lightning Bolt",aragorn)
    aragorn.wield(sword)

    print(gandalf)
    print(aragorn)

    gandalf.castSpell("Heal",gandalf)
    aragorn.fight(gandalf)

    gandalf.fight(aragorn)
    aragorn.fight(gandalf)

    print(gandalf)
    print(aragorn)


main()
