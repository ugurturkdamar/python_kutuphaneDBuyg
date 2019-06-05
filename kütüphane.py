import sqlite3
import time

class Kitap():

    def __init__(self,isim,yazar,yayinevi,tür,baskı):

        self.isim=isim
        self.yazar=yazar
        self.yayinevi=yayinevi
        self.tür=tür
        self.baskı=baskı

    def __str__(self):
        return "Kitap İsmi:{}\nYazar:{}\nYayınevi:{}\nTür:{}\nBaskı:{}".format(self.isim,self.yazar,self.yayinevi,self.tür,self.baskı)

class Kütüphane():

    def __init__(self):
        self.baglantiOlustur()

    def baglantiOlustur(self):
        self.con = sqlite3.connect("kütüphane.db")

        self.cursor = self.con.cursor()

        self.cursor.execute("create table if not exists kitaplar(isim text,yazar text,yayınevi text,tür text,baskı int)")

        self.con.commit()

    def baglantiKes(self):

        self.con.close()

    def kitaplariGoster(self):

        self.cursor.execute("select * from kitaplar")

        data = self.cursor.fetchall()

        if (len(data) == 0):
            print("Kütüphanede kitap bulunmuyor.")
        else:
            for i in data:
                kitap = Kitap(i[0],i[1],i[2],i[3],i[4])
                print(kitap)

    def kitapSorgula(self,isim):

        self.cursor.execute("select * from kitaplar where isim=?",(isim,))

        data = self.cursor.fetchall()

        if (len(data) == 0):
            print("Böyle bir kitap bulunmuyor.")
        else:
            kitap = Kitap(data[0][0],data[0][1],data[0][2],data[0][3],data[0][4])

            print(kitap)

    def kitapEkle(self,kitap):

        self.cursor.execute("insert into kitaplar values(?,?,?,?,?)",(kitap.isim,kitap.yazar,kitap.yayinevi,kitap.tür,kitap.baskı))

        self.con.commit()

    def kitapSil(self,isim):

        self.cursor.execute("delete from kitaplar where isim = ?",(isim,))

        self.con.commit()

    def baskıYukselt(self,isim):

        self.cursor.execute("select * from kitaplar where isim=?",(isim,))

        data = self.cursor.fetchall()

        if(len(data) == 0):
            print("Böyle bir kitap bulunmuyor.")
        else:
            baskı = data[0][4]

            baskı+=1

            self.cursor.execute("update kitaplar set baskı = ? where isim = ? ",(baskı,isim))

            self.con.commit()

    def populerKitaplar(self):

        self.cursor.execute("select * from kitaplar order by baskı desc")

        data = self.cursor.fetchall()

        if(len(data) == 0):
            print("Kütüphanede kitap yok!")
        else:
            for i in data:
                kitap = Kitap(i[0],i[1],i[2],i[3],i[4])
                print(kitap)

    def kitapAdıGuncelle(self,yeni_isim,eski_isim):

        self.cursor.execute("update kitaplar set isim=? where isim=?",(yeni_isim,eski_isim))

        self.con.commit()

            
































