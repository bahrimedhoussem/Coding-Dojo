SELECT * FROM dojos_and_ninjas_schema.dojos;
INSERT INTO dojos (name) 
VALUES('dojo_africa');
INSERT INTO dojos (name) 
VALUES('dojo_usa'),('dojo_tunisia');
DELETE FROM dojos WHERE id = 1 ;
DELETE FROM dojos WHERE id = 2 ;
DELETE FROM dojos WHERE id = 3 ;
INSERT INTO dojos (name) 
VALUES('dojo_africa');
INSERT INTO dojos (name) 
VALUES('dojo_usa'),('dojo_tunisia');
INSERT INTO ninjas (first_name , last_name ,dojo_id) 
VALUES('houssem','bahri', 6) ;
INSERT INTO ninjas (first_name , last_name ,dojo_id) 
VALUES('iheb', 'hgds', 6),('ahmed','ggfg', 6);
INSERT INTO ninjas (first_name , last_name ,dojo_id) 
VALUES('walid','hfhf', 5) ;
INSERT INTO ninjas (first_name , last_name ,dojo_id) 
VALUES('ghaith', 'hgds', 5),('mortadha','ggfg', 5);
INSERT INTO ninjas (first_name , last_name ,dojo_id) 
VALUES('taco','hfhf', 4) ;
INSERT INTO ninjas (first_name , last_name ,dojo_id) 
VALUES('joe', 'asq', 4),('james','ggfg', 4);
DELETE FROM ninjas WHERE dojo_id = 6;
DELETE FROM ninjas WHERE dojo_id = 5;
DELETE FROM ninjas WHERE dojo_id = 4;

INSERT INTO ninjas (first_name , last_name ,dojo_id) 
VALUES('houssem','bahri', 6) ;
INSERT INTO ninjas (first_name , last_name ,dojo_id) 
VALUES('iheb', 'hgds', 6),('ahmed','ggfg', 6);
SELECT * from ninjas where id = 14;
SELECT * FROM ninjas 
JOIN dojos ON dojos.id = ninjas.dojo_id
where ninjas.id = 6;
select * from ninjas
join dojos on dojos.id=ninjas.dojo_id;

