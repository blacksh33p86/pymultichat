-- phpMyAdmin SQL Dump
-- version 4.0.6deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Erstellungszeit: 23. Okt 2013 um 14:25
-- Server Version: 5.5.32-0ubuntu7
-- PHP-Version: 5.5.3-1ubuntu2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Datenbank: `chatsrv`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `cs_activities`
--

CREATE TABLE IF NOT EXISTS `cs_activities` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `action` varchar(25) COLLATE utf8_bin NOT NULL,
  `connection` varchar(21) COLLATE utf8_bin NOT NULL,
  `stamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `userid` bigint(20) NOT NULL,
  `value` varchar(200) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `cs_dynamicchannels`
--

CREATE TABLE IF NOT EXISTS `cs_dynamicchannels` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `orderid` int(11) NOT NULL,
  `creatorid` bigint(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `cs_fixedchannels`
--

CREATE TABLE IF NOT EXISTS `cs_fixedchannels` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `orderid` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `cs_guests`
--

CREATE TABLE IF NOT EXISTS `cs_guests` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `stamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `nickname` varchar(50) COLLATE utf8_bin NOT NULL,
  `connection` varchar(21) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `cs_users`
--

CREATE TABLE IF NOT EXISTS `cs_users` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nickname` varchar(50) NOT NULL,
  `password` varchar(32) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `privilege` tinyint(4) NOT NULL,
  `onlinestatus` tinyint(1) NOT NULL,
  `email` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `verified` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

