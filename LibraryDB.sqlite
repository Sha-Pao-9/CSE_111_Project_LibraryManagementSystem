DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Bookmarks;
DROP TABLE IF EXISTS Edit;
DROP TABLE IF EXISTS Search;
DROP TABLE IF EXISTS Book;
DROP TABLE IF EXISTS Info;
DROP TABLE IF EXISTS Authors;
DROP TABLE IF EXISTS Author_Book;
DROP TABLE IF EXISTS Category;


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

CREATE TABLE Edit (
    add_id INT FOREIGN KEY,
    re_id INT FOREIGN KEY
);

CREATE TABLE Search (
    s_id INT PRIMARY KEY,
    s_title VARCHAR(100) NOT NULL,
    s_category VARCHAR(50) NOT NULL,
    s_publisher VARCHAR(100) NOT NULL,
    s_isbn INT NOT NULL
);

CREATE TABLE Book (
    b_id INT PRIMARY KEY,
    b_name VARCHAR(100) NOT NULL
);

CREATE TABLE Info (
    i_id INT PRIMARY KEY,
    i_title VARCHAR(100) NOT NULL,
    i_author VARCHAR(100) NOT NULL,
    i_avgRating INT NOT NULL,
    i_isbn INT NOT NULL,
    i_language VARCHAR(20) NOT NULL,
    i_numPages INT NOT NULL,
    i_publishDate DATETIME NOT NULL,
    i_publisher VARCHAR(100) NOT NULL
);

CREATE TABLE Authors (
    a_id INT NOT NULL,
    a_name VARCHAR(100) NOT NULL
);

CREATE TABLE Author_Book (
    a_id INT FOREIGN KEY,
    b_id INT FOREIGN KEY
);

CREATE TABLE Category (
    c_id INT PRIMARY KEY,
    c_name VARCHAR(50) NOT NULL
);
