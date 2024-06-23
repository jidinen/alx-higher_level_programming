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
    cux.execute("SELECT id, name FROM states")

    states = cux.fetchall()

    for i in states:
        if (i[1][0] == "N"):
            print(i)
   

    db.close()


if __name__ == "__main__":
    fiLter()
