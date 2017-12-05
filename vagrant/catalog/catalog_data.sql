-- for postgress replace NOW() with NOW()

-- INSERT INTO cat_user VALUES (100, 'Samson', 'Sam@123#', NOW(), NOW());
-- INSERT INTO cat_user VALUES (101, 'Nancy', 'Nan@123#', NOW(), NOW());
-- INSERT INTO cat_user VALUES (102, 'Meryl', 'Mery@123#', NOW(), NOW());
-- INSERT INTO cat_user VALUES (103, 'Meritta', 'Meri@123#', NOW(), NOW());
-- INSERT INTO cat_user VALUES (104, 'Sophie', 'Sop@123#', NOW(), NOW());


INSERT INTO category VALUES (10, 'Cricket', 100, NOW(), NOW());
INSERT INTO category VALUES (11, 'Basketball', 101, NOW(), NOW());
INSERT INTO category VALUES (12, 'Badminton', 102, NOW(), NOW());
INSERT INTO category VALUES (13, 'Football', 103, NOW(), NOW());
INSERT INTO category VALUES (14, 'Indoor', 104, NOW(), NOW());


INSERT INTO item VALUES (1000, 'Cricket ball', 100, NOW(), NOW(), 10);
INSERT INTO item VALUES (1001, 'Crickets bat', 100, NOW(), NOW(), 10);
INSERT INTO item VALUES (1002, 'Basketball net', 101, NOW(), NOW(), 11);
INSERT INTO item VALUES (1003, 'Racket', 102, NOW(), NOW(), 12);
INSERT INTO item VALUES (1004, 'Studs', 103, NOW(), NOW(), 13);
INSERT INTO item VALUES (1005, 'Chess', 104, NOW(), NOW(), 14);