CREATE  PROCEDURE inoutparameter(IN the_department varchar(45) , OUT the_count INT)
BEGIN
 select count(*) into the_count from cricketer where team=the_department;
END