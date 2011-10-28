#!/usr/bin/env python

#TODO Remove this file before deployment

# A minimal SQLite shell for experiments

import sqlite3

conn = sqlite3.connect(":memory:")
conn.isolation_level = None
cursor = conn.cursor()

buffer = ""

print "Enter your SQL commands to execute in sqlite3."
print "Enter a blank line to exit."

while True:
    line = raw_input()
    if line == "":
        break
    buffer += line
    if sqlite3.complete_statement(buffer):
        try:
            buffer = buffer.strip()
            cursor.execute(buffer)

            if buffer.lstrip().upper().startswith("SELECT"):
                print cursor.fetchall()
        except sqlite3.Error, e:
            print "An error occurred:", e.args[0]
        buffer = ""

conn.close()
