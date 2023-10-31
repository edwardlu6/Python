def your_dream():
    while True:
        print("You are an outstanding computer engineer in a major corporation, earning high salaries, living a decent life.")
        print("One day you are having a strange dream and you have counsciousness in this dream.")
        print("You are sitting on a chair in a spacious and dark room. It is rainy heavily outside.")
        print("There is a table in front of you. On the opposed side of the table is a man in black jacket.")
        print("The man tells you that you are living in a simulation. You are enslaved by machines.")
        print("Then he offers you two options to continue the conversation: red pill or blue pill.")
        print("You take the blue pill.You wake up in your bed, and believe what you want to believe.")
        print("You take the red pill. You stay in wonderland, and find out how deep the rabbit hole goes.")
        

        
        choice = str.lower(input("Which pill will you choose?(red/blue)"))

        
        if choice == "red":
            
            return mirror()
        elif choice == "blue":
            
            return bedroom()
    
        else:
            print("I don't understand this choice")

def mirror():
    
    while True:
        print("The man leads you in front of a mirror.")
        print("You touched the mirror. Then the mirror melts as you touch it.")
        print("Walls, chairs now gradually become green numbers and letters.")
        print("You feel afraid and wonder if you should continue.")

        choice = str.lower(input("Will you stay and continue or come back?(stay/come back)"))

        if choice == "stay":
            print("The mirror sticks to your right arm and gradually flow into your mouth.")
            print("You start screaming, and your voice sounds like electric flows.")
            return new_world()
            


        elif choice == "come back":
            return your_dream()

        else:
            print("I don't understand this choice")

def new_world():
    while True:
        print("You wake up in a human-sized container.")
        print("Then you get up and found that there are many towers with containers filled with humans. You are one of them.:")
        print("You are completely shocked and don't know what to do next.")
    
        choice = str.lower(input("Will you leave or stay in the container?(leave/stay)"))

        if choice == 'leave':
              return game_over1()
        elif choice == 'stay':
            return mirror()

        else:
            print("I don't understand this choice.")


def game_over1():
    print("You are ejected through a pipeline into a massive water pool.")
    print("You lose your strength and consciousness and drown in the water.")
    print("A spaceship catch you using a metal arm. You are saved!")
    print("You wake up in the spaceship and see many people you don't know.")
    print("Game over, you win!")


def bedroom():
    while True:
        print("You wake up on your bed, still thinking about last night dream.")
        print("It is sunny outside. You can choose to go to work as usual or continue to sleep.")

        choice = str.lower(input("Will you go to work or sleep?(work/sleep)"))

        if choice == "work":
            return office()
        elif choice == 'sleep':
            return your_dream()
        else:
            print("I don't understand this choice.")


def office():
    while True:
        print("You come to your office. You sit down in front of your computer.")
        print("You still keep thinking about the dream and question if this is reality.")

        choice = str.lower(input("Will you continue working or leave the office?(work/leave)"))

        if choice == 'work':
            return game_over2()
        elif choice == 'leave':
            return bedroom()
        else:
            print("I don't understand this choice.")

def game_over2():
    print("After so many years, you are promoted to the chairman of the company.")
    print("You sit inside the chairman office, feeling pround for your achievement.")
    print("You forget anything about the strange dream many years ago and everything here feels so real.")
    print("Game over, you lose!")

room = your_dream()
