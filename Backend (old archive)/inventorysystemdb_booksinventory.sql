-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: inventorysystemdb
-- ------------------------------------------------------
-- Server version	8.0.26

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
-- Table structure for table `booksinventory`
--

DROP TABLE IF EXISTS `booksinventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `booksinventory` (
  `title` varchar(255) NOT NULL,
  `author` varchar(255) DEFAULT NULL,
  `date_of_publication` varchar(255) DEFAULT NULL,
  `isbn` varchar(255) DEFAULT NULL,
  `nr_of_pages` varchar(255) DEFAULT NULL,
  `link_cover` varchar(255) DEFAULT NULL,
  `language` varchar(255) DEFAULT NULL,
  `google_selflink` varchar(255) DEFAULT NULL,
  `google_id` varchar(255) DEFAULT NULL,
  `product_id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`product_id`,`title`)
) ENGINE=InnoDB AUTO_INCREMENT=4154 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booksinventory`
--

LOCK TABLES `booksinventory` WRITE;
/*!40000 ALTER TABLE `booksinventory` DISABLE KEYS */;
INSERT INTO `booksinventory` VALUES ('Hobbit czyli tam i z powrotem','J. R. R. Tolkien','2014','9788324403875','320','https://bigimg.taniaksiazka.pl/images/popups/CF6/9788324403875.jpg','en',NULL,NULL,4128),('J. R. R. Tolkien - pisarz stulecia','T. A. Shippey','2019','9788381166485','428','https://histmag.org/grafika/2019_recenzje/tolkien.jpg','pl',NULL,NULL,4136),('Tolkien i C. S. Lewis - historia niezwykłej przyjaźni','Colin Duriez','2011','9788375950373','283','http://books.google.com/books/content?id=kNEA-jgNI7wC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api','pl',NULL,NULL,4137),('Sezon burz. Wiedzmin','Andrzej Sapkowski','2013','9788375780598','404','https://ecsmedia.pl/c/sezon-burz-wiedzmin-tom-8-b-iext81246019.jpg','pl',NULL,NULL,4139),('Inferno - (Robert Langdon Book 4)','Dan Brown','2013','9781448169795','624','http://books.google.com/books/content?id=yrRdbryIcvcC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api','en',NULL,NULL,4141),('The J.R.R. Tolkien Companion & Guide','[\'Christina Scull\', \'Wayne G. Hammond\']','2006','9780618391028','996','http://books.google.com/books/content?id=wohlAAAAMAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api','en',NULL,NULL,4142),('Tolkien Biografia','Humphrey Carpenter','2016','9788328027633','416','https://ecsmedia.pl/c/tolkien-biografia-w-iext83636020.jpg','pl',NULL,NULL,4144),('Wieża jaskółki','Andrzej Sapkowski','1997','9788370541248','428','http://books.google.com/books/content?id=YFhhAAAAMAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api','pl',NULL,NULL,4146),('The Da Vinci Code - A Novel','Dan Brown','2003','9780375432309','739','http://books.google.com/books/content?id=F8CXH1J8bggC&printsec=frontcover&img=1&zoom=1&source=gbs_api','en',NULL,NULL,4148),('Inferno - ','Dan Brown','2016','9788379999781','688','http://books.google.com/books/content?id=Qq0kDQAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api','pl',NULL,NULL,4149),('Zaginiony symbol','Dan Brown','2010','9788379992263','624','http://books.google.com/books/content?id=OdooCQAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api','pl',NULL,NULL,4150),('Zwodniczy punkt - ','Dan Brown','none date','9788379992584','528','http://books.google.com/books/content?id=cJ6mCQAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api','pl',NULL,NULL,4151),('Anioły i demony - ','Dan Brown','none date','9788375088045','560','http://books.google.com/books/content?id=zlrTCQAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api','pl',NULL,NULL,4152),('Początek','Dan Brown','2017','9788381101462','576','http://books.google.com/books/content?id=TrM9DwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api','pl',NULL,NULL,4153);
/*!40000 ALTER TABLE `booksinventory` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-14  1:54:01
