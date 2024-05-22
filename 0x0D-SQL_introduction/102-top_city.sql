-- Import the temperatures table data
-- Display the top 3 cities by average temperature during July and August
USE hbtn_0c_0;
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE MONTH(date) IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
