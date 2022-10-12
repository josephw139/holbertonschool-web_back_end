-- decreases quanity of an item after adding new order

CREATE TRIGGER trigger AFTER INSERT ON orders
FOR EACH ROW UPDATE items
SET quantity = quantity - NEW.number WHERE
name = NEW.item_name
