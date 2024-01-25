from models import db, Pet
from app import app

with app.app_context():
    db.drop_all()
    db.create_all()

    Pet.query.delete()

    finn = Pet(name='Finn', species="Lab", photo_url='https://i.postimg.cc/vHQTT0N0/finn.jpg', age='8', notes='Scared of everything', available=True)
    rey = Pet(name='Rey', species="Pit", photo_url='https://i.postimg.cc/13VQ36sW/Rey.jpg', age='7', notes='Ball is life', available=True)
    barb = Pet(name='Barb', species="Shiba Inu", photo_url='https://plus.unsplash.com/premium_photo-1668208365386-4198381c6f6e?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', age='31', notes='BAE', available=True)

    db.session.add_all([finn, rey, barb])
    db.session.commit()



