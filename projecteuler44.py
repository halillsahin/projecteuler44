def beşgensel(x):
    return x*(3*x-1)/2
def kontrol(x):
    return ((1+(1+24*x)**(1/2))/6).is_integer()
for i in range(1,5000):
    sayı1=beşgensel(i)
    for a in range(i-1,0,-1):
        sayı2=beşgensel(a)
        if kontrol(sayı1-sayı2) and kontrol(sayı1+sayı2):
            print(sayı1-sayı2)
            break
