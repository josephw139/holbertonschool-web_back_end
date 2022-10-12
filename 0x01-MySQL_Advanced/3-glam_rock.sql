-- lists all bands 'Glam rock' as main style

SELECT band_name, (split-formed) as lifespan FROM
metal_bands WHERE style = 'Glam rock' ORDER BY lifepsan DESC
