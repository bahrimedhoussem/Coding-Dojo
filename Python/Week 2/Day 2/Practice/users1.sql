SELECT * FROM my_schema.users;
INSERT INTO users (first_name,last_name,email) 
VALUES ('jean', 'smith', "aa@email.com"), ('andrea', 'pirlo','hgf@jhgf.com') , ('josé' , 'milan', 'dd@dd.com') ;
	SELECT * FROM users
    WHERE email = 'aa@email.com';
    SELECT* FROM users
    where  id = 3;
   UPDATE users SET last_name = "pancakes" 
WHERE users.id = 3;
DELETE FROM users
 WHERE id = 2;
	SELECT * FROM users
ORDER BY first_name DESC;