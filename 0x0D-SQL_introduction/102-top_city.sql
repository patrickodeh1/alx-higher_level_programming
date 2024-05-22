-- Import the temperatures table data
-- Display the top 3 cities by average temperature during July and August

SOURCE temperatures.sql;

SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
WHERE month IN ('July', 'August')
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
