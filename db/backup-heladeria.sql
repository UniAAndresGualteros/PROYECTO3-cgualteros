CREATE DATABASE  IF NOT EXISTS `heladeria` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `heladeria`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: heladeria
-- ------------------------------------------------------
-- Server version	8.0.37

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
-- Table structure for table `ingredientes`
--

DROP TABLE IF EXISTS `ingredientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ingredientes` (
  `idIngrediente` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(80) NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `calorias` decimal(10,2) NOT NULL,
  `inventario` decimal(10,2) NOT NULL,
  `es_vegetariano` tinyint(1) NOT NULL,
  `tipo_ingrediente` varchar(15) NOT NULL,
  `sabor_base` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`idIngrediente`),
  KEY `ingredientes_ibfk_2` (`sabor_base`),
  KEY `tipoingrediente` (`tipo_ingrediente`),
  CONSTRAINT `ingredientes_ibfk_2` FOREIGN KEY (`sabor_base`) REFERENCES `sabores` (`idSabor`)
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingredientes`
--

LOCK TABLES `ingredientes` WRITE;
/*!40000 ALTER TABLE `ingredientes` DISABLE KEYS */;
INSERT INTO `ingredientes` VALUES (1,'Helado',4500.00,57.50,5.00,0,'Base',1),(2,'Helado',4500.00,57.50,4.00,1,'Base',2),(3,'Helado',4500.00,57.50,3.00,0,'Base',3),(4,'Helado',4500.00,57.50,4.00,0,'Base',4),(5,'Helado',4500.00,57.50,5.00,0,'Base',5),(6,'Helado',4500.00,57.50,5.00,0,'Base',6),(7,'Helado',4500.00,57.50,5.00,1,'Base',7),(8,'Gomitas',2300.00,59.40,4.60,0,'Complemento',0),(9,'Barquillos',2800.00,47.00,5.00,0,'Complemento',0),(10,'Galletas Oreo',4000.00,170.00,4.60,0,'Complemento',0),(11,'Fresas',2000.00,33.00,4.80,1,'Complemento',0),(12,'Mango',2000.00,60.00,5.00,1,'Complemento',0),(13,'Durazno',300.00,72.90,5.00,1,'Complemento',0);
/*!40000 ALTER TABLE `ingredientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos`
--

DROP TABLE IF EXISTS `productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productos` (
  `idProducto` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(80) NOT NULL,
  `tipo_producto` varchar(30) NOT NULL,
  `presentacion` varchar(30) NOT NULL,
  PRIMARY KEY (`idProducto`),
  KEY `presentacion` (`presentacion`),
  KEY `tipo_producto` (`tipo_producto`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` VALUES (1,'Malteada Explosion','Malteada','12 oz'),(2,'Dalmata','Malteada','14 oz'),(3,'Sensacion','Copa','Copa Mediana'),(4,'Serafin','Copa','Copa Grande');
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sabores`
--

DROP TABLE IF EXISTS `sabores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sabores` (
  `idSabor` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  PRIMARY KEY (`idSabor`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sabores`
--

LOCK TABLES `sabores` WRITE;
/*!40000 ALTER TABLE `sabores` DISABLE KEYS */;
INSERT INTO `sabores` VALUES (0,'Sin Sabor'),(1,'Chocolate'),(2,'Fresa'),(3,'Vainilla'),(4,'Macadamia'),(5,'Ron con Pasas'),(6,'Chicle'),(7,'Caramelo');
/*!40000 ALTER TABLE `sabores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ventas`
--

DROP TABLE IF EXISTS `ventas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ventas` (
  `idVenta` int NOT NULL AUTO_INCREMENT,
  `fecha_venta` datetime NOT NULL,
  `producto` int NOT NULL,
  `ingrediente_1` int NOT NULL,
  `ingrediente_2` int NOT NULL,
  `ingrediente_3` int NOT NULL,
  `precio_base` decimal(10,0) NOT NULL,
  `precio_plastico` decimal(10,0) NOT NULL DEFAULT '0',
  `precio_total` decimal(10,0) NOT NULL,
  PRIMARY KEY (`idVenta`),
  KEY `producto` (`producto`),
  KEY `ingrediente_1` (`ingrediente_1`),
  KEY `ingrediente_2` (`ingrediente_2`),
  KEY `ingrediente_3` (`ingrediente_3`),
  CONSTRAINT `ventas_ibfk_1` FOREIGN KEY (`producto`) REFERENCES `productos` (`idProducto`),
  CONSTRAINT `ventas_ibfk_2` FOREIGN KEY (`ingrediente_1`) REFERENCES `ingredientes` (`idIngrediente`),
  CONSTRAINT `ventas_ibfk_3` FOREIGN KEY (`ingrediente_2`) REFERENCES `ingredientes` (`idIngrediente`),
  CONSTRAINT `ventas_ibfk_4` FOREIGN KEY (`ingrediente_3`) REFERENCES `ingredientes` (`idIngrediente`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ventas`
--

LOCK TABLES `ventas` WRITE;
/*!40000 ALTER TABLE `ventas` DISABLE KEYS */;
INSERT INTO `ventas` VALUES (1,'2024-07-21 18:47:10',3,4,8,10,10800,0,10800),(2,'2024-07-21 18:47:45',1,3,8,11,8800,500,9300),(3,'2024-07-21 20:17:32',3,2,3,10,13000,0,13000);
/*!40000 ALTER TABLE `ventas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-21 20:25:25
