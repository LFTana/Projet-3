choix=input("Tapez B pour convertir un nombre binaire en décimal\nou D pour convertir un nombre décimal en binaire: ")
if choix==str("B") or choix==str("b"): #choix pour convertir un nombre binaire en nombre décimal
	try: #pour lever les exceptions
		bi=input("Entrez un nombre binaire: ")
	except NameError:
		print("Veuillez saisir un nombre.")  # exception qui pourra être levé par Python si la valeur n'a pas été définie
	except ValueError:
		print("Veuilez saisir un nombre.")   #exception qui pourra être levé par Python face à diverses erreurs de « valeurs »
	dec=0
	i=0
	l=True
	for x in range(0,len(bi)):
		if bi[x] in ["2","3","4","5","6","7","8","9"]:
			l=False
	while l!=True:
		print("Un nombre binaire est composé de 1 et de 0\nVeuillez resaisir un nombre binaire.")
		try: #pour lever les exceptions
			bi=input("Entrez un nombre binaire: ")
		except NameError:
			print("Veuillez saisir un nombre.")  # exception qui pourra être levé par Python si la valeur n'a pas été définie
		except ValueError:
			print("Veuilez saisir un nombre.")   #exception qui pourra être levé par Python face à diverses erreurs de « valeurs »
		for y in range(0,len(bi)):
			if bi[y] in ["2","3","4","5","6","7","8","9"]:
				l=False
			else:
				l=True
	else:
		if len(bi)>16:
			print("Veuillez saisir un nombre binaire à 16 bits")
		else:        
			if int(bi)>0: 
				while i<len(bi):
					rang=int(bi[i]) #rang des chiffres du nombre binaire
					if rang==1: #si le chiffre est 1
						dec=dec+2**(len(bi)-(i+1)) #va convertir le chiffre binaire en chiffre décimal selon son rang et va additioner les décimaux
					else: #si le chiffre n'est pas 1 (dans ce cas là 0)
						dec+=0
					i+=1
				print(bi,"vaut",dec,"en décimal")
			else:
				nbi=bi[1:]
				while i<len(nbi):
					rang=int(nbi[i]) #rang des chiffres du nombre binaire
					if rang==1: #si le chiffre est 1
						dec=dec+2**(len(nbi)-(i+1)) #va convertir le chiffre binaire en chiffre décimal selon son rang et va additioner les décimaux
					else: #si le chiffre n'est pas 1 (dans ce cas là 0)
						dec+=0
					i+=1
				dec=-1*dec
				print(bi,"vaut",dec,"en décimal")
                
elif choix==str("D") or choix==str("d"): #choix pour convertir un nombre décimal en nombre binaire
		try:
			dec=int(input("Entrer nombre décimal: "))
		except NameError:
			print("Veuillez saisir un nombre.")  # exception qui pourra être levé par Python si la valeur n'a pas été définie
		except ValueError:
			print("Veuilez saisir un nombre.")   #exception qui pourra être levé par Python face à diverses erreurs de "valeurs"
		if dec>65535:
			print("Veuillez saisir un nombre inférieur à 65535 car le résultat ne doit pas dépasser 16 bits.")
		else:
			if dec<0:
				bi=bin(dec)
				z=bi[3:]
				ch=""
				for k in range(0,len(z)): #effectue le complément à deux
					if z[k]=="1":
						ch=ch+"0"
					elif z[k]=="0":
						ch=ch+"1"
				print(ch)
				nch=""
				if int(ch[len(ch)-1])==0:
					nch=ch[:(len(ch)-1)]+"1"
					print(dec,"vaut",nch,"en binaire.")
				else:
					print("fsdd")
			else:
				print(dec,"vaut",bin(dec)[2:],"en binaire.") #bin est la fonction qui permet de convertir un nombre décimal positif en binaire
else:
	print("Veuillez saisir D ou B.")
