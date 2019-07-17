-- script creates the database hbtn_0d_usa and the table states
-- id INT unique, auto generated, can’t be null and is a primary key
-- name VARCHAR(256) can’t be null; if the database hbtn_0d_usa already
-- exists, your script should not fail. Script does not fail if table exists.
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
USE `hbtn_0d_usa`
CREATE TABLE IF NOT EXISTS `states`
(
	id INT PRIMARY KEY UNIQUE AUTO_INCREMENT NOT NULL,
	name VARCHAR(256) NOT NULL
)
ENGINE=InnoDB;
