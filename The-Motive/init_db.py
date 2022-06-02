from listings import db
from listings.models.listing import Listing

# Clear it all out

db.drop_all()

# Set it back up

db.create_all()

# Seed data

l = Listing(title="Start", body="First", email="1@email.com")
db.session.add(l)
db.session.commit()
