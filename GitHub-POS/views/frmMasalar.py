import mysql
from forms.frmMasalarUi import Ui_frmMasalar
from PyQt5 import QtWidgets
from database.connect_to_database import connect_to_database
from PyQt5.QtGui import QPixmap, QIcon



class frmMasalar(QtWidgets.QWidget):
    def __init__(self):
        super(frmMasalar, self).__init__()
        self.ui = Ui_frmMasalar()
        self.ui.setupUi(self)
        self.showFullScreen()

        
        self.ui.btnCikis.clicked.connect(self.back_application)
        # Butonların tanımlanması
        self.masa_buttons = [
            self.ui.btnMasa1, self.ui.btnMasa2, self.ui.btnMasa3, self.ui.btnMasa4, self.ui.btnMasa5,
            self.ui.btnMasa6, self.ui.btnMasa7, self.ui.btnMasa8, self.ui.btnMasa9, self.ui.btnMasa10,
            self.ui.btnMasa11, self.ui.btnMasa12, self.ui.btnMasa13, self.ui.btnMasa14, self.ui.btnMasa15,
            self.ui.btnMasa16, self.ui.btnMasa17, self.ui.btnMasa18, self.ui.btnMasa19, self.ui.btnMasa20,
            self.ui.btnMasa21, self.ui.btnMasa22, self.ui.btnMasa23, self.ui.btnMasa24, self.ui.btnMasa25,
            self.ui.btnMasa26, self.ui.btnMasa27, self.ui.btnMasa28,
        ]

        # masa butonlarına tıklandığında yapılacak işlemler
        for i , masa_button in enumerate(self.masa_buttons, start=1):
            masa_button.clicked.connect(lambda _, masa_no=i: self.masa_button_clicked(masa_no))


        #Database baglantısı baslatma
        self.connection = connect_to_database()


        #Masalardaki masa butonları uzerındekı elemetlerı guncelleme ıslemlerı
        self.tables_control()   # Masalardaki masa butonları uzerındekı elemetlerı kontrol edılmesı
        self.update_table_status()  #masalardakı durumları guncelleme

    def back_application(self):
        QtWidgets.QApplication.quit()

    def masa_button_clicked(self, masa_no):   # sıpariş sayfasına gecme
        print(f"Masa {masa_no} tıklandı")
        from views.frmSiparis import frmSiparis
        self.sipari = frmSiparis(str(masa_no))
        self.sipari.show()
        self.close()

    def tables_control(self):   # Masalardaki masa butonları uzerındekı elemetlerı guncelleme
        if self.connection is not None:
            try:
                cursor = self.connection.cursor()
                # Adisyonlar tablosundan masa numarasına gore masa butonları uzerındekı elemetlerı guncelleme
                query = "SELECT masaİd, durum, tarih FROM adisyonlar WHERE durum = 'açık' AND servisTuru = 'normal'"
                cursor.execute(query)
                adisyonlar = cursor.fetchall()

                for adisyon in adisyonlar:
                    masa_id = adisyon[0]
                    masa_durum = adisyon[1]
                    tarih = adisyon[2]

                    if masa_durum == "açık":
                        #masa durum labelını doldurcaz
                        label_durum = getattr(self.ui, f"lblBtnDurum_{masa_id}")
                        label_durum.setText("Dolu")

                        #masa saatıs saatınını doldurcaz
                        label_tarih = getattr(self.ui, f"lblBtnSaat_{masa_id}")
                        label_tarih.setText(tarih.strftime("%H:%M"))

                        #masa toplam tutarını doldurcaz
                        toplm_tutar = self.calculate_total_sales(masa_id)
                        label_tutar = getattr(self.ui, f"lblBtnFiyat_{masa_id}")
                        label_tutar.setText(f"$ {str(toplm_tutar)}")

                    else:
                        label_durum = getattr(self.ui, f"lblBtnDurum_{masa_id}")
                        label_durum.setText("Boş")

                cursor.close()

            except mysql.connector.Error as err:
                print("Hata tables_control:", err)
        else:
            print("Veritabanı baglantısı baslatılamadi")

    def calculate_total_sales(self, masa_id):   # masa toplam tuatarını hesaplama
        if self.connection is not None:
            try:
                cursor = self.connection.cursor()

                #masaid gore satıslarının toplamını hesapla
                query = (f"SELECT SUM(u.fiyat * s.adet) FROM satislar s JOIN urunler u ON s.urunId = u.id WHERE s.adisyonId = (SELECT id FROM adisyonlar WHERE masaId = '{masa_id}' AND durum = 'açık' and servisTuru = 'normal') and s.durum = 'açık'")
                cursor.execute(query)
                total_sales = cursor.fetchone()[0]
                cursor.close()

                return total_sales if total_sales else "Boş"

            except mysql.connector.Error as err:
                print("Hata calculate_total_sales:", err)
                return "hata"
        else:
            print("Veritabanı bağlantısı başarısız")


    def update_table_status(self):   #masalardakı resim durumları guncelleme
        if self.connection is not None:
            try:
                cursor = self.connection.cursor()
                query = "SELECT id, durum FROM masalar"
                cursor.execute(query)
                masa_durumlari = cursor.fetchall()

                # Adisyonlar tablosundan masa numarasına gore masa butonları uzerındekı resımlerı guncelleme
                for masa_id, masa_durumu in masa_durumlari:
                    masa_button = self.masa_buttons[masa_id - 1]

                    if masa_durumu == "1":
                        #masa bosken resim doldurcaz
                        image_path = f":/nmasalar/resimler/MASA/bos_masa.png"
                        pixmap = QPixmap(image_path)
                        masa_button.setIcon(QIcon(pixmap))

                    elif masa_durumu == "2":
                        #masa doluyken resim doldurcaz
                        image_path = f":/nmasalar/resimler/MASA/dolu_masa.png"
                        pixmap = QPixmap(image_path)
                        masa_button.setIcon(QIcon(pixmap))

            except mysql.connector.Error as err:
                print("Hata update_table_status:", err)
        else:
            print("Veritabanı baglantısı baslatılamadi")
        