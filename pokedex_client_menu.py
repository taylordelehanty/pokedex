#!/usr/bin/env python3

import pokedex_client_methods
import pokedex

def menu(status):
    pokedex_client_methods.startup()

    while status:
        action = input('Press the corresponding key to the action you want to perform:\ns: search for a Pokemon\na: look at all Pokemon\ne: exit the Pokedex\n')
        if action == 's':
            pokedex_client_methods.search_for_pkmn()
        elif action == 'a':
            pokedex_client_methods.see_all()
        elif action == 'e':
            status = False
            return status
        else:
            print("I'm sorry, that is not a registered key. Please try again.")

status = True

menu(status)
