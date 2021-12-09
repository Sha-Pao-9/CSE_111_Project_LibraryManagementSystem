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
    p_name VARCHAR(100) NOT NULL
);


INSERT INTO Publisher(p_id, p_name) VALUES
('001', 'HarperCollins'),
('002', 'Wiley'),
('003', 'World Scientific'),
('004', 'St.Martins Paperbacks'),
('005', 'Four Corners Publishing'),
('006', 'Lulu.com'),
('007', 'Harper Perennial'),
('008', 'Mariner Books'),
('009', 'Library Binding'),
('010','Livre de Poche'),
('011','Turtleback Books'),
('012','Tor Books'),
('013','Delta'),
('014','DK Publishing'),
('015','Random House Books for Young Readers'),
('016','Liberty Fund Inc'),
('017','Arthur A. Levine Books'),
('018','Del Rey'),
('019','Paw Prints'),
('20', 'Bantum'),
('21', 'Harper Perennial Modern Classics'),
('22', 'Scribner'),
('23','Penguin Books'),
('24','Hachette Book Group');


CREATE TABLE PublisherAuthors (
    PAp_id INT NOT NULL,
    PAa_id INT NOT NULL
);

INSERT INTO PublisherAuthors(PAp_id, PAa_id) VALUES
('001', '001'),
('002', '002'),
('003', '003'),
('004', '004'),
('005', '005'),
('006', '006'),
('001', '007'),
('007', '008'),
('008', '009'),
('009', '010'),
('0011', '011'),
('0012', '012'),
('0018', '012'),
('0013', '013'),
('0020', '013'),
('0014', '017'),
('0015', '014'),
('0016', '015'),
('0017', '018'),
('0019', '016'),
('20', '20'),
('20', '21'),
('20', '22'),
('21', '23'),
('22', '24'),
('23','25'),
('24','26');

CREATE TABLE Authors (
    a_id INT NOT NULL,
    a_name TEXT(100) NOT NULL
);

INSERT INTO Authors(a_id, a_name) VALUES
('001', 'Steve Young'),
('002', 'Molly E. Holzschlag'),
('003', 'Stephen Hawking'),
('004', 'Tom Henderson'),
('005', 'Whitney Stewart'),
('006', 'Howard Hopkins'),
('007', 'Michael Allaby'),
('008', 'Gaston Leroux'),
('009', 'Penelope Fitzgerald'),
('010', 'Douglas Adams'),
('011', 'Stephen King'),
('012', 'J.K. Rowling'),
('013', 'Eric Nylund'),
('014', 'James Buckley Jr.'),
('015', 'Dr Seuss'),
('016', 'Rick Riordan'),
('017', 'Antonia Fraser'),
('018', 'Edmund Burke'),
('019', 'Joseph Staten'),
('0020', 'Anne Frank'),--diary of young--
('0021', 'Eleanor Roosevelt'),--diary of young--
('0022', 'B.M. Mooyaart-Doubleday'),--diary of young--
('0023', 'Harper Lee'),---tkm---
('0024', 'F. Scott Fitzgerald'),
('0025','Don Quixote'),
('0026','Andrzej Sapkowski');


CREATE TABLE BookAuthor (
    --FOREIGN KEY(b_id) REFERENCES Book(b_id)
    --FOREIGN KEY(b_id) REFERENCES Book(b_id)
    BAb_id INT NOT NULL,
    BAa_id INT NOT NULL
);

INSERT INTO BookAuthor(BAb_id, BAa_id) VALUES
('0001', '001'),
('0002', '002'),
('0003', '003'),
('0004', '004'),
('0005', '005'),
('0006', '006'),
('0007', '007'),
('0008', '008'),
('0009', '009'),
('0010', '010'),
('0011', '011'),
('0012', '012'),
('0018', '012'),
('0013', '013'),
('0020', '013'),
('0014', '017'),
('0015', '014'),
('0016', '015'),
('0017', '018'),
('0019', '016'),
('0022', '020'),--diary of young--
('0022', '021'),--diary of young--
('0022', '022'),--diary of young--
('0023', '023'),--tkm--
('0024', '024'),---tgb--
('0025','025'),
('0026','026');


CREATE TABLE Book (
    b_id INT PRIMARY KEY,
    b_title VARCHAR(100) NOT NULL,
    b_isbn INT NOT NULL,
    b_language TEXT(20) NOT NULL,
    b_numPages INT NOT NULL,
    b_publishYear DATETIME NOT NULL,
    bc_id INT NOT NULL,
    ba_id INT NOT NULL
);

