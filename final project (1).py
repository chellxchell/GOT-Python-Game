#Chelly Compendio
#Final Project

import random

play = "1"
    
#intro
def intro():
    print("\nWelcome to the Game of Thrones.")
    print("""\nKing's Landing is the home of the royalty of Westeros, a western continent that is made up of the Seven Kingdoms.
Westeros was once ruled by the Targaryens, until a rebellion drove them out. It is now ruled by Tommen Baratheon.
Beyond the Seven Kingdoms, the remaining member of the Targaryen family is
planning her return.
Castle Black is a castle far in the North occupied by the Night's Watch, a
military order made up of pardoned criminals.""")
    place = input("""\nPress 1 to go to King's Landing.
Press 2 to go to Beyond the Seven Kingdoms.
Press 3 to go to Castle Black. """)
    if place == "1":
        place1()
    elif place == "2":
        place2()
    elif place == "3":
        place3()
    else:
        print("That is not a valid entry.")

#----------------------------------------------------------------------------------------------------------------------------------
#KING'S LANDING

def place1():
    print ("\nYou are Margaery Tyrell, Queen of the Seven Kingdoms and wife of King Tommen.")
    personchoice = chooseperson(input("""You are in your room in the Red Keep, the castle that houses Westeros royalty
when you are summoned by the High Sparrow. Do you seek him out or ignore him?
                                         \n1. Ignore him.
2. Find the High Sparrow. """))
    chooseperson(personchoice)

def chooseperson(personchoice):
    if personchoice == "1":
        ignore()
    if personchoice  == "2":
        sparrow()
    
def ignore():
    print("\nYou ignore the High Sparrow's call and stay in the castle drinking wine. Nothing happens.")

def sparrow():
    defense=input("""\nYou are escorted into the town to meet the High Sparrow. The High Sparrow is
a religious icon that has grown popular with the people in recent months.
As soon as he sees you, he accuses you of being an accomplice to your brother
for treason. What do you do?
\n1. Deny every one of his accusations.
2. Support your brother and potentially lose your status as queen.""")
    if defense == "1":
        deny()
    if defense == "2":
        defensive()
        
def deny():
    denyfate = random.randint(1,2)
    if denyfate == 1:
        print("\nThe High Sparrow believes you and lets you go. You return to the Red Keep.")
    if denyfate == 2:
        print("\nThe High Sparrow dooes not believe you. He has you arrested and thrown in a cell.")
        imprisoned()
    
def defensive():
    supportfate = random.randint(1,2)
    if supportfate == 1:
        saved()
    if supportfate == 2:
        imprisoned()

def saved():
    print("""\nThe guards turn you to leave. Just before you go out the door, you hear a loud
bang and the Kingsguard storms the room.""")
    print("Your husband Tommen follows and tells the guards to arrest the High Sparrow.")
    print("You have been saved. You return to the Red Keep.")
        
def imprisoned():
    print("\nThe High Sparrow has you arrested and thrown in a cell.")
    imprisonedchoice = input("""You have been in your cell for days with little food. One of the High
Sparrow's followers enters your cell.
He tells you that in order to be released, you must make your Walk of Atonement
barefoot all the way from the temple to the castle barefoot.
\nDo you
1. accept
2. refuse?""")
    if imprisonedchoice == "1":
        walkofshame()
    if imprisonedchoice == "2":
        refusefate = random.randint(1,2)
        if refusefate == 1:
            saved()
        if refusefate == 2:
            print("\nYou have refused the offer. The guard has orders to kill you if you refuse. You are dead.")

def walkofshame():
    walkfate = random.randint(1,3)
    if walkfate == 1:
        print("""\nYou make the walk of shame. On the way to the castle, one of the commoners
throws a knife at you. You are dead.""")
    if walkfate == 2:
        print("""\nYou make it to the castle. However, you collapse from exhaustion. You
die instantly.""")
    if walkfate == 3:
        print("\nYou have made it the castle in one piece. Congradulations, you're alive!")

#----------------------------------------------------------------------------------------------------------------------------------
#BEYOND THE SEVEN KINGDOMS

