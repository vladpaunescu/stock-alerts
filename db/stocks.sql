-- phpMyAdmin SQL Dump
-- version 3.5.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Nov 17, 2012 at 06:21 PM
-- Server version: 5.5.24-log
-- PHP Version: 5.4.3

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `bursa`
--

--
-- Dumping data for table `stocks`
--

INSERT INTO `stocks` (`stock_id`, `name`, `symbol`) VALUES
(6, 'Banca Romana de Dezvoltare', 'BRD'),
(8, 'Biofarm', 'BIO'),
(7, 'Brokerul Cluj', 'BRK'),
(5, 'Bursa de valori Bucuresti', 'BVB'),
(10, 'Electromagnetica', 'ELMA'),
(1, 'Fondul Proprietatea', 'FP'),
(3, 'Petrom', 'SNP'),
(4, 'Transelectrica', 'TEL'),
(9, 'Transgaz', 'TGN'),
(2, 'Transilvania', 'TLV');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