--Ratings are 1-5 floats
INSERT INTO Book (b_id, b_title, b_isbn, b_language, b_numPages, b_publishYear, bc_id, ba_id) VALUES
('0001','15 Minutes','0060725087', 'English', '176', '2006', '01', '001'),
('0002','250 HTML and Web Design Secrets', '0764568450', 'English', '432', '2004', '02', '002'),
('0003', 'A Brief History of Time: From the Big Bang to Black Holes', '0553173251', 'English', '224', '1997', '02', '003'),
('0004', 'A Deadly Affair', '0312977646', 'English', '384', '2001', '03', '004'),
('0005', 'Blues Across the Bay', '1893577082', 'English', '151', '2001', '01', '005'),
('0006', 'Night Demons', '1430318708', 'English', '380', '2007', '04', '006'),
('0007', 'Biology', '0004709284', 'English', '333', '1996', '02', '007'),
('0008', 'The Phantom of the Opera', '9780060809249','French', '360', '1909', '05', '008'),
('0009', 'The Blue Flower', '0006550193', 'English', '226', '1995', '06', '009'),
('0010', 'The Ultimate Hitchhiker''s Guide to the Galaxy', '1448714362', 'English', '815', '2010', '07', '010'),
('0011','Dreamcatcher', '2253151440', 'English', '880', '2003', '07', '011'),
('0012','Harry Potter and the Sorcerers Stone (Harry Potter, #1)', '0613959922', 'English', '293', '2001', '08', '012'),
('0013','Halo: Ghosts of Onyx', '2253151440', 'English', '356', '2007', '07', '013'),
('0014','Mary Queen of Scots', '0749301082', 'English', '906', '2001', '09', '017'),
('0015','The World Of Baseball', '0789498456', 'English', '48', '2003', '10', '014'),
('0016','Horton Hears a Who!', '0394900782', 'English', '72', '1962', '01', '015'),
('0017','Further Reflections on the Revolution in France', '0865970998', 'English', '361', '1992', '11', '018'),
('0018','Harry Potter and the Prisoner of Azkaban (Harry Potter, #3)', '0439554926', 'English', '422', '2003', '08', '012'),
('0019','The Lightning Thief (Percy Jackson and the Olympians, #1)', '1435256891', 'English', '377', '2008', '08', '016'),
('0020','Halo: The Fall of Reach', '0345451341', 'English', '352', '2001', '07', '013'),
('0021','Halo: Contact Harvest', '0765315696', 'English', '353', '2007', '07', '019'),
('22','The Diary of a Young Girl','553296981', 'English', '710', '1947', '12', 'null' ),
('23','To Kill a Mockingbird','61120081','English','336','1960', '13', 'null'),
('24','The Great Gatsby', '0743273567','English','200','1925', '13', 'null'),
('25','Don Quixote', '0142437239','Spanish','1023','2003', '6', 'null'),
('26','Blood of Elves', '031602919X','Polish','398','2009', '8', 'null');

CREATE TABLE Category (
    c_id INT PRIMARY KEY,
    c_name TEXT(50) NOT NULL
);

INSERT INTO Category(c_id, c_name) VALUES
('01','Children'),
('02','Education'),
('03', 'Crime'),
('04', 'Horror'),
('05', 'Romance'),
('06', 'Historical Fiction'),
('07', 'Science Fiction'),
('08', 'Fantasy'),
('09', 'Biography'),
('10', 'Sports'),
('11', 'French Revolution'),
('12','NonFiction'),--diary of young--
('13', 'Domestic fiction')--tkm--
;


CREATE TABLE Ratings (
    r_id INT PRIMARY KEY,
    r_title VARCHAR(50) NOT NULL,
    r_rating REAL(3)
);

INSERT INTO Ratings(r_id, r_title, r_rating) VALUES
('0001', '0001', 3.87),
('0002', '0002', 3.45),
('0003', '0003', 4.18),
('0004', '0004', 3.42),
('0005', '0005', 5.0),
('0006', '0006', 5.0),
('0007', '0007', 0.0),
('0008', '0008', 3.96),
('0009', '0009', 3.46),
('0010', '0010', 4.35),
('0011', '0020', 4.27),
('0012', '0019', 4.25),
('0013', '0013', 4.16),
('0014', '0014', 4.05),
('0015', '0016', 4.47),
('0016', '0015', 4.67),
('0017', '0018', 4.57),
('0018', '0021', 3.98),
('0019', '0012', 4.47),
('0020', '0011', 3.63),
('0022','0022',4.10),
('0023','0023',4.25),
('0024','0024',3.93),--tgb--
('0025','0025', 3.88),
('0026','0026', 4.09);
