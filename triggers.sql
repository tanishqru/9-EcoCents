-- Trigger to update points when points are credited
DELIMITER //
CREATE TRIGGER update_points_credited
AFTER INSERT ON points
FOR EACH ROW
BEGIN
    UPDATE points
    SET balance_points = (SELECT initial_points FROM users WHERE uid = NEW.uid) + NEW.points_credited - NEW.points_debited
    WHERE points_id = NEW.points_id;
END;
//
DELIMITER ;

-- Trigger to update money when money is credited
DELIMITER //
CREATE TRIGGER update_money_credited
AFTER INSERT ON money
FOR EACH ROW
BEGIN
    UPDATE money
    SET balance_money = (SELECT initial_money FROM users WHERE uid = NEW.uid) + NEW.money_credited - NEW.money_debited
    WHERE money_id = NEW.money_id;
END;
//
DELIMITER ;

-- Trigger to update points debited in the "ecocents" database
DELIMITER //
CREATE TRIGGER ecocents.update_points_debited
AFTER INSERT ON ecocents.points
FOR EACH ROW
BEGIN
    IF NEW.points_debited IS NOT NULL THEN
        UPDATE ecocents.points
        SET balance_points = (SELECT initial_points FROM ecocents.users WHERE uid = NEW.uid) + NEW.points_credited - NEW.points_debited
        WHERE points_id = NEW.points_id;
    END IF;
END;
//
DELIMITER ;

-- Trigger to update money debited in the "ecocents" database
DELIMITER //
CREATE TRIGGER ecocents.update_money_debited
AFTER INSERT ON ecocents.money
FOR EACH ROW
BEGIN
    IF NEW.money_debited IS NOT NULL THEN
        UPDATE ecocents.money
        SET balance_money = (SELECT initial_money FROM ecocents.users WHERE uid = NEW.uid) + NEW.money_credited - NEW.money_debited
        WHERE money_id = NEW.money_id;
    END IF;
END;
//
DELIMITER ;

-- Trigger to update points balance
DELIMITER //
CREATE TRIGGER update_points_balance
AFTER INSERT ON ecocents.points
FOR EACH ROW
BEGIN
    UPDATE ecocents.points
    SET balance_points = (SELECT initial_points FROM ecocents.users WHERE uid = NEW.uid) + NEW.points_credited - NEW.points_debited
    WHERE points_id = NEW.points_id;
END;
//
DELIMITER ;

-- Trigger to update money balance
DELIMITER //
CREATE TRIGGER update_money_balance
AFTER INSERT ON ecocents.money
FOR EACH ROW
BEGIN
    UPDATE ecocents.money
    SET balance_money = (SELECT initial_money FROM ecocents.users WHERE uid = NEW.uid) + NEW.money_credited - NEW.money_debited
    WHERE money_id = NEW.money_id;
END;
//
DELIMITER ;

-- Trigger to update shares_available in the project table when a share is purchased
DELIMITER //
CREATE TRIGGER ecocents.update_shares_available
AFTER INSERT ON ecocents.share_purchase
FOR EACH ROW
BEGIN
    UPDATE ecocents.project
    SET shares_available = shares_available - NEW.qty
    WHERE project_id = NEW.share_id;
END;
//
DELIMITER ;