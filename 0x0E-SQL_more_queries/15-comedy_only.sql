-- lists all Comedy shows 
SELECT a.title
FROM tv_shows a
JOIN tv_show_genres b
ON a.id = b.show_id
JOIN tv_genres c
ON b.genre_id = c.id
WHERE c.name = 'Comedy'
ORDER BY a.title ASC;
