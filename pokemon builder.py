import os
import time

typelist = ['NORMAL','FIRE','WATER','ELECTRIC','GRASS','ICE','FIGHTING','POISON','GROUND','FLYING','PSYCHIC','BUG','ROCK','GHOST','DRAGON','DARK','STEEL','FAIRY']
Type1 = '???'
Type2 = '???'                    ##setting some variables
BaseStats = [0,0,0,0,0,0]
hp = 'bruh'
attack = 'bruh'                 ##others are used lower down or closer to their respective
defence = 'bruh'                ##parts of the program so its easier to code/debug
specialattack = 'bruh'
specialdefence = 'bruh'
speed = 'bruh'
genderrates = ['AlwaysFemale','FemaleSevenEighths','Female75Percent','Female50Percent','Female25Percent','FemaleOneEighth','AlwaysMale','Genderless']
GenderRate = 'bruh'
growthrates = ['Fluctuating','Erratic','Fast','Medium','Parabolic','Slow']
GrowthRate = 'bruh'
BaseEXP = 'bruh'


##getting names
Name = input('mons name: ')
Name = Name.capitalize()
InternalName = Name.upper()

##getting types
Dtype = input('\nis dual type y/n: ')
if Dtype == 'n':
    while Type1 not in typelist:
        print('')
        Type1 = input('type 1: ')
        Type1 = Type1.upper()
        print('')
        if Type1 not in typelist:
            print('error: type not valid')
else:
    while Type1 not in typelist or Type2 not in typelist or Type1 == Type2:
        print('')
        Type1 = input('type 1: ')
        Type2 = input('type 2: ')
        Type1 = Type1.upper()
        Type2 = Type2.upper()
        print('')
        if Type1 not in typelist:
            print('error: type 1 not valid')
        if Type2 not in typelist:
            print('error: type 2 not valid')
        if Type1 == Type2:
            print('error: type 1 is the same as type 2')


print('enter base stats (use online base stats to compare)')

## getting hp stat
while type(hp) == str:
    print('')
    print('20 Base HP is same as magikarp\n50 Base HP is same as hitmons\n100 Base HP is same as mew, tyranitar and kyogre\n160 Base HP is same as snorlax\n255 Base HP is same as blissey\n')
    hp = input('Hp: ')
    try:
        hp = int(hp)
    except:
        print('\nerror: input not an integer')
        
## getting attack stat
while type(attack) == str:
    print('')
    attack = input('Attack: ')
    try:
        attack = int(attack)
    except:
        print('\nerror: input not an integer')

## getting defence stat
while type(defence) == str:
    print('')
    defence = input('Defence: ')
    try:
        defence = int(defence)
    except:
        print('\nerror: input not an integer')

## getting special attack stat
while type(specialattack) == str:
    print('')
    specialattack = input('Special Attack: ')
    try:
        specialattack = int(specialattack)
    except:
        print('\nerror: input not an integer')

## getting special defence stat
while type(specialdefence) == str:
    print('')
    specialdefence = input('SpecialDefence: ')
    try:
        specialdefence = int(specialdefence)
    except:
        print('\nerror: input not an integer')

## getting speed stat
while type(speed) == str:
    print('')
    speed = input('Speed: ')
    try:
        speed = int(speed)
    except:
        print('\nerror: input not an integer')

## assign stats to a list for easy access
BaseStats[0] = hp
BaseStats[1] = attack
BaseStats[2] = defence
BaseStats[3] = specialattack
BaseStats[4] = specialdefence
BaseStats[5] = speed

##getting gender rate
gcheck = False
gcheck2 = [0,1,2,3,4,5,6,7]
while gcheck == False:
    print('possible Gender Rates:\n')
    for i in range(0,8):
        print(str(i + 1) + ' ' + genderrates[i])
    Grate = input('\nchoose number for gender rate: ')
    Grate = int(Grate) - 1
    if Grate in gcheck2:
        GenderRate = genderrates[int(Grate)]
        gcheck = True
    else:
        print('error: gender rate out of range')

