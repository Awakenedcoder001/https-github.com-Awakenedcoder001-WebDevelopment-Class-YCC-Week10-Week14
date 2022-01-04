CREATE  PROCEDURE outparameter(OUT the_count INT)
BEGIN
 select count(*) into the_count from cricketer where designation="bowler"; 
END