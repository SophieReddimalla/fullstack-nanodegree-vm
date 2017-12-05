 CREATE VIEW vw_latest_items
 AS 
 SELECT i.description item, i.created, c.description category
 FROM item i 
 JOIN category c ON i.cat_id = c.id
 ORDER BY created DESC 
 LIMIT 3;
 

