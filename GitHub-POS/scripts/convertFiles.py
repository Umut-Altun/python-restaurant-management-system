import subprocess

# Dönüştürülecek UI dosyalarını listeye ekleyin
ui_files = [
    "ui/frmGiris.ui",
    "ui/frmArkaPlan.ui",
    "ui/frmMenu.ui",
    "ui/frmMasalar.ui",
    "ui/frmSiparis.ui",
    "ui/frmOdeme.ui",
]

# Her UI dosyasını py dosyasına dönüştürün
for ui_file in ui_files:
    py_file = "forms/{}.py".format(ui_file.split("/")[-1].replace(".ui", "Ui"))
    command = ["pyuic5", ui_file, "-o", py_file]
    
    try:
        subprocess.run(command, check=True)
        print("{} başarıyla dönüştürüldü.".format(ui_file))
    except subprocess.CalledProcessError:
        print("{} dönüştürülürken bir hata oluştu.".format(ui_file))






# resim dönüştürme  = pyrcc5 -o ImageRestorant_rc.py ImageRestorant.qrc
# demoya donuştürme = pyinstaller --onefile --icon=restorant.ico frmGiris.py
# demoya donuştürme = pyinstaller --onefile --icon=restorant.ico --noconsole frmGiris.py