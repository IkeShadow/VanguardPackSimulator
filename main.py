import json
import os
import random
from Sets import OG

set_objects = dict()


def sort_sets():
    for file in os.listdir(os.path.join('.', 'JSON Setlists')):
        if file.endswith('.json'):
            with open(os.path.join('JSON Setlists', file)) as json_data:
                set_name = os.path.splitext(str(file))[0]
                for i in OG.OGSets.sets:
                    if set_name.startswith(i):
                        set_objects[set_name] = OG.OGSets()
                    data = json.load(json_data)
                    for x in data:
                        if '\n' in x['rarity']:
                            for r in x['rarity'].split('\n'):
                                set_objects[set_name].add_card(str(r), str(x['card_name']))
                        else:
                            set_objects[set_name].add_card(str(x['rarity']), str(x['card_name']))


def main():
    sort_sets()

    print(set_objects.keys())
    selected_set_name = input('What pack do you want to open?')
    selected_set = set_objects[selected_set_name]

    while True:
        try:
            numb_pack = int(input('How many packs do you want to open?'))
        except ValueError:
            print("Please enter a number.")
            continue
        else:
            break

    for p in range(0, numb_pack):
        print(selected_set.create_pack())


if __name__ == '__main__':
    main()
