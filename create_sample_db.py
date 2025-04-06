import sqlite3
import os
import random

with sqlite3.connect("demo.db") as con:
	con.execute(
		"CREATE TABLE kv (key BLOB PRIMARY KEY NOT NULL, value BLOB NOT NULL) WITHOUT ROWID, STRICT"
	)
	for i in range(1000):
		con.execute(
			"INSERT INTO kv (key, value) VALUES (?, ?)",
			(
				os.urandom(random.randint(4, 10)),
				os.urandom(random.randint(4, 20)),
			),
		)
	con.commit()
