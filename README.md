# Tournaments
## Description
This project work with PostgreSQL database to setup a database of tournament and generate Swiss-System tournament.

## What's included?
Tournament Project
- tournament.sql
- tournament.py
- tournament_test.py

### tournament.sql
This sql file sets up the tournament database schema like player, matches and views

### tournament.py
This python file contains methods to connect, read, add, delete players and matches
them into swiss-pairings.

### tournament_test.py
This python file has scripts to test the methods implemented in tournament.py file
 which are required for passing the tests.

## How to setup environment?
Follow the guidelines provided [here](https://docs.google.com/document/d/16IgOm4XprTaKxAa8w02y028oBECOoB1EI1ReddADEeY/pub?embedded=true)
Don't fork / Clone the git repo mentioned there, instead clone [this](https://github.com/ishanatmuz/fullstack-nanodegree-vm)

## How to execute tests?
After setting up the environment.
1. Navigate to the project folder `cd /vagrant/tournament`
2. Open psql like this `psql`
3. Initialize database like this `\i tournament.sql`
4. Quit and execute the test like this `python tournament_test.py`
5. Test results will be printed on the screen.