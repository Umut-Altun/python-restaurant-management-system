-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: restorant
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `adisyonlar`
--

DROP TABLE IF EXISTS `adisyonlar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `adisyonlar` (
  `id` int NOT NULL AUTO_INCREMENT,
  `masaİd` int NOT NULL,
  `tarih` datetime NOT NULL,
  `durum` varchar(15) NOT NULL,
  `servisTuru` varchar(15) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adisyonlar`
--

LOCK TABLES `adisyonlar` WRITE;
/*!40000 ALTER TABLE `adisyonlar` DISABLE KEYS */;
INSERT INTO `adisyonlar` VALUES (1,1,'2024-07-26 22:58:43','kapalı','normal'),(2,10,'2024-07-26 22:58:57','kapalı','normal'),(3,2,'2024-07-26 23:00:10','kapalı','normal'),(4,5,'2024-07-26 23:00:17','kapalı','normal'),(5,16,'2024-07-26 23:00:58','kapalı','normal'),(6,12,'2024-07-26 23:01:13','kapalı','normal'),(7,5,'2025-02-19 22:31:01','kapalı','normal'),(8,3,'2025-02-19 22:36:07','kapalı','normal');
/*!40000 ALTER TABLE `adisyonlar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hesapodemeleri`
--

DROP TABLE IF EXISTS `hesapodemeleri`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hesapodemeleri` (
  `id` int NOT NULL AUTO_INCREMENT,
  `adisyonİd` int NOT NULL,
  `odemeTuru` varchar(15) NOT NULL,
  `toplamTutar` decimal(10,2) NOT NULL,
  `tarih` datetime NOT NULL,
  `servisTuru` varchar(15) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hesapodemeleri`
--

LOCK TABLES `hesapodemeleri` WRITE;
/*!40000 ALTER TABLE `hesapodemeleri` DISABLE KEYS */;
INSERT INTO `hesapodemeleri` VALUES (1,1,'KART',589.00,'2025-02-19 22:29:35','normal'),(2,3,'KART',57.00,'2025-02-19 22:29:39','normal'),(3,6,'KART',146.00,'2025-02-19 22:29:45','normal'),(4,4,'KART',5.00,'2025-02-19 22:29:50','normal'),(5,2,'KART',412.00,'2025-02-19 22:29:56','normal'),(6,5,'KART',5.00,'2025-02-19 22:30:09','normal'),(7,7,'KART',500.00,'2025-02-19 22:31:07','normal'),(8,8,'KART',1694.00,'2025-02-19 22:36:12','normal');
/*!40000 ALTER TABLE `hesapodemeleri` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kategoriler`
--

DROP TABLE IF EXISTS `kategoriler`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `kategoriler` (
  `id` int NOT NULL AUTO_INCREMENT,
  `kategoriAdi` varchar(45) NOT NULL,
  `aciklama` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kategoriler`
--

LOCK TABLES `kategoriler` WRITE;
/*!40000 ALTER TABLE `kategoriler` DISABLE KEYS */;
INSERT INTO `kategoriler` VALUES (1,'Ana Yemek','-'),(2,'Makarna','-'),(3,'Salata','-'),(4,'Çorba','-'),(5,'FastFood','-'),(6,'İçecek','-'),(7,'AraSıcak','-'),(8,'Tatlı','-'),(9,'Dürüm','-');
/*!40000 ALTER TABLE `kategoriler` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `masalar`
--

DROP TABLE IF EXISTS `masalar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `masalar` (
  `id` int NOT NULL AUTO_INCREMENT,
  `durum` varchar(15) NOT NULL,
  `masaDurum` varchar(15) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `masalar`
--

LOCK TABLES `masalar` WRITE;
/*!40000 ALTER TABLE `masalar` DISABLE KEYS */;
INSERT INTO `masalar` VALUES (1,'1','kapalı'),(2,'1','kapalı'),(3,'1','kapalı'),(4,'1','kapalı'),(5,'1','kapalı'),(6,'1','kapalı'),(7,'1','kapalı'),(8,'1','kapalı'),(9,'1','kapali'),(10,'1','kapalı'),(11,'1','kapalı'),(12,'1','kapalı'),(13,'1','kapalı'),(14,'1','kapali'),(15,'1','kapalı'),(16,'1','kapalı'),(17,'1','kapali'),(18,'1','kapali'),(19,'1','kapalı'),(20,'1','kapali'),(21,'1','kapali'),(22,'1','kapalı'),(23,'1','kapali'),(24,'1','kapali'),(25,'1','kapali'),(26,'1','kapalı'),(27,'1','kapalı'),(28,'1','kapalı');
/*!40000 ALTER TABLE `masalar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personelhareketleri`
--

DROP TABLE IF EXISTS `personelhareketleri`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `personelhareketleri` (
  `id` int NOT NULL AUTO_INCREMENT,
  `personelAd` varchar(45) NOT NULL,
  `durum` varchar(15) NOT NULL,
  `tarih` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personelhareketleri`
--

LOCK TABLES `personelhareketleri` WRITE;
/*!40000 ALTER TABLE `personelhareketleri` DISABLE KEYS */;
INSERT INTO `personelhareketleri` VALUES (1,'admin','Başarılı','2024-06-13 00:47:58'),(2,'admin','Başarılı','2024-06-14 21:41:58'),(3,'admin','Başarılı','2024-06-16 20:52:33'),(4,'admin','Başarılı','2024-06-16 20:55:27'),(5,'admin','Başarılı','2024-06-26 17:57:45'),(6,'admin','Başarılı','2024-06-26 18:09:17'),(7,'admin','Başarılı','2024-07-26 22:58:31'),(8,'admin','Başarılı','2024-07-26 23:00:51'),(9,'admin','Başarılı','2024-07-26 23:05:56'),(10,'admin','Başarılı','2025-02-19 22:28:40'),(11,'admin','Başarılı','2025-02-19 22:30:30'),(12,'admin','Başarılı','2025-02-19 22:34:58'),(13,'admin','Başarılı','2025-02-19 22:36:00');
/*!40000 ALTER TABLE `personelhareketleri` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personeller`
--

DROP TABLE IF EXISTS `personeller`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `personeller` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ad` varchar(20) NOT NULL,
  `soyad` varchar(20) NOT NULL,
  `sifre` varchar(15) NOT NULL,
  `gorev` varchar(15) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personeller`
--

LOCK TABLES `personeller` WRITE;
/*!40000 ALTER TABLE `personeller` DISABLE KEYS */;
INSERT INTO `personeller` VALUES (1,'Admin','Admin','123','Yetkili Giriş'),(4,'umut','altun','123','Garson');
/*!40000 ALTER TABLE `personeller` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `satislar`
--

DROP TABLE IF EXISTS `satislar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `satislar` (
  `id` int NOT NULL AUTO_INCREMENT,
  `adisyonİd` int NOT NULL,
  `urunİd` int NOT NULL,
  `masaİd` int NOT NULL,
  `adet` int NOT NULL,
  `servisTuru` varchar(15) NOT NULL,
  `durum` varchar(15) NOT NULL,
  `satisZamani` datetime NOT NULL,
  `urunNot` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `satislar`
--

LOCK TABLES `satislar` WRITE;
/*!40000 ALTER TABLE `satislar` DISABLE KEYS */;
INSERT INTO `satislar` VALUES (1,1,1,1,1,'normal','kapalı','2024-07-26 22:58:43',''),(2,1,14,1,1,'normal','kapalı','2024-07-26 22:58:43',''),(3,1,16,1,1,'normal','kapalı','2024-07-26 22:58:43',''),(4,1,38,1,1,'normal','kapalı','2024-07-26 22:58:43',''),(5,1,37,1,1,'normal','kapalı','2024-07-26 22:58:43',''),(6,1,29,1,2,'normal','kapalı','2024-07-26 22:58:43',''),(7,1,30,1,1,'normal','kapalı','2024-07-26 22:58:43',''),(8,1,21,1,1,'normal','kapalı','2024-07-26 22:58:43',''),(9,1,22,1,1,'normal','kapalı','2024-07-26 22:58:43',''),(10,2,38,10,1,'normal','kapalı','2024-07-26 22:58:57',''),(11,2,37,10,1,'normal','kapalı','2024-07-26 22:58:57',''),(12,2,22,10,2,'normal','kapalı','2024-07-26 22:58:57',''),(13,2,23,10,3,'normal','kapalı','2024-07-26 22:58:57',''),(14,2,24,10,2,'normal','kapalı','2024-07-26 22:58:57',''),(15,3,29,2,1,'normal','kapalı','2024-07-26 23:00:10',''),(16,3,30,2,1,'normal','kapalı','2024-07-26 23:00:10',''),(17,4,34,5,1,'normal','kapalı','2024-07-26 23:00:17',''),(18,5,34,16,1,'normal','kapalı','2024-07-26 23:00:58',''),(19,6,30,12,1,'normal','kapalı','2024-07-26 23:01:13',''),(20,6,29,12,1,'normal','kapalı','2024-07-26 23:01:13',''),(21,6,34,12,1,'normal','kapalı','2024-07-26 23:01:13',''),(22,6,33,12,1,'normal','kapalı','2024-07-26 23:01:13',''),(23,6,32,12,1,'normal','kapalı','2024-07-26 23:01:13',''),(24,6,31,12,1,'normal','kapalı','2024-07-26 23:01:13',''),(25,7,1,5,2,'normal','kapalı','2025-02-19 22:31:01',''),(26,7,8,5,2,'normal','kapalı','2025-02-19 22:31:01',''),(27,8,1,3,7,'normal','kapalı','2025-02-19 22:36:07','');
/*!40000 ALTER TABLE `satislar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `urunler`
--

DROP TABLE IF EXISTS `urunler`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `urunler` (
  `id` int NOT NULL AUTO_INCREMENT,
  `kategoriİd` int NOT NULL,
  `urunAd` varchar(45) NOT NULL,
  `aciklama` varchar(45) NOT NULL,
  `fiyat` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `urunler`
--

LOCK TABLES `urunler` WRITE;
/*!40000 ALTER TABLE `urunler` DISABLE KEYS */;
INSERT INTO `urunler` VALUES (1,1,'Soya Tavuk','-',242),(8,1,'Barbekü Tavuk','-',8),(13,3,'Mevsim Salata','-',54),(14,1,'Izgara Tavuk','-',56),(16,1,'Tavuk Sote','-',12),(17,1,'Meksika Tavuk','-',23),(18,3,'Tavuklu Salata','-',54),(19,3,'Ton Balık Salata','-',56),(20,3,'Çoban Salata','-',55),(21,2,'Alfredo Penne','-',56),(22,2,'Kori Penne','-',66),(23,2,'Soya Penne','-',56),(24,2,'Arabiata Penne','-',23),(25,4,'Mercimek','-',67),(26,4,'Yayla','-',32),(27,4,'Ezogelin','-',76),(28,4,'Tavuk','-',97),(29,5,'Patates Kızartma','-',34),(30,5,'Elma Patates','-',23),(31,6,'Su','-',5),(32,6,'Şişe Kola','-',34),(33,6,'Kutu Kola','-',45),(34,7,'Soğan Halkası','-',5),(35,8,'Sütlaç','-',55),(36,8,'Tulumba','-',33),(37,9,'Tavuk Dürüm','-',34),(38,9,'Tantuni Dürüm','-',32);
/*!40000 ALTER TABLE `urunler` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-02-21 16:57:55
