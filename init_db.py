from motive.models.user import db, User

# Clear it all out

db.drop_all()

# Set it back up

db.create_all()

# Seed data

