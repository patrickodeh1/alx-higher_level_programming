-- computes averages
-- computes score average
SELECT AVG(id) AS avg_id, AVG(score) AS avg_score, AVG(name_length) AS avg_name_length
FROM (
    SELECT id, score, LENGTH(name) AS name_length
    FROM second_table
) AS subquery;