##getting growth rate
grcheck = False
grcheck2 = [0,1,2,3,4,5]
os.startfile('Expnextlevel.png')
os.startfile('ExpGraph.png')
while grcheck == False:
    print('possible Growth Rates:\n')
    for i in range(0,6):
        print(str(i + 1) + ' ' + growthrates[i])
    Grate = input('\nchoose number for growth rate: ')
    Grate = int(Grate) - 1
    if Grate in grcheck2:
        GrowthRate = growthrates[int(Grate)]
        grcheck = True
    else:
        print('error: growth rate out of range')


##getting Base EXP
while type(BaseEXP) == str:
    print('')
    BaseEXP = input('BaseEXP: ')
    try:
        BaseEXP = int(BaseEXP)
    except:
        print('\nerror: input not an integer')


##getting effort points
EffortPoints = [0,0,0,0,0,0]
print('\ninput effort values (dont forget that theres a max of 3 evs for a pokemon)')
print('in order: Hp, Atk, Def, Sp.A, Sp.D, Spe')
i = 0
while i <= 5:
    if sum(EffortPoints) < 3:
        try:
            EffortPoints[i] = int(input('value ' + str(i+1) + ': '))
            i = i + 1
        except:
            print('error: value input is not an integer: restarting ##getting effort points\n')
            print('input effort values (dont forget that theres a max of 3 evs for a pokemon)\nin order: Hp, Atk, Def, Sp.A, Sp.D, Spe')
            EffortPoints = [0,0,0,0,0,0]
            i = 0
    else:
        if sum(EffortPoints) == 3:
            i = 6
        else:
            i = 0
            print('restarting due to too many effort points')
            EffortPoints = [0,0,0,0,0,0]
print('Effort points: ' + str(EffortPoints))

## getting rareness(catch rate)
print('(Catch Rate can not be more than 255 and lowest catch rate is 3)')
catchguide  = (input('would you like a guide to pokemon catch rates?\ny/n: ')).upper()
if catchguide == 'Y':
    import webbrowser
    webbrowser.open('https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_catch_rate')
    print('255 provides a 43.9% chance to catch at full health with a normal ball\n200 provides a 36.6% chance\n150 provides a 29.5% chance\n100 provides a 21.7% chance\n 50 provides a 12.9% chance\n  3 provides a  1.6% chance')
Rareness = 300
while Rareness < 3 or Rareness > 255:
    try:
        Rareness = int(input('\ninput catch rate: '))
        if Rareness < 3 or Rareness > 255:
            print('invalid catch rate')
    except:
        print('invalid catch rate')



##getting  Happiness (base friendship)

print('Base friendship, max of 255 min of 0, usually 70,\nexceptions are friendly or unfreindly looking pokemon (who usually have friendship evos)\nand almost all legendaries\n')
Happiness = 300
while Happiness < 0 or Happiness > 255:
    try:
        Happiness = int(input('\ninput base friendship: '))
        if Happiness < 0 or Happiness > 255:
            print('invalid friendship')
    except:
        print('error: input not an integer')


## Getting abilities and hidden abilities
hiddenabilitycheck = (input('should ' + Name + ' receive hidden abilities?\ny/n: ')).upper()
Abilities = input('\ninput pokemons abilities\nbe VERY careful you spell the abilities correctly, and make sure they are seperated by a , and do not use spaces\nlike this: POISONPOINT,RIVALRY\n(input is not case sensitive)\n: ').upper()
if hiddenabilitycheck == 'Y':
    HiddenAbility = (input('input hidden ability: ')).upper()

print('Due to the time and thought put into making movepools I have decided it is better that the move pool be added in the text file\n so that it may be easily modified and left as a work in progress if need be\n(that and I cant be bothered to make a list of every move in the game)')


