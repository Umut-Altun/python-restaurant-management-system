🍽️ Restaurant Yönetim & Adisyon Sistemi

📌 Proje Hakkında

Bu proje, Python (PyQt5) ve MySQL kullanılarak geliştirilen bir Restaurant Yönetim ve Adisyon Sistemidir. Restoran işletmelerinin masaları yönetmesine, müşteri siparişlerini takip etmesine ve mutfak, raporlama gibi işlemleri kolaylaştırmasına yardımcı olur.

🚀 Özellikler

✅ Masa Yönetimi: Restorandaki masaları görüntüleme ve kontrol etme
✅ Paket Sipariş Yönetimi: Paket servis siparişlerini takip etme
✅ Müşteri Yönetimi: Müşteri bilgilerini kaydetme ve görüntüleme
✅ Ayarlar: Sistem ayarlarını yapılandırma
✅ Mutfak Yönetimi: Mutfaktaki siparişleri takip etme
✅ Raporlama: Günlük satış ve işlem raporları alma
✅ Yetkilendirme Sistemi: Admin ve kullanıcı seviyelerinde erişim kontrolleri
✅ Gerçek Zamanlı Tarih & Saat: Sistem tarih ve saat bilgisini dinamik olarak güncelleme
✅ Wi-Fi Bağlantı Kontrolü: Sistem bağlantı durumunu periyodik olarak kontrol etme

🛠️ Teknolojiler

🔹 Python (PyQt5) - Masaüstü arayüz geliştirme
🔹 MySQL - Veritabanı yönetimi
🔹 QTimer - Gerçek zamanlı işlemler için zamanlayıcı
🔹 Wi-Fi Durum Kontrolü - Ağ bağlantı kontrolü

📦 Kurulum

1️⃣ Gerekli Bağımlılıkları Yükleyin

Aşağıdaki komutları çalıştırarak bağımlılıkları yükleyin:

pip install PyQt5 mysql-connector-python

2️⃣ Veritabanını Ayarlayın

MySQL veritabanınızı oluşturun ve aşağıdaki tabloları ekleyin:

CREATE TABLE personelhareketleri (
    id INT AUTO_INCREMENT PRIMARY KEY,
    personelAd VARCHAR(255),
    tarih TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

3️⃣ Projeyi Çalıştırın

Ana menüyü başlatmak için aşağıdaki komutu çalıştırın:

python main.py

📸 Arayüz Görselleri

📷 [Buraya ekran görüntüleri eklenebilir]

🤝 Katkıda Bulunun

Bu projeye katkıda bulunmak için pull request gönderebilir veya issue açabilirsiniz.

📜 Lisans

Bu proje MIT Lisansı ile lisanslanmıştır.

🎯 Proje Sahibi: [GitHub Kullanıcı Adınız]
