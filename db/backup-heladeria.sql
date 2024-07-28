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
INSERT INTO `ingredientes` VALUES (1,'Helado',4500.00,57.50,12.00,0,'Base',1),(2,'Helado',4500.00,57.50,17.00,1,'Base',2),(3,'Helado',4500.00,57.50,6.00,0,'Base',3),(4,'Helado',4500.00,57.50,3.00,0,'Base',4),(5,'Helado',4500.00,57.50,3.00,0,'Base',5),(6,'Helado',4500.00,57.50,4.00,0,'Base',6),(7,'Helado',4500.00,57.50,7.00,1,'Base',7),(8,'Gomitas',2300.00,59.40,4.60,0,'Complemento',0),(9,'Barquillos',2800.00,47.00,0.00,0,'Complemento',0),(10,'Galletas Oreo',4000.00,170.00,4.00,0,'Complemento',0),(11,'Fresas',2000.00,33.00,10.00,1,'Complemento',0),(12,'Mango',2000.00,60.00,4.20,1,'Complemento',0),(13,'Durazno',300.00,72.90,4.40,1,'Complemento',0);
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
  `precio_publico` decimal(10,2) NOT NULL,
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
INSERT INTO `productos` VALUES (1,'Malteada Explosion','Malteada','12 oz',16000.00),(2,'Dalmata','Malteada','14 oz',23000.00),(3,'Sensacion','Copa','Copa Mediana',15000.00),(4,'Serafin','Copa','Copa Grande',22000.00);
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `idRol` int NOT NULL AUTO_INCREMENT,
  `nombre_rol` varchar(20) NOT NULL,
  PRIMARY KEY (`idRol`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'es_admin'),(2,'es_empleado'),(3,'es_cliente');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
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
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `rol_usuario` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `rol_usuario` (`rol_usuario`),
  CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`rol_usuario`) REFERENCES `roles` (`idRol`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'HeladosAdmin','C0ntr4s3ñ4*1',1),(2,'RodrigoD','EmpleadoHel1',2),(3,'JacintaP','EmpleadoHel2',2),(4,'VacaInlechera123','ClienteHel1',3),(5,'SamiHeladero','ClienteHel2',3);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
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
  `precio_base` decimal(10,2) NOT NULL,
  `precio_plastico` decimal(10,2) NOT NULL DEFAULT '0.00',
  `precio_total` decimal(10,2) NOT NULL,
  `precio_publico` decimal(10,2) NOT NULL,
  PRIMARY KEY (`idVenta`),
  KEY `producto` (`producto`),
  KEY `ingrediente_1` (`ingrediente_1`),
  KEY `ingrediente_2` (`ingrediente_2`),
  KEY `ingrediente_3` (`ingrediente_3`),
  CONSTRAINT `ventas_ibfk_1` FOREIGN KEY (`producto`) REFERENCES `productos` (`idProducto`),
  CONSTRAINT `ventas_ibfk_2` FOREIGN KEY (`ingrediente_1`) REFERENCES `ingredientes` (`idIngrediente`),
  CONSTRAINT `ventas_ibfk_3` FOREIGN KEY (`ingrediente_2`) REFERENCES `ingredientes` (`idIngrediente`),
  CONSTRAINT `ventas_ibfk_4` FOREIGN KEY (`ingrediente_3`) REFERENCES `ingredientes` (`idIngrediente`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ventas`
--

LOCK TABLES `ventas` WRITE;
/*!40000 ALTER TABLE `ventas` DISABLE KEYS */;
INSERT INTO `ventas` VALUES (1,'2024-07-21 18:47:10',3,4,8,10,10800.00,0.00,10800.00,15000.00),(2,'2024-07-21 18:47:45',1,3,8,11,8800.00,500.00,9300.00,16000.00),(3,'2024-07-21 20:17:32',3,2,3,10,13000.00,0.00,13000.00,15000.00),(10,'2024-07-21 20:41:09',4,2,5,9,11800.00,0.00,11800.00,22000.00),(11,'2024-07-27 15:06:35',1,13,12,7,6800.00,500.00,7300.00,16000.00),(12,'2024-07-27 15:16:42',1,4,3,9,11800.00,500.00,12300.00,16000.00),(13,'2024-07-27 15:17:12',1,1,2,13,9300.00,500.00,9800.00,16000.00),(14,'2024-07-27 22:12:30',2,10,1,3,13000.00,500.00,13500.00,23000.00),(15,'2024-07-28 01:06:54',4,7,10,12,10500.00,0.00,10500.00,22000.00),(16,'2024-07-28 01:07:25',2,10,12,6,10500.00,500.00,11000.00,23000.00),(17,'2024-07-28 01:08:24',2,5,12,13,6800.00,500.00,7300.00,23000.00),(18,'2024-07-28 01:08:51',4,7,9,1,11800.00,0.00,11800.00,22000.00);
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

-- Dump completed on 2024-07-28  1:32:16
