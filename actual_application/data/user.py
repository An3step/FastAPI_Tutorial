from data.init import conn, curs, IntegrityError
from error.Web_Exceptions import Duplicate, Missing
from model.user import User

curs.execute("""CREATE TABLE IF NOT EXISTS users
                (name TEXT PRIMARY KEY,
                hashed_password TEXT)""")

curs.execute("""CREATE TABLE IF NOT EXISTS xusers
             (name TEXT PRIMARY KEY,
             hashed_password TEXT)""")

def row_to_model(row: tuple)->User:
    name, hashed_password = row
    return User(name=name, hashed_password=hashed_password)

def model_to_dict(user: User)->dict:
    return user.model_dump()

def get_one(name: str)->User:
    stmt = "SELECT * FROM users WHERE name=:name"
    curs.execute(stmt, {"name": name})
    row = curs.fetchone()
    if row is None:
        raise Missing(name, 'User')
    return row_to_model(row)

def get_all()->list[User]:
    stmt = 'SELECT * FROM users'
    curs.execute(stmt)
    rows = curs.fetchall()
    if rows is None:
        return []
    return [row_to_model(rows) for row in rows]

def create(user: User, table: str = "users")->User:
    """Добавление пользователя в таблицу user или xuser"""
    stmt = f"""INSERT into {table}
              (name, hashed_password)
              VALUES
              (:name, :hashed_password)"""
    try:
        curs.execute(stmt, model_to_dict(user))
        conn.commit()
        return get_one(user.name)
    except IntegrityError:
        conn.rollback()
        raise Duplicate(user.name, f"Among {table} User")

def modify(name: str, user: User)->User:
    stmt = f"""UPDATE TABLE users
              SET name=:name, hashed_password=:hashed_password
              WHERE name={name}"""
    curs.execute(stmt, model_to_dict(user))
    if curs.rowcount == 0:
        raise Missing(name, "User")
    return get_one(user.name)

def delete(name: str)->User:
    stmt = """DELETE FROM users
              WHERE name=:name
              RETURNING name, hashed_password"""
    curs.execute(stmt, {"name": name})
    if curs.rowcount == 0:
        raise Missing(name, f"User")
    return create(row_to_model(curs.fetchone()), table = 'xusers')