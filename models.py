import sqlite3 as sql


def insertUser(name, email, password):
    try:
        connect = sql.connect("database.db")
        cursor = connect.cursor()
        cursor.execute(
            "INSERT INTO users (name,email,password) VALUES (?,?,?)",
            (name, email, password),
        )
        connect.commit()
        connect.close()
        return True
    except Exception as e:
        print(e)
        return False


def retrieveUsers(email):
    try:
        connect = sql.connect("database.db")
        cursor = connect.cursor()
        cursor.execute("SELECT name,email FROM users WHERE email=?", [email])
        users = cursor.fetchone()
        connect.close()
        return users
    except Exception as e:
        return False


def checkDuplicate(email):
    connect = sql.connect("database.db")
    cursor = connect.cursor()
    cursor.execute("SELECT email FROM users WHERE email=?", [email])
    email = cursor.fetchone()
    connect.close()
    return email


def checkPassword(password, email):
    connect = sql.connect("database.db")
    cursor = connect.cursor()
    cursor.execute("SELECT password FROM users WHERE email=?", [email])
    passw = cursor.fetchone()
    connect.close()
    return passw


def delete():
    try:
        connect = sql.connect("database.db")
        cursor = connect.cursor()
        cursor.execute("DELETE FROM users")
        connect.close()
        return True
    except Exception as e:
        return False
