import pickle
import random
print("***************************************************************************")
print("Pwogram sa ap pemet ou jwe woulet")
nomb_chwazi = random.randrange(0, 101)
k='Wap gen pouw chwazi nonb nan de 0 a 100'
print(k.upper())
#print("Odinate chwazi yon nonb nan anteval 0 a 100 ki: ", nomb_chwazi)
print("***************************************************************************")

chans_rete = 5
eseye = 0
esko_itilizate=0

 
try:
    with open('done.pickle', 'rb') as fiche:
        done = pickle.load(fiche)
except FileNotFoundError:
    done = {}
epsedo = input("Rantre non w (sans espaces) : ")

while True:
    epsedo = input("Antre non itilizatew (san let majiskil, san espas): ")
    if ' ' not in epsedo and epsedo.islower(): 
        break
    else:
        print("Non itilizatew pa sipoze gen espas ak let majiskil")

if epsedo in done:
    esko_itilizate = done[epsedo]
    print("Bonjour! {}, esko avan ou te : {}".format(epsedo, esko_itilizate))
else:
    print("Bonjour! {}, byenvini nan jwet nou an !".format(epsedo))
    done[epsedo] = 0
g=False

while True:
    while chans_rete > 0:

        chwa_itilizate = float(input("Chwazi yon nomb: "))
        if chwa_itilizate < 0 or chwa_itilizate >= 100:
            print("Tanpri, chwazi yon nomb nan anteval 0 a 100 selman.")
            continue
        eseye += 1
        if chwa_itilizate < nomb_chwazi:
            print("Nonb ou chwazi a pi piti pase nonb pa odinate a.")
        elif chwa_itilizate > nomb_chwazi:
            print("Nonb ou chwazi a pi gwo pase nonb pa odinate a.")
        else:
            print("******************************************************************************")
            nouvo_esko= 30 * chans_rete
            esko_itilizate += nouvo_esko
            print("BRAVO!!! {} -- esko ou pou pati sa se: {} e nouvo esko ou se: {}".format(epsedo, nouvo_esko,esko_itilizate))
        
            done[epsedo] = esko_itilizate 
            with open('done.pickle', 'wb') as fiche:
                pickle.dump(done, fiche) 
                break

        chans_rete -= 1
        print("ou rete: ", chans_rete, " chans")
    if chans_rete == 0:
        print("-----------------------------------------------------------------------------------------")
        print("Ou pedi! Nonb la se", nomb_chwazi, "score ou rete {}".format(esko_itilizate))
    #chans_rete += 5  
    print("-----------------------------------------------------------------------------------------------")

    stop= input("peze k siw vle kanpe jwe e nenpot lot touche pou kontinye: ")
    if stop.lower()=='k':
        chans_rete==0
        print("Mesi paske ou te jwe ak nou")
        break
    else:
        chans_rete = 5
        print("Ou genyen {} chans knyea".format(chans_rete))
        nomb_chwazi = random.randrange(0, 101)
        print ("Nou kontan ou kontinye jwe ak nou")
        
