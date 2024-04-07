CREATE DATABASE IF NOT EXISTS library;
USE library;

CREATE USER 'ctf_user'@'%' IDENTIFIED BY 'hHd86KcneHU92HUhd';
GRANT ALL PRIVILEGES ON library.* TO 'ctf_user'@'%';
FLUSH PRIVILEGES;

-- Création de la table pour les livres avec une colonne distincte pour les Authors
CREATE TABLE Books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    Author VARCHAR(255) NOT NULL
);

-- Insertion de quelques Titles de livres avec Authors séparés
INSERT INTO Books (Title, Author) VALUES ('Papillon', 'Henri Charriere');
INSERT INTO Books (Title, Author) VALUES ('The Shawshank Redemption', 'Stephen King');
INSERT INTO Books (Title, Author) VALUES ('The Count of Monte Cristo', 'Alexandre Dumas');
INSERT INTO Books (Title, Author) VALUES ('Escape from Alcatraz', 'J. Campbell Bruce');
INSERT INTO Books (Title, Author) VALUES ('The Great Escape', 'Paul Brickhill');
INSERT INTO Books (Title, Author) VALUES ('Escape', 'Carolyn Jessop');
INSERT INTO Books (Title, Author) VALUES ('Shantaram', 'Gregory David Roberts');
INSERT INTO Books (Title, Author) VALUES ('Life and Death in Shanghai', 'Nien Cheng');
INSERT INTO Books (Title, Author) VALUES ('The Long Walk', 'Slavomir Rawicz');
INSERT INTO Books (Title, Author) VALUES ('Escape from Sobibor', 'Richard Rashke');

-- Création de la table admin
CREATE TABLE Admin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(50)
);

-- Insertion du flag et des identifiants administrateur
INSERT INTO Admin (username, password) VALUES ('Flag', 'polycyber{SQL_Br3ak0ut}');
INSERT INTO Admin (username, password) VALUES ('Librarian', 'R3ad-2-3scap3!');
