
import math as m
Sn = [] # verilen iki nokta arası uzaklılıkları
Pn = [] # sonuç listesi bu listede bulunmak istenen noktaların koordinatları ikili şekilde bulunacak
Bt = [] # verilen açılar
yeniBt = [] # kırılma acısı hatası hesaplanırken güncellenen Bt değerlerinin konulacağı liste 
devam = False
# Bt = kırılma açıları 
# Bt_sum = beta kırılma açıları toplamı .
# IS = ilk semt açısı
# SS = son semt açısı
# devam = "devam = true" olursa eğer tekrar ölçüm yapılması gerek 
# bu nedenle kullanıcıya yeniden ölçüm yap mesajı verilir ve hesaba devam edilmez
# .

def kirilmaAcisiHatasi(Bt, IS, SS, devam):
    Bt_Sum = sum(Bt)
    
    fB = SS - (IS + Bt_Sum + len(Bt)+(200*180/200)) # kırılma açılarında yapılan hata miktarı
    FB = 1,5 * m.sqrt(len(Bt)) # yönetmelikteki formül(aşşağıdaki kontrol evresinde hata payının kabul edilebilirliğini kontrol etmek için kullanılır)
    if fB < FB:
        x = fB/len(Bt) # hata miktarı bt adedine bölünerek bt lere eklemek için hazır hale getirilir
    else :
        devam == True
    for i in Bt:
        e = i+x # sıradaki bt değerine daha önce bt adedine bölünerek bulunan x eklenir
        yeniBt.append(e) # hata kabul edilebilirse; Bt leri güncellemek için yeniBt listesi oluşturulur 
                         # ve oluşan listeye güncellenmiş bt eklenir
    return yeniBt # böylece kenar kapatma hatası düzelir ve hesapta kullanılmak üzere bt; yeniBt olarak güncellenmiş olur

# Dy ve Dx hesapla fonksiyonunda elde edilen  deltay ve delta x i temsil eder  
# Yb ve Xb verilen ilk noktanın koordinatları
# Yc ve Xc verilen son noktanın koordinatları
# Bt kırılma açıları
def kenKapHata(Dy, Dx, Yb, Xb, Yc, Xc, Bt):
    Dyt = sum(Dy) # Dyt delta y lerin toplamı
    Dxt = sum(Dx) # Dxt delta x lerin toplamı
    S = m.sqrt(Dyt**2 + Dxt**2) 
    Fy = Yc - Yb # y için koordinatlar farkı
    Fx = Xc - Xb # x için koordinatlar farkı
    fy = Fy - Dyt # kenar kapatma hatası
    fx = Fx - Dxt # kenar kapatma hatası


    fQ = (1/S) * (fy * Dxt - fx * Dyt) # enine kapanma hatası
    fL = (1/S) * (fy * Dyt - fx * Dxt) # boyuna kapanma hatası
    fQ_max = 0.05 + 0.15 * m.sqrt(S/1000) # S yi kilometre cinsine çevirmemiz gerekiyor bu nedenle 1000 e böldük
    fL_max = 0.05 + 0.04 * m.sqrt(len(Bt)-1)
    # fqmax ve flmax yönetmelikteki kabul edilebilirliği kontrol ediyor

    # buradan sonrası dhunt yöntemi ile orantılı bir şekilde hataları Dy(delta y) ve Dx(delta x) üzerine eklenecek not sayı 0.08 gibi bir değer geliyor ona dikkat etmek gerek hata olabilir
    # ya da kırılma acısı hatasında olduğu gibi de yapılabilir 
    if fQ < fQ_max and fL < fL_max:
        # deneme.py dosyası içerisindeki yöntem (dhunt) ile 
        # Dy ve Dx üzerine orantılı olarak eklenecek 
        # (dhunt yöntemi orantılı yapıyor)
        return 0


# açık poligon ile aynı  SA = (Bt +Xy) + Z bu SA formülünde parantez içerisindeki alan T yi temsil ediyor ve +Z işlemi Kontrol(T) içerisinde yapılıyor
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
    x = 0
    i=0
    c = 0
    Dyl = [] # bulunacak delta y ve delta xler bu iki liste içerisine daha sonra 
    Dxl = [] # kenar kapatma hesabı ile güncellenmek üzere eklenecek
    kirilmaAcisiHatasi(Bt, IS, SS, devam)
    for i in range (len(yeniBt)):
        # 1.adım
        T = (Xy+yeniBt[c]) # konterol(T) fonksiyonunda +z işlemi yapılmak üzere ayrı hesaplanıyor
        SA = kontrol(T) # ve SA bu işlemden sonra bulunuyor
        # 2.adım 
        Dy = Sn[c]*m.sin(m.radians(SA*(180/200)))
        Dx = Sn[c]*m.cos(m.radians(SA*(180/200)))
        #delta y ve delta x leri listelere aldık daha sonra bu listeler ile kenar kapatma hata hesabı yapılacak
        # burada güncellenen 
        Dyl.append(Dy)
        Dxl.append(Dx)
        Py = Dy + Yn
        Px = Dx + Xn
        Xy = SA

        n = [] # bu liste sadece bir noktanın koordinatlarını alacak
        n.append(Py)
        n.append(Px)
        Pn.append(n) # bulunan koordinatlar listesi(n) Pn(sonuç) listesine eklenecek
        Yn = Py # bir sonraki döngüde başka bir noktaya geçilebilmesi için noktanın y ve x değerleri güncelleniyor
        Xn = Px       
        c+=1
    
    print(Pn)
#he(61.2547, [321.4856,47.1457,227.4785], 5474.48, 2457.72, [100.61,79.54,147.12])









