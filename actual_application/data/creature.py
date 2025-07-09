import sqlite3
from model.creature import Creature
from data.init import curs, conn, IntegrityError
from error.Web_Exceptions import Duplicate, Missing

curs.execute("""CREATE TABLE IF NOT EXISTS creatures
             (name TEXT PRIMARY KEY,
             description TEXT,
             country TEXT,
             area TEXT,
             aka TEXT)""")

def row_to_model(row: tuple)->Creature:
    name, description, country, area, aka = row
    return Creature(name=name, description=description, country=country, area=area, aka=aka)

def model_to_dict(creature: Creature)->dict:
    return creature.model_dump()

def get_one(name: str)->Creature | None:
    stmt = 'SELECT * FROM creatures where name=:name'
    curs.execute(stmt, {"name": name})
    row = curs.fetchone()
    if row is None:
        raise Missing(name, 'Creature')
    return row_to_model(row)

def get_all()->list[Creature]:
    stmt = 'SELECT * from creatures'
    curs.execute(stmt)
    rows = curs.fetchall()
    if rows is None:
        return []
    return [row_to_model(row) for row in rows]

def create(creature: Creature)->Creature:
    stmt = """insert into creatures values
    (:name, :description, :country, :area, :aka)"""
    try:
        curs.execute(stmt, model_to_dict(creature))
    except IntegrityError:
        conn.rollback()
        raise Duplicate(creature.name, 'Creature')
    conn.commit()
    return get_one(creature.name)

def modify(creature: Creature)->Creature:
    stmt = """UPDATE creatures
                SET name=:name,
                country=:country,
                area=:area,
                aka=:aka
                WHERE name=:name_orig"""
    params = model_to_dict(creature)
    params['name_orig'] = creature.name
    curs.execute(stmt, params)
    if curs.rowcount == 0:
        conn.rollback()
        raise Missing(creature.name, 'Creature')
    conn.commit()
    return get_one(creature.name)

def delete(name: str)->Creature:
    stmt = """DELETE FROM creatures
              WHERE name=:name
              RETURNING name, country, area, description, aka"""
    curs.execute(stmt, {"name": name})
    if curs.rowcount == 0:
        conn.rollback()
        raise Missing(name, 'Creature')
    conn.commit()
    return row_to_model(curs.fetchone())

