 -- script that lists all shows contained in hbtn_0d_tvshows
-- without a genre linked.
SELECT tv_genres.name as genre, COUNT(*) as number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres ON
tv_show_genres.genre_id=tv_genres.id
GROUP BY genre
ORDER BY number_of_shows DESC;
