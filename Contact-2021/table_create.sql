CREATE TABLE data (
    contact_id  integer CONSTRAINT firstkey PRIMARY KEY NOT NULL,
    lastname    varchar(50),
    firstname   varchar(100), 
    address     varchar(300),
    phonenumber varchar(50),
    email       varchar(100),
    addinform   varchar(500),
    dt          varchar(50),
    d           varchar(20),
    url_photo   varchar(100),
    img         varchar(80)
);