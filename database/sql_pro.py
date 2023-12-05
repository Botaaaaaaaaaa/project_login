from sqlalchemy import create_engine,Column,Integer,String,Sequence,Text,ForeignKey,TIMESTAMP, func
from sqlalchemy.orm import sessionmaker,relationships
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import insert,select

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'User'
    user_id = Column(Integer, primary_key= True)
    login = Column(String(50))
    password = Column(String(50))



class Notes(Base):
    __tablename__ = 'Note'
    note_id  = Column(Integer, primary_key= True)
    title = Column(String(50))
    content = Column(Text)

    user_id = Column(Integer, ForeignKey('User.user_id'))

    updated_at =Column(
        TIMESTAMP,server_default = func.now(),onupdate = func.current_timestamp()
    )

    def __repr__(self):
        return f"Note: {self.note_id} for {self.user_id},Title: {self.title}"
    
engine = create_engine('postgresql://postgres:admin@localhost:5433/Notes')

Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)
session = Session()

def insert_user():
    stmt = (
        insert(User).
        values(user_id=1,login='bota@gmail.com', password ='12345')
    )
    session.execute(stmt)
    session.commit()

def select_user():
    stmt = select(User).where(User.user_id == id)
    user = session.execute(stmt)
    print(user.scalar().one_or_none)

def insert_notes():
    stmt = (
        insert(Notes).
        values(note_id=1,title='Hello world!', content ='Life is wonderful, Is not it?')
    )
    session.execute(stmt)
    session.commit()