SELECT * FROM users.users_1;
INSERT INTO users_1 (first_name, last_name, email) 
VALUES( 'houssem', 'bahri' , 'houssembahri@hotmail.fr');
SELECT * 
FROM users_1
WHERE email = 'houssembahri@hotmail.fr';
SELECT *
FROM users_1
WHERE id = 4;
UPDATE users_1
SET last_name = 'Pancakes'
WHERE id = 4;

SELECT first_name 
FROM users_1;




