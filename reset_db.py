# This file drops/deletes all the existing tables and data created and creates new tables according to the table models in database.py.
# Use only when previous data is not required
from database import Base, engine

Base.metadata.drop_all(bind=engine)
print("All tables dropped.")

# Recreate all tables based on the updated models
Base.metadata.create_all(bind=engine)
print("All tables recreated.")
