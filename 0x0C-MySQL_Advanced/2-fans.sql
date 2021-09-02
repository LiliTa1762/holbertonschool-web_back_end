-- Best band ever
-- Ordered by fans
USE holberton;
SELECT origin, SUM(fans) AS "nb_fans" FROM metal_bands
GROUP BY origin
