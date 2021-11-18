DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Bookmarks;
DROP TABLE IF EXISTS Search;
DROP TABLE IF EXISTS Publisher;
DROP TABLE IF EXISTS PublisherAuthors;
DROP TABLE IF EXISTS Authors;
DROP TABLE IF EXISTS BookAuthor;
DROP TABLE IF EXISTS Book;
DROP TABLE IF EXISTS Category;
DROP TABLE IF EXISTS Ratings;


CREATE TABLE User (
    u_userkey INT PRIMARY KEY,
    u_name VARCHAR(100) NOT NULL,
    u_email VARCHAR(100) NOT NULL,
    u_password VARCHAR(100) NOT NULL
);

INSERT INTO User(u_userkey, u_name, u_email, u_password) VALUES
('1', 'John Doe', 'JD@fakeemail.com', '1234'),
('2', 'Jane Amelia ', 'JA@fakeemail.com', '1256');



CREATE TABLE Bookmarks (
    bm_id INT PRIMARY KEY,
    bm_userkey INT NOT NULL,
    bm_title VARCHAR(100) NOT NULL,
    bm_author TEXT(100) NOT NULL, 
    bm_publisher TEXT(100) NOT NULL,
    bm_numPages INT NOT NULL,
    bm_addYear DATETIME NOT NULL
);

--INSERT INTO Bookmarks(bm_userkey, bm_title, bm_author, bm_publisher, bm_numPages, bm_addYear) VALUES
INSERT INTO Bookmarks(bm_id, bm_userkey, bm_title, bm_author, bm_publisher, bm_numPages, bm_addYear) VALUES
('1', '1', 'Halo: Ghosts of Onyx', 'Eric Nylund','Tor Books', '356', '2007'),
('2', '1', 'Halo: The Fall of Reach', 'Eric Nylund','Tor Books', '352', '2001'),
('3', '1', 'Halo: Contact Harvest', 'Joseph Staten','Tor Books', '353', '2007'),

('4', '2', 'Harry Potter and the Sorcerers Stone (Harry Potter, #1)', 'Eric Nylund','Tor Books', '356', '2007'),
('5', '2', 'Horton Hears a Who!', 'Eric Nylund','Tor Books', '352', '2001'),
('6', '2', 'Harry Potter and the Prisoner of Azkaban (Harry Potter, #3)', 'Joseph Staten','Tor Books', '353', '2007');
CREATE TABLE Search (
    s_id INT PRIMARY KEY,
    s_title VARCHAR(100) NOT NULL,
    s_category TEXT(50) NOT NULL,
    s_publisher TEXT(100) NOT NULL,
    s_isbn INT NOT NULL
);

--INSERT INTO Search(s_id, s_title, s_category, s_publisher, s_isbn) VALUES


CREATE TABLE Publisher (
    p_id INT PRIMARY KEY,
    p_name TEXT(100) NOT NULL
);


INSERT INTO Publisher(p_id, p_name) VALUES
('001', 'HarperCollins'),

('010','Livre de Poche'),
('011','Turtleback Books'),
('012','Tor Books'),
('013','Delta'),
('014','DK Publishing'),
('015','Random House Books for Young Readers'),
('016','Liberty Fund Inc'),
('017','Arthur A. Levine Books'),
('018','Del Rey'),
('019','Paw Prints');

CREATE TABLE PublisherAuthors (
    p_id INT NOT NULL,
    a_id INT NOT NULL
);

INSERT INTO PublisherAuthors(p_id, a_id) VALUES
('001', '001');

CREATE TABLE Authors (
    a_id INT NOT NULL,
    a_name TEXT(100) NOT NULL
);

INSERT INTO Authors(a_id, a_name) VALUES
('001', 'Steve Young'),
('011', 'Stephen King'),
('012', 'J.K. Rowling'),
('013', 'Eric Nylund'),
('014', 'James Buckley Jr.'),
('015', 'Dr Seuss'),
('016', 'Rick Riordan'),
('017', 'Antonia Fraser'),
('018', 'Edmund Burke'),
('019', 'Joseph Staten');



CREATE TABLE BookAuthor (
    --FOREIGN KEY(b_id) REFERENCES Book(b_id)
    --FOREIGN KEY(b_id) REFERENCES Book(b_id)
    BAb_id INT NOT NULL,
    BAa_id INT NOT NULL
);

INSERT INTO BookAuthor(BAb_id, BAa_id) VALUES
('0001', '001'),

('0011', '011'),
('0012', '012'),
('0018', '012'),
('0013', '013'),
('0020', '013'),
('0014', '017'),
('0015', '014'),
('0016', '015'),
('0017', '018'),
('0019', '016');



CREATE TABLE Book (
    b_id INT PRIMARY KEY,
    b_title VARCHAR(100) NOT NULL,
    b_rating REAL(3) NOT NULL,
    b_isbn INT NOT NULL,
    b_language TEXT(20) NOT NULL,
    b_numPages INT NOT NULL,
    b_publishYear DATETIME NOT NULL
);
--Ratings are 1-5 floats
INSERT INTO Book (b_id, b_title, b_rating, b_isbn, b_language, b_numPages, b_publishYear) VALUES
('0001','15 Minutes','3.87','0060725087', 'English', '176', '2006'),

('0011','Dreamcatcher','3.63','2253151440', 'English', '880', '2003'),
('0012','Harry Potter and the Sorcerers Stone (Harry Potter, #1)','4.47','0613959922', 'English', '293', '2001'),
('0013','Halo: Ghosts of Onyx','4.16','2253151440', 'English', '356', '2007'),
('0014','Mary Queen of Scots','4.05','0749301082', 'English', '906', '2001'),
('0015','The World Of Baseball','4.67','0789498456', 'English', '48', '2003'),
('0016','Horton Hears a Who!','4.47','0394900782', 'English', '72', '1962'),
('0017','Further Reflections on the Revolution in France','4.2','0865970998', 'English', '361', '1992'),
('0018','Harry Potter and the Prisoner of Azkaban (Harry Potter, #3)','4.57','0439554926', 'English', '422', '2003'),
('0019','The Lightning Thief (Percy Jackson and the Olympians, #1)','4.25','1435256891', 'English', '377', '2008'),
('0020','Halo: The Fall of Reach','4.27','0345451341', 'English', '352', '2001'),
('0021','Halo: Contact Harvest','3.98','0765315696', 'English', '353', '2007');

CREATE TABLE Category (
    c_id INT PRIMARY KEY,
    c_name TEXT(50) NOT NULL
);

--INSERT INTO Category(c_id, c_name) VALUES

CREATE TABLE Ratings (
    r_id INT PRIMARY KEY,
    r_title VARCHAR(50) NOT NULL,
    r_rating REAL(3)
);

--INSERT INTO Ratings(r_id, r_title, r_rating) VALUES
INSERT INTO Ratings(r_id, r_title, r_rating) VALUES
('0011', '0020','4.27'),
('0012', '0019','4.25'),
('0013', '0013','4.16'),
('0014', '0014','4.05'),
('0015', '0016','4.47'),
('0016', '0015','4.67'),
('0017', '0018','4.57'),
('0018', '0021','3.98'),
('0019', '0012','4.47'),
('0020', '0011','3.63');


