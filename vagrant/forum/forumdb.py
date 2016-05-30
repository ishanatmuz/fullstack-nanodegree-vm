#
# Database access functions for the web forum.
# 

import time
import psycopg2
import bleach

## Get posts from database.
def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    ## Database connection
    db = psycopg2.connect("dbname=forum")
    cursor = db.cursor()
    query = "SELECT content, time FROM posts ORDER BY TIME DESC"
    cursor.execute(query)
    rows = cursor.fetchall()
    posts = [{'content': str(row[1]), 'time': str(row[0])} for row in rows]
    db.close()
    return posts

## Add a post to the database.
def AddPost(content_text):
    '''Add a new post to the database.

    Args:
      content_text: The text content of the new post.
    '''
    time_stamp = time.strftime('%c', time.localtime())
    ## Database connection
    db = psycopg2.connect("dbname=forum")
    cursor = db.cursor()
    query = "insert into posts (content, time) values (%s, %s);"
    data = (bleach.clean(content_text), time_stamp,)
    cursor.execute(query, data)
    db.commit()
    db.close()