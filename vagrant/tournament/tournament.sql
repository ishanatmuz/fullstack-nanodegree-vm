-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament

create table players (
  id serial NOT NULL PRIMARY KEY,
  name text NOT NULL
);

create table matches (
  ID serial not null PRIMARY KEY,
  winner int NOT NULL REFERENCES players (id),
  loser int NOT NULL REFERENCES players (id) CHECK (loser != winner)
);

create view wins as
select players.id, players.name, count(matches.winner) as wins
from players full join matches on players.id = matches.winner
group by players.id, matches.winner
order by players.id, matches.winner;

create view losses as
select players.id, players.name, count(matches.loser) as losses
from players full join matches on players.id = matches.loser
group by players.id, matches.loser
order by players.id, matches.loser;

create view match as
select wins.id, wins.name, wins, losses, wins + losses as match
from wins, losses where wins.id = losses.id order by wins desc;
