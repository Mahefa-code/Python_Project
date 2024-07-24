import random
def jeu_devinette():
    nombre_a_deviner = random.randint(1,100)
    print(nombre_a_deviner)
    tentative = 0
    print("J'ai choisi un nombre entre 1 et 100")

    while True:
        essai = input("Entrez votre devinette : ")
        try : 
            int(essai)
        except ValueError:
            print(f'Entre un nombre valide')
            continue
        essai = int(essai)
        tentative += 1
        if essai < nombre_a_deviner:
            print("Trop bas ! Essayer encore")
        elif essai > nombre_a_deviner:
            print("trop haut! Essayer encore")
        else:
            print(f"Félicitations ! Vous avez deviné le nombre en {tentative} tentative")
            break