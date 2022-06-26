SELECT name
FROM people JOIN stars ON people.id = stars.person_id
JOIN movies on movies.id = stars.movie_id
where movie_id
IN(
    --movies kevin Bacon starred in
    SELECT movie_id
    FROM people JOIN stars ON people.id = stars.person_id
    JOIN movies on movies.id = stars.movie_id
    WHERE name = 'Kevin Bacon' AND birth = 1958
) AND NOT name = 'Kevin Bacon'