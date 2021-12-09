INSERT INTO Category(c_id, c_name) VALUES
('12','NonFiction'),--diary of young--

('13', 'Domestic fiction')--tkm--

;

INSERT INTO Publisher(p_id, p_name) VALUES
('20', 'Bantum'),
('21', 'Harper Perennial Modern Classics'),
('22', 'Scribner'),
('23','Penguin Books'),
('24','Hachette Book Group')
;

INSERT INTO PublisherAuthors(PAp_id, PAa_id) VALUES
('20', '20'),
('20', '21'),
('20', '22'),

('21', '23'),

('22', '24'),

('23','25'),

('24','26')
;


INSERT INTO Authors(a_id, a_name) VALUES
('0020', 'Anne Frank'),--diary of young--
('0021', 'Eleanor Roosevelt'),--diary of young--
('0022', 'B.M. Mooyaart-Doubleday'),--diary of young--

('0023', 'Harper Lee'),---tkm---

('0024', 'F. Scott Fitzgerald'),

('0025','Don Quixote'),

('0026','Andrzej Sapkowski')
;



INSERT INTO BookAuthor(BAb_id, BAa_id) VALUES
('0022', '020'),--diary of young--
('0022', '021'),--diary of young--
('0022', '022'),--diary of young--

('0023', '023'),--tkm--

('0024', '024'),---tgb--

('0025','025'),

('0026','026')
;

INSERT INTO Book (b_id, b_title, b_isbn, b_language, b_numPages, b_publishYear, bc_id, ba_id) VALUES
('22','The Diary of a Young Girl','553296981', 'English', '710', '1947', '12', 'null' ),

('23','To Kill a Mockingbird','61120081','English','336','1960', '13', 'null'),

('24','The Great Gatsby', '0743273567','English','200','1925', '13', 'null'),

('25','Don Quixote', '0142437239','Spanish','1023','2003', '6', 'null'),

('26','Blood of Elves', '031602919X','Polish','398','2009', '8', 'null')

;


INSERT INTO Ratings(r_id, r_title, r_rating) VALUES
('22','22',4.10),

('23','23',4.25),

('24','24',3.93),--tgb--

('25','25', 3.88),
('26','26', 4.09)

;

