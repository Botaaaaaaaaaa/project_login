from .sql_pro import User,Notes,session
from sqlalchemy import select,insert,update,delete
from .sql_pro import *

def get_user(login,password):
    stmt = select(User).where(User.login == login and User.password == password)
    res = session.execute(stmt)
    return res.scalars().one_or_none()
    
def add_user(login,password):
    stmt = insert(User).values(login=login, password=password)
    session.execute(stmt)
    session.commit()

def add_note(user_id,title,content):
    stmt = insert(Notes).values(user_id = user_id,title=title, content=content)
    session.execute(stmt)
    session.commit()

def update_note(note_id,title,content):
    stmt = (
        update(Notes).
        where(Notes.note_id == note_id).
        values(title=title,content=content)
    )
    session.execute(stmt)
    session.commit()

def get_all_notes_by_user(user_id):
    stmt = select(Notes).where(Notes.user_id == user_id)

    res = session.execute(stmt)
    return res.scalars().fetchall()

def get_user_by_id(id: int) -> User:
    stmt = select(User).where(User.user_id==id)

    res = session.execute(stmt)
    return res.scalars().one_or_none()

def get_note_by_id(note_id: int) -> Notes|None:
    stmt = select(Notes).where(Notes.note_id==note_id)

    res = session.execute(stmt)
    return res.scalars().one_or_none()

def get_all_notes_by_user(user_id):
    stmt = select(Notes).where(Notes.user_id==user_id)

    res = session.execute(stmt)
    return res.scalars().fetchall()

def get_last_note_id():
    stmt =select(Notes).order_by(Notes.updated_at.desc()).limit(1)
    note = session.execute(stmt)
    session.commit()
    return note.scalars().one_or_none().note_id


def delete_note(note_id):
    stmt = delete(Notes).where(Notes.note_id == note_id)

    session.execute(stmt)
    session.commit()