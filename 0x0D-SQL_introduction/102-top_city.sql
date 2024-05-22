-- Import the temperatures table data
-- Display the top 3 cities by average temperature during July and August

SELECT city
FROM temperatures
WHERE month IN ('July', 'August')
GROUP BY city
ORDER BY temperatures DESC
LIMIT 3;
