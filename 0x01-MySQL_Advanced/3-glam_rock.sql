-- lists all bands 'Glam rock' as main style

SELECT band_name, (IFNULL(split, 2020) - formed) as lifespan FROM
metal_bands WHERE style = 'Glam rock' ORDER BY lifepsan DESC;
