CREATE TABLE Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT
)

CREATE TABLE Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    tilte TEXT,
    artist_id INTEGER,
    genre_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
)

insert into Artist (name) values ('Led Zepplin')
insert into Artist (name) values ('AC/DC')

insert into Genre (name) values ('Rock');
insert into Genre (name) values ('Metal');