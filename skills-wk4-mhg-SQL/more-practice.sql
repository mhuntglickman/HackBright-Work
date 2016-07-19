-- Include your solutions to the More Practice problems in this file.
--MHG Skills Assessment WK4 SQL


-- INSERT
INSERT INTO models VALUES(2015, 'Chevrolet', 'Malibu');
INSERT INTO models VALUES(2015, 'Subaru', 'Outback');

-- CREATE TABLE
CREATE TABLE awards(
					name VARCHAR(25) NOT NULL, 
					year INTEGER NOT NULL, 
					winner_id INTEGER NOT NULL PRIMARY KEY);
-- I made all the fields necessary because it would seem silly to know a winner won
-- an unknown award or for that matter won an award with an unknown year.

--MORE INSERTS
INSERT INTO awards VALUES('IIHS Safety Award', 2015, 49);
INSErT INTO awards VALUES('IIHS Safety Award', 2015, 50);

