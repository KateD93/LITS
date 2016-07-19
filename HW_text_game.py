import os
inventory = []
max_size_inventory = 4
max_gold = 20
win_items = ["PHONE", "DOCUMENT", "KEY"]

items_used_state = [{
    "FLOWER": 0,
    "BED": 0,
    "CHAIR": 0,
    "BOOKCASE": 0,
    "TV": 0,
    "SOFA": 0,
    "WEIGHT": 0,
    "ORBITRECK": 0,
    "DRYER": 0,
    "WASHING_MACHINE": 0,
    "DESK": 0,
    "COMPUTER": 0
},{"NEWSPAPER": 0,
   "GLASSES": 0,
   "BOOK": 0,
   "PHONE": 0,
   "KEY":0,
   "SOAP": 0,
   "TOWEL": 0,
   "JUMPROPE": 0,
   "BALL": 0,
   "CONSOLE": 0,
   "DISK": 0,
   "NOTE": 0,
   "PEN": 0,
   "DOCUMENT": 0
     },
    ["LAMP", "BATH", "SINK", "NOTE", "PEN", "SOAP", "TOWEL"]]

room_items_description = [{"NEWSPAPER": "You see the fresh newspaper.",
                           "FLOWER": "This beautiful flower.... is cactus.",
                           "BED": "This is your lovely best place in this room. Save it!",
                           "LAMP": "Very nice you find thing, but this is just lamp."},
                          {"GLASSES": "Your glasses is very cute.",
                           "BOOK": "This is Python the king smile emoticon =-)).",
                           'PHONE': "Your lovely IPhone.",
                           "CHAIR": "Description: simple chair.",
                           "BOOKCASE": "Bookcase is`n empty.",
                           "KEY": "Your apartment will be safe thanks to this object."},
                          {"TV": "This is TV. Not very interesting.",
                           "SOFA": "This is place for a rest."},
                          {"BATH": "Just bath.",
                           "SINK": "Just sink.",
                           "SOAP": "Just soap for the hand washing.",
                           "TOWEL": "Just towel."},
                          {"JUMPROPE": "Pink jump rope very important for keep yourself in good shape.",
                           "BALL": "BALL and BALL and BALL, BALL, BALL.",
                           "WEIGHT": "You like it, because you strong guy.",
                           "ORBITRECK": "Just do it!"},
                          {"DRYER": "You hate this thing, but why?",
                           "WASHING_MACHINE": "Cleaning clothes now. Do not disturb her!"},
                          {"CONSOLE": "For time for playing =P",
                           "DISK": "Disk of your favorite group.",
                           "DESK": "Place with more mess in it."},
                          {"NOTE": "Your important note for work.",
                           "PEN": "Your favorite pen.",
                           "DOCUMENT": "Important documents. You need this item or no? How are you think?",
                           "COMPUTER": "Very big important machine in your life."}]
def start():
    os.system("clear")
    global gold
    gold = 0
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Hello, Dear!!! Welcome to our interesting and exciting quest game =-)"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Relax body you are in your house. This is just usual day when you waking up and preparing to go to work "\
    "But....not to day. Today you are hurry because your boss returns from vacation =-B, if you now what i mean."\
    "Actually your task is successfully collect important items and find the money to the way of your work."



def goldCount():
    #os.system("clear")
    global gold
    print "Current gold is {}".format(gold)


def command():
    x = str(raw_input("Type command:"))
    return x


def func_inventory():
    if inventory != []:
        for items in inventory:
            print items
        print "Do you want to remove item from your inventory?[YES/NO]"
        answer = command()
        if answer == "YES":
            print "Please enter the name of the item which you want to remove."
            prompt_l = command()
            if prompt_l in inventory:
                inventory.remove(prompt_l)
                items_used_state[1][prompt_l] = 0
                print "Item remove successfully!"
            else:
                print "You don`t have this item in you inventory."
        elif answer == "NO":
            print "You are come back in room."
    elif inventory == []:
        print "Your inventory is empty."
    else:
        print "You type wrong command. Try again."
        print "You are come back in room."


