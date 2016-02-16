#!/usr/bin/env python3

import http.client, urllib.request, urllib.parse
import json
import ast
from image_handler import PokemonDisplay

class Pokedex:

    api_main = 'pokeapi.co'
    path = '/api/v1/'
    resource1 = 'pokedex'
    resource2 = '1'
    all_pkmn_dict = {}

    def set_all_pkmn_dict(self):
        data_dict = self.get_dict_from_api(self.api_main, self.make_whole_path(self.resource1, self.resource2))
        for k in data_dict['pokemon']:
            pkmn_name = k['name']
            pkmn_num = (k['resource_uri'].split('/'))[3]
            self.all_pkmn_dict[pkmn_name] = pkmn_num

    def get_dict_from_api(self, api_main, path):
        conn = http.client.HTTPConnection(api_main)
        conn.request("GET", urllib.parse.quote(path))
        response = conn.getresponse()
        if response.status == 200:
            data = response.read()
            decoded_data = data.decode('latin1')
            return ast.literal_eval(decoded_data)
        else:
            raise Exception("HTTP call failed: " + response.reason)

    def see_all_pkmn(self):
        all_pkmn = []
        for k, v in sorted(self.all_pkmn_dict.items()):
            if int(v) < 1000:
                v = v.zfill(3)
                all_pkmn.append((k,v))
        all_pkmn.sort(key = lambda pkmn: pkmn[1])
        return all_pkmn

    def get_html_from_site(self, site, path):
        conn = http.client.HTTPConnection(site)
        conn.request("GET", urllib.parse.quote(path))
        response = conn.getresponse()
        if response.status == 200:
            data = response.read()
            return data
        else:
            raise Exception("HTTP call failed: " + response.reason + site + path)

    def make_html_path(self, move):
        if move.lower() != 'will-o-wisp':
            return '/attackdex-xy/' + move.replace('-', '').replace(' ', '').lower() + '.shtml'
        elif move.lower() != 'mud-slap':
            return '/attackdex-xy/' + move.replace(' ', '').lower() + '.shtml'
        else:
            print('/attackdex-xy/' + move.replace(' ', '').lower() + '.shtml')
            return '/attackdex-xy/' + move.replace(' ', '').lower() + '.shtml'

    def make_whole_path(self, first_resource, second_resource):
        first_part = first_resource.lower() + '/'
        second_part = second_resource.lower() + '/'
        return self.path + first_part + second_part

    def choose_pkmn(self):
        pkmn_being_searched_for = input('''What is the name of the Pokemon you would like to search for?\n''').lower()
        return pkmn_being_searched_for

    def pkmn_in_dict(self, pkmn_being_searched_for):
        return pkmn_being_searched_for.lower() in self.all_pkmn_dict
        
    def part_of_pkmn_name_in_dict(self, pkmn_being_searched_for):
        for k,v in self.all_pkmn_dict.items():
            if pkmn_being_searched_for.lower() in k:
                return True
        return False

    def get_pkmn_info(self, pkmn_being_searched_for):
        if self.pkmn_in_dict(pkmn_being_searched_for):
            pkmn_name = pkmn_being_searched_for.upper()
            pkmn_id = self.get_pkmn_id(pkmn_being_searched_for)
            all_pkmn_info_dict = self.get_dict_from_api(self.api_main, self.make_whole_path('pokemon', self.all_pkmn_dict[pkmn_being_searched_for.lower()]))
            pkmn_types = self.get_pkmn_types(all_pkmn_info_dict['types'])
            pkmn_height = self.get_pkmn_height(all_pkmn_info_dict['height'])
            pkmn_weight = self.get_pkmn_weight(all_pkmn_info_dict['weight'])
            pkmn_base_hp = self.get_pkmn_hp(all_pkmn_info_dict['hp'])
            pkmn_base_atk = self.get_pkmn_atk(all_pkmn_info_dict['attack'])
            pkmn_base_def = self.get_pkmn_def(all_pkmn_info_dict['defense'])
            pkmn_base_sp_atk = self.get_pkmn_sp_atk(all_pkmn_info_dict['sp_atk'])
            pkmn_base_sp_def = self.get_pkmn_sp_def(all_pkmn_info_dict['sp_def'])
            pkmn_base_speed = self.get_pkmn_speed(all_pkmn_info_dict['speed'])
            pkmn_moves = self.get_moves(all_pkmn_info_dict['moves'])
            pkmn_generation_appearance = self.get_pkmn_generation(pkmn_id)
            return [(pkmn_name, pkmn_id, pkmn_types, pkmn_height, pkmn_weight, pkmn_base_hp, pkmn_base_atk, pkmn_base_def, pkmn_base_sp_atk, pkmn_base_sp_def, pkmn_base_speed, pkmn_moves, pkmn_generation_appearance)]

        elif self.part_of_pkmn_name_in_dict(pkmn_being_searched_for):
            pkmn_results_list_of_tuples = []
            for k,v in self.all_pkmn_dict.items():
                if pkmn_being_searched_for.lower() in k:
                    pkmn_results_list_of_tuples.append((k,v))
            return pkmn_results_list_of_tuples
        else:
            return []
        
    def get_pkmn_height(self, height_location):
        height_formatted = int(height_location) / 10
        return 'Height: ' + str(height_formatted) + ' m'

    def get_pkmn_weight(self, weight_location):
        weight_formatted = int(weight_location) / 10
        return 'Weight: ' + str(weight_location) + ' kg'

    def get_pkmn_id(self, pkmn_being_searched_for):
        return (self.all_pkmn_dict[pkmn_being_searched_for.lower()])

    def get_pkmn_types(self, list_of_types):
        if len(list_of_types) == 1:
            return 'Type: ' + list_of_types[0]['name']
        else:
            return 'Types: ' + list_of_types[0]['name'] + ', ' + list_of_types[1]['name']

    def get_pkmn_hp(self, hp_location):
        return 'Base Hit Points: ' + str(hp_location)

    def get_pkmn_atk(self, atk_location):
        return 'Base Attack: ' + str(atk_location)

    def get_pkmn_def(self, def_location):
        return 'Base Defense: ' + str(def_location)

    def get_pkmn_sp_atk(self, sp_atk_location):
        return 'Base Special Attack: ' + str(sp_atk_location)

    def get_pkmn_sp_def(self, sp_def_location):
        return 'Base Special Defense: ' + str(sp_def_location)

    def get_pkmn_speed(self, speed_location):
        return 'Base Speed: ' + str(speed_location)

    def get_moves(self, moves_location):
        learned_moves_tuples = []
        taught_moves_tuples = []
        tutor_moves_tuples = []
        for k in moves_location:
            if k['learn_type'] == 'level up':
                name = k['name']
                level = k['level']
                learned_moves_tuples.append((name, level))
                learned_moves_tuples = sorted(learned_moves_tuples, key = lambda move: move[1])
            elif k['learn_type'] == 'machine':
                name = k['name']
                #print(name.lower())
                #move_html = self.get_html_from_site('www.serebii.net', self.make_html_path(name))
                #print(move_html)
                #use html parser to find TM num
                tm_num = 'TM'
                taught_moves_tuples.append((name, tm_num))
                taught_moves_tuples = sorted(taught_moves_tuples, key = lambda move: move[1])
            elif k['learn_type'] == 'tutor':
                name = k['name']
                tutor = 'Tutor'
                tutor_moves_tuples.append((name, tutor))
                tutor_moves_tuples = sorted(tutor_moves_tuples, key = lambda move: move[1])
        return (self.format_moves(learned_moves_tuples), self.format_moves(taught_moves_tuples), self.format_moves(tutor_moves_tuples))

    def get_all_move_info(self, ):
        move_dict = self.get_dict_from_api(self.api_main,)
        accuracy = move_dict['accuracy']
        power = move_dict['power']
        power_points = move_dict['pp']
        description = move_dict['description']
        return ("Accuracy: " + accuracy, "Power: " + power, power_points, description)

    def format_moves(self, list_of_moves_tuples):
        formatted_moves = []
        for move in list_of_moves_tuples:
            if type(move[1]) == int:
                information = '{} (Lv{})'
                formatted_moves.append(information.format(move[0], move[1]))
            elif move[1] == 'Tutor' or 'TM' in move[1]:
                information = '{} ({})'
                formatted_moves.append(information.format(move[0], move[1]))
            else:
                "An Error occurred"
        return formatted_moves

    def get_pkmn_generation(self, pkmn_num):
        pkmn_num = int(pkmn_num)
        if 1 <= pkmn_num <= 151:
            return 'Generation 1'
        elif 152 <= pkmn_num <= 252:
            return 'Generation 2'
        elif 253 <= pkmn_num <= 386:
            return 'Generation 3'
        elif 387 <= pkmn_num <= 493:
            return 'Generation 4'
        elif 494 <= pkmn_num <= 649:
            return 'Generation 5'
        elif 650 <= pkmn_num <= 721:
            return 'Generation 6'
        else:
            return 'Not from a specific generation'

    def get_pkmn_pic(self, pkmn_id):
        pkmn_id_formatted = str(pkmn_id).zfill(3)
        url = 'http://serebii.net/xy/pokemon/' + pkmn_id_formatted + '.png'
        pkmn_img = PokemonDisplay(url).draw_image()
        

    def main(self):
        print('''Welcome to the Pokedex. My name is Dexter, and I am your personal Pokemon encyclopedia. I am able to look up any Pokemon that Pokemon researchers already have information on.''')
