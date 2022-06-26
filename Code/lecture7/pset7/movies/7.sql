SELECT title, rating
FROM ratings JOIN movies ON ratings.movie_id = movies.id
where year = 2010
ORDER BY rating DESC, title;