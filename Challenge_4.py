#! /usr/bin/python3
# Program Name: Challenge_1.py
# Author: Luke Gosnell
# Contributors: Tom Morissey
# Date: 2/25/2015
# A fun demo of a text-based adventure game. 

class player(object):
    def __init__(self):
        self.Health=100
        self.Items=[]
    def __str__(self):
        print("Health:",self.Health)
        print("Items:","\n",self.Items)
        return ""

print("""
    Welcome to the best text-based adventure game ever!!
    (TRIAL VERSION)
    Press enter to play.
    """)
input("")

player=player()
Items=player.Items
while player.Health > 0:
    print("""
    You are taking your usual Sunday evening stroll through the park when suddenly
    you are approached by a man in black leaning against a tree. He takes a look at your attire.
    """)
    print("""
    ────────────────────────────────
    ───────────────██████████───────
    ──────────────████████████──────
    ──────────────██────────██──────
    ──────────────██▄▄▄▄▄▄▄▄▄█──────
    ──────────────██▀███─███▀█────── 
    █─────────────▀█────────█▀──────
    ██──────────────────█───────────
    ─█──────────────██──────────────
    █▄────────────████─██──████
    ─▄███████████████──██──██████ ──
    ────█████████████──██──█████████
    ─────────────████──██─█████──███
    ──────────────███──██─█████──███
    ──────────────███─────█████████
    ──────────────██─────████████▀
    ────────────────██████████
    ────────────────██████████
    ─────────────────████████
    ──────────────────██████████▄▄
    ────────────────────█████████▀
    ─────────────────────████──███
    ────────────────────▄████▄──██
    ────────────────────██████───▀
    ────────────────────▀▄▄▄▄▀

    "Red shirt, blue jeans, green cap... You're the one."


    He takes your hand and pulls you into a van parked nearby.

    """)
    choice1 = input("""
    1. Scream for help
    2. "What's going on?!?"
    3. View menu

    Choice: """)
    if choice1 == "3":
        print("")
        print(player)
        print("""
    Press enter to exit menu.""")
        input("")
        choice1 = input("""
    1. Scream for help
    2. "What's going on?!?"

    Choice: """)
    if choice1 == "1":
        print("The man has no choice but to shoot you dead. You were a danger to his operations. Better luck next time.")
        print("Press enter")
        input("")
        exit()
        
    elif choice1 == "2":
        print("""
    The man ignores you and hands you a small dagger.

    After a very long ride, the van comes to a sudden hault

    "Good luck, we're rooting for you," the man says, pushing you out of the van.

    You tumble down a rocky hill, taking -50 HP.

    You look up, seeing that you are in the middle of a forest.

    You need to find health...

    There is a tinkling noise behind a nearby bush, but you also notice various herbs growing by a small stream.
    _________________________________________________________________________""")

    choice2 = input("""
    1. Look behind the bush
    2. Try using the herbs by the stream
    3. View menu

    Choice: """)
        
    player.Health=player.Health-50
    Items.append("Dagger")

    if choice2 == "3":
        print("")
        print(player)
        print("""
    Press enter to exit menu.""")
        input("")
        choice2 = input("""
    1. Look behind the bush
    2. Try using the herbs by the stream

    Choice: """)
    if choice2 == "1":
        print("""
    You look behind the bush and see a group of fairies conversing.

    "AHHH! HUMAN!!" one of them screams. They all attempt to fly away, but you manage to capture one.

    "Please don't eat me!!" it pleads. "I can heal you!"
    _________________________________________________________________________""")

        choice2A = input("""
    1. Ask the fairy to heal you
    2. Eat the fairy
    3. View Menu

    Choice: """)
        if choice2A == "3":
            print("")
            print(player)
            print("""
    Press enter to exit menu.""")
            input("")
            choice2A = input("""
    1. Ask the fairy to heal you
    2. Eat the fairy

    Choice: """)
        if choice2A == "1":
            print("""
    "Sure!" The fairy sounds happy to help.

    She sprinkles you with a magical dust.

    Good, you're healin- No, wait... You start to cough, feeling excrutiating pain.

    The fairy slips out of your grasp and flies away. "HAHA, SUCKER!!"

    -30 HP

    It starts getting late...
    _________________________________________________________________________""")
            player.Health=player.Health-30
            
        elif choice2A == "2":
            print("""
    Down the Hatch! This will surely heal you.

    You put the fairy in your mouth and begin chewing. Crunchy...

    It screams in agony as you swallow... You begin feeling better.

    Good choice!

    +40 HP

    It starts getting late...
    _________________________________________________________________________""")
            player.Health=player.Health+40
            
    elif choice2 == "2":
        print("""
    You make your way toward the stream.

    You grab an oddly-shaped leaf, hoping for the best.

    You press the leaf against your body and start rubbing.

    You quickly start feeling dizzy...

    ...

    ...

    ...

    You wake up slowly with a blistering headache as the sun sets.

    -20 HP
    _________________________________________________________________________""")
        player.Health=player.Health-20
    print("""
    Night is coming fast and its time to look for shelter.

    You look around for about 30 minutes until you find a cave.

    It is dark and it will be very difficult to find any other shelter.
    _________________________________________________________________________""")

    choice3 = input("""
    1. Sleep in the cave
    2. Go look for other shelter
    3. View Menu

    Choice: """)

    if choice3 == "3":
        print("")
        print(player)
        print("""
    Press enter to exit menu.""")
        input("")
        choice3 = input("""
    1. Sleep in the cave
    2. Go look for other shelter

    Choice: """)

    if choice3 == "1":
        print("""
    You decide to sleep in the cave.

    You go inside and a storm picks up not long after.

    You hear the rustling of the trees outside due to the strong winds.

    You decide to go a little deeper into the cave and find a pile of berries!

    You begin eating.

    +10 HP

    A pile of berries... just sitting there... How strange...

    ...

    "ROOOAAAARR!!!!"
    _________________________________________________________________________""")
        player.Health=player.Health+10

        choice3A=input("""
    1. Stab behind you
    2. Run away
    3. View Menu

    Choice: """)
        if choice3A == "3":
             print("")
             print(player)
             print("""
    Press enter to exit menu.""")
             input("")
             choice3A=input("""
    1. Stab behind you
    2. Run away

    Choice: """)
        if choice3A == "1":
            print("""
    You choose to immediatelty stab the giant bear lurking behind you.

    "AAAUUUGH" The bear roars traumatically, going down in just one hit.

    What a pathetic creature.

    You skin the bear alive for its fur.

    You now have a fur coat to protect you from the bitter cold!
    _________________________________________________________________________""")
            Items.append("Fur Coat")
            print("""
    You head outside wearing your fur coat and are undamaged from the storm.
    _________________________________________________________________________""")
            print("End of trial. Hope you had fun!")
            exit()

        elif choice3A== "2":
            print("""
    You choose to run like a pansy.

    Your stubby legs don't take you far and the bear catches up.

    You drop your dagger and the bear eats you alive.

    -30 HP

    You fall into its stomach.
    _________________________________________________________________________""")
            player.Health=player.Health-30
            Items.remove("Dagger")
            print("""
    Its pretty obvious what your choices are here.
    _________________________________________________________________________""")
            choice3B = input("""
    1. Try to crawl back up
    2. Let nature run its course...
    3. View menu

    Choice: """)
            if choice3B == "3":
                print("")
                print(player)
                print("""
    Press enter to exit menu.""")
                input("")
                choice3B=input("""
    1. Try to crawl back up
    2. Let nature run its course...

    Choice: """)
            if choice3B == "1":
                print("""
    You attempt to crawl back out of the bear's mouth.

    After many attempts, you manage to crawl up to its windpipe.

    You stick your head through, but its too tight around your neck.

    You choke both yourself and the bear to death.

    Wow.
    _________________________________________________________________________""")
                print("Game over")
                input("")
                exit()
            elif choice3B == "2":
                print("""
    Why would you choose that?!?

    Oh well, you get out undamaged.

    Yay.

    You escape from the cave and head outside.

    The storm is still strong and you are damaged without any protection from it.

    -10 HP
    _________________________________________________________________________""")
                player.Health=player.Health-10
                print("End of trial. Hope you had fun!")
                exit()

    if choice3 == "2":
        print("""
    A storm picks up as the sky turns black.

    You walk around for a long time.

    You are buffetted from the storm.

    -20 HP
    _________________________________________________________________________""")
        player.Health=player.Health-20
        print("End of trial. Hope you had fun!")
        exit()


print("Game over.")
input("")
exit()