## getting Compatibility (egg group)
EggGroups = ['Amorphous','Bug','Dragon','Fairy','Field','Flying','Grass','HumanLike','Mineral','Monster','Water1','Water2','Water3','Ditto','Undiscovered']
EggGroup = ['Amorphous Pokémon are not usually based on real creatures; instead they comprise shapeless blobs or gases\nMost Ghost and Poison Pokémon are here',
            'As the name implies, this group consists of mainly Bug types (with the exception of Trapinch, Vibrava, Flygon, Gligar, Gliscor and Drapion)\nThere are very few Pokémon here also in a second group, and several do not learn egg moves',
            'As the name suggests, the Pokémon in this group are dragon-like and reptilian in appearance\nSurprisingly, less than half of the Pokémon in this group are Dragon type. Most of the Pokémon here belong to a second group too',
            'Fairy Pokémon are mostly cute Pokémon, or majestic in their appearance\nPokémon X&Y introduced Fairy as a type, and so many of the Pokémon in this group are now Fairy type',
            'This is by far the largest egg group, previously known as Ground. As well as having many Ground type Pokémon, the Field group contains lots of land-based mammals and has the most diverse range of types\nThis makes for easy breeding of multiple moves\nOddly (perhaps disturbingly), this group contains Wailord, one of the largest Pokémon in existence, and some of the smallest like Skitty and Diglett',
            'All Pokémon in this group are part Flying type, except for Decidueye\nThis means they are mostly bird-like in appearance',
            'All the Pokémon in this group (previously known as Plant) are some kind of plants;\nas such, nearly every member is part Grass type. Most Pokémon also belong to a second group',
            'The Pokémon in this group (previously known as Humanshape) are bipedal, like humans\n Most Fighting type Pokémon are in this group',
            'Mineral Pokémon are mostly based on inanimate objects. Most are Rock and Steel type\nThe majority of Pokémon here are only in this group and many are genderless, making for difficult breeding',
            'Pokémon in the Monster group are large, powerful beasts\nIt is one of the largest and most diverse groups. Many of the starters are in this group',
            'The first of three water-based egg groups, Pokémon in Water 1 are generally amphibious (surviving in and out of water)\nAll the Water type starters are in this group',
            'The second of three water egg groups. The Pokémon here are generally based on fish\nand as expected all are Water type (except for Inkay/Malamar)',
            'The last of three water egg groups, Water 3 is a mix of different Pokémon types\nincluding fossil Pokémon, crabs and invertebrates',
            "Unsurprisingly, this egg group contains Ditto! Technically this is a real egg group but it's more of a meta-group\nDitto can breed with all Pokémon besides itself and the Undiscovered group",
            'None of the Pokémon in this group are able to breed, thus do not produce any eggs\nThe group mostly consists of legendary and baby Pokémon']
print('the following are all egg groups conveniently numbered:\n')
for i in range(0,15):
    print (str(i+1) + ' ' + EggGroups[i])
eggknow = (input('\nwould you like to know about egg groups?\ny/n: ')).upper()
while eggknow == 'Y':
    try:
        egroup = int(input('\ninput the number of the egg group you would like to learn about: '))
        egroup = egroup-1
        if egroup > 14 or egroup < 0:
            print('error: input out of range')
        else:
            print('\n' + EggGroup[egroup])
            time.sleep(2)
            eggknow = (input('\nwould you like to know about other egg groups?\ny/n: ')).upper()
    except:
        print('error: input was not a number')

multiegg = 3
try:
    multiegg = int(input('\n\nis your mon in 1 or 2 egg groups?: '))
    if multiegg != 1 and multiegg != 2:
        print('error: input not 1 or 2')
except:
    print('error: input not 1 or 2')

while multiegg != 1 and multiegg != 2:
    try:
        multiegg = int(input('\nis this mon in 1 or 2 egg groups?: '))
        if multiegg != 1 and multiegg != 2:
            print('error: input not 1 or 2')
    except:
        print('error: input not 1 or 2')

