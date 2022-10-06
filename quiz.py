print('\n\n\nWelkom bij de gigantische Webdevelopers Quiz 2022')

antwoord=input('Ben je klaar om de Quiz te spelen? (ja/nee) :')
punten=0
aantal_vragen=15
 
if antwoord.lower()=='ja':

    print('\n\nMooi. Dan gaat de gigantische Webdevelopers Quiz 2022 beginnen!!\nGeef bij iedere vraag als antwoord de voornaam van een student uit de klas op.\n\n')

    antwoord=input('Vraag 1: Waar werd El Greco geboren ')
    if antwoord.lower()=='Griekenland':
        punten += 1
        print('goed!')
    else:
        print('fout!')
 
    antwoord=input('Vraag 2: Uit welke opera komen de personages Zuniga, Escamillo en Frasquita? ')
    if antwoord.lower()=='Carmen':
        punten += 1
        print('goed')
    else:
        print('fout')

    antwoord=input('Vraag 3: Welke Franse ingenieur bouwde twee bruggen voor de stad Porto? ')
    if antwoord.lower()=='Gustave Eiffel':
        punten += 1
        print('goed')
    else:
        print('fout')

    antwoord=input('Vraag 4: In welke stad kan je het beroemde beeld David van Michelangelo bewonderen? ')
    if antwoord.lower()=='Firenze':
        punten += 1
        print('goed')
    else:
        print('fout')
    
    antwoord=input('Vraag 5: Wat is de naam van de Joodse kandelaar met religieuze betekenis? ')
    if antwoord.lower()=='Menora':
        punten += 1
        print('goed')
    else:
        print('fout')
    
    antwoord=input('Vraag 6: Wie schilderde het plafond van de Sixtijnse kapel? ')
    if antwoord.lower()=='Michelangelo':
        punten += 1
        print('goed')
    else:
        print('fout')
    
    antwoord=input('Vraag 7: Wie schreef het boek Waterschapsheuvel ')
    if antwoord.lower()=='Richard Adams':
        punten += 1
        print('goed')
    else:
        print('fout')

    antwoord=input('Vraag 8: Wat is de echte naam van zanger, dichter en tekstschrijver Drs. P. ')
    if antwoord.lower()=='Heinz Herman Polzer':
        punten += 1
        print('goed')
    else:
        print('fout')
    
    antwoord=input('Vraag 9: Aan welke, wereldberoemde, Nederlandse grafisch kunstenaar is een permanente tentoonstelling gewijd in het paleis Lange Voorhout in Den Haag ')
    if antwoord.lower()=='Maurits Cornelis Escher':
        punten += 1
        print('goed')
    else:
        print('fout')
    
    antwoord=input('Vraag 10: Wat is het adres van Sherlock Holmes \nA: Bakerstreet 221B, Londen\nB: Ballerinas\nC: Gustave Eiffel\nD: Firenze\n')
    if antwoord=='A':
        punten += 1
        print('goed')
    else:
        print('fout')

    antwoord=input('Vraag 11: Wat hebben Yvette Chauvir en Anna Pavlova gemeen ')
    if antwoord.lower()=='Ballerinas':
        punten += 1
        print('goed')
    else:
        print('fout')

    antwoord=input('Vraag 12: Hoe noemt de kunstenares die gehuwd is met dokter Lecomte ')
    if antwoord.lower()=='Begga DHaese':
        punten += 1
        print('goed')
    else:
        print('fout')

    antwoord=input('Vraag 13: In welk toneelstuk van Marc Camoletti slaagt een man erin een affaire te hebben met drie airhostessen met de nodige problemen tot gevolg ')
    if antwoord.lower()=='Boeing Boeing':
        punten += 1
        print('goed')
    else:
        print('fout')

    antwoord=input('Vraag 14: Wie schreef American Psycho ')
    if antwoord.lower()=='Bret Easton Ellis':
        punten += 1
        print('goed')
    else:
        print('fout')

    antwoord=input('Vraag 15: Onder welke naam is het schilderij "De compagnie van kapitein Frans Banning Cocq en luitenant Willem van Ruytenburgh maakt zich gereed om uit te marcheren." beter bekend ')
    if antwoord.lower()=='De nachtwacht':
        punten += 1
        print('goed')
    else:
        print('fout')

    print('\n\nBedankt voor het spelen van de Quiz, je hebt '+str(punten)+' van de '+str(aantal_vragen)+' vragen juist beantwoord!')
    cijfer = round(float(10/aantal_vragen*punten), 1)
    print('Je cijfer voor project komt daarmee op een voorlopige '+str(cijfer)+'.')
    if punten >= 2: print('Goed bezig!')
    else:           print('Hmmm, kan beter... nog even oefenen chef.\n\n')

elif antwoord.lower()=='nee':
    print('De Quiz gaat niet beginnen, want ik begrijp dat je er nog niet klaar voor bent.\nJammer joh!')
else:
    print('Dit antwoord ken ik niet!')

def is_valide_studentnaam(studentnaam):
    namen = ['stijn','prosper','mohamed','max','charlotte','thijs','julian','rowan','nizar','cas','quinten','sean','sander','thomas','jason','johan','ryan','danny','jeffrey','romano','daan','nick','michael','tygo']
    for naam in namen:
        if naam==studentnaam.lower(): 
            return True
    return False

def calculate(calculation):
    return eval(calculation)

print(is_valide_studentnaam('Johan'))
print(is_valide_studentnaam('Marcel'))
print(is_valide_studentnaam('Thijs'))
print(is_valide_studentnaam('Michael'))
print(is_valide_studentnaam('Kees'))
calc = input('Geef een berekening op: ')
print(calculate(calc))