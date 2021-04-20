import json
import os
from collections import Counter
from Sets import OG, PR, EB

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

                for i in PR.PRSets.sets:
                    if set_name.startswith(i):
                        set_objects[set_name] = PR.PRSets()
                        data = json.load(json_data)
                        for x in data:
                            set_objects[set_name].add_card(str(x['card_name']))

                for i in EB.EBSets.sets:
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
    full_pack = []

    print(set_objects.keys())
    while True:
        try:
            selected_set_name = input('What pack do you want to open?')
            selected_set = set_objects[selected_set_name.upper()]
        except KeyError:
            print("Please enter a valid set.")
            continue
        else:
            break

    while True:
        try:
            numb_pack = int(input('How many packs do you want to open?'))
        except ValueError:
            print("Please enter a number.")
            continue
        else:
            break
    t_tracker = input('Would you like to see each individual pack?')

    if numb_pack == 0:
        rare = input('Select your Rarity!')
        print(selected_set.pull_card(rare))
    else:
        if t_tracker.upper() == "YES":
            for p in range(0, numb_pack):
                print(selected_set.create_pack())
        else:
            for p in range(0, numb_pack):
                full_pack += selected_set.create_pack()
            total = Counter(full_pack)
            for i in total:
                print("% s : % s" % (i, total[i]), end="\n")


if __name__ == '__main__':
    main()
