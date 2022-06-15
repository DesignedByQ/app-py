from application import app, db
from application.models import Games

@app.route('/add/<gname>')
def add(gname):
    new_game = Games(name=gname)
    db.session.add(new_game)
    db.session.commit()
    return gname + " " + "Added to database"

@app.route('/read')
def read():
    all_games = Games.query.all()
    games_string = ""
    for game in all_games:
        games_string += "<br>"+ game.name
    return games_string

@app.route('/update/<oldname>/<newname>')
def update(oldname, newname):
    first_game = Games.query.filter_by(name=oldname).first()
    first_game.name = newname
    db.session.commit()
    return first_game.name

@app.route('/delete/<product>')
def delete(product):
    to_be_del = Games.query.filter_by(name=product).first()
    db.session.delete(to_be_del)
    db.session.commit()
    return 'First item deleted'