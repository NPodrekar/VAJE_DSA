p = 61
q = 53
n = p * q
fi = (p-1)*(q-1)
e = 7
d = 1783
divisors = []
for i in range(1,121):
    if 120 % i == 0:
        divisors.append(i)
print(divisors)        

for i in range(n):
    if(e*i % fi) == 1:
        print(i)

def fnRSA(besedilo,kljuc,n):
    sifra = ""
    for char in besedilo:
        crka = chr(((ord(char))** kljuc) % n)
        sifra += crka 
    return sifra

print(fi)