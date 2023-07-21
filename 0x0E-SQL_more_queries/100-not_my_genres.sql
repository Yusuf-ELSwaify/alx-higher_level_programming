-- uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
-- -- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- -- Each record should display: tv_genres.name
SELECT name
FROM tv_genres
WHERE id not in(
    SELECT g.id
    FROM tv_shows s
    RIGHT JOIN tv_show_genres sg ON s.id = sg.show_id
    INNER JOIN tv_genres g ON sg.genre_id = g.id
    WHERE s.title = "Dexter"
    )
ORDER BY 1;
