# Pokemon lists
pokemon_names = ['charmander', 'squirtle', 'bulbasaur', 'gyrados']
pokemon_amounts = [3, 2, 5, 1]
pokemon_fees = ['100.00', '50.00', '25.00', '1000.00']
pokemon_types = [['fire'], ['water'], ['grass'], ['water', 'flying']]
valid_pokemon_types = ['bug', 'dark', 'dragon', 'electric', 'fairy', 'fighting', 'fire', 'flying', 'ghost', 'grass', 'ground', 'ice', 'normal', 'poison', 'psychic', 'rock', 'steel', 'water']


    

while True:
    print('Welcome to the Pokemon Center!')
    choice = str.lower(input('(a)dd, (r)emove, r(e)port, (s)earch by name, search by (t)ype, (l)ist or (q)uit:'))
    if choice == 's':
        name = str.lower(input('Name of Pokemon to search for:'))
        for i in range(len(pokemon_names)):
            if pokemon_names[i] == name:
                print('We have', pokemon_amounts[i], name.capitalize(), 'at the Pokemon Center')
                print('It will cost $',  pokemon_fees[i], ' to adopt this Pokemon', sep = '')
                if i < 3:
                    print(name.capitalize(), 'has the following types:', print(pokemon_types[i][0].capitalize()))
                elif i == 3:
                    print(name.capitalize(), 'has the following types:', pokemon_types[i][0].capitalize(), pokemon_types[i][1].capitalize())
    elif choice == 'l':
        print('Name                    Amount Available        Adoption Fee Type(s)')
        for i in range(len(pokemon_names)):
            if len(pokemon_types[i]) > 1:
                print(format(pokemon_names[i].capitalize(), '<38'), pokemon_amounts[i], format(float(pokemon_fees[i]), '>19,.2f'), end = ' ')
                for j in range(len(pokemon_types[i])):
                    print(pokemon_types[i][j].capitalize(), end = ' ')
                print()
            elif len(pokemon_types[i]) == 1:
                print(format(pokemon_names[i].capitalize(), '<38'), pokemon_amounts[i], format(float(pokemon_fees[i]), '>19,.2f'), pokemon_types[i][0].capitalize())

    elif choice == 't':
        type = input('Enter Pokemon type:')
        if type == 'water':
            print('Name                    Amount Available        Adoption Fee Type(s)')
            print('Squirtle                               2               50.00 Water ')
            print('Gyrados                                1            1,000.00 Water Flying ')
        elif type == 'fire':
            print('Name                    Amount Available        Adoption Fee Type(s)')
            print('Charmander                             3              100.00 Fire ')
        elif type == 'grass':
            print('Name                    Amount Available        Adoption Fee Type(s)')
            print('Bulbasaur                              5               25.00 Grass ')
        elif type == 'flying':
            print('Name                    Amount Available        Adoption Fee Type(s)')
            print('Gyrados                                1            1,000.00 Water Flying ')
        else:
            print('We have no Pokemon of that type at our Pokemon Center')

    elif choice == 'a':
        new_name = input('Enter name of new pokemon:')
        if new_name in pokemon_names:
            print('Duplicate name, add operation cancelled')
        else:
            pokemon_names += [new_name]
            while True:
                number = int(input('How many of these Pokemon are you adding?'))
                if number <= 0:
                    print('Invalid, please try again')
                    continue
                else:
                    pokemon_amounts += [number]
                    break
            while True:
                fee = float(input('What is the adoption fee for this Pokemon?'))
                if fee <= 0:
                    print('Invalid, please try again')
                    continue
                else:
                    pokemon_fees += [fee]
                    break
            print("Next you will be prompted to enter the 'types' for this Pokemon.  Pokemon can have multiple types. Type 'help' to view all possible Pokemon types, and type 'end' to stop entering types. You must enter at least one valid 'type'")
            added_type = []
            while True:
                type1 = str.lower(input('What type of Pokemon is this?'))
                
                if type1 == 'help':
                    print('* bug','* dark','*dragon','* electric','* fairy','* fighting','* fire','* flying','* ghost','* grass','* ground','* ice','* normal','* poison','* psychic','* rock','* steel','* water', sep = '\n')
                elif type1 in valid_pokemon_types:
                    print('Type', type1, 'added')
                    added_type += [type1]
                elif type1 == 'end':
                    print('Pokemon Added!')
                    break
                else:
                    print('This is not a valid type, please try again')
            pokemon_types += [added_type]
    elif choice == 'r':
        remove_name = str.lower(input('Enter name of Pokemon to remove:'))

        for i in range(len(pokemon_names)):
            if pokemon_names[i] == remove_name:
                pokemon_names.remove(pokemon_names[i])
                del pokemon_amounts[i]
                del pokemon_fees[i]
                del pokemon_types[i]    
                print('Pokemon removed')
                break
        else:
            print('Pokemon not found, cannot remove')
    elif choice == 'e':
        pokemon_fees_int  = []
        for i in range(len(pokemon_fees)):
            pokemon_fees_int.append(float(pokemon_fees[i]))
        print('Highest priced Pokemon:', pokemon_names[pokemon_fees_int.index(max(pokemon_fees_int))], '@ $' + format(max(pokemon_fees_int), ',.2f'), 'per Pokemon')
        print('Lowest priced Pokemon:',  pokemon_names[pokemon_fees_int.index(min(pokemon_fees_int))], '@ $' + format(min(pokemon_fees_int), ',.2f'), 'per Pokemon')
        sum = 0
        for i in range(len(pokemon_fees_int)):
            sum += pokemon_amounts[i] * pokemon_fees_int[i]
        print('Total cost to adopt all Pokemon in the Center: $' + format(sum, ',.2f'))
        
    elif choice == 'q':
        print('See you next time!')
        break
    else:
        print('Unknown command, please try again')
        
