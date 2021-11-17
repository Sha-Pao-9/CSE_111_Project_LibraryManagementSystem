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
    u_email VARCHARD(100) NOT NULL,
    u_password VARCHAR(100) NOT NULL
);

CREATE TABLE Bookmarks (
    bm_userkey INT PRIMARY KEY,
    bm_title VARCHAR(100) NOT NULL,
    bm_author VARCHAR(100) NOT NULL, 
    bm_publisher VARCHAR(100) NOT NULL,
    bm_numPages INT NOT NULL,
    bm_addDate DATETIME NOT NULL
);

CREATE TABLE Search (
    s_id INT PRIMARY KEY,
    s_title VARCHAR(100) NOT NULL,
    s_category VARCHAR(50) NOT NULL,
    s_publisher VARCHAR(100) NOT NULL,
    s_isbn INT NOT NULL
);

CREATE TABLE Publisher (
    p_id INT PRIMARY KEY,
    p_name VARCHAR(100) NOT NULL
);

CREATE TABLE PublisherAuthors (
    p_id INT NOT NULL,
    a_id INT NOT NULL
);

CREATE TABLE Authors (
    a_id INT NOT NULL,
    a_name VARCHAR(100) NOT NULL
);

CREATE TABLE BookAuthor (
    --FOREIGN KEY(b_id) REFERENCES Book(b_id)
    --FOREIGN KEY(b_id) REFERENCES Book(b_id)
    b_id INT NOT NULL,
    a_id INT NOT NULL
);

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


CREATE TABLE Category (
    c_id INT PRIMARY KEY,
    c_name VARCHAR(50) NOT NULL
);

CREATE TABLE Ratings (
    r_id INT PRIMARY KEY,
    r_title VARCHAR(50) NOT NULL,
    r_rating INT(30)
);