def end_Game():
    if gold >= max_gold and win_items == inventory:
        os.system("clear")
        print "--- !!!(-8 CONGRATULATIONS. You won the game 8-) !!! ---"
    else:
        os.system("clear")
        print "--- ))-=  Sorry try again. You lose game  =-(( ---"
    raise SystemExit(0)


def help_func():
    print "\n\n Commands:\n N -- North\n S -- South\n E -- East\n W -- West\n " \
          "Anything in ALL CAPS is a command\n GOLD -- check gold count\n " \
          "INVENTORY -- Check inventory\n EXIT -- you are finishing game\n"


def lobby():
    global gold
    goldCount()
    prompt_hallway()


def prompt_hallway():
    global gold
    global inventory
    print "______________________________________________________________________"
    print "You are in the hallway. You can go to the East, West, North and South."
    prompt_l = command()
    if prompt_l == "HELP":
        help_func()
    elif prompt_l == "N":
        master_Bedroom()
    elif prompt_l == "S":
        library_Room()
    elif prompt_l == "W":
        keeping_Room()
    elif prompt_l == "E":
        rest_Room()
    elif prompt_l == "GOLD":
        goldCount()
        prompt_hallway()
    elif prompt_l == "INVENTORY":
        func_inventory()
        prompt_hallway()
    elif prompt_l == "EXIT":
        end_Game()
    else:
        print "You write wrong command, try again."
        prompt_hallway()


def master_Bedroom():
    os.system("clear")
    global gold
    global inventory
    print "______________________________________________________________________"
    print "You are in Master Room"
    print "There is doors to East, West and South"
    print "There are is a {d}".format(d=room_items_description[0].keys())
    prompt_l = command()
    if prompt_l == "HELP":
        help_func()
        master_Bedroom()
    elif prompt_l == "S":
        library_Room()
    elif prompt_l == "W":
        keeping_Room()
    elif prompt_l == "E":
        rest_Room()
    elif prompt_l == "GOLD":
        goldCount()
        master_Bedroom()
    elif prompt_l == "INVENTORY":
        func_inventory()
        master_Bedroom()
    elif prompt_l in items_used_state[0] and room_items_description[0] and items_used_state[0].get(prompt_l) == 0:
        print room_items_description[0].get(prompt_l)
        if gold < max_gold:
            print "You find 5 gold"
            gold = gold + 5
            items_used_state[0][prompt_l] = 1
            master_Bedroom()
        else:
            print "You have enough money! Just walk around the {}".format(prompt_l)
            master_Bedroom()
    elif prompt_l in items_used_state[0] and room_items_description[0] and items_used_state[0].get(prompt_l) == 1:
        print room_items_description[0].get(prompt_l)
        print "You walk around the {}".format(prompt_l)
        master_Bedroom()
    elif prompt_l in items_used_state[1] and room_items_description[0] and items_used_state[1].get(prompt_l) == 0:
        print room_items_description[0].get(prompt_l)
        print "You can add this thing in inventory. Do you want to do it? [YES/NO?]"
        answer = command()
        if answer == "YES":
            if len(inventory) == 0 or len(inventory) < max_size_inventory:
                inventory.append(prompt_l)
                items_used_state[1][prompt_l] = 1
                print "Item add in inventory successfully."
                master_Bedroom()
            else:
                print "Your inventory is full. You can`t add item. Please clean your inventory."
                master_Bedroom()
        elif answer == "NO":
            print "You are come back in room."
            master_Bedroom()
        else:
            master_Bedroom()
    elif prompt_l in items_used_state[1] and room_items_description[0] and items_used_state[1].get(prompt_l) == 1:
        print "You have this item in your inventory."
        master_Bedroom()
    elif prompt_l in items_used_state[2] and room_items_description[0]:
        print room_items_description[0].get(prompt_l)
        master_Bedroom()
    elif prompt_l == "EXIT":
        end_Game()
    else:
        print "You write wrong command, try again."
        master_Bedroom()


