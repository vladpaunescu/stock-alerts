-- phpMyAdmin SQL Dump
-- version 3.5.3
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Nov 13, 2012 at 11:06 PM
-- Server version: 5.5.28-0ubuntu0.12.10.1
-- PHP Version: 5.4.6-1ubuntu1

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `bursa`
--
DROP DATABASE `bursa`;
CREATE DATABASE `bursa` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `bursa`;

-- --------------------------------------------------------

--
-- Table structure for table `alerts`
--

DROP TABLE IF EXISTS `alerts`;
CREATE TABLE IF NOT EXISTS `alerts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `stock_id` int(11) NOT NULL,
  `date_added` datetime NOT NULL,
  `value` decimal(10,4) NOT NULL COMMENT 'stock value when added',
  `type` enum('value','percent') NOT NULL COMMENT 'type may be percent variation or value variation',
  `target_value` decimal(10,4) NOT NULL,
  `date_completed` datetime DEFAULT NULL COMMENT 'the moment when the alert is completed',
  `viewed` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `stock_id` (`stock_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `daily_quotes`
--

DROP TABLE IF EXISTS `daily_quotes`;
CREATE TABLE IF NOT EXISTS `daily_quotes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `stock_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `value` decimal(10,4) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `stock_id` (`stock_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `realtime_quotes`
--

DROP TABLE IF EXISTS `realtime_quotes`;
CREATE TABLE IF NOT EXISTS `realtime_quotes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `stock_id` int(11) NOT NULL,
  `date_added` datetime NOT NULL,
  `value` decimal(10,4) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `stock_id` (`stock_id`),
  KEY `stock_id_2` (`stock_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `stocks`
--

DROP TABLE IF EXISTS `stocks`;
CREATE TABLE IF NOT EXISTS `stocks` (
  `stock_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `symbol` varchar(20) NOT NULL,
  PRIMARY KEY (`stock_id`),
  UNIQUE KEY `name` (`name`,`symbol`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` varchar(64) NOT NULL,
  `email` varchar(20) DEFAULT NULL,
  `first_name` varchar(20) DEFAULT NULL,
  `last_name` varchar(20) DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `sex` varchar(1) DEFAULT NULL,
  `job` varchar(20) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `watchlist`
--

DROP TABLE IF EXISTS `watchlist`;
CREATE TABLE IF NOT EXISTS `watchlist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `stock_id` int(11) NOT NULL,
  `date_added` datetime NOT NULL,
  `value` decimal(10,4) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `stock_id` (`stock_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `alerts`
--
ALTER TABLE `alerts`
  ADD CONSTRAINT `FK_alerts_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_alerts_1` FOREIGN KEY (`stock_id`) REFERENCES `stocks` (`stock_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `daily_quotes`
--
ALTER TABLE `daily_quotes`
  ADD CONSTRAINT `FK_daily_quotes` FOREIGN KEY (`stock_id`) REFERENCES `stocks` (`stock_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `realtime_quotes`
--
ALTER TABLE `realtime_quotes`
  ADD CONSTRAINT `FK_realtime_quotes` FOREIGN KEY (`stock_id`) REFERENCES `stocks` (`stock_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `watchlist`
--
ALTER TABLE `watchlist`
  ADD CONSTRAINT `FK_watchlist_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_watchlist_1` FOREIGN KEY (`stock_id`) REFERENCES `stocks` (`stock_id`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
