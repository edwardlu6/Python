print("You stand before the entrance of a dark, foreboding dungeon. The door creaks as a musty scent wafts from within. Do you dare enter, or turn back while you still can?")
option1 =str.lower(input("(e)nter the dungeon or (t)urn back:"))

if option1 == "t":
    print("You turn back, never knowing what dangers or treasures lurked within the dungeon")

elif option1 == "e":
    print("You find yourself in a dimly lit room with rough stone walls and a low ceiling. To your north, you see a narrow passage leading deeper into the dungeon. To your east, there is a wide archway that opens up to another part of the dungeon. You can hear faint shuffling sounds coming from beyond it. Will you venture north or east?")
    option2 = str.lower(input("(n)orth or (e)ast:"))

    if option2 == "e":
        print("As you step through the archway to the east, you find yourself in a small, cramped chamber. The air is musty and the only source of light comes from flickering torches on the walls. You soon realize that there is no way out, and you are trapped in this room. It seems that your journey has come to an end.")


    elif option2 == "n":
        print("You make your way up the narrow passage to the north and find yourself in a diamond-shaped room. The room is dimly lit and the walls glint with flecks of sparkling mineral deposits. To your east, you see another passage leading deeper into the dungeon. To your west, there is another passage that disappears into the shadows. Which way will you choose?")
        option3 = str.lower(input("(w)est or (e)ast:"))

        if option3 == "e":
            print("You venture down the passage to the east and enter a grand chamber filled with glittering treasures. The room is awash in light from torches on the walls and a chandelier hanging from the high ceiling. Piles of gold coins and gems, stacks of precious artifacts and shimmering pieces of jewelry are scattered throughout the room. The riches contained in this chamber are truly beyond imagining. It looks like luck has finally smiled upon you.")

        elif option3 == "w":
            print("You continue down the passage to the west and enter a room with seven doors. To your west, there is another door leading deeper into the dungeon. Along the north wall, there are three doors, and along the south wall, there are three more doors. Each door is made of sturdy iron and has a small, square window at eye level. The room is silent except for the faint echo of dripping water. Which door will you choose to open?")
            option4 = str.lower(input("(w)est, (n1), (n2), (n3), (s1), (s2) or (s3):"))

            if option4 == "n1":
                print("You open the door to the north and find yourself in a room filled with strange, glowing mushrooms. The air is thick with a sweet, cloying scent. You take a deep breath and suddenly feel your limbs grow heavy. Your vision blurs, and the room begins to spin. You sink to the floor, overcome by the poisonous fumes. Just as you think your journey is over, you feel a sharp pain in your arm. You realize that you've been injected with an antidote and are slowly coming back to your senses. You see a figure in the distance, beckoning you to follow. You gather your strength and make your way back to the main dungeon. Your journey continues another day!")
            elif option4 == "n2":
                print("You open the door to the north and find yourself in a room filled with strange, glowing mushrooms. The air is thick with a sweet, cloying scent. You take a deep breath and suddenly feel your limbs grow heavy. Your vision blurs, and the room begins to spin. You sink to the floor, overcome by the poisonous fumes. Just as you think your journey is over, you feel a sharp pain in your arm. You realize that you've been injected with an antidote and are slowly coming back to your senses. You see a figure in the distance, beckoning you to follow. You gather your strength and make your way back to the main dungeon. Your journey continues another day!")
            elif option4 == "n3":
                print("You open the door to the north and find yourself in a room filled with powerful magical artifacts. The room is lit by a soft, glowing light, and you feel a strange energy in the air. You quickly gather what you can and make your way back to the door, but it's locked tight. Suddenly, the room begins to shake, and you hear a deep rumbling. You realize that you've stumbled upon a powerful magical portal and have been transported to another part of the dungeon. You are trapped - game over!")
            elif option4 == "w":
                print("You continue down the passage to the west and enter a grand chamber filled with intricate machinery. The room is filled with the sounds of gears grinding and steam hissing from pipes overhead. In the center of the room, you see a large, bronze clockwork mechanism that rises up to the high ceiling. The mechanism is ticking away, counting down to something. Panic sets in as you realize that this room is a trap. You turn to run, but it's too late. The mechanism reaches its conclusion and the room is consumed by a burst of flame and steam. Your journey has come to an abrupt end.")
            elif option4 == "s1":
                print("You open the door to the south and find yourself in a room filled with healing potions and magical artifacts. You realize that you've stumbled upon a treasure trove of powerful magic. You quickly grab what you can and turn to leave, but the door slams shut behind you. You hear a grinding noise, and the room begins to fill with a deadly gas. You cough and gasp for breath, but just as you think all is lost, you spot a crack in the wall. You quickly make your way through the small opening and find yourself back in the main dungeon. Your journey continues another day!")
            elif option4 == "s2":
                print("You open the door to the south and find yourself in a room filled with powerful magical creatures. The room is filled with the sounds of their growls and snarls, and you realize that you're in grave danger. You turn to run, but the door slams shut behind you. You're surrounded on all sides by the dangerous creatures. You draw your weapon and prepare to fight for your life. Just as you're about to be overcome, you hear a loud noise in the distance. The creatures turn and flee, and you make your escape back to the main dungeon. Your journey continues another day!")
            elif option4 == "s3":
                print("You open the door to the south and find yourself in a room filled with a mysterious, glowing orb. The room is silent except for the soft glow of the orb. You approach it, drawn by its power, and reach out to touch it. Suddenly, you're enveloped in a warm, comforting light, and you feel a powerful energy coursing through your veins. Just as you're basking in the glow, you hear a loud noise in the distance. The orb goes dark, and you find yourself in complete darkness with no way to move.  You are stuck in the room and are cursed to never be able to leave the dungeon ...")

            else:
                print("Unknown command, game over")
          


        else:
            print("Unknown command, game over")
            

    else:
        print("Unknown command, game over") 

else:
    print("Unknown command, game over")
    
