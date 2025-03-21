from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://postgresuser:developer@localhost:5432/temporary"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

# Define the declarative base
Base = declarative_base()

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to create tables explicitly
def init_db():
    Base.metadata.create_all(bind=engine)
