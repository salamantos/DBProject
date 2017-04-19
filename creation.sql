-- Database: "AprilFoolsJokes"

--drop table relationship; drop table stories; drop table results; drop table jokes; drop table people;

CREATE TABLE people(
	id 			int 			PRIMARY KEY,
	name 		varchar(100) 	NOT NULL
);

CREATE TABLE jokes(
	id 			int 			PRIMARY KEY,
	title 		varchar(100) 	DEFAULT '',
	date 		date,
	from_who 	int 			REFERENCES people(id),
	to_who 		int 			REFERENCES people(id)
);
	
CREATE TABLE relationship(
	person1 	int 			REFERENCES people(id),
	person2		int 			REFERENCES people(id),
	rel 		varchar(100) 	NOT NULL
);
	
CREATE TABLE stories(
	joke_id 	int 			REFERENCES jokes(id),
	text 		text 			NOT NULL DEFAULT ''
);

CREATE TABLE results(
	joke_id 	int 			REFERENCES jokes(id),
	rating 		int 			NOT NULL,
	comment 	text 			DEFAULT ''
);