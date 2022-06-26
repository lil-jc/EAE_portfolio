SELECT DISTINCT title
FROM people JOIN stars ON people.id = stars.person_id
JOIN ratings ON ratings.movie_id = stars.movie_id
JOIN movies ON movies.id = stars.movie_id
where name = 'Chadwick Boseman'
ORDER BY rating DESC
LIMIT 5;