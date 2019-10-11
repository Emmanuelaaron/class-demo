import psycopg2

connection = psycopg2.connect("dbname=example user=postgres host=localhost password=comforter")

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table2;')

cursor.execute('''
    CREATE TABLE table2(
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT False
    );
''')

cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (1, True))
cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (2, True))
cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (3, True))

cursor.execute('SELECT * from table2;')
result = cursor.fetchmany(2)
print('fetchmany(2)', result)
result2 = cursor.fetchone()
print('fetchone', result2)


connection.commit()

connection.close()

