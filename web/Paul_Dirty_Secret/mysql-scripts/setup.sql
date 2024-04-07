CREATE DATABASE IF NOT EXISTS barbadb;

CREATE USER IF NOT EXISTS 'challuser' IDENTIFIED BY 'ThisIsADumbPassword';
CREATE USER IF NOT EXISTS 'flaguser' IDENTIFIED BY 'ThisIsADumbPasswordAGAIN';

FLUSH PRIVILEGES;

DROP TABLE IF EXISTS barbadb.Users;
DROP TABLE IF EXISTS barbadb.Secret;

CREATE TABLE barbadb.Users (
    id          INTEGER PRIMARY KEY AUTO_INCREMENT,
    username    VARCHAR(255),
    passwd      VARCHAR(255)
);

CREATE TABLE barbadb.Secret(
    secret      VARCHAR(255)
);

INSERT INTO barbadb.Users(username,passwd) VALUES ("ppierre", "123456789123456789123456789");
INSERT INTO barbadb.Users(username,passwd) VALUES ("ppaul", "123456789123456789123456789");
INSERT INTO barbadb.Users(username,passwd) VALUES ("lfer", "123456789123456789123456789");

INSERT INTO barbadb.Secret(secret) VALUES ("0e39467675362791795113850062806237025205");

DROP TABLE IF EXISTS barbadb.Flag;

CREATE TABLE barbadb.Flag(
    secret_flag VARCHAR(255)
);

INSERT INTO barbadb.Flag(secret_flag) VALUES("polycyber{One_server_multiple_vhosts...And_use_===_please!}");

GRANT SELECT ON barbadb.Flag TO 'flaguser'@'%';
GRANT SELECT ON barbadb.Users TO 'challuser'@'%';
GRANT SELECT ON barbadb.Secret TO 'challuser'@'%';

FLUSH PRIVILEGES;


