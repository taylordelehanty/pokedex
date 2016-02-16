#!/usr/bin/env python3

import pokedex

dexter = pokedex.Pokedex()

def startup():
    dexter.set_all_pkmn_dict()
    dexter.main()

def search_for_pkmn():
    pkmn_name = dexter.choose_pkmn()
    pkmn_list = dexter.get_pkmn_info(pkmn_name)
    if len(pkmn_list) == 0:
        print("Your search found no results.")
    elif len(pkmn_list) == 1:
        try:
            pkmn_id = dexter.get_pkmn_id(pkmn_name)
            print(pkmn_list)
            dexter.get_pkmn_pic(pkmn_id)
        except:
            y_n = input("Did you mean " + pkmn_list[0][0] + "?")
            if y_n != 'y':
                pass
            else:
                pkmn_list = dexter.get_pkmn_info(pkmn_list[0][0])
                pkmn_id = dexter.get_pkmn_id(pkmn_list[0][0])
                print(pkmn_list)
                dexter.get_pkmn_pic(pkmn_id)
    else:
        print(pkmn_list, "\nYour search returned multiple results!\nWould you like to search again?")

def see_all():
    print(dexter.see_all_pkmn())
