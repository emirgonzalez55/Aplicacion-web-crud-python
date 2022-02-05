-- MySQL dump 10.13  Distrib 8.0.27, for Linux (x86_64)
--
-- Host: localhost    Database: bd
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `chipsets`
--

DROP TABLE IF EXISTS `chipsets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chipsets` (
  `id` int NOT NULL AUTO_INCREMENT,
  `marca` varchar(45) DEFAULT NULL,
  `modelo` varchar(45) DEFAULT NULL,
  `rendimiento` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=159 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chipsets`
--

LOCK TABLES `chipsets` WRITE;
/*!40000 ALTER TABLE `chipsets` DISABLE KEYS */;
INSERT INTO `chipsets` VALUES (1,'Qualcomm','snapdragon 450','90'),(2,'Qualcomm','snapdragon 650','90'),(3,'Qualcomm','snapdragon 636','90'),(4,'Qualcomm','snapdragon 888','90'),(5,'Qualcomm','snapdragon 650','90'),(6,'Qualcomm','snapdragon 425','90'),(8,'MediaTek','MediaTek','90'),(9,'MediaTek','MediaTek','90'),(10,'MediaTek','MediaTek','90'),(11,'MediaTek','MediaTek','90'),(12,'Exynos','Exynos','90'),(13,'Exynos','Exynos','90'),(14,'Exynos','Exynos','90'),(15,'Exynos','Exynos','90'),(16,'Exynos','Exynos','90');
/*!40000 ALTER TABLE `chipsets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `graficas`
--

DROP TABLE IF EXISTS `graficas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `graficas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `marca` varchar(45) DEFAULT NULL,
  `modelo` varchar(45) DEFAULT NULL,
  `rendimiento` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=90 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `graficas`
--

LOCK TABLES `graficas` WRITE;
/*!40000 ALTER TABLE `graficas` DISABLE KEYS */;
INSERT INTO `graficas` VALUES (1,'AMD','Radeon RX 6900 XT','90'),(2,'AMD','Radeon RX 6800 XT','90'),(3,'AMD','Radeon RX 6800','90'),(4,'AMD','Radeon RX 6700 XT','90'),(5,'AMD','Radeon RX 6600 XT','90'),(6,'NVIDIA','RTX 3050','90'),(7,'NVIDIA','RTX 3060','90'),(8,'NVIDIA','RTX 3070','90'),(9,'NVIDIA','RTX 3080','90'),(10,'NVIDIA','RTX 3090','90');
/*!40000 ALTER TABLE `graficas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `procesadores`
--

DROP TABLE IF EXISTS `procesadores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `procesadores` (
  `id` int NOT NULL AUTO_INCREMENT,
  `marca` varchar(45) DEFAULT NULL,
  `modelo` varchar(45) DEFAULT NULL,
  `rendimiento` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=827 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `procesadores`
--

LOCK TABLES `procesadores` WRITE;
/*!40000 ALTER TABLE `procesadores` DISABLE KEYS */;
INSERT INTO `procesadores` VALUES (2,'AMD','Ryzen 5 3600','90'),(3,'AMD','Ryzen 5 3600X','90'),(4,'AMD','Ryzen 7 3700','90'),(5,'AMD','Ryzen 5 1600','70'),(6,'AMD','Ryzen 5 3900x','90'),(7,'AMD','Ryzen 5 3950x','90'),(14,'INTEL','i5 7400','60'),(15,'INTEL','I7 7700K','80'),(119,'INTEL','I7 8700K','80'),(120,'INTEL','I5 6600','80');
/*!40000 ALTER TABLE `procesadores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `password` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=141 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'emir','81dc9bdb52d04dc20036dbd8313ed055'),(2,'admin','81dc9bdb52d04dc20036dbd8313ed055'),(3,'root','$2b$12$8GgLTW5BgfCvOI./oJlqzOo/cwxNrnev6Btl1RCsDQ6TUMtYgcEyy');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-05 18:18:14
