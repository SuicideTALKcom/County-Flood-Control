CREATE DATABASE homes_db;
USE homes_db;
CREATE TABLE details(
	name VARCHAR(30)NOT NULL,
    address VARCHAR (250) NOT NULL,
    price INT,
    days_on_market INT,
    agent VARCHAR (40),
    office VARCHAR(50),
    neighborhood VARCHAR(60),
    id INT AUTO_INCREMENT,
    PRIMARY KEY(id)
);

SELECT * FROM home;

DROP TABLE home;

