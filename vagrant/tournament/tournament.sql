-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


create table players (
  id serial NOT NULL PRIMARY KEY,
  name text NOT NULL ,
  wins INT,
  matches INT
);

create table matches (
  ID serial not null PRIMARY KEY,
  player1 int NOT NULL REFERENCES players (id),
  player2 int NOT NULL REFERENCES players (id),
  winner int NOT NULL CHECK (winner = player1 OR winner = player2)
);