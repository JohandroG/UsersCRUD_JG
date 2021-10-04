CREATE DATABASE users_schema;

USE users_schema;

CREATE TABLE users(
id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
first_name VARCHAR(45) NOT NULL,
last_name VARCHAR(45) NOT NULL,
email VARCHAR(45) NOT NULL,
created_at DATETIME NOT NULL,
updated_at DATETIME NOT NULL
);

INSERT INTO users(id,first_name,last_name,email,created_at,updated_at)
VALUES 
(1,'John', 'Ramirez','johnr@gmail.com',SYSDATE(),SYSDATE() ),
(2,'Juan', 'Alvarez','juana@gmail.com',SYSDATE(),SYSDATE() ),
(3,'Pedro', 'Venegas','pedrov@gmail.com',SYSDATE(),SYSDATE() );