-- 01. Querying data
SELECT LastName FROM employees;
SELECT LastName,FirstName from employees;
SELECT * FROM employees;
SELECT FirstName AS '이름' FROM employees;
SELECT Name, Milliseconds / 60000 '재생 시간(분)'
From tracks;
-- 02. Sorting data
SELECT FirstName
FROM employees
ORDER BY FirstName;

SELECT FirstName
FROM employees
ORDER BY FirstName DESC;

SELECT Country, City
FROM customers
ORDER BY Country DESC, City ASC;

SELECT Name, Milliseconds/60000 AS '재생 시간(분)'
FROM tracks
ORDER BY Milliseconds DESC;

-- NULL 정렬 예시
SELECT ReportsTo
From employees
ORDER BY ReportsTo;

-- 03. Filtering data
SELECT DISTINCT Country
FROM customers
ORDER BY Country;

SELECT LastName,FirstName,City
FROM customers
WHERE City = 'Prague';

SELECT LastName,FirstName, Company, count
FROM customers
WHERE Company IS NULL 
AND Country = 'USA';

SELECT LastName,FirstName, Company, count
FROM customers
WHERE Company IS NULL 
OR Country = 'USA';

SELECT Name, Bytes
FROM tracks
-- WHERE Bytes >= 100000
-- AND Bytes <= 500000;
Bytes BETWEEN 100000 AND 500000
ORDER BY Bytes;

SELECT LastName,FirstName,Country
FROM customers
-- WHERE Country = 'Canada'
-- OR Country = 'Germany'
-- or Country = 'France';
WHERE Country IN ('Canada','Germany','France');

SELECT LastName,FirstName
FROM customers
WHERE LastName LIKE '%son';
-- 끝에는 son이어야함
SELECT LastName,FirstName
FROM customers
WHERE FirstName LIKE '___a';
-- NULL 값은 =  로 비교하지 않음


SELECT TrackId, Name, Bytes
FROM tracks
ORDER BY Bytes DESC
LIMIT 7;

SELECT TrackId, Name, Bytes
FROM tracks
ORDER BY Bytes DESC
-- LIMIT 3,4;
LIMIT 4 OFFSET 3;
-- 04. Grouping data

SELECT Country, COUNT(*)
FROM customers
GROUP BY Country;
-- 여기까지는 DISTINCT랑 똑같, COUNT로 차이

SELECT Composer, AVG(Bytes)
FROM tracks
GROUP By Composer
ORDER BY AVG(Bytes) DESC;

SELECT Composer, AVG(Milliseconds / 60000) AS avgOfMinute
FROM tracks
GROUP BY Composer
HAVING avgOfMinute < 10;

--  HAVING <-> GROUP BY

