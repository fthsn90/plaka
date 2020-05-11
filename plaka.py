from tkinter import *
import tkinter
import random


pencere= Tk()
pencere.title('Plaka Bulma Oyunu')
pencere.geometry("400x400")
pencere.configure(bg="gray")
ustyazi = Label(pencere,text="Plaka Bulma Oyunu",font="Arial 20 bold",bg="gray",justify="center").pack(side=TOP,padx=30,pady=10)



def yeni():
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    r5.destroy()
    plakane.destroy()
    btn.destroy()
    btn2.destroy()
    lblcvp.destroy()
    puanlbl.destroy()
    yenisoru()
def cevapla():
    global puan
    for i in illerplaka:
        if i ==var.get():
            if illerplaka[var.get()]==cvp:
                lblcvp["text"]=str(var.get().title())+" şehri doğru cevap! Tebrikler"
                puan+=5
                puanlbl["text"]=puan
            else:
                lblcvp["text"]=str(var.get().title())+" şehri yanlış cevap!"
                puan -=5
                puanlbl["text"]=puan


def ilgetir():
    global adcevap,cvp,illerplaka
    iller = ['BALIKESİR', 'BİLECİK', 'BURSA', 'ÇANAKKALE', 'EDİRNE', 'İSTANBUL', 'KIRKLARELİ', 'KOCAELİ', 'SAKARYA', 'TEKİRDAĞ', 'YALOVA', 'DÜZCE', 'AMASYA', 'ARTVİN', 'BOLU', 'ÇORUM', 'GİRESUN', 'GÜMÜŞHANE', 'KASTAMONU', 'ORDU', 'RİZE', 'SAMSUN', 'SİNOP', 'TOKAT', 'TRABZON', 'ZONGULDAK', 'BAYBURT', 'BARTIN', 'KARABÜK', 'AFYON', 'AYDIN', 'DENİZLİ', 'İZMİR', 'KÜTAHYA', 'MANİSA', 'MUĞLA', 'UŞAK', 'ANKARA', 'ÇANKIRI', 'ESKİŞEHİR', 'KAYSERİ', 'KIRŞEHİR', 'KONYA', 'NEVŞEHİR', 'NİĞDE', 'SİVAS', 'YOZGAT', 'AKSARAY', 'KARAMAN', 'KIRIKKALE', 'AĞRI', 'BİNGÖL', 'BİTLİS', 'ELAZIĞ', 'ERZİNCAN', 'ERZURUM', 'KARS', 'MALATYA', 'MUŞ', 'TUNCELİ', 'VAN', 'ARDAHAN', 'IĞDIR', 'ADANA', 'ANTALYA', 'BURDUR', 'HATAY', 'ISPARTA', 'MERSİN', 'KAHRAMANMARAŞ', 'OSMANİYE', 'ADIYAMAN', 'DİYARBAKIR', 'GAZİANTEP', 'HAKKARİ', 'MARDİN', 'SİİRT', 'ŞANLIURFA', 'BATMAN', 'ŞIRNAK', 'KİLİS']
    illerplaka = {"BALIKESİR":"10", "BİLECİK":"11", "BURSA":"16", "ÇANAKKALE":"17", "EDİRNE":"22", "İSTANBUL":"34", "KIRKLARELİ":"39", "KOCAELİ":"41", "SAKARYA":"54", "TEKİRDAĞ":"59", "YALOVA":"77", "DÜZCE":"81", "AMASYA":"5", "ARTVİN":"1", "BOLU":"14", "ÇORUM":"19", "GİRESUN":"28", "GÜMÜŞHANE":"29", "KASTAMONU":"37", "ORDU":"52", "RİZE":"53", "SAMSUN":"55", "SİNOP":"57", "TOKAT":"60", "TRABZON":"61", "ZONGULDAK":"67", "BAYBURT":"69", "BARTIN":"74", "KARABÜK":"78", "AFYON":"3", "AYDIN":"9", "DENİZLİ":"20", "İZMİR":"35", "KÜTAHYA":"43", "MANİSA":"45", "MUĞLA":"48", "UŞAK":"64", "ANKARA":"6", "ÇANKIRI":"18", "ESKİŞEHİR":"26", "KAYSERİ":"38", "KIRŞEHİR":"40", "KONYA":"42", "NEVŞEHİR":"50", "NİĞDE":"51", "SİVAS":"58", "YOZGAT":"66", "AKSARAY":"68", "KARAMAN":"70", "KIRIKKALE":"71", "AĞRI":"4", "BİNGÖL":"12", "BİTLİS":"13", "ELAZIĞ":"23", "ERZİNCAN":"24", "ERZURUM":"25", "KARS":"36", "MALATYA":"44", "MUŞ":"49", "TUNCELİ":"62", "VAN":"65", "ARDAHAN":"75", "IĞDIR":"76", "ADANA":"1", "ANTALYA":"7", "BURDUR":"15", "HATAY":"31", "ISPARTA":"32", "MERSİN":"33", "KAHRAMANMARAŞ":"46", "OSMANİYE":"80", "ADIYAMAN":"2", "DİYARBAKIR":"21", "GAZİANTEP":"27", "HAKKARİ":"30", "MARDİN":"47", "SİİRT":"56", "ŞANLIURFA":"63", "BATMAN":"72", "ŞIRNAK":"73", "KİLİS":"56"}
    sec1 = random.sample(iller,1)
    aday1 = iller.remove(sec1[0])
    a1 = sec1[0]
    cvp = illerplaka[a1]
    sec2 = random.sample(iller,1)
    iller.remove(sec2[0])
    a2 = sec2[0]
    sec3 = random.sample(iller,1)
    iller.remove(sec3[0])
    a3 = sec3[0]
    sec4 = random.sample(iller,1)
    iller.remove(sec4[0])
    a4 = sec4[0] 
    sec5 = random.sample(iller,1)
    iller.remove(sec5[0])
    a5 = sec5[0]
    adcevap = [a1,a2,a3,a4,a5]
    random.shuffle(adcevap)

def yenisoru():
    global var,lblcvp,r1,r2,r3,r4,r5,plakane,btn,btn2,puanlbl
    ilgetir()
    plakane= Entry(pencere,width=5)
    plakane.pack()
    plakane.insert(0,cvp)
    var = StringVar()


    r1=Radiobutton(pencere, text=adcevap[0], value=adcevap[0],variable=var,bg="gray")
    r1.pack(pady=7)
    r2=Radiobutton(pencere, text=adcevap[1], value=adcevap[1],variable=var,bg="gray")
    r2.pack(pady=7)
    r3=Radiobutton(pencere, text=adcevap[2], value=adcevap[2],variable=var,bg="gray")
    r3.pack(pady=7)
    r4=Radiobutton(pencere, text=adcevap[3], value=adcevap[3],variable=var,bg="gray")
    r4.pack(pady=7)
    r5=Radiobutton(pencere, text=adcevap[4], value=adcevap[4],variable=var,bg="gray")
    r5.pack(pady=7)

    btn = Button(pencere,text="Cevapla",command=cevapla)
    btn.pack()
    btn2 = Button(pencere,text="Yeni Soru Getir",command=yeni)
    btn2.pack()
    lblcvp = Label(pencere,text="",bg="gray")
    lblcvp.pack(padx=10,pady=10)
    puanlbl = Label(pencere,text=puan,bg="gray")
    puanlbl.pack(padx=10,pady=10)
puan = 0
yenisoru()
pencere.mainloop()
