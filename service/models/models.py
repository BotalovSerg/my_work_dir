from sqlalchemy import Column, Integer, String


from database.connection import Base


class Staff(Base):
    __tablename__ = "company_staff"

    id = Column(Integer, primary_key=True, index=True)
    last_name = Column(String)
    first_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)