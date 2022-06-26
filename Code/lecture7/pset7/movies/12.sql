
select title
from ratings join stars on ratings.movie_id = stars.movie_id
join people on people.id = stars.person_id
join movies on movies.id = stars.movie_id
where name in('Johnny depp','Helena Bonham Carter')
order by title;
