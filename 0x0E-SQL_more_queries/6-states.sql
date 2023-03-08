--craete database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
--create table
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
       id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
       name VARCHAR() NOT NULL
)ENGINE=INNODB;
