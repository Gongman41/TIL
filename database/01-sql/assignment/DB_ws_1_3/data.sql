SELECT *
FROM users
WHERE first_name LIKE '하%';

SELECT *
FROM users
WHERE phone LIKE '%555';

SELECT *
FROM users
WHERE country LIKE '경상%';

SELECT *
FROM users
WHERE (country LIKE '경%' OR '층%') AND country LIKE '__남%';