def library_Room():
    os.system("clear")
    global gold
    global inventory
    print "______________________________________________________________________"
    print "You are in the Library."
    print "There are doors to the East, West and North"
    print "There are is a {}".format(room_items_description[1].keys())
    prompt_l = command()
    if prompt_l == "HELP":
        help_func()
    if prompt_l == "N":
        prompt_hallway()
    elif prompt_l == "W":
        play_Room()
    elif prompt_l == "E":
        trainings_Room()
    elif prompt_l == "GOLD":
        goldCount()
        library_Room()
    elif prompt_l == "INVENTORY":
        func_inventory()
        library_Room()
    elif prompt_l in items_used_state[0] and room_items_description[1] and items_used_state[0].get(prompt_l) == 0:
        print room_items_description[1].get(prompt_l)
        if gold < max_gold:
            print "You find 5 gold"
            gold = gold + 5
            items_used_state[0][prompt_l] = 1
            library_Room()
        else:
            print "You have enough money! Just walk around the {}".format(prompt_l)
            library_Room()
    elif prompt_l in items_used_state[0] and room_items_description[1] and items_used_state[0].get(prompt_l) == 1:
        print room_items_description[1].get(prompt_l)
        print "You walk around the {}".format(prompt_l)
        library_Room()
    elif prompt_l in items_used_state[1] and room_items_description[1] and items_used_state[1].get(prompt_l) == 0:
        print room_items_description[1].get(prompt_l)
        print "You can add this thing in inventory. Do you want do it? [YES/NO?]"
        answer = command()
        if answer == "YES":
            if len(inventory) == 0 or len(inventory) < max_size_inventory:
                inventory.append(prompt_l)
                items_used_state[1][prompt_l] = 1
                print "item add in inventory successfully."
                library_Room()
            else:
                print "Your inventory is full. You can`t add item. Please clean your inventory."
                library_Room()
        elif answer == "NO":
            print "You are come back in room."
            library_Room()
        else:
            library_Room()
    elif prompt_l in items_used_state[1] and room_items_description[1] and items_used_state[1].get(prompt_l) == 1:
        print "You have this item in your inventory."
        library_Room()
    elif prompt_l in items_used_state[2] and room_items_description[1]:
        print room_items_description[1].get(prompt_l)
        library_Room()
    elif prompt_l == "EXIT":
        end_Game()
    else:
        print "You write wrong command, try again."
        library_Room()


def keeping_Room():
    os.system("clear")
    global gold
    global inventory
    print "______________________________________________________________________"
    print "You are in the Keeping Room."
    print "There are doors to the East, North and South"
    print "There are is a {}".format(room_items_description[2].keys())
    prompt_l = command()
    if prompt_l == "HELP":
        help_func()
    if prompt_l == "N":
        gym_Room()
    elif prompt_l == "S":
        play_Room()
    elif prompt_l == "E":
        prompt_hallway()
    elif prompt_l == "GOLD":
        goldCount()
        keeping_Room()
    elif prompt_l == "INVENTORY":
        func_inventory()
        keeping_Room()
    elif prompt_l in items_used_state[0] and room_items_description[2] and items_used_state[0].get(prompt_l) == 0:
        print room_items_description[2].get(prompt_l)
        if gold < max_gold:
            print "You find 5 gold"
            gold = gold + 5
            items_used_state[0][prompt_l] = 1
            keeping_Room()
        else:
            print "You have enough money! Just walk around the {}".format(prompt_l)
            keeping_Room()
    elif prompt_l in items_used_state[0] and room_items_description[2] and items_used_state[0].get(prompt_l) == 1:
        print room_items_description[2].get(prompt_l)
        print "You walk around the {}".format(prompt_l)
        keeping_Room()
    elif prompt_l in items_used_state[1] and room_items_description[2] and items_used_state[1].get(prompt_l) == 0:
        print room_items_description[2].get(prompt_l)
        print "You can add this thing in inventory. Do you want do it? [YES/NO?]"
        answer = command()
        if answer == "YES":
            if len(inventory) == 0 or len(inventory) < max_size_inventory:
                inventory.append(prompt_l)
                items_used_state[1][prompt_l] = 1
                print "item add in inventory successfully."
                keeping_Room()
            else:
                print "Your inventory is full. You can`t add item. Please clean your inventory."
                keeping_Room()
        elif answer == "NO":
            print "You are come back in room."
            keeping_Room()
        else:
            keeping_Room()
    elif prompt_l in items_used_state[1] and room_items_description[2] and items_used_state[1].get(prompt_l) == 1:
        print "You have this item in your inventory."
        keeping_Room()
    elif prompt_l in items_used_state[2] and room_items_description[2]:
        print room_items_description[2].get(prompt_l)
        keeping_Room()
    elif prompt_l == "EXIT":
        end_Game()
    else:
        print "You write wrong command, try again."
        keeping_Room()


