import mysql.connector

DB_CONFIG = {
    "host": "localhost", 
    "user": "root",           
    "password": "mysql12",  #burdakı sifreyi degistirin
    "auth_plugin": "mysql_native_password",
    "database": "restorant"
}


def connect_to_database():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            return connection
    except mysql.connector.Error as err:
        print("Bağlantı Hatası connect_to_database:", err)
    except Exception as e:
        print("Bilinmeyen bir hata oluştu connect_to_database:", e)  
    return None
