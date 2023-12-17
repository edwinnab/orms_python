import sqlite3

DB_CONN = sqlite3.Connection("../db/wholesale.db")
DB_CURSOR = DB_CONN.cursor()
