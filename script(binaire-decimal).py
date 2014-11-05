choix=input("Tapez B pour convertir un nombre binaire en décimal\nou D pour convertir un nombre décimal en binaire: ")
if choix==str("B") or choix==str("b"): #script du convertisseur nombre binaire en nombre décimal
        try: #pour lever les exceptions
                bi=int(input("Entrez un nombre binaire: "))
        except NameError:
                print("Veuillez saisir un nombre")  # exception qui pourra être levé par Python si la valeur n'a pas été définie
        except ValueError:
                print("Veuilez saisir un nombre")   #exception qui pourra être levé par Python face à diverses erreurs de « valeurs »
        dec,i=0,0
        while i<len(bi):
                rang=int(bi[i]) #rang des chiffres du nombre binaire
                if rang==1: #si le chiffre est 1
                        dec=dec+2**(len(bi)-(i+1)) #va convertir le chiffre binaire en chiffre décimal selon son rang et va additioner les décimaux
                else: #si le chiffre n'est pas 1 (dans ce cas là 0)
                        dec+=0
                i+=1
                print(bi,"vaut",dec,"en décimal")
elif choix==str("D") or choix==str("d"): #script du convertisseur nombre décima en nombre lbinaire
        try:
                dec=int(input("Entrer nombre décimal: "))
        except NameError:
                print("Veuillez saisir un nombre")  # exception qui pourra être levé par Python si la valeur n'a pas été définie
        except ValueError:
                print("Veuilez saisir un nombre")   #exception qui pourra être levé par Python face à diverses erreurs de « valeurs »
        print(dec,"vaut",bin(dec)[2:],"en binaire") #bin est la fonction qui permet de convertir un nombre décimal et binaire
else:
        print("Veuillez saisir D ou B")