def rest_Room():
    os.system("clear")
    global gold
    global inventory
    print "______________________________________________________________________"
    print  "You are in the Restroom."
    print "There are doors in the West, North and South."
    print "There are is a {d}".format(d=room_items_description[3].keys())
    prompt_l = command()
    if prompt_l == "HELP":
        help_func()
    if prompt_l == "N":
        laundry_Room()
    elif prompt_l == "S":
        trainings_Room()
    elif prompt_l == "W":
        prompt_hallway()
    elif prompt_l == "GOLD":
        goldCount()
        rest_Room()
    elif prompt_l == "INVENTORY":
        func_inventory()
        rest_Room()
    elif prompt_l in items_used_state[0] and room_items_description[3] and items_used_state[0].get(prompt_l) == 0:
        print room_items_description[3].get(prompt_l)
        if gold < max_gold:
            print "You find 5 gold"
            gold = gold + 5
            items_used_state[0][prompt_l] = 1
            rest_Room()
        else:
            print "You have enough money! Just walk around the {}".format(prompt_l)
            rest_Room()
    elif prompt_l in items_used_state[0] and room_items_description[3] and items_used_state[0].get(prompt_l) == 1:
        print room_items_description[3].get(prompt_l)
        print "You walk around the {}".format(prompt_l)
        rest_Room()
    elif prompt_l in items_used_state[1] and room_items_description[3] and items_used_state[1].get(prompt_l) == 0:
        print room_items_description[3].get(prompt_l)
        print "You can add this thing in inventory. Do you want do it? [YES/NO?]"
        answer = command()
        if answer == "YES":
            if len(inventory) == 0 or len(inventory) < max_size_inventory:
                inventory.append(prompt_l)
                items_used_state[1][prompt_l] = 1
                print "Item added in inventory successfully."
                rest_Room()
            else:
                print "Your inventory is full. You can`t add item. Please clean your inventory."
                rest_Room()
        elif answer == "NO":
            print "You are come back in room."
            rest_Room()
        else:
            rest_Room()
    elif prompt_l in items_used_state[1] and room_items_description[3] and items_used_state[1].get(prompt_l) == 1:
        print "You have this item in your inventory."
        rest_Room()
    elif prompt_l in items_used_state[2] and room_items_description[3]:
        print room_items_description[3].get(prompt_l)
        rest_Room()
    elif prompt_l == "EXIT":
        end_Game()
    else:
        print "You write wrong command, try again."
        rest_Room()


def gym_Room():
    os.system("clear")
    global gold
    global inventory
    print "______________________________________________________________________"
    print  "You are in the Gym."
    print "There are doors in the East and South."
    print "There are is a {d}".format(d=room_items_description[4].keys())
    prompt_l = command()
    if prompt_l == "HELP":
        help_func()
    if prompt_l == "E":
        master_Bedroom()
    elif prompt_l == "S":
        keeping_Room()
    elif prompt_l == "GOLD":
        goldCount()
        gym_Room()
    elif prompt_l == "INVENTORY":
        func_inventory()
        gym_Room()
    elif prompt_l in items_used_state[0] and room_items_description[4] and items_used_state[0].get(prompt_l) == 0:
        print room_items_description[4].get(prompt_l)
        if gold < max_gold:
            print "You find 5 gold"
            gold = gold + 5
            items_used_state[0][prompt_l] = 1
            gym_Room()
        else:
            print "You have enough money! Just walk around the {}".format(prompt_l)
            gym_Room()
    elif prompt_l in items_used_state[0] and room_items_description[4] and items_used_state[0].get(prompt_l) == 1:
        print room_items_description[4].get(prompt_l)
        print "You walk around the {}".format(prompt_l)
        gym_Room()
    elif prompt_l in items_used_state[1] and room_items_description[4] and items_used_state[1].get(prompt_l) == 0:
        print room_items_description[4].get(prompt_l)
        print "You can add this thing in inventory. Do you want do it? [YES/NO?]"
        answer = command()
        if answer == "YES":
            if len(inventory) == 0 or len(inventory) < max_size_inventory:
                inventory.append(prompt_l)
                items_used_state[1][prompt_l] = 1
                print "Item added in inventory successfully."
                gym_Room()
            else:
                print "Your inventory is full. You can`t add item. Please clean your inventory."
                gym_Room()
        elif answer == "NO":
            print "You are come back in room."
            gym_Room()
        else:
            gym_Room()
    elif prompt_l in items_used_state[1] and room_items_description[4] and items_used_state[1].get(prompt_l) == 1:
        print "You have this item in your inventory."
        gym_Room()
    elif prompt_l in items_used_state[2] and room_items_description[4]:
        print room_items_description[4].get(prompt_l)
        gym_Room()
    elif prompt_l == "EXIT":
        end_Game()
    else:
        print "You write wrong command, try again."
        gym_Room()


