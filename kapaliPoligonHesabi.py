import math as m
k = "ic"
Bic = False
Bdis = False
devam = False
B = []
yeniBt = []
Sn = []
Pn = []
Bt = []
Pcount = 4
def BetaKarar():
    if k == "ic":
        Bic = True
    elif k == "dis":
        Bdis == True
    else: 
        print("something goes wrong")


def kirilmaAciHata(Bic, Bdis, n, Bt):
    Bt_sum = m.sum(Bt)
    
    if Bic == True and Bdis == False:
        fB = Bt_sum - (n - 2 ) * (200*180/200)
    elif Bic == False and Bdis == True:
        fB = Bt_sum - (n + 2 ) * (200*180/200)
    FB = 1.5 * m.sqrt(n)
    if fB < FB:
            x = fB/len(Bt)
    else :
        devam == True
    for i in Bt:
        e = i+x
        yeniBt.append(e)
    return yeniBt

def kenKapHata(Dy,Dx):
    Dyt = sum(Dy)
    Dxt = sum(Dx)
    fs = m.sqrt(Dyt**2 + Dxt**2)
    fsMax = 0.01 * m.sqrt()

#hesap ana gövde;
# --------------------------------- 
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

def hesapla(Xy, Bt, Yn, Xn, Sn): 
    SA_list = []
    x = 0
    i=0
    c = 0
    Bic = True
    Dyl = []
    Dxl = []
    kirilmaAciHata(Bic,Bdis,len(Bt),Bt)
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
# ------------------------------------------------

