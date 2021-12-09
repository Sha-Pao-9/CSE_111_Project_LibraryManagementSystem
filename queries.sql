--1 new account
INSERT INTO User 
VALUES ( '3' , 'Paolo Tercero' , 'Paolo Tercero@gmail.com', 'genericpassword');

DELETE FROM User
WHERE u_name = 'Paolo Tercero';
--2 update password
UPDATE  User
SET     u_password = 'newpassword'
WHERE   u_userkey = 3;

UPDATE Ratings
SET r_rating = 1.00
FROM Book
ON Ratings.r_title = Book.b_id
SET r_rating = 1.00
WHERE Book.b_id = 7;

--3 new book
INSERT INTO Book (b_id, b_title, b_isbn, b_language, b_numPages, b_publishYear, bc_id, ba_id) VALUES
('0022','Game of Thrones','0553588486 ', 'English', '835', '2005','08', '22');


DELETE FROM Book
WHERE b_id = '0022';
--4 change book
INSERT INTO Authors(a_id, a_name) VALUES
('022', 'George R.R. Martin');

--5 Delete certain book
DELETE FROM Book
WHERE b_title = 'Game of Thrones';



--6 display all books rated higher than 4.30
SELECT  b_title, r_rating
FROM    Book, 
        Ratings
WHERE   r_title = b_id
AND     r_rating > 4.30;

-- 7 show all isgn # of books bookmarked by John Doe
SELECT  u_name, bm_title, b_isbn
FROM    User,
        Bookmarks,
        Book 
WHERE   u_userkey = bm_userkey
AND     bm_title = b_title
AND     u_name = 'John Doe'

--8 select users book martes wth rating greater than 4.20
SELECT  u_name, bm_title, b_isbn, r_rating
FROM    User,
        Bookmarks,
        Book,
        Ratings
WHERE   u_userkey = bm_userkey
AND     bm_title = b_title
AND     r_title = b_id
AND     r_rating > 4.20;

--9 many to many slect books with pages less than 300
SELECT  a_name, b_title, b_numPages
FROM    Authors,
        Book,
        BookAuthor
WHERE b_numPages < 300
AND BAa_id = a_id
AND BAb_id = b_id;

--9 many to many, select authors with their books

SELECT  a_name, b_title, b_numPages
FROM    Authors,
        Book,
        BookAuthor
WHERE   BAa_id = a_id
AND     BAb_id = b_id;

-- 10
SELECT *
FROM  Book
WHERE b_title LIKE 'Ha%';

--11 select the autors with book that start with Ha
SELECT  a_name, b_title
FROM    Authors, 
        BookAuthor,(
                SELECT *
                FROM  Book
                WHERE b_title LIKE 'Ha%') as HAbooks
WHERE HAbooks.b_id = BAb_id
AND   BAa_id = a_id;

SELECT b_title  --12
FROM Book, Category
WHERE bc_id = c_id
AND c_name = 'Education';

SELECT r_rating --13
FROM Ratings 
WHERE r_rating < 4.00;

SELECT p_name --14
FROM Publisher, Book 
WHERE p_id = b_id 
AND b_language = 'English';

SELECT b_title, a_name  --15 Complex?----
FROM Book, Authors, Ratings 
WHERE ba_id = a_id
AND r_id = b_id
AND r_rating > 3.5;

SELECT b_title, MAX(r_rating) --16
FROM Book, Ratings
WHERE b_id = r_id;

SELECT a_name, b_title  --17-----
FROM Book, Category, Authors
WHERE bc_id = c_id
AND ba_id = a_id
AND c_name = 'Horror';

SELECT a_name, b_title --18 Complex----
FROM Book, Category, Authors
WHERE bc_id = c_id
AND ba_id = a_id
AND c_name = 'Romance'
AND b_language IS NOT 'English';


SELECT b_title, r_rating, a_name, b_publishYear --19 Complex
FROM Book, Ratings, Authors
WHERE b_id = r_id
AND ba_id = a_id
AND b_publishYear > '2000';


SELECT p_name
FROM Publisher, PublisherAuthors, Book, Authors --20 Complex
WHERE p_id = PAp_id
AND  PAa_id = a_id
AND ba_id = a_id
AND b_language = 'English';


SELECT b_title -- 21
FROM Book, Authors
WHERE ba_id = a_id
AND b_numPages > 300;