def laundry_Room():
    os.system("clear")
    global gold
    global inventory
    print "______________________________________________________________________"
    print "You are in the Landry."
    print "There are doors to the West and South."
    print "There are is a {d}".format(d=room_items_description[5].keys())
    prompt_l = command()
    if prompt_l == "HELP":
        help_func()
    if prompt_l == "W":
        master_Bedroom()
    elif prompt_l == "S":
        rest_Room()
    elif prompt_l == "GOLD":
        goldCount()
        laundry_Room()
    elif prompt_l == "INVENTORY":
        func_inventory()
        laundry_Room()
    elif prompt_l in items_used_state[0] and room_items_description[5] and items_used_state[0].get(prompt_l) == 0:
        print room_items_description[5].get(prompt_l)
        if gold < max_gold:
            print "You find 5 gold"
            gold = gold + 5
            items_used_state[0][prompt_l] = 1
            laundry_Room()
        else:
            print "You have enough money!. Just walk around the {}".format(prompt_l)
            laundry_Room()
    elif prompt_l in items_used_state[0] and room_items_description[5] and items_used_state[0].get(prompt_l) == 1:
        print room_items_description[5].get(prompt_l)
        print "You walk around the {}".format(prompt_l)
        laundry_Room()
    elif prompt_l in items_used_state[1] and room_items_description[5] and items_used_state[1].get(prompt_l) == 0:
        print room_items_description[5].get(prompt_l)
        print "You can add this thing in inventory. Do you want do it? [YES/NO?]"
        answer = command()
        if answer == "YES":
            if len(inventory) == 0 or len(inventory) < max_size_inventory:
                inventory.append(prompt_l)
                items_used_state[1][prompt_l] = 1
                print "Item added in inventory successfully."
                laundry_Room()
            else:
                print "Your inventory is full. You can`t add item. Please clean your inventory."
                laundry_Room()
        elif answer == "NO":
            print "You are come back in room."
            laundry_Room()
        else:
            laundry_Room()
    elif prompt_l in items_used_state[1] and room_items_description[5] and items_used_state[1].get(prompt_l) == 1:
        print "You have this item in your inventory."
        laundry_Room()
    elif prompt_l in items_used_state[2] and room_items_description[5]:
        print room_items_description[5].get(prompt_l)
        laundry_Room()
    elif prompt_l == "EXIT":
        end_Game()
    else:
        print "You write wrong command, try again."
        laundry_Room()


