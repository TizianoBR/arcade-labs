class Room:
    def __init__(self, desc, final, search, right, left, forward, back, autoReturn=None):
        self.desc = desc
        self.descFinal = final
        self.descSearch = search

        self.right = right
        self.left = left
        self.forward = forward
        self.back = back
        self.autoReturn = autoReturn

        self.completed = False
        self.itemFound = False
        self.descSearchFound = "There isn't anything else interesting here."


class Item:
    def __init__(self, name, desc, actList, actFinal, owned=False):
        self.name = name
        self.desc = desc
        self.owned = owned
        self.actList = actList
        self.actFinal = actFinal


def main():
    item_list = []
    cantUse = "Can't use that item here."
    flipCoin = "You hold the coin in front of you and then flip it in the air for good luck.\nNothing happens."

    item = Item("coin", "A golden coin that you always carry around as a lucky charm",
                [flipCoin,
                 "You hold the coin in your hand and push the door to see if it opens by some stroke of luck.\nNothing happens.",
                 flipCoin, flipCoin, flipCoin, flipCoin, flipCoin,
                 "You hold the coin in front of you and then flip it in the air for good luck.\nIn the middle of its trajectory in the air it suddenly shoots towards a pile of junk.\nYou rush to the place where you saw the coin disappear and after a bit of searching you find it stuck to to a magnet.\nYou struggle for a bit to detach the magnet from the coin and save the in different pockets.",
                 "You aren't sure if you should take out the coin right now, so you grip it tightly inside your pocket.",
                 flipCoin, "There isn't enough space to flip the coin, but you hold it in your hand regardless.",
                 "There isn't enough space to flip the coin, but you hold it in your hand regardless."],
                [flipCoin, flipCoin, flipCoin, flipCoin, flipCoin, flipCoin, flipCoin, flipCoin,
                 "You aren't sure if you should take out the coin right now, so you grip it tightly inside your pocket.",
                 flipCoin, "There isn't enough space to flip the coin, but you hold it in your hand regardless.",
                 "There isn't enough space to flip the coin, but you hold it in your hand regardless."], True)
    item_list.append(item)

    item = Item("spear", "It is old and somewhat rusty, but it still does its job",
                [
                    "You use the spear as a lever to lift the loose tile and find an elegant looking key which you promptly put in your pocket.",
                    cantUse, cantUse, cantUse, cantUse, cantUse, cantUse,
                    "You try to force the access to the ventilation with the spear, but you can't get a good angle to open it.\nYou'll need something else.",
                    cantUse, "You don't think you actually stand a chance, do you?", cantUse, cantUse, cantUse],
                [cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse,
                 "You don't think you actually stand a chance, do you?", cantUse, cantUse, cantUse])
    item_list.append(item)

    item = Item("key", "A big and ornate key you found hidden outside the castle",
                [cantUse,
                 "You put the key in the keyhole and turn it.\nThe door opens up revealing a darkness that almost looks like it eats the light coming from the room you are in.",
                 cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse],
                [cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse,
                 cantUse, cantUse, ])
    item_list.append(item)

    item = Item("canned meat", "It somehow hasn't gone bad yet",
                [cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse,
                 "You slowly pull the canned meat out, open it and slide it towards the dragon",
                 cantUse, cantUse, cantUse],
                [cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse,
                 cantUse, cantUse])
    item_list.append(item)

    item = Item("screwdriver", "It's just a screwdriver. Who would place this in a trapped chest!?",
                [cantUse,
                 "You try to pick the lock using the screwdriver.\nUnfortunately, you have no idea how to pick a lock, so it remains closed.",
                 cantUse, cantUse, cantUse, cantUse, cantUse,
                 "You use the screwdriver to remove the screws holding up the access to the ventilation system.\nNow the way is cleared.",
                 cantUse, cantUse, cantUse, cantUse],
                [cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse,
                 cantUse, cantUse])
    item_list.append(item)

    item = Item("magnet", "It is quite strong for its size. It could likely move a large piece of metal from far away",
                [cantUse, cantUse, cantUse, cantUse,
                 "You hold the magnet up to the chest.\nYou standing rather far away from it, but after a while the chest slowly makes its way to you.\nJust as the chest reaches your position the floor around where the the chest previously was collapses.\nGrateful that you didn't fall to your death, you open the chest and find... a screwdriver.\nIt may not be what you expected, but you keep it anyways",
                 cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse],
                [cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse,
                 cantUse, cantUse])
    item_list.append(item)

    item = Item("candle", "It comes with flint and steel to light it up",
                [cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse,
                 "You take out the candle and light it up, letting its light flood the room.\nNow that you can see it, you realize it's actually not that long, just a few meters, so you can leave the candle on the floor and it illuminates the whole hallway.",
                 cantUse, cantUse, cantUse, cantUse, ],
                [cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse, cantUse,
                 cantUse, cantUse])
    item_list.append(item)

    room_list = []

    room = Room(
        "You are outside the castle.\nThere is a tile on the floor that looks loose, but you can't grip it well enough to lift it.\nYou can go forwards to enter the castle again or you can abandon this adventure and go back.",
        "You are outside the castle.\nYou can go forwards to enter the castle again or you can abandon this adventure and go back.",
        "You look around for something that would help you lift the loose tile, but there is nothing useful here.\nYou might have to search somewhere else.",
        None, None, 1, 13)
    room_list.append(room)

    room = Room(
        "You are at the entrance.\nThere is an ornate locked door in front of you, as well as two doorways, one to the left and one to the right.\nYou can also go back outside.",
        "You are at the entrance.\nYou can go to the right, to the left or forwards.",
        "You look under the mat in front the locked door.\nSadly, the key in nowhere to be found.",
        2, 5, 8, 0)
    room_list.append(room)

    room = Room(
        "You are at a long hallway with doors at the end and to the left.\nYou can see a trunk with wax on the floor right next to it.",
        "You are at a long hallway with doors at the end and to the right.\nYou can see an opened trunk on the side.",
        "You open the trunk and find big candle alongside flint and steel to light it up.\nThis may be useful later.",
        None, 3, 4, 1)
    room_list.append(room)

    room = Room(
        "You are in what appears to be a dining room.\nIt doesn't lead anywhere, but you can try looking for something useful",
        "You are in what appears to be a dining room.\nIt appears abandoned, you probably won't find anything else here.",
        "You look around the kitchen.\nAfter looking for a while you find a piece of canned meat that hasn't gone bad yet.\nYou decide to keep in case you ever need an emergency snack.",
        None, None, None, 2)
    room_list.append(room)

    room = Room(
        "You are in a very spacious room.\nIt is mostly empty, except for a elegant looking chest at the center of the room.",
        "You are in a very spacious room.\nIt is mostly empty, except for an opened chest that lies in a corner and a somewhat large hole at the center of the room.",
        "You near the chest and, see that its unlocked.\nYour common sense tells you that opening a chest in a large empty room inside an abandoned castle home to a beast is not a very good idea, but curiosity gets the best of you and open the chest anyways.\nBefore you can even reach out your hand to the chest, the floor beneath you opens up and you fall for what feels like an eternity.\nIn your last moments you think that perhaps there was a better way to see the contents of the chest and then everything goes black.",
        None, None, None, 2)
    room_list.append(room)

    room = Room(
        "You are in a largely uninteresting room.\nThere is a mirror on a wall where you can see your reflection, although its a bit blurry.\nYou can go to the right or through a unclean looking door in front of you",
        "You are in a largely uninteresting room.\nThere is a mirror on a wall where you can see your reflection, although its a bit blurry.\nYou can go to the right or through a unclean looking door in front of you",
        "As soon as you see the mirror you try to go through the glass like you saw someone do in a movie a long time ago.\nThe mirror turns out to be completely solid though, so the only thing you get out of you attempts to reach an alternate dimension is a headache from pushing your head against the glass.",
        6, None, 7, 1)
    room_list.append(room)

    room = Room(
        "You are in an armory.\nIt looks like noone has benn here for a long time.\nMaybe you can find a weapon in good condition here?",
        "You are in an armory.\nAll the items here are so rusted the might break if you look at them too hard.",
        "You start looking for a usable weapon.\nIt doesn't take too long until you find a spear in a decent condition.\nYou keep the spear for later.",
        None, None, None, 5)
    room_list.append(room)

    room = Room(
        "You are in a storage room.\nThere is so much dust here that the other rooms look like they are brand new in comparison.\nThere is an access to the ventilation system on the right, but the lid is screwed to the wall.\nYou are going to need something to open it.",
        "You are in a storage room.\nThere is so much dust here that the other rooms look like they are brand new in comparison.\nYou can access the ventilation system on the right.",
        "You look around in the storage room, but its too messy, you would need to get very lucky to find anything here.\nMaybe you can try your luck with an object you have on you?",
        11, None, None, 5)
    room_list.append(room)

    room = Room(
        "You arrive at a hallway.\nIts almost pitch black, to the point where you can barely see your hands.\nGoing through the hallway without vision would be dangerous.",
        "You arrive at a very short hallway.\nA candle on the floor gives of a warm light.\nThe only exits are the door in front of you and the way you came from.",
        "You squint trying to see if there is a light switch on the wall, but to no avail.",
        None, None, 9, 1)
    room_list.append(room)

    room = Room(
        "You see a huge dragon before you! The dragon doesn't seem aggressive, but you shouldn't provoke it.",
        "You see a huge dragon before you! The dragon is busy eating and doesn't pay much attention to you.\nYou still probably shouldn't annoy it.",
        "You try to find courage within you, however, the search is fruitless, so you just stand frozen in place.",
        None, None, 15, 8)
    room_list.append(room)

    room = Room(
        "You reach a room full of treasures.\nYou can't help but start celebrating loudly, which catches the attention of the dragon on the next room.\nThe dragon looks at you and its treasure and quickly connects the dots.\nThe dragon angrily plunges in your direction and then, everything goes black.\nTHE END",
        "You reach a room full of treasures.\nYou can't help but start celebrating loudly.\nYou suddenly realize the dragon is i the next room shut up as fast as you started cheering.\nFortunately, the dragon was distracted with its food and didn't notice, so you can you grab a good amount of gold and jewelry and happily go back home.\nTHE END",
        "",
        None, None, None, None, 12)
    room_list.append(room)

    room = Room(
        "You are inside the ventilation system.\nYou are above the dragon right now, you could go forwards and try to kill the dragon by taking it by surprise.\nAlternatively, you can continue through the ventilation system to the left.",
        "",
        "You look at the narrow ventilation duct you are in.\nThere isn't anything noteworthy.",
        None, 12, 14, 7)
    room_list.append(room)

    room = Room(
        "You are still inside the ventilation system, right next to.\nYou can go forward and enter the treasure room or ga back.",
        "",
        "Nothing interesting in this ventilation duct.",
        None, None, 10, 11)
    room_list.append(room)

    room = Room(
        "You decide that this whole thing is a bit much for you, so you go back home empty handed, without any treasure, but keeping your life.\nTHE END",
        "",
        "",
        None, None, None, None, 0)
    room_list.append(room)

    room = Room(
        "You decide to try to slay the dragon and take the treasure, unfortunately you failed to consider that you don't have a weapon and basically stand no chance against the dragon.\nThe dragon turns to you and then everything goes black.\nTHE END",
        "You grab the spear and decide to slay the dragon, so you drop into the room aiming for the dragon's neck.\nThe dragon, completely unharmed turns to you and returns the attack.\nA moment later, everything goes black.\nTHE END",
        "",
        None, None, None, None, 11)
    room_list.append(room)

    room = Room(
        "You try to slip past the dragon quietly, but the dragon doesn't take it very well and reaches towards you with its jaw.\nThen, everything goes black.\nTHE END",
        "You try to slip past the dragon quietly now that it's distracted with its food.\nThe dragons sees you and starts to make some menacing sound.\nYou decide this was a bad idea and back up.",
        "",
        None, None, None, None, 9)
    room_list.append(room)

    current_room = 1

    for i in range(len(room_list)):
        print(str(i) + room_list[i].desc + "\n")

    print(
        "\nYou find yourself in front of an abandoned castle.\nYou have heard stories of a beast that made the place its home, as well as stories of treasure hidden here.\nWith some hesitation you push the main door and enter the castle.")
    print()

    progressFlags = [
        ["spear", "key", 0],
        ["key", "key", 1],
        ["search", "candle", 2],
        ["search", "canned meat", 3],
        ["magnet", "screwdriver", 4],
        [None],
        ["search", "spear", 6, 14],
        ["coin", "magnet"],
        ["candle", None, 8],
        ["canned meat", "canned meat", 9, 10, 15],
        [None],
        [None],
        [None]
    ]
    while True:
        if not room_list[current_room].completed:
            print(room_list[current_room].desc)
        else:
            print(room_list[current_room].descFinal)

        if current_room == 10 and room_list[10].completed:
            break

        if not (room_list[current_room].autoReturn is None):
            current_room = room_list[current_room].autoReturn
            print()
            if not room_list[current_room].completed:
                print(room_list[current_room].desc)
            else:
                print(room_list[current_room].descFinal)

        validCommand = False
        while not validCommand:
            strInput = input("What will you do?   (type \"help\" for a list of commands)\n")
            strInput = strInput.lower()
            print()
            if strInput == "help":
                print("search: search the the room you are in or interact with an object in the room")
                print("f / forward: move to the room in front of you")
                print("b / back: move to the room behind you")
                print("r / right: move to the room to your right")
                print("l / left: move to the room on your left")
                print("quit: exit the game")
                print("You can use an item by typing the name of the item. Type \"inventory\" to see your items")

            elif strInput == "inventory":
                for item in item_list:
                    if item.owned:
                        print(item.name + ": " + item.desc)

            elif strInput == "f" or strInput == "forward":
                if ((current_room == 1 and not room_list[1].completed) or
                        (current_room == 8 and not room_list[8].completed) or
                        (current_room == 9 and room_list[9].completed) or
                        room_list[current_room].forward is None):
                    print("You can't go that way")
                else:
                    current_room = room_list[current_room].forward
                    validCommand = True

            elif strInput == "b" or strInput == "back":
                if room_list[current_room].back is None:
                    print("You can't go that way")
                else:
                    current_room = room_list[current_room].back
                    validCommand = True

            elif strInput == "r" or strInput == "right":
                if (current_room == 7 and not room_list[7].completed) or room_list[current_room].right is None:
                    print("you can't go that way")
                else:
                    current_room = room_list[current_room].right
                    validCommand = True

            elif strInput == "l" or strInput == "left":
                if room_list[current_room].left is None:
                    print("You can't go that way")
                else:
                    current_room = room_list[current_room].left
                    validCommand = True

            elif strInput == "quit":
                exit()

            else:
                if strInput == "search":
                    if not room_list[current_room].completed:
                        print(room_list[current_room].descSearch)
                    else:
                        print(room_list[current_room].descSearchFound)
                    validCommand = True

                else:
                    for item in item_list:
                        if strInput == item.name and item.owned:
                            if not room_list[current_room].completed:
                                print(item.actList[current_room])
                            else:
                                print(item.actFinal[current_room])
                            validCommand = True

                instructions = progressFlags[current_room]
                if instructions[0] == strInput:
                    receive = instructions[1]
                    for item in item_list:
                        if receive == item.name:
                            if item.owned:
                                item.owned = False
                            else:
                                item.owned = True
                    for i in range(2, len(instructions)):
                        room_list[instructions[i]].completed = True

                if strInput == "coin" and current_room == 7 and not item_list[5].owned:
                    room_list[7] = Room(
                        "You are in a storage room.\nThere is so much dust here that the other rooms look like they are brand new in comparison.\nThere is an access to the ventilation system on the right, but the lid is screwed to the wall.\nYou are going to need something to open it.",
                        "You are in a storage room.\nThere is so much dust here that the other rooms look like they are brand new in comparison.\nYou can access the ventilation system on the right.",
                        "You don't think you'll be able to find anything else among this mess.",
                        11, None, None, 5)
                    item_list[0].actList[7] = flipCoin
                    progressFlags[7] = ["screwdriver", None, 7]

                if not validCommand:
                    print("That isn't a valid action")

            print()


main()
