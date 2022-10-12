-- decreases quanity of an item after adding new order

CREATE TRIGGER trigger AFTER INSERT ON orders
FOR EACH ROW UPDATE items
SET quanity = quanity - NEW.number WHERE
name = NEW.item_name
