import mysql.connector
from forms.frmSiparisUi import Ui_frmSiparis
from PyQt5 import QtWidgets
from database.connect_to_database import connect_to_database
import mysql
from datetime import datetime
from PyQt5.QtWidgets import QMessageBox

class frmSiparis(QtWidgets.QWidget):
    def __init__(self, masa_no=None):
        super(frmSiparis, self).__init__()
        self.ui = Ui_frmSiparis()
        self.ui.setupUi(self)
        self.showFullScreen()

        #Tıklanan masanın numarasını alma
        self.ui.lblMasaNo.setText(masa_no)

        # Kategori ID'lerini butonlarla eşleştiren bir sözlük oluşturun
        category_buttons = {
            self.ui.btnAnaYemek: 1,
            self.ui.btnMakarna: 2,
            self.ui.btnSalata: 3,
            self.ui.btnCorba: 4,
            self.ui.btnFastfood: 5,
            self.ui.btnIcecekler: 6,
            self.ui.btnArasicak: 7,
            self.ui.btnTatli: 8,
            self.ui.btnDurum: 9,
        }

        #Butonlara tıklama İşlemleri
        for button, category_id in category_buttons.items():
            button.clicked.connect(lambda _, category_id=category_id: self.get_items_by_category(category_id))

        
        # butonlara tıklandığında yapılacak işlemler
        self.ui.btnGeri.clicked.connect(self.back_application)
        self.ui.twIcindekiler.itemClicked.connect(self.contents_table)
        self.ui.btnOdeme.clicked.connect(self.payment_application)
        self.ui.btnUrunSil.clicked.connect(self.order_table_delete)
        self.ui.btnSiparis.clicked.connect(self.order_application)


        #database baglantısı baslatma
        self.connection = connect_to_database()


    def get_items_by_category(self, category_id):   # Kategori id'sine gore urunleri getirme
        if self.connection is not None:
            try:
                cursor = self.connection.cursor()

                #urunler tablosundan kategori id'sine gore urunleri getirme
                query = "SELECT id, urunAd, fiyat FROM urunler WHERE kategoriİd = %s"
                cursor.execute(query, (category_id,))
                items = cursor.fetchall()

                # tablewiewdekı verılerı temızleme
                self.ui.twIcindekiler.setRowCount(0)

                #verilerimizii tabloya ekleme
                for row_num, (urunAd,fiyat, id) in enumerate(items):
                    self.ui.twIcindekiler.insertRow(row_num)
                    self.ui.twIcindekiler.setItem(row_num, 0, QtWidgets.QTableWidgetItem(str(fiyat)))
                    self.ui.twIcindekiler.setItem(row_num, 1, QtWidgets.QTableWidgetItem(str(id)))
                    self.ui.twIcindekiler.setItem(row_num, 2, QtWidgets.QTableWidgetItem(str(urunAd)))

                cursor.close()

            except mysql.connector.Error as err:
                print("Hata get_items_by_category:", err)

        else:
            print("Veritabanı baglantısı baslatılamadi")

    def contents_table(self, item):   #urunlerı ıcerık tablosuna aktarma
        #secılen urunlerın bılgılerını alma
        selected_row = item.row()
        urun_fiyati = self.ui.twIcindekiler.item(selected_row, 0).text()
        urun_id = self.ui.twIcindekiler.item(selected_row, 1).text()
        urun_notu = ""
        urun_adi = self.ui.twIcindekiler.item(selected_row, 2).text()

        # twsiparis tablosundakı mevcut satırları kontrol etme
        for row in range(self.ui.twSiparis.rowCount()):
            existing_item = self.ui.twSiparis.item(row, 4)
            if existing_item and existing_item.text() == urun_adi:
                #urun zaten mevcut ise adetini arttırma
                adet_item = self.ui.twSiparis.item(row, 1)
                current_adet = int(adet_item.text()) if adet_item else 0
                new_adet = current_adet + 1
                adet_item = QtWidgets.QTableWidgetItem(str(new_adet))
                self.ui.twSiparis.setItem(row, 1, adet_item)
                return
            

        #twsiparis yenı bir satır ekleme ıslemlerını
        row_position = self.ui.twSiparis.rowCount()
        self.ui.twSiparis.insertRow(row_position)

        #urun bılgıelrını twspiarisler tablosuna yerlestır
        self.ui.twSiparis.setItem(row_position, 0, QtWidgets.QTableWidgetItem(urun_fiyati))
        self.ui.twSiparis.setItem(row_position, 2, QtWidgets.QTableWidgetItem(urun_notu))
        self.ui.twSiparis.setItem(row_position, 3, QtWidgets.QTableWidgetItem(urun_id))
        self.ui.twSiparis.setItem(row_position, 4, QtWidgets.QTableWidgetItem(urun_adi))
            
    def back_application(self):  # Masalar sayfasına donme
        from views.frmMasalar import frmMasalar
        self.masalar = frmMasalar()
        self.masalar.show()
        self.close()

    def order_table_delete(self):  # siparisi silme
        #secılen urunu alma
        selected_items = self.ui.twSiparis.selectedItems()
        if not selected_items:
            return
        
        #secılen urunun buludungu satırı alma
        selected_row = selected_items[0].row()
        self.ui.twSiparis.removeRow(selected_row)

    def payment_application(self):   # odeme sayfasına gecme
        masa_no = self.ui.lblMasaNo.text()
        from views.frmOdeme import frmOdeme
        self.odeme = frmOdeme(masa_no)
        self.odeme.show()
        self.close()

    def order_application(self):   # siparis verme ıslemlerı
        #twsiparisler tablosundakı verılerın kontrolu
        for col in range(self.ui.twSiparis.columnCount()):
            item = self.ui.twSiparis.item(0, 0)
            if item is None or item.text() == "":
                QMessageBox.critical(self, "Hata", "Siparisler bos olamaz")
                return

        #twsiparislerdekı urunlerın adetını kontrol et
        for row in range(self.ui.twSiparis.rowCount()):
            adet_item = self.ui.twSiparis.item(row, 1)
            if adet_item is None or adet_item.text() == "":
                QMessageBox.critical(self, "Hata", "Siparisler bos olamaz")
                return
            

        #siparis verme ıslemlerını
        table_number = self.ui.lblMasaNo.text()    #MASA 1
        print(f"Masa {table_number} numarasdıır...")

        # masa durumu kondtol eden ıslem masa dolu mu bosmu
        adisyon_id = self.chech_table_status(table_number)

        print(f"\n ----- MASANIN ACMA DURUMU {adisyon_id} ----- \n")
        #sıpasrıslerın varlgını ve yoklugnu kontrol etme
        if adisyon_id is not None:
            #mevcut bır adsıyon var sıparısler bunun uzerıne eklesın
            self.add_order_to_existing_adisyon(adisyon_id)
        else:
            #mevcut adısyon yok ıse yenı bır adsıyon olustur ve sıparıslerı ekle
            adisyon_id = self.create_new_adisyon(table_number)
            self.add_order_to_existing_adisyon(adisyon_id)

        self.update_table_status(table_number)
        
        print(f"\n ----- MASANIN ACMA DURUMU TAMAMLANDI ----- \n")

        self.close()
        from views.frmMasalar import frmMasalar
        self.masalar = frmMasalar()
        self.masalar.show()


    def chech_table_status(self, table_number):     # masa durumunu kontrol eden ıslem
        if self.connection is not None:
            try:
                cursor = self.connection.cursor()

                #masalar tablosundan belırlı bir masa numarasına gore adisyon durumunu kontrol etme
                query = "SELECT id FROM adisyonlar WHERE masaİd = %s AND durum = 'açık' AND servisTuru = 'normal'"
                cursor.execute(query, (table_number,))
                result = cursor.fetchone()
                cursor.close()

                if result:
                    return result[0]
                else:
                    return None

            except mysql.connector.Error as err:
                print("Hata chech_table_status:", err)
        else:
            print("Veritabanı baglantısı baslatılamadi")

    def create_new_adisyon(self, table_number):     # Yeni adisyon olusturma
        if self.connection is not None:
            try:
                cursor = self.connection.cursor()

                #yenı bır adsıyon olusturma
                query = "INSERT INTO adisyonlar (masaİd, tarih, durum, servisTuru) VALUES (%s, %s, %s, %s)"
                current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                cursor.execute(query, (table_number, current_datetime, "açık", "normal"))
                self.connection.commit()

                #olusturulan adısyonun id numarsaını al
                query = "SELECT LAST_INSERT_ID()"
                cursor.execute(query)
                adisyon_id = cursor.fetchone()[0]

                cursor.close()
                print(f"Masa {table_number} adisyon olusturuldu... Adisyon ID: {adisyon_id}")

                return adisyon_id

            except mysql.connector.Error as err:
                print("Hata create_new_adisyon:", err)
        else:
            print("Veritabanı baglantısı baslatılamadi")
    
    def add_order_to_existing_adisyon(self, adisyon_id):    # Mevcut adisyona sipariş ekleme
        table_number = self.ui.lblMasaNo.text()

        if self.connection is not None:
            try:
                cursor = self.connection.cursor()

                for satir in range(self.ui.twSiparis.rowCount()):
                    #siparis detaylarını tablodan alma ıslemlerı
                    urun_id = self.ui.twSiparis.item(satir, 4).text()
                    adet = self.ui.twSiparis.item(satir, 1).text()
                    urum_not = self.ui.twSiparis.item(satir, 2).text()

                    #satıs zamanını alma
                    tarih_ve_saat = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    servis_turu = "normal"
                    durum = "açık"

                    #siparisi satıslar tablosudnakı verılerle uyusturarak ekle
                    query = "INSERT INTO satislar (adisyonİd, urunİd, masaİd, adet, servisTuru, durum, satisZamani, urunNot) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                    cursor.execute(query, (adisyon_id, urun_id, table_number, adet, servis_turu, durum, tarih_ve_saat, urum_not))
                    self.connection.commit()

                cursor.close()
                print(f"Masa {table_number} için siparişler eklendi.")


            except mysql.connector.Error as err:
                print("Hata add_order_to_existing_adisyon:", err)
        else:
            print("Veritabanı baglantısı baslatılamadi")

    def update_table_status(self, table_number):     # Masa durumunu guncelleme
        if self.connection is not None:
            try:
                cursor = self.connection.cursor()
                query = "UPDATE masalar SET durum = 2, masaDurum = 'açık' WHERE id = %s "
                cursor.execute(query, (table_number,))

                self.connection.commit()
                cursor.close()
                print(f"Masa {table_number} durumu guncellenmıstır...")

            except mysql.connector.Error as err:
                print("Hata update_table_status", err)
        else:
            print("Database baglantısı hatalı")