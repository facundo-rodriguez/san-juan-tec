
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

def conexion(Base):
    engine = create_engine("mysql+mysqlconnector://ufbukk5zlb3qoenn:Z9D11yLSLrBSexLhQLoy@bakq3vchlgx0itfy4wqc-mysql.services.clever-cloud.com:3306/bakq3vchlgx0itfy4wqc?charset=utf8mb4",echo=False)
    Base.metadata.create_all(engine)
    session=Session(engine)

    return session