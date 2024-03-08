-- lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT states.name, cities,id
FROM states
JOIN cities ON states.name = cities.name
ORDER BY cities.id ASC;
