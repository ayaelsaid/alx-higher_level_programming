-- lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT id, name
FROM cities
WHERE states.id =  1 
ORDER BY id ASC;
