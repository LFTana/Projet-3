#voilà le script du convertisseur nombre binaire en nombre décimal
bi=input("Entrer nombre binaire: ")
dec,i=0,0
while i<len(bi):
    rang=int(bi[i]) #rang des chiffres du nombre binaire
    if rang==1: #si le chiffre est 1
        dec=dec+2**(len(bi)-(i+1)) #va convertir le chiffre binaire en chiffre décimal selon son rang et va additioner les décimaux
    else: #si le chiffre n'est pas 1 (dans ce cas là 0)
        dec+=0
    i+=1
print(bi,"=",dec)

#voila le script du convertisseur nombre décima en nombre lbinaire
dec=input("Entrer nombre Décimal: ")
bi=int(dec)
print(bin(bi)) #bin est la fonction qui permet de convertir un nombre décimal et binaire
