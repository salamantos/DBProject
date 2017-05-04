-- Database: "AprilFoolsJokes"

--drop table relationship; drop table stories; drop table results; drop table jokes; drop table people;

CREATE TABLE people(
	id		INTEGER			PRIMARY KEY,
	name 		VARCHAR(100) 		NOT NULL
);

CREATE TABLE jokes(
	id 		INTEGER			PRIMARY KEY,
	title 		VARCHAR(100)		DEFAULT '',
	from_who 	INTEGER			REFERENCES people(id),
	text 		TEXT        		NOT NULL DEFAULT ''
);
	
CREATE TABLE relationship(
	person1 	INTEGER			REFERENCES people(id),
	person2		INTEGER			REFERENCES people(id),
	rel 		VARCHAR(100)		NOT NULL
);
	
CREATE TABLE people_get_joke(
	people_id 	INTEGER			REFERENCES people(id),
	joke_id 	INTEGER 		REFERENCES jokes(id)
);

CREATE TABLE results(
	joke_id 	INTEGER			PRIMARY KEY REFERENCES jokes(id),
	rating 		INTEGER			NOT NULL,
	comment 	TEXT 			DEFAULT ''
);