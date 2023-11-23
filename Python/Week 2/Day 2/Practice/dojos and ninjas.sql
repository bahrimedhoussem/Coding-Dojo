SELECT * FROM dojos; 
INSERT INTO dojos (name) 
VALUES ("iheb"),("fares"),("sadok");
DELETE FROM dojos WHERE (id = '1');
DELETE FROM dojos WHERE (id = '2');
DELETE FROM dojos WHERE (id = '3');	
INSERT INTO dojos (name) 
VALUES ("cesar"),("sobby"),("loren");
SELECT * FROM ninjas;
INSERT INTO ninjas (first_name,last_name,age,dojo_id) 
VALUES ("allela","fehri",23,4),("walid","fehri",18,4),("ahmed","fehri",26,4);
INSERT INTO ninjas (first_name,last_name,age,dojo_id) 
VALUES ("fares","alaya",30,5),("ghaith","ouni",31,5),("gaith","jridi",32,5);
INSERT INTO ninjas (first_name,last_name,age,dojo_id) 
VALUES ("amen","maatalh",30,6),("jassem","abidi",31,6),("iheb","benslimen",32,6);
SELECT * FROM ninjas
JOIN dojos ON ninjas.dojo_id = dojos.id
WHERE dojos.id = 4;
SELECT * FROM ninjas
JOIN dojos ON ninjas.dojo_id = dojos.id
WHERE dojos.id = 5;
SELECT * FROM ninjas
JOIN dojos ON ninjas.dojo_id = dojos.id
WHERE dojos.id = 6;
-- fetch the last ninja in ninjas table
SELECT dojo_id FROM ninjas
ORDER BY ninjas.id DESC
LIMIt 1;
-- Query: Retrieve the last ninja's dojo
SELECT * from dojos 
WhERE id = (SELECT dojo_id FROM ninjas
ORDER BY ninjas.id DESC
LIMIt 1);		
SELECT * from ninjas 
join dojos on dojos.id = ninjas.dojo_id 
where ninjas.id = 6 ;
SELECT * from ninjas 
JOIN dojos on dojos.id = ninjas.dojo_id;



