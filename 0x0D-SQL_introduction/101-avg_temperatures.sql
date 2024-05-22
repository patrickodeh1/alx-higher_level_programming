-- Import the temperatures table data
-- Calculate the average temperature by city

SOURCE temperatures.sql;
SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
