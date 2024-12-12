from flask import Flask, request, redirect, render_template, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

############################################################
# SETUP
############################################################

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/plantsDatabase"
mongo = PyMongo(app)

############################################################
# ROUTES
############################################################

@app.route('/')
def plants_list():
    """Display the plants list page."""
    # Fetch all plants from the 'plants' collection
    plants_data = mongo.db.plants.find()

    context = {
        'plants': plants_data,
    }
    return render_template('plants_list.html', **context)

@app.route('/about')
def about():
    """Display the about page."""
    return render_template('about.html')

@app.route('/create', methods=['GET', 'POST'])
def create():
    """Display the plant creation page & process data from the creation form."""
    if request.method == 'POST':
        # Safely get the form data
        plant_name = request.form.get('plant_name')
        variety = request.form.get('variety')
        photo_url = request.form.get('photo')
        date_planted = request.form.get('date_planted')

        # Check if any required fields are missing
        if not plant_name or not variety or not photo_url or not date_planted:
            return "Error: All fields are required!"

        # Prepare the plant object for insertion into MongoDB
        new_plant = {
            'name': plant_name,
            'variety': variety,
            'photo_url': photo_url,
            'date_planted': date_planted
        }

        # Insert the new plant into the database
        inserted_plant = mongo.db.plants.insert_one(new_plant)

        # Redirect to the details page of the new plant using the inserted ID
        return redirect(url_for('detail', plant_id=inserted_plant.inserted_id))

    # If it's a GET request, render the form for creating a new plant
    return render_template('create.html')


@app.route('/plant/<plant_id>')
def detail(plant_id):
    """Display the plant detail page & process data from the harvest form."""
    # Find the plant by its ObjectId
    plant_to_show = mongo.db.plants.find_one({'_id': ObjectId(plant_id)})

    # Fetch all harvests for this plant from the 'harvests' collection
    harvests = mongo.db.harvests.find({'plant_id': plant_id})

    context = {
        'plant': plant_to_show,
        'harvests': harvests
    }
    return render_template('detail.html', **context)

@app.route('/harvest/<plant_id>', methods=['POST'])
def harvest(plant_id):
    """
    Accepts a POST request with data for 1 harvest and inserts it into the database.
    """
    # Create a new harvest object with form data
    new_harvest = {
        'quantity': request.form['quantity'],  # e.g. '3 tomatoes'
        'date': request.form['date'],
        'plant_id': plant_id
    }

    # Insert the harvest into the 'harvests' collection
    mongo.db.harvests.insert_one(new_harvest)

    return redirect(url_for('detail', plant_id=plant_id))

@app.route('/edit/<plant_id>', methods=['GET', 'POST'])
def edit(plant_id):
    """Shows the edit page and accepts a POST request with edited data."""
    if request.method == 'POST':
        # Create the updated plant data from the form
        updated_plant = {
            'name': request.form['name'],
            'variety': request.form['variety'],
            'photo_url': request.form['photo_url'],
            'date_planted': request.form['date_planted']
        }

        # Update the plant in the database
        mongo.db.plants.update_one(
            {'_id': ObjectId(plant_id)},
            {'$set': updated_plant}
        )

        # Redirect to the plant detail page
        return redirect(url_for('detail', plant_id=plant_id))
    else:
        # Fetch the plant to edit from the database
        plant_to_show = mongo.db.plants.find_one({'_id': ObjectId(plant_id)})

        context = {
            'plant': plant_to_show
        }

        return render_template('edit.html', **context)

@app.route('/delete/<plant_id>', methods=['POST'])
def delete(plant_id):
    # Delete the plant from the 'plants' collection
    mongo.db.plants.delete_one({'_id': ObjectId(plant_id)})

    # Delete all harvests for this plant from the 'harvests' collection
    mongo.db.harvests.delete_many({'plant_id': plant_id})

    # Redirect back to the plants list
    return redirect(url_for('plants_list'))

if __name__ == '__main__':
    app.run(debug=True)