egchoice = False
while egchoice == False:
    try:
        group1 = int(input('\nenter the number of the first egg group: '))
        group1 = group1 - 1
        if group1 > 14 or group1 < 0:
            print('error: input out of range')
        elif group1 == 13:
            print('\nwhoa there buckeroo!')
            print('you cant just go giving random mons the ditto egg group!')
            dittocheck = input("i'm going to have to ask you to type the word DITTO to make sure you know what your doing: ")
            if dittocheck == 'DITTO':
                print('huh, alright you do you I guess')
            else:
                print('you have failed the ditto check, no ditto egg group for you!')


        
        if multiegg == 2:
            group2 = int(input('\nenter the number of the second egg group: '))
            group2 = group2 - 1
            if group2 > 14 or group2 < 0:
                print('error: input out of range')
            elif group2 == 13:
                print('\nwhoa there buckeroo!')
                print('you cant just go giving random mons the ditto egg group!')
                dittocheck = input("i'm going to have to ask you to type the word DITTO to make sure you know what your doing: ")
                if dittocheck == 'DITTO':
                    print('huh, alright you do you I guess')
                else:
                    print('you have failed the ditto check, no ditto egg group for you!')

            if group1 == group2:
                print('same egg group used twice, try again')
            else:
                print('egg groups ' + EggGroups[group1] + ' and ' + EggGroups[group2] + ' used')
                egchoice = True
        else:
            print('egg group ' + EggGroups[group1] + ' used')
            egchoice = True

    except:
        print('error: somethings gone wrong and i couldnt be bothered to find out what it was, try again')


## getting the steps it takes to hatch an egg
hatchchek = False
while hatchchek == False:
    try:
        StepsToHatch = int(input('How many steps does it take for your pokemon to hatch from an egg?\n(10k is the highest a legit pokemon egg gets 2.5k is the lowest a mon gets(except for magikarp who gets 1280))\n: '))
        hatchchek = True
    except:
        print('error: your input was not a number')


## getting haight and weight
hwcheck = False
while hwcheck == False:
    try:
        Height = float(input('input height in meters: '))
        Weight = float(input('input weight in Kg: '))
        hwcheck = True
    except:
        print('it is likely you did not enter a number try again')



##getting colour for the pokedex search
Colour = ['Red','Blue','Yellow','Green','Black','Brown','Purple','Gray','White','Pink']
print('the following is a list of available colours to be used for searching in the pokedex: \n')
for i in range(0,10):
    print(str(i+1) + ' ' + Colour[i])
try:
    clr = int(input('\nenter the number of the pokemons colour: '))
    clr = clr - 1
    if clr > 9 or clr < 0:
        print('value out of range')
except:
    clr = 99
    print('error: you didnt enter a number or somthing')
while clr > 9 or clr < 0:
    try:
        clr = int(input('\nenter the number of the pokemons colour: '))
        clr = clr - 1
        if clr > 9 or clr < 0:
            print('input out of range')
    except:
        bruh = 'bruh'
Color = (Colour[clr])



##getting shape for the pokedex search
shapes = ['Head','Serpantine','Finned','HeadArms','HeadBase','BipedalTail','HeadLegs','Quadruped','Winged','Multiped','MultiBody','Bipedal','MultiWinged','Insectoid']
print('the following is a list of available shapes to be used for searching in the pokedex: \n')
for i in range(0,14):
    print(str(i+1) + ' ' + shapes[i])
try:
    Shap = int(input('\nenter the number of the pokemons shape: '))
    Shap = Shap - 1
    if Shap > 13 or Shap < 0:
        print('value out of range')
except:
    Shap = 99
    print('error: you didnt enter a number or somthing')
while Shap > 13 or Shap < 0:
    try:
        Shap = int(input('\nenter the number of the pokemons shape: '))
        Shap = Shap - 1
        if Shap > 13 or Shap < 0:
            print('input out of range')
    except:
        bruh = 'bruh'
Shape = (shapes[Shap])

##getting habitat, except due to the fact it isnt used in essentials or smthn im just going to set it to the same thing for everything
Habitat = 'WatersEdge'

##getting the 'kind' of pokemon it is for example, charizard is the 'Flame' pokemon
Kind = input("What kind of pokemon is it?\nFor example Charizard is the 'Flame' pokemon\n: ")
Kind = Kind.capitalize()


## pokedex entry:
Pokedex  = input('enter the pokedex entry: ')


Generation = 1

