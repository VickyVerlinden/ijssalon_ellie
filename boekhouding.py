from helper import *
from presentatie import *  
import csv 

inkomsten = {
    "Aardbeien-ijs-totaal" : 1000,
    "Vanille-ijs-totaal" : 2000,
    "Chocolade-ijs-totaal" : 1500,
    "Waterijsjes-totaal" : 750
}
totaal_inkomsten = sum(inkomsten.values())

def presenteer(inkomsten, totaal_inkomsten):
    for smaak, bedrag in inkomsten.items():
        print(f"{smaak}: {bedrag} euro")
presenteer(inkomsten, sum(inkomsten.values()))
print("================")
print(f"Totaal inkomsten: {totaal_inkomsten} euro") 



with open('boekhouding.csv', 'w',newline="") as csvfile:
    for key, value in inkomsten.items():
        writer = csv.writer(csvfile, delimiter=';')
    writer.writerow([key,value])