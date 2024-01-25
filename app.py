from flask import Flask, request, redirect, render_template, flash
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "123456"

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.route('/')
def root():
    """Homepage redirects to list of pets."""

    return redirect("/pets")

@app.route('/pets')
def list_pets():
    """Show list of pets in the system."""
    pets = Pet.query.all()
    return render_template('pets.html', pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Pet add form; handle adding."""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect("/pets")

    else:
        return render_template(
            "pet_add_form.html", form=form)
    
@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Pet edit form; handle editing."""

    form = EditPetForm()
    pet_to_edit = Pet.query.get_or_404(pet_id)

    if form.validate_on_submit():
        photo_url = form.photo_url.data
        notes = form.notes.data
        available = form.available.data

        pet_to_edit.photo_url = photo_url
        pet_to_edit.notes = notes
        pet_to_edit.available = available

        db.session.commit()

        return redirect("/")

    else:
        return render_template("pet_edit_form.html", form=form, pet_to_edit=pet_to_edit)    
    

