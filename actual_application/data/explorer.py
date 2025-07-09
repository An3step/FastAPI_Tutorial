import sqlite3
from model.explorer import Explorer
from data.init import curs, conn, IntegrityError
from error.Web_Exceptions import Duplicate, Missing

curs.execute("""CREATE TABLE IF NOT EXISTS explorers
             (name TEXT PRIMARY KEY,
             description TEXT,
             country TEXT)""")

def row_to_model(row: tuple)->Explorer:
    name, description, country = row
    return Explorer(name=name, country=country, description=description)

def model_to_dict(explorer: Explorer)->dict:
    return explorer.model_dump()

def get_one(name: str)->Explorer:
    stmt = 'SELECT * FROM explorers where name=:name'
    curs.execute(stmt, {"name": name})
    row = curs.fetchone()
    if row is None:
        raise Missing(name, 'Explorer')
    return row_to_model(row)

def get_all()->list[Explorer]:
    stmt = 'SELECT * from explorers'
    curs.execute(stmt)
    rows = curs.fetchall()
    if rows is None:
        return []
    return [row_to_model(row) for row in rows]

def create(explorer: Explorer)->Explorer:
    stmt = """insert into explorers values
    (:name, :description, :country)"""
    try:
        curs.execute(stmt, model_to_dict(explorer))
    except IntegrityError:
        conn.rollback()
        raise Duplicate(explorer.name, 'Explorer')
    conn.commit()
    return get_one(explorer.name)

def modify(explorer: Explorer)->Explorer:
    stmt = """UPDATE explorers
                SET name=:name,
                country=:country,
                description=:description
                WHERE name=:name_orig"""
    params = model_to_dict(explorer)
    params['name_orig'] = explorer.name
    curs.execute(stmt, params)
    if curs.rowcount == 0:
        conn.rollback()
        raise Missing(explorer.name, 'Explorer')
    conn.commit()
    return get_one(explorer.name)

def delete(name: str)->Explorer:
    stmt = """DELETE FROM explorers
              WHERE name=:name
              RETURNING name, description, country"""
    if curs.rowcount == 0:
        conn.rollback()
        raise Missing(name, 'Explorer')
    conn.commit()
    return row_to_model(curs.fetchone())

