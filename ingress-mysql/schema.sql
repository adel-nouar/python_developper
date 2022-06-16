DROP DATABASE IF EXISTS `DB`;
CREATE DATABASE `DB`;
USE `DB`;

DROP TABLE IF EXISTS `ingress`;
CREATE TABLE `ingress` (
  `ingest_time` datetime,
  `ingest_value` varchar(100) NOT NULL
);