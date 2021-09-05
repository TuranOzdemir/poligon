
import math as m
Sn = []
Pn = []
Bt = []
yeniBt = []
Pcount = 4
devam = False
Slis = []


def kirilmaAcisiHatasi(Bt, IS, SS, devam):
    Bt_Sum = sum(Bt)
    
    fB = SS - (IS + Bt_Sum + len(Bt)+200) #Bt_Sum dan sonra gelen + veya - olacak kontrol et /// +200 grad cinsinden hata olabilir
    FB = 1,5 * m.sqrt(len(Bt))
    if fB < FB:
        x = fB/len(Bt)
    else :
        devam == True
    for i in Bt:
        e = i+x
        yeniBt.append(e)
    return yeniBt

def kenKapHata(Dy, Dx, Yb, Xb, Yc, Xc, Bt, Slis):
    Dyt = sum(Dy)
    Dxt = sum(Dx)
    S = m.sqrt(Dyt**2 + Dxt**2)
    Fy = Yc - Yb
    Fx = Xc - Xb
    fy = Fy - Dyt
    fx = Fx - Dxt

    # fs = m.sqrt(fy**2 + Fx**2) 
    # kapalı Kapalı poligon hesabında geçki başlanan noktada 
    # bittiği için enine ve boyuna hataları hesaplanamaz. Bu nedenle doğrusal kapanma hatası 
    # fs kenar kapanma hatası hesaplanır. 

    fQ = (1/S) * (fy * Dxt - fx * Dyt) 
    fL = (1/S) * (fy * Dyt - fx * Dxt)
    fQ_max = 0.05 + 0.15 * m.sqrt(S/1000) # S yi kilometre cinsine çevirmemiz gerekiyor bu nedenle 1000 e böldük
    fL_max = 0.05 + 0.04 * m.sqrt(len(Bt)-1)
    Slis.sort()
    lenfy = fy*100
    if lenfy < 0:
        lenfy * -1
    lenfx = fx*100
    if lenfx < 0:
        lenfx *-1


    if fQ < fQ_max and fL < fL_max:
        # deneme.py dosyası içerisindeki yöntem (dhunt) ile 
        # Dy ve Dx üzerine orantılı olarak eklenecek 
        # (dhunt yöntemi orantılı yapıyor)
        return 0

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

# Xy 1. semt açısı
# Bt beta kırılma açıları
# Yn ve Xn ilk noktanın verilen koordinatları 
# Sn verilen iki nokta arası uzunluklar



def hesapla(Xy, Bt, Yn, Xn, Sn, IS, SS): 
    SA_list = []
    x = 0
    i=0
    c = 0
    Dyl = []
    Dxl = []
    kirilmaAcisiHatasi(Bt, IS, SS, devam)
    for i in range (len(yeniBt)):
        # 1.adım
        T = (Xy+yeniBt[c])
        SA = kontrol(T)
        # 2.adım 
        Dy = Sn[c]*m.sin(m.radians(SA*(180/200)))
        Dx = Sn[c]*m.cos(m.radians(SA*(180/200)))
        #delta y ve delta x leri listelere aldık daha sonra bu listeler ile kenar kapatma hata hesabı yapılacak
        Dyl.append(Dy)
        Dxl.append(Dy)
        Py = Dy + Yn
        Px = Dx + Xn
        Xy = SA

        n = []
        n.append(Py)
        n.append(Px)
        Pn.append(n)
        Yn = Py
        Xn =Px       
        c+=1
    
    print(Pn)
#he(61.2547, [321.4856,47.1457,227.4785], 5474.48, 2457.72, [100.61,79.54,147.12])









