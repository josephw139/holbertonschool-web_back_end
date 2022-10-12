-- creates function divides first by the second number or returns 0 if the second number is 0.

DELIMITER //

CREATE FUNCTION SafeDiv (a INT, b INT) RETURNS FLOAT
BEGIN
	IF b = 0 THEN
		RETURN 0;
	END IF;
	RETURN a / b;
END //

DELIMITER ;