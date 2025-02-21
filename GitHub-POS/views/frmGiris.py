from datetime import datetime
import mysql.connector
from forms.frmGirisUi import Ui_frmGiris
from PyQt5 import QtWidgets
from database.connect_to_database import connect_to_database
from views.frmMenu import frmMenu
from PyQt5.QtWidgets import QMessageBox


class frmGiris(QtWidgets.QWidget):
    def __init__(self):
        super(frmGiris, self).__init__()
        self.ui = Ui_frmGiris()
        self.ui.setupUi(self)
        self.showFullScreen()


        # Butonlara tıklandığında yapılacak işlemler
        self.ui.btnGiris.clicked.connect(self.login_button_clicked)
        self.ui.btnCikis.clicked.connect(self.exit_application)

        #Database baglantısı baslatma
        self.connection = connect_to_database()


    def login_button_clicked(self):  # Giriş butonuna tıklandığında yapılacak işlemler
        username = self.ui.cbKullanici.text()
        password = self.ui.lnSifre.text()

        # Kullanıcı adı ve şifre kontrolü
        if self.check_user_login(username, password):
            print(f" {username} başarılı, Giriş Yapıldı")
            self.user_login_record()   # Kullanıcı giriş bilgilerini kaydetme
            self.open_menu_window()  # Menü penceresini açma
            self.close()  # Giriş penceresini kapatma
        else:
            self.show_error_message("Kullanıcı adı veya şifre yanlış")

    def check_user_login(self, username, password):   # Kullanıcı adı ve şifre kontrolü
        if self.connection is not None:
            try:
                cursor = self.connection.cursor()
                query = "SELECT * FROM personeller WHERE ad = %s AND sifre = %s"
                cursor.execute(query, (username, password))
                user = cursor.fetchone()
                cursor.close()
                if user:
                    return True

            except mysql.connector.Eror as err:
                print("hata check_user_login:", err)
        else:
            print("Veritabanı baglantısı baslatılamadi")
            return False
        
    def user_login_record(self):  # Kullanıcı giriş bilgilerini kaydetme
        if self.connection is not None:
            try:
                cursor = self.connection.cursor()
                login_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                selected_user = self.ui.cbKullanici.text()

                query = "INSERT INTO personelhareketleri (personelAd, durum, tarih) VALUES (%s, %s, %s)"
                cursor.execute(query, (selected_user, "Giriş Yapıldı", login_time))
                self.connection.commit()
                cursor.close()

            except mysql.connector.Eror as err:
                print(f"Hata user_login_record:", err)
        else:
            print("Veritabanı baglantısı baslatılamadi")

    def open_menu_window(self): # Menü penceresini açma
        self.frmMenu = frmMenu()
        self.frmMenu.show()

    def show_error_message(self, message):  # Hata mesajı gösterme
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Kullanıcı Girişi Hatası")
        msg.exec_()

    def exit_application(self):  # Uygulamayı kapatma
        QtWidgets.QApplication.quit()