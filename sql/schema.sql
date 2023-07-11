CREATE TABLE Customer (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE,
  phone_number VARCHAR(20) NOT NULL UNIQUE,
  address VARCHAR(255)
);


CREATE TABLE Vehicle (
  id INT PRIMARY KEY AUTO_INCREMENT,
  category ENUM('small', 'family', 'van') NOT NULL,
  status ENUM('available', 'unavailable') NOT NULL,
  rent_price DECIMAL(10, 2) NOT NULL,
  photo BLOB NOT NULL,
  details VARCHAR(255) NOT NULL
);

CREATE TABLE Booking (
  id INT PRIMARY KEY AUTO_INCREMENT,
  hire_date DATE NOT NULL,
  return_date DATE NOT NULL,
  vehicle_id INT,
  customer_id INT,
  FOREIGN KEY (vehicle_id) REFERENCES Vehicle(id),
  FOREIGN KEY (customer_id) REFERENCES Customer(id)
);

DELIMITER //
CREATE TRIGGER check_booking_dates
BEFORE INSERT ON Booking
FOR EACH ROW
BEGIN
    IF DATEDIFF(NEW.return_date, NEW.hire_date) > 7 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Error: Hire duration cannot exceed 7 days';
    END IF;
END //
DELIMITER ;

CREATE TABLE Payment_Invoice (
  id INT PRIMARY KEY AUTO_INCREMENT,
  amount DECIMAL(10, 2) NOT NULL,
  payment_type ENUM('cash', 'online') NOT NULL,
  transaction_date DATE NOT NULL,
  booking_id INT,
  FOREIGN KEY (booking_id) REFERENCES Booking(id)
);