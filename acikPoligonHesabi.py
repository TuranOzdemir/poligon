
import math as m
def kontrol(T):
    if 0<=T and T<=200:
        T+=200
    elif 200<=T and T<=400:
        T-=200
    elif 400<=T and T<=600:
        T-=200
    elif 600<=T and T<=800:
        T-=600
    return T
Sn = []
Pn = []
Bt = []
Pcount = 4
# Xy 1. semt açısı
# Bt beta kırılma açıları
# Yn ve Xn ilk noktanın verilen koordinatları 
# Sn verilen iki nokta arası uzunluklar
def semtAcisi(Xy, Bt, Yn, Xn, Sn): 
    SA_list = []
    x = 0
    i=0
    c = 0
    for i in range (len(Bt)):
        # 1.adım
        T = (Xy+Bt[c])
        SA = kontrol(T)
        # 2.adım 
        Py = Sn[c]*m.sin(m.radians(SA*(180/200)))+Yn
        Px = Sn[c]*m.cos(m.radians(SA*(180/200)))+Xn
        Xy = SA
        n = []
        n.append(Py)
        n.append(Px)
        Pn.append(n)
        Yn = Py
        Xn =Px       
        c+=1
    print(Pn)
semtAcisi(61.2547, [321.4856,47.1457,227.4785], 5474.48, 2457.72, [100.61,79.54,147.12])




