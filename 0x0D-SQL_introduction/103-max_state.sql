-- Import the temperatures table data
-- Display the maximum temperature of each state

SOURCE temperatures.sql;

SELECT state, MAX(temperature) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