def play_Room():
    os.system("clear")
    global gold
    global inventory
    print "______________________________________________________________________"
    print "You are in the Games Room."
    print "There are doors to the North and East."
    print "There are is a {d}".format(d=room_items_description[6].keys())
    prompt_l = command()
    if prompt_l == "HELP":
        help_func()
    if prompt_l == "N":
        keeping_Room()
    elif prompt_l == "E":
        library_Room()
    elif prompt_l == "GOLD":
        goldCount()
        play_Room()
    elif prompt_l == "INVENTORY":
        func_inventory()
        play_Room()
    elif prompt_l in items_used_state[0] and room_items_description[6] and items_used_state[0].get(prompt_l) == 0:
        print room_items_description[6].get(prompt_l)
        if gold < max_gold:
            print "You find 5 gold"
            gold = gold + 5
            items_used_state[0][prompt_l] = 1
            play_Room()
        else:
            print "You have enough money! Just walk around the {}".format(prompt_l)
            play_Room()
    elif prompt_l in items_used_state[0] and room_items_description[6] and items_used_state[0].get(prompt_l) == 1:
        print room_items_description[6].get(prompt_l)
        print "You walk around the {}".format(prompt_l)
        play_Room()
    elif prompt_l in items_used_state[1] and room_items_description[6] and items_used_state[1].get(prompt_l) == 0:
        print room_items_description[6].get(prompt_l)
        print "You can add this thing in inventory. Do you want do it? [YES/NO?]"
        answer = command()
        if answer == "YES":
            if len(inventory) == 0 or len(inventory) < max_size_inventory:
                inventory.append(prompt_l)
                items_used_state[1][prompt_l] = 1
                print "Item added in inventory successfully."
                play_Room()
            else:
                print "Your inventory is full. You can`t add item. Please clean your inventory."
                play_Room()
        elif answer == "NO":
            print "You are come back in room."
            play_Room()
        else:
            play_Room()
    elif prompt_l in items_used_state[1] and room_items_description[6] and items_used_state[1].get(prompt_l) == 1:
        print "You have this item in your inventory."
        play_Room()
    elif prompt_l in items_used_state[2] and room_items_description[6]:
        print room_items_description[6].get(prompt_l)
        play_Room()
    elif prompt_l == "EXIT":
        end_Game()
    else:
        print "You write wrong command, try again."
        play_Room()


def trainings_Room():
    os.system("clear")
    global gold
    global inventory
    print "______________________________________________________________________"
    print "You are in the Study Room."
    print "There are doors to the North and West."
    print "There are is a {d}".format(d=room_items_description[7].keys())
    prompt_l = command()
    if prompt_l == "HELP":
        help_func()
    if prompt_l == "N":
        rest_Room()
    elif prompt_l == "W":
        library_Room()
    elif prompt_l == "GOLD":
        goldCount()
        trainings_Room()
    elif prompt_l == "INVENTORY":
        func_inventory()
        trainings_Room()
    elif prompt_l in items_used_state[0] and room_items_description[7] and items_used_state[0].get(prompt_l) == 0:
        print room_items_description[7].get(prompt_l)
        if gold < max_gold:
            print "You find 5 gold"
            gold = gold + 5
            items_used_state[0][prompt_l] = 1
            trainings_Room()
        else:
            print "You have enough money! Just walk around the {}".format(prompt_l)
            trainings_Room()
    elif prompt_l in items_used_state[0] and room_items_description[7] and items_used_state[0].get(prompt_l) == 1:
        print room_items_description[7].get(prompt_l)
        print "You walk around the {}".format(prompt_l)
        trainings_Room()
    elif prompt_l in items_used_state[1] and room_items_description[7] and items_used_state[1].get(prompt_l) == 0:
        print room_items_description[7].get(prompt_l)
        print "You can add this thing in inventory. Do you want do it? [YES/NO?]"
        answer = command()
        if answer == "YES":
            if len(inventory) == 0 or len(inventory) < max_size_inventory:
                inventory.append(prompt_l)
                items_used_state[1][prompt_l] = 1
                print "Item added in inventory successfully."
                trainings_Room()
            else:
                print "Your inventory is full. You can`t add item. Please clean your inventory."
                trainings_Room()
        elif answer == "NO":
            print "You are come back in room."
            trainings_Room()
        else:
            trainings_Room()
    elif prompt_l in items_used_state[1] and room_items_description[7] and items_used_state[1].get(prompt_l) == 1:
        print "You have this item in your inventory."
        trainings_Room()
    elif prompt_l in items_used_state[2] and room_items_description[7]:
        print room_items_description[7].get(prompt_l)
        trainings_Room()
    elif prompt_l == "EXIT":
        end_Game()
    else:
        print "You write wrong command, try again."
        trainings_Room()

start()
lobby()
