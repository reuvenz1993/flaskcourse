from app import db,Puppy

# Create the tables in the database
# (Usually won't do it this way!)
db.create_all()

sam = Puppy('sammy',3)
frank = Puppy('frank',5)

print(sam.id)
print(frank.id)

db.session.add_all([sam,frank])

db.session.commit()

print(sam.id)
print(frank.id)