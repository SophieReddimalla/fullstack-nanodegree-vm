--- Item Catalog Project
--- 
--- By Sophie Reddimalla  15/11/2017
------------------------------------------------
CREATE TABLE cat_user(
    id         integer,
    username   varchar(50),
    password   varchar(50),
    created    timestamp,
    modified   timestamp,
     PRIMARY KEY(id)
);

CREATE TABLE category(
   id           integer,
   description  varchar(50),
   created_by   integer REFERENCES cat_user,
   created      timestamp,
   modified     timestamp,
   PRIMARY KEY(id)
);

CREATE TABLE item(
    id          integer,
    description varchar(50),
    created_by  integer REFERENCES cat_user,
    created     timestamp,
    modified    timestamp,
    cat_id      integer REFERENCES category,
    PRIMARY KEY(id)
);



