prijzen = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5
    }
aanbieding = prijzen["vanille"]*0.8
reclame_tekst = "Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts €"
#oefening 5 klopt niet, dit is berekend op basis van de waarden van aardbei-ijs, maar de vraag is vanille-ijs (reclame_tekst2)
reclame_tekst3 = "Vandaag", "in", "de", "aanbieding", ":", "vanille-ijs", ",", "1", "liter", "-", "slechts", "€"
print(("Vandaag in de aanbieding : vanille-ijs, 1 liter - slechts €3,20").upper())
reclame_tekst4 = ["Vandaag", "in", "de", "aanbieding", ":", "vanille-ijs", ",", "1", "liter", "-", "slechts", "€"]
el = "Vandaag", "in", "de", "aanbieding", ":", "vanille-ijs", ",", "1", "liter", "-", "slechts", "€", "3,20"
for i in el:
    print(i)
print(("el").lower())