## getting wild held items
itemcheck = input('can the pokemon hold an item when found in the wild?\ny/n: ')
itemcheck = itemcheck.upper()
if itemcheck == 'Y':
    print('Common means 50% find rate\nUncommon means 5%\nRare means 1%\nYou can only have one item per percentage\nand if all items are the same thing then theres a 100% item rate')
    WildItemCommon = input('Common held item(50%): ')
    WildItemCommon = WildItemCommon.upper()
    WildItemUncommon = input('Uncommon held item(5%): ')
    WildItemUncommon = WildItemUncommon.upper()
    WildItemRare = input('Rare held item(1%): ')
    WildItemRare = WildItemRare.upper()


##idk how shadows are represented ingame according to the values so ill just skip it here and it can be tweaked for each individual mon

## and evos can be pr complecated too so im not going to try that either




### assigning everything in the right order and format to a file so that it can be easily put into a game!!
## yaay!!!
monfile = open(InternalName + '.txt','a')
monfile.write('Name = ' + Name)
monfile.write('\n')
monfile.write('InternalName = ' + InternalName)
monfile.write('\n')
monfile.write('Type1 = ' + Type1)
if Dtype == 'y':
    monfile.write('\n')
    monfile.write('Type2 = ' + Type2)
monfile.write('\n')
monfile.write('BaseStats = ')
for i in range(0,6):
    monfile.write(str(BaseStats[i]))
    if i != 5:
        monfile.write(',')
monfile.write('\n')
monfile.write('GenderRate = ' + GenderRate)
monfile.write('\n')
monfile.write('GrowthRate = ' + GrowthRate)
monfile.write('\n')
monfile.write('BaseEXP = ' + str(BaseEXP))
monfile.write('\n')
monfile.write('EffortPoints = ')
for i in range(0,6):
    monfile.write(str(EffortPoints[i]))
    if i != 5:
        monfile.write(',')
monfile.write('\n')
monfile.write('Rareness = ' + str(Rareness))
monfile.write('\n')
monfile.write('Happiness = ' + str(Happiness))
monfile.write('\n')
monfile.write('Abilities = ' + str(Abilities))
monfile.write('\n')
if hiddenabilitycheck == 'Y':
    monfile.write('HiddenAbility = ' + HiddenAbility)
    monfile.write('\n')
monfile.write('Moves = ')
monfile.write('\n')
monfile.write('TutorMoves = ')
monfile.write('\n')
monfile.write('EggMoves = ')
monfile.write('\n')
if multiegg == 2:
    monfile.write('Compatibility = ' + EggGroups[group1] + ',' + EggGroups[group2])
else:
    monfile.write('Compatibility = ' + EggGroups[group1])
monfile.write('\n')
monfile.write('StepsToHatch = ' + str(StepsToHatch))
monfile.write('\n')
monfile.write('Height = ' + str(Height))
monfile.write('\n')
monfile.write('Weight = ' + str(Weight))
monfile.write('\n')
monfile.write('Color = ' + Color)
monfile.write('\n')
monfile.write('Shape = ' + Shape)
monfile.write('\n')
monfile.write('Habitat = ' + Habitat)
monfile.write('\n')
monfile.write('Kind = ' + Kind)
monfile.write('\n')
monfile.write('Pokedex = ' + Pokedex)
monfile.write('\n')
monfile.write('Generation = ' + str(Generation))
if itemcheck == 'Y':
    monfile.write('\n')
    monfile.write('WildItemCommon = ' + WildItemCommon)
    monfile.write('\n')
    monfile.write('WildItemUncommon = ' + WildItemUncommon)
    monfile.write('\n')
    monfile.write('WildItemRare = ' + WildItemRare)
monfile.write('\n')
monfile.write('BattlerPlayerX = 0')
monfile.write('\n')
monfile.write('BattlerPlayerY = 0')
monfile.write('\n')
monfile.write('BattlerEnemyX = 0')
monfile.write('\n')
monfile.write('BattlerEnemyY = 0')
monfile.write('\n')
monfile.write('BattlerShadowX = 0')
monfile.write('\n')
monfile.write('BattlerShadowSize = 2')
monfile.close()

print('Mons file complete\nEvolutions, Forms, Learnsets, positions and shadow size will need to be added or adjusted manually')
time.sleep(20)
