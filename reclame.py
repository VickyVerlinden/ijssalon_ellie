from algemene_functies import mijn_functies_2

def aanbieding_1(smaak, prijs, korting):
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor 3,60 euro"
    return uitvoer

print(aanbieding_1("aardbei", 4, 0.1))

def inkomsten_totaal(inkomsten):
    inkomsten = (220+430+125+160+205+90+245)
    btw = (0.09)
    uitvoer = f"Het totaal van alle inkomsten van deze week is {inkomsten} euro, waarover {btw} euro btw betaald dient te worden"
    return uitvoer

totaal = inkomsten_totaal(220+430+125+160+205+90+245)
print(totaal)

def laag_en_hoog(mijn_lijst):
    maximum = max(mijn_lijst)
    minimum = min(mijn_lijst)
    nieuwe_lijst = [maximum, minimum]
    return nieuwe_lijst

cijfers = [220, 430, 125, 160, 205, 90, 245]
resultaat = laag_en_hoog(cijfers)
print(resultaat)

def gemiddelde(mijn_lijst):
    lengte = len(cijfers)
    som = sum(cijfers)
    gemiddelde = som/lengte
    nieuwe_lijst = [gemiddelde]
    return nieuwe_lijst

cijfers = [220, 430, 125, 160, 205, 90, 245]
resultaat = gemiddelde(cijfers)
print(resultaat)

def gemiddelde(mijn_lijst):
    lengte = len(cijfers)
    som = sum(cijfers)
    gemiddelde = som/lengte
    uitvoer = f"De gemiddelde inkomsten deze week is {gemiddelde} euro."
    return uitvoer

cijfers = [220, 430, 125, 160, 205, 90, 245]
resultaat = gemiddelde(cijfers)
print(resultaat)

def laag_en_hoog(invoer_lijst):
    maximum = max(invoer_lijst)
    minimum = min(invoer_lijst)
    nieuwe_lijst = [maximum, minimum]
    return nieuwe_lijst

cijfers = [10, 5, 3, 2, 1, 2, 9]
resultaat = laag_en_hoog(cijfers)
print(resultaat)

def combinatie(invoer_lijst_2):
    laag_en_hoog = (invoer_lijst_2)
    korte_lijst = laag_en_hoog
    return korte_lijst

mijn_functie_2 = [korte_lijst]
resultaat = combinatie(mijn_functie_2)
print(resultaat)