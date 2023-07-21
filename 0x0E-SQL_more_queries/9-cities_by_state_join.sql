-- lists all cities contained in the database hbtn_0d_usa
SELECT c.id AS id , c.name AS name, s.name AS name
FROM cities as c
JOIN states as s ON c.state_id = s.id;
