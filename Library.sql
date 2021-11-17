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
;


CREATE TABLE Bookmarks (
    bm_userkey INT PRIMARY KEY,
    bm_title VARCHAR(100) NOT NULL,
    bm_author VARCHAR(100) NOT NULL, 
    bm_publisher VARCHAR(100) NOT NULL,
    bm_numPages INT NOT NULL,
    bm_addDate DATETIME NOT NULL
);

INSERT INTO Bookmarks(bm_userkey, bm_title, bm_author, bm_publisher, bm_numPages, bm_addDate) VALUES
;

CREATE TABLE Search (
    s_id INT PRIMARY KEY,
    s_title VARCHAR(100) NOT NULL,
    s_category VARCHAR(50) NOT NULL,
    s_publisher VARCHAR(100) NOT NULL,
    s_isbn INT NOT NULL
);

INSERT INTO Search(s_id, s_title, s_category, s_publisher, s_isbn) VALUES
;

CREATE TABLE Publisher (
    p_id INT PRIMARY KEY,
    p_name VARCHAR(100) NOT NULL
);


INSERT INTO Publisher(p_id, p_name) VALUES
;

CREATE TABLE PublisherAuthors (
    p_id INT NOT NULL,
    a_id INT NOT NULL
);

INSERT INTO PublisherAuthors(p_id, a_id) VALUES
;

CREATE TABLE Authors (
    a_id INT NOT NULL,
    a_name VARCHAR(100) NOT NULL
);

INSERT INTO Authors(a_id, a_name) VALUES
;

CREATE TABLE BookAuthor (
    --FOREIGN KEY(b_id) REFERENCES Book(b_id)
    --FOREIGN KEY(b_id) REFERENCES Book(b_id)
    b_id INT NOT NULL,
    a_id INT NOT NULL
);

INSERT INTO BookAuthor(p_id, p_name) VALUES
;

CREATE TABLE Book (
    b_id INT PRIMARY KEY,
    b_title VARCHAR(100) NOT NULL,
    b_rating INT NOT NULL,
    b_isbn INT NOT NULL,
    b_language VARCHAR(20) NOT NULL,
    b_numPages INT NOT NULL,
    b_publishDate DATETIME NOT NULL,
    b_publisher VARCHAR(100) NOT NULL
);

INSERT INTO Book(b_id, b_title, b_rating, b_isbn, b_language, b_numPages, b_publishDate, b_publisher) VALUES
;

CREATE TABLE Category (
    c_id INT PRIMARY KEY,
    c_name VARCHAR(50) NOT NULL
);

INSERT INTO Category(c_id, c_name) VALUES
;

CREATE TABLE Ratings (
    r_id INT PRIMARY KEY,
    r_title VARCHAR(50) NOT NULL,
    r_rating INT(30)
);

INSERT INTO Ratings(r_id, r_title, r_rating) VALUES
;

