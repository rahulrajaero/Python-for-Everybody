import json
import sqlite3

filename = 'roster_data.json'

conn = sqlite3.connect('db.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

CREATE TABLE User (
  id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  name  TEXT UNIQUE
);

CREATE TABLE Course (
  id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  title  TEXT UNIQUE
);

CREATE TABLE Member (
  user_id   INTEGER,
  course_id INTEGER,
  role      INTEGER,
  PRIMARY KEY (user_id, course_id)
);
''')

json_data = json.loads(open(filename).read())
#name, course, role
counter = 0
for entry in json_data:
  name = entry[0]
  title = entry[1]
  role = entry[2]
  
  cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name,))
  cur.execute('SELECT id FROM User WHERE name = ?', (name,))
  user_id = cur.fetchone()[0]
  
  cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (title,))
  cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
  course_id = cur.fetchone()[0]
  
  cur.execute('INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES (?, ?, ?)', (user_id, course_id, role))
  
  if counter == 10:
    conn.commit()
    counter = 0
  else:
    counter += 1

cur.execute('SELECT hex(User.name || Course.title || Member.role) AS X FROM User JOIN Member JOIN Course ON User.id = Member.user_id AND Member.course_id = Course.id ORDER BY X')
result = cur.fetchone()
print(result)