#!/usr/bin/python3

"""
 writing a Mysqldb script


"""
import MySQLdb
import sys
"""
importing Mysqldb module and sys function as an argumeent vector
"""


def fiLter():
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
                         port=3306)

    cux = db.cursor()
    xix = sys.argv[4]
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY states.id"

    cux.execute(query, (xix.encode('utf-8'),))

    states = cux.fetchall()

    for i in states:
        print(i)

    db.close()


if __name__ == "__main__":
    fiLter()
