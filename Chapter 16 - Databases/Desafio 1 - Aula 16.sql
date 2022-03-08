CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
)

DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Queenie', 21);
INSERT INTO Ages (name, age) VALUES ('Pardeepraj', 32);
INSERT INTO Ages (name, age) VALUES ('Jude', 23);
INSERT INTO Ages (name, age) VALUES ('Fynn', 33);

SELECT hex(name || age) AS X FROM Ages ORDER BY X
