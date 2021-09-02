-- Old school band - by main style
USE holberton
SELECT band_name, (IFNULL(split, 2020) - formed) AS lifespan FROM metal_bands WHERE style LIKE "%Glam rock%" GROUP BY band_name;
