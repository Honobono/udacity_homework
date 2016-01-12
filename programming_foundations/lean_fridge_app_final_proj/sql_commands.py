import sqlite3
db = sqlite3.connect('lean_fridge.db')
c = db.cursor()

def itemTable():
    c.execute("CREATE TABLE itemProperty(ID INT, name varchar(20), dates varchar(10), count INT, category varchar(20), note varchar(50))")

def dataInsert():
    c.execute("INSERT INTO itemProperty VALUES(1, 'apple', '2015-01-11', 3, 'fruit', 'Fuji organic apples')")
    c.execute("INSERT INTO itemProperty VALUES(2, 'orange', '2015-01-10', 4, 'fruit', 'for smoothies')")
    c.execute("INSERT INTO itemProperty VALUES(3, 'banana', '2015-01-09', 6, 'fruit', 'for breakfast')")
    c.execute("INSERT INTO itemProperty VALUES(4, 'yogurt', '2015-01-09', 2, 'diary', 'on sale')")
    c.execute("INSERT INTO itemProperty VALUES(5, 'pasta', '2015-01-01', 2, 'grain', 'on sale, 2 bulks')")
    c.execute("INSERT INTO itemProperty VALUES(6, 'carrot', '2015-01-10', 6, 'vegetable', 'carrot sticks or stew')")
    c.execute("INSERT INTO itemProperty VALUES(7, 'potato', '2015-01-02', 5, 'vegetable', 'eat before sprouted, purple potatoes')")
    c.execute("INSERT INTO itemProperty VALUES(8, 'celery', '2015-01-03', 4, 'vegetable', '4 stalks')")
    c.execute("INSERT INTO itemProperty VALUES(9, 'tomato', '2015-01-04', 8, 'vegetable', 'romano tomatoes, small')")
    c.execute("INSERT INTO itemProperty VALUES(10, 'almond milk', '2015-01-05', 2, 'diary', 'expires in 2 weeks')")
    db.commit()

def stockTable():
    c.execute("CREATE TABLE stock(ID INT, name varchar(20), sum INT)")

def dataInsert():
    c.execute("INSERT INTO stock VALUES(1, 'apple', 3)")
    db.commit()


