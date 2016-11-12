CREATE TABLE IF NOT EXISTS meal (
   id INT NOT NULL AUTO_INCREMENT,
   name VARCHAR(100) NOT NULL,
   calorie INT,
   type VARCHAR(20) NOT NULL,
   submission_date DATE,
   PRIMARY KEY  (id)
);
