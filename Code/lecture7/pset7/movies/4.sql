SELECT COUNT(title)
FROM movies
where id in (SELECT movie_id FROM ratings where rating = 10.0);