from flask import Flask, render_template, request, redirect
from random import randint

app = Flask(__name__)

'''
Note: this sample code does NOT store the dogs data to a database.
Instead, we store the dogs data in memory in the below "dogs" Python object.
Consequently, the dogs data is reset every time the application is restarted.
If you would like, you can replace this dogs data structure with your own database connection logic.
'''

dogs = [
    {
        "id": 1,
        "name": "Spot",
        "breed": "Boston Terrier",
        "age": 2,
        "photo_name": "dog_1.jpg",
        "available_for_adoption": True
    },
    {
        "id": 2,
        "name": "Pixie",
        "breed": "Pug",
        "age": 7,
        "photo_name": "dog_2.jpg",
        "available_for_adoption": True
    },
    {
        "id": 3,
        "name": "Ellie",
        "breed": "Golden Retriever",
        "age": 3,
        "photo_name": "dog_3.jpg",
        "available_for_adoption": True
    }
]


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/dogs', methods=['GET'])
@app.route('/dogs/<dog_id>', methods=['GET'])
def all_dogs(dog_id=None):
    if dog_id:  # show single dog
        single_dog = [dogs[int(dog_id)]] if len(dogs)-1 >= int(dog_id) else []
        return render_template('dogs.html', dogs=single_dog)
    else:  # show all dogs
        return render_template('dogs.html', dogs=dogs)


@app.route('/random-dog', methods=['GET'])
def random_dog():
    random_dog_index = randint(0, len(dogs)-1)  # generate a random index in the dogs array
    random_dog = dogs[random_dog_index]
    return render_template('random_dog.html', dog=random_dog)


@app.route('/create-dog', methods=['GET', 'POST'])
def create_dog():
    dog_name = request.form['dog_name']
    dog_breed = request.form['dog_breed']
    dog_age = request.form['dog_age']
    dog_is_available_for_adoption = True

    new_dog = {
        "id": len(dogs),
        "name": dog_name,
        "breed": dog_breed,
        "age": dog_age,
        "photo_name": "placeholder_dog.png",
        "available_for_adoption": dog_is_available_for_adoption
    }

    dogs.append(new_dog)

    return redirect('/dogs')


if __name__ == "__main__":
    app.run(debug=True)
