SELECT genre,COUNT(title) AS count
FROM songs
GROUP BY genre;

SELECT genre,COUNT(title) AS count, AVG(duration) AS average_duration
FROM songs
GROUP BY genre;