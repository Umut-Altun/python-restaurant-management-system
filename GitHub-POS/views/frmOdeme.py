from forms.frmOdemeUi import Ui_frmOdeme
from PyQt5 import QtWidgets
from database.connect_to_database import connect_to_database
import mysql
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt5.QtCore import QDateTime

class frmOdeme(QtWidgets.QWidget):
    def __init__(self, masa_no=None):
        super(frmOdeme, self).__init__()
        self.ui = Ui_frmOdeme()
        self.ui.setupUi(self)
        self.showFullScreen()

        self.ui.lblOdemeMasaNo.setText(masa_no)

        #butonları tıklanma olaylarına baglama
        self.ui.btnGeri.clicked.connect(self.back_application)
        self.ui.btnUrunGetir.clicked.connect(self.populate_table)
        self.ui.btnHesapKapat.clicked.connect(self.close_account)

        #database baglantısı baslatma
        self.connection = connect_to_database()


    def back_application(self):
        from views.frmMasalar import frmMasalar
        self.masalar = frmMasalar()
        self.masalar.show()
        self.close()

    def populate_table(self):
        masa_no = self.ui.lblOdemeMasaNo.text()
        servis_turu = "normal"
        durum = "açık"

        if self.connection is not None:
            try:
                cursor = self.connection.cursor()

                #siparisleri veritabanından alma
                query = (
                    "SELECT s.id, s.urunİd, s.adisyonİd, s.masaİd, s.adet,s.urunNot, u.urunAd, u.fiyat " \
                    "FROM satislar AS s " \
                    "INNER JOIN urunler AS u ON s.urunİd = u.id " \
                    "WHERE s.masaİd = %s AND s.servisTuru = %s AND s.durum = %s")
                
                cursor.execute(query, (masa_no, servis_turu, durum))

                #tablodakı verılerımı varsa temızlensın
                self.ui.twSiparisOdeme.setRowCount(0)

                #toplam tutarı hesaplama
                total_price = 0

                #verileri tabloya ekleyerek fıyat toplamını gosterıcez
                for row_num, (satis_id, urun_id, adisyon_id, masa_id, adet, urun_not, urun_adi, fiyat) in enumerate(cursor.fetchall()):
                    self.ui.twSiparisOdeme.insertRow(row_num)
                    self.ui.twSiparisOdeme.setItem(row_num, 0, QTableWidgetItem(urun_adi))
                    self.ui.twSiparisOdeme.setItem(row_num, 1, QTableWidgetItem(str(adet)))
                    self.ui.twSiparisOdeme.setItem(row_num, 2, QTableWidgetItem(str(fiyat)))
                    self.ui.twSiparisOdeme.setItem(row_num, 3, QTableWidgetItem(str(urun_not)))
                    self.ui.twSiparisOdeme.setItem(row_num, 4, QTableWidgetItem(str(satis_id)))
                    self.ui.twSiparisOdeme.setItem(row_num, 5, QTableWidgetItem(str(urun_id)))
                    self.ui.twSiparisOdeme.setItem(row_num, 6, QTableWidgetItem(str(adisyon_id)))
                    self.ui.twSiparisOdeme.setItem(row_num, 7, QTableWidgetItem(str(masa_id)))

                    #her urunun adetını ve fıyatını carp ve toplam fıyata ekle
                    item_total = adet * fiyat
                    total_price += item_total

                #toplam tutarı lblToplam tutarda goster
                self.ui.lblToplamTutar.setText(str(total_price))

                cursor.close()
            except mysql.connector.Error as err:
                print("Hata populate_table:", err)
        else:
            print("Veritabanı bağlantısı başarısız")

    def close_account(self):
        self.masa_no = self.ui.lblOdemeMasaNo.text()

        #odeme turu kontrollerı
        payment_type = ""
        if self.ui.rbNakit.isChecked():
            payment_type = self.ui.rbNakit.text()   #nakit
        elif self.ui.rbKart.isChecked():
            payment_type = self.ui.rbKart.text()   #kart

        if not payment_type:
            QMessageBox.critical(self, "Odeme Türü Hatas", "Lütfen ödeme türünü seçin...")
            return
        

        # hesap kapatılsın mı uyarısı
        if self.ui.btnHesapKapat.clicked:
            confirmation = QMessageBox.critical(self, "Onaylama", "Masa Kapatılmasını Onaylıyorum", QMessageBox.Ok | QMessageBox.Cancel)
            if confirmation == QMessageBox.Ok:
                if self.connection is not None:
                    try:
                        cursor = self.connection.cursor()

                        # adsiyon idlerini bır kumede saklayalım
                        adisyon_ids = set()

                        #sıparıs verılerını alıp her adsıyon toplam tutarı hesaplama
                        adisyon_totals = {}

                        for row_num in range(self.ui.twSiparisOdeme.rowCount()):
                            adisyon_id = int(self.ui.twSiparisOdeme.item(row_num, 6).text())
                            adisyon_ids.add(adisyon_id)   # her adsiyonu bır kere lısteye eklemıs

                            #sıparıs toplam tutarlarını hespalama
                            item_price = float(self.ui.twSiparisOdeme.item(row_num, 1).text())
                            item_quantity = int(self.ui.twSiparisOdeme.item(row_num, 2).text())
                            item_total = item_price * item_quantity

                            if adisyon_id in adisyon_totals:
                                adisyon_totals[adisyon_id] += item_total
                            else:
                                adisyon_totals[adisyon_id] = item_total

                            #her adsıyon ıcın odeme ve masa durmu guncelleme ıslemlerı
                            toplam_tutar = adisyon_totals[adisyon_id]
                            tarih = QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss")
                            servis_turu = "normal"

                            print(f"\n ------------ MASA KAPATMA İŞLEMLERİ BAŞLADI ------------")
                            try:
                                #verileri hesapodemelerı tablosuna ekleme
                                cursor.execute(
                                    "INSERT INTO hesapodemeleri (adisyonİd, odemeTuru, toplamTutar, tarih, servisTuru) VALUES (%s,%s,%s,%s,%s)",
                                    (adisyon_id, payment_type, toplam_tutar, tarih, servis_turu)
                                )
                                print(f"DB masa {self.masa_no} için Hesap ödemeleri tamamlandı")
                            except Exception as ex:
                                print(f"Hata Hesap ödemeleri", ex)


                            try:
                                # adisoyon durumlarını guncelle 
                                cursor.execute(
                                    "UPDATE adisyonlar SET durum = %s WHERE masaİd = %s AND servisTuru = %s",
                                    ("kapalı", self.masa_no, servis_turu)
                                )
                                print(f"DB masa {self.masa_no} için Adisyon guncellemesı tamamlandı")
                            except Exception as ex:
                                print(f"Hata Adisyon guncellemesı", ex)

                                
                            try:
                                # masa durumlarını guncelle
                                cursor.execute(
                                    "UPDATE masalar SET durum = %s, masaDurum = %s WHERE id=%s",
                                    (1, "kapalı", self.masa_no)
                                )
                                print(f"DB masa {self.masa_no} için Masa guncellenmesı tamamlandı")
                            except Exception as ex:
                                print(f"Hata Masa guncellenmesı", ex)


                            try:
                                # siparisleri guncellemek
                                cursor.execute(
                                    "UPDATE satislar SET durum = %s WHERE masaİd=%s AND servisTuru = %s",
                                    ("kapalı", self.masa_no, servis_turu)
                                )
                                print(f"DB masa {self.masa_no} için satıslar guncellendı tamamlandı")
                            except Exception as ex:
                                print(f"Hata satıslar guncellenmesı", ex)

                            print(f" ------------ MASA KAPATMA İŞLEMLERİ TAMAMLANDI ------------")

                        self.connection.commit()

                        #hesao odemesını aldıktan sonra tabloyu bosalt
                        self.ui.twSiparisOdeme.setRowCount(0)
                        self.ui.lblToplamTutar.setText("0.00")
                        self.close()

                        #odeme ıslemlerının somnunda masaalra donus yapsın
                        from views.frmMasalar import frmMasalar
                        self.frm_masalar = frmMasalar()
                        self.frm_masalar.show()

                    except mysql.connector.Error as err:
                        print("Hata:", err)
                else:
                    print("Veritabanı bağlantısı başarısız")



        
