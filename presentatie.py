from helper import onderstreep

mijn_dict = {'vis': 10, 'vlees': 25, 'overig': 15}
totaal = 50

def presenteer(dict, totaal):
    for item in mijn_dict:
        print(f"{item} : {mijn_dict[item]} euro")
presenteer(mijn_dict, sum(mijn_dict.values()))
print("================")
print(f"totaal : {totaal} euro")



