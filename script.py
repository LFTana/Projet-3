bi=input("Entrer nombre binaire: ")
dec,i=0,0
while i<len(bi):
    rang=int(bi[i])
    if rang==1:
        dec=dec+2**(len(bi)-(i+1))
    else:
        dec+=0
    i+=1
print(bi,"(base 2)est égale à",dec,"(base 10)")
