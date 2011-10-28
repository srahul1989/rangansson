#!/usr/bin/env python

#
# A test script to practice SQLite statements
#
# References:
# SQLite Docs: http://www.sqlite.org/docs.html
# SQL Language syntax: http://www.sqlite.org/lang.html
# Syntax for expr: http://www.sqlite.org/lang_expr.html
# 


import sqlite3

conn = sqlite3.connect("rainfall")
conn.isolation_level = None
cursor = conn.cursor()

#TODO CHECK constraints are not working yet. link table has not been tested at all

cursor.execute("""CREATE TABLE IF NOT EXISTS people (id INTEGER PRIMARY KEY,
                                                        name TEXT NOT NULL,
                                                        birth INT,
                                                        death INT,
                                                        CONSTRAINT CHECK (death>=birth)""")

cursor.exeucte("""CREATE TABLE IF NOT EXISTS link (id INTEGER PRIMARY KEY,
                                                    left_side INTEGER,
                                                    right_side INTEGER,
                                                    relation TEXT,
                                                    CONSTRAINT FOREIGN KEY (left_side) REFERENCES people(id),
                                                    CONSTRAINT FOREIGN KEY (right_side) REFERENCES people(id),
                                                    CONSTRAINT CHECK (left_side != right_side))""")


immediate_family = [(None, 'Harshavardhan', 19860320, None),
                    (None, 'Rangan', 19580710, None),
                    (None, 'Chitra', 19600427, None),
                    (None, 'Ankit', 19990821, None),]


cursor.executemany("""INSERT INTO people VALUES (?,?,?,?)""", immediate_family)
