-- lists all genres in the database hbtn_0d_tvshows_rate by their rating
SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating
FROM tv_genres
INNER JOIN tv_show_genre ON tv_show_genres.genre_id = tv_show_genre.id
INNER JOIN tv_shows ON tv_show_genre.show_id = tv_shows.id
INNER JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.name
ORDER BY rating DESC;
