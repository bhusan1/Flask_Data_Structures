from flask import Flask, render_template

app = Flask(__name__)

class GalileanMoons:
    def __init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth

@app.route("/data_structures")
def render_data_structures():

    movies = [
        "Avatar",
        "Gangs of Wasseypur",
        "3 idiots"
    ]

    car = {
        "brand" : "Tesla",
        "model" : "Model2",
        "year" : "2022",
    }

    moons = GalileanMoons("Io", "Europa", "Ganymede", "Callisto")

    ## Alternate way: we can add these in kwargs 
    """
        kwargs = {
            "movies" : movies,
            "car" : car,
            "moons" : moons
        }
    """
    ## and call it in render_template as **kwargs

    return render_template("data_structures.html",
     movies=movies, car=car, moons=moons)