def place2():
    print("""\nYou are Daenerys Targaryen, Queen of the Andals and the First Men, Breaker of
Chains, and Mother of Dragons.You are on a quest to take back the Seven Kingdoms, your birthright that was taken away from you from a rebellion that happened
before you were born""")
    danychoice = input("""\nYou are flying on one of your dragons. Where do you go?
1. Meereen
2. To the Dothraki """)
    if danychoice == "1":
        meereen()
    if danychoice == "2":
        dothraki()

def meereen():
    slavechoice = input("""\nYou arrive with your army to Meereen, a city in in which many men, women, and
children have been enslaved by the rich. You have enough men to fight their
masters, but doing so would result in unrest in the city.
Do you attempt to free the slaves?
1. yes
2. no """)
    if slavechoice == "1":
        freeslaves()
    if slavechoice == "2":
        denyslaves()

def denyslaves():
    print("""\nYou have chosen to do nothing. You pass Meereen and continue on your quest
to take back the Seven Kingdoms.""")

def freeslaves():
    print("""\nYou have chosen to free the slaves. The slaves aid you and you overthrow the
tyrannical rule of the slave masters, and the chains are broken.""")
    masterfate = input("""Now you must decide the fate of those who enslaved others.
Do you
1. kill them all
2. show mercy and let them live """)
    if masterfate == "1":
        killmasters()
    if masterfate == "2":
        savemasters()

def killmasters():
    killmfate = random.randint(1,2)
    if killmfate == 1:
        print("""\nYou have killed all the masters and there is no one standing in your way.
Meereen is yours.""")
    if killmfate == 2:
        rebellion()

def savemasters():
    savemfate = random.randint(1,2)
    if savemfate == 1:
        rebellion()
    if savemfate == 2:
        print("\nThe masters are grateful that you have saved them. You rule Meereen in peace.")

def rebellion():
    print("""\nDespite your choice with the masters, a group called the Sons of the Harpy has
risen up against you. Their goal is to assassinate you and take back Meereen.""")
    harpyfate = random.randint(1,2)
    if harpyfate == 1:
        print("""The Sons of the Harpy gather their forces and run you out of Meereen.
You are left with nothing.""")
    if harpyfate == 2:
        print("""The Sons of the Harpy attempt on your life, but your guards and advisers
are able to stop it. The rebellion has been squashed and you rule in peace.""")

def dothraki():
    print("""\nYou have been captured by Dothraki warriors. The Dothraki are a race of nomadic
horse mounted warriors in Essos. They are led by leaders called Khals.
They do not know who you are or that you speak their language.""")
    tellchoice = input("""Do you
1. tell them
2. play dumb """)
    if tellchoice == "1":
        tell()
    if tellchoice == "2":
        donttell()
        
def tell():
    tellfate = random.randint(1,2)
    if tellfate == 1:
        widow()
    if tellfate == 2:
        print("""\nYou tell the Khals that you are Daenerys Targaryen, Queen of the Andals
and the First Men, Breaker of Chains, and Mother of Dragons.""")
        print("They laugh at you and sentence you to die by fire.")
        firefate()

def firefate():
    firedeath = random.randint(1,2)
    if firedeath == 1:
        death()
    if firedeath == 2:
        firekill()

def firekill():
    print("\nThe Khals don't know that you're immune to fire. You burn down the whole village.")

def death():
    print("\nYou have died.")
    
def widow():
    widowfate = random.randint(1,2)
    if widowfate == 1:
        print("""\nThey send you to live with the rest of the Khal widows.
You live out the rest of your days there.""")
    if widowfate == 2:
        firekill() 

def donttell():
    donttellfate = random.randint(1,2)
    if donttellfate == 1:
        print("\nYou don't tell the Khals who you are. They sentence you to die by fire.")
        firefate()
    if donttellfate == 2:
        print("\nThe Khals have decided to imprison you.")
        imprison()

def imprison():
    imprisonfate = random.randint(1,2)
    if imprisonfate == 1:
        print("\nYou live out the rest of your days in prison.")
        death()
    if prisonfate == 2:
        print("\nThey place you in a cell but you are able to escape. You set fire to the camp.")
        firekilll()

#----------------------------------------------------------------------------------------------------------------------------------
#CASTLE BLACK

def place3():
    print("""\nYou are Jon Snow, the illegitimate son of Eddard Stark,
the Lord of House Stark and Warden of the North.
You are the Lord Commander, or the leader of the Night's Watch.
The Wall is a 700-foot tall wall of solid ice that was created along the border
of the Seven Kingdoms to protect the people against the Wildlings, a group of
people that do not submit to any laws.""")
    print("""Your current problem is the White Walkers, a species of deadly, humanoid
creatures led by the Night King.""")
    fightboltonchoice = input("""\nYour childhood home House Stark has been taken by Ramsay Bolton.
Do you take back the House first or fight the White Walkers with no
noble support?
1. Fight them alone
2. Take back House Stark.""")
    if fightboltonchoice == "1":
        whitewalkers()
    if fightboltonchoice == "2":
        bolton()

def whitewalkers():
    print("""\nYou decide to fight the White Walkers.
You lead your army to the wall and battle with them.""")
    whitefate = random.randint(1,2)
    if whitefate == 1:
        print("\nThe White Walkers slaughter you all.")
        death()
    if whitefate == 2:
        flee()

def flee():
    print("\nThe White Walkers push you back and your army flees.")
    fleefate = random.randint(1,2)
    if fleefate == 1:
        print("\nThey catch up to you and slaughter you.")
        death()
    if fleefate == 2:
        wildlings()

def wildlings():
    wildlingchoice = input("""The only ones that can help you are the Wildlings,
the people that have been fighting against you for thousands of years.
You decide to ask for their help.
Do you return to fight the White Walkers
or try to take House Stark back from the Boltons?
1. Fight the White Walkers
2. Take back House Stark """)
    if wildlingchoice == "1":
        whitewalkers2()
    if wildlingchoice == "2":
        bolton()

def whitewalkers2():
    print("\nYou have decided to fight the White Walkers again.")
    walkerfate = random.randint(1,2)
    if walkerfate == 1:
        beatwhite()
    if walkerfate == 2:
        castleoverrun()

def castleoverrun():
    print("""The White Walkers slaughter you.
Your entire army is dead and the White Walkers make their way south.""")
    death()

def beatwhite():
     print("""You successfully beat the White Walkers and they are eradicated from the Seven Kingdoms.
You live the rest of your days as Lord Commander of the Night's Watch.""")

def bolton():
    print("""\nYou decide to travel to House Stark to take it back.
You are met by Ramsay Bolton, the psychotic murderer that rules over the house.""")
    boltonfate = random.randint(1,2)
    if boltonfate == 1:
        print("Ramsay's forces slaughter you.")
        death()
    if boltonfate == 2:
        boltondecide=input("""\nYour army successfully takes back House Stark,
the home that you grew up in. What do you do with Ramsay Bolton?
1. imprison him
2. execute him.""")
        if boltondecide == "1":
            print("""\nYou have imprisoned Ramsay Bolton.
You give House Stark to its rightful heir, your half-sister Sansa Stark.""")
            fightwhite = input("""Do you wish to fight the White Walkers?
1. yes
2. no""")
            if fightwhite == "1":
                whitewalkers2()
            if fightwhite == "2":
                print("\nYou ignore the threat and return to Castle Black. They find you anyway.")
                castleoverrun()
        if boltondecide == "2":
            print("""\nYou have executed Ramsay Bolton.
You give House Stark to its rightful heir, your half-sister Sansa Stark.""")
            fightwhite2 = input("""Do you wish to fight the White Walkers?
1. yes
2. no""")
            if fightwhite2 == "1":
                whitewalkers2()
            if fightwhite2 == "2":
                print("""\nYou ignore the threat and return to Castle Black.
They find you anyway.""")
                castleoverrun()
    
while play == "1":   
    intro()
    play = input("""\nWould you like to keep playing?
1. Yes
2. No """)
    
input("\nPress the enter key to exit.")
