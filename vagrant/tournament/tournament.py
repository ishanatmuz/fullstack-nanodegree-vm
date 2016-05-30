#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    cursor = db.cursor()
    query = "TRUNCATE matches CASCADE"
    cursor.execute(query)
    query = "UPDATE players set wins = 0, matches = 0"
    cursor.execute(query)
    db.commit()
    db.close()

def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    cursor = db.cursor()
    query = "truncate players CASCADE "
    cursor.execute(query)
    db.commit()
    cursor
    db.close()

def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    cursor = db.cursor()
    query = "select count(*) as len from players"
    cursor.execute(query)
    rows = cursor.fetchall()
    # print rows
    db.close()
    return int(rows[0][0])

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    cursor = db.cursor()
    query = "INSERT INTO players (name, wins, matches) VALUES (%s, %s, %s)"
    data = (bleach.clean(name), 0, 0,)
    cursor.execute(query, data)
    db.commit()
    db.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    cursor = db.cursor()
    query = "SELECT id, name, wins, matches from players order by wins desc"
    cursor.execute(query)
    rows = cursor.fetchall()
    standings = [(int(row[0]), str(row[1]), int(row[2] or 0), int(row[3] or 0)) for row in rows]
    db.close()
    return standings

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    cursor = db.cursor()
    query = "INSERT INTO matches(player1, player2, winner) VALUES (%s, %s, %s)"
    data = (winner, loser, winner,)
    cursor.execute(query, data)
    query = "UPDATE players set wins = wins + 1, matches = matches + 1 where id = %s"
    data = (winner,)
    cursor.execute(query, data)
    query = "UPDATE players set matches = matches + 1 where id = %s"
    data = (loser,)
    cursor.execute(query, data)
    db.commit()
    db.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    pairs = []
    standings = playerStandings()
    numberOfPairs = len(standings) / 2
    for i in xrange(numberOfPairs):
        player1 = standings[2 * i]
        player1id = player1[0]
        player1name = player1[1]
        player2 = standings[(2 * i) + 1]
        player2id = player2[0]
        player2name = player2[1]
        pairs.append((player1id, player1name, player2id, player2name))

    return pairs