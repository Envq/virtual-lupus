"""Implementation of the controller of the game"""
from model import Game

from flask import Flask, request
from flask.templating import render_template


# INITIALIZATION FLASK
app = Flask("virtual-lupus Game")

# INITIALIZATION CONTROLLER
app._game = Game()
app._numPlayers = None
app._players = None
app._roles = None


# FUNCTIONS
@app.route("/")
def home():
    """Home page"""

    return render_template("homePage.html")


@app.route("/setupGame")
def setupGame():
    """Setup gameplay"""
    app._numPlayers = 0
    app._players = list()
    app._roles = list()

    return render_template("setupGame.html")


@app.route("/setupPlayer", methods=["POST"])
def setupPlayer():
    """Startup player"""
    if request.method == "POST":
        app._numPlayers = request.form["numPlayers"]
        error = request.form["error"]
        for i in range(app._numPlayers):
            app._roles.append(request.form["role" + str(i)])
    
    return render_template("setupPlayer.html", error = error)


@app.route("/lobby", methods=["POST"])
def lobby():
    """Startup player"""
    if request.method == "POST":
        name = request.form["name"]

    if name not in app._players:
        return render_template("lobby.html", playerName = name)
    else:
        return render_template("setupPlayer.html")


@app.route("/gameplay", methods=["POST"])
def gameplay():
    """New Game"""
    if request.method == "POST":
        name = request.form["name"]

    app._game.initGame(app._players, app._roles)

    return render_template("role.html", role = app._game.getRole(name))



# MAIN
if __name__ == "__main__":
    app.run(debug=True)
    # http://localhost:5000/
