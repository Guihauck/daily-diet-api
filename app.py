from flask import Flask, request, jsonify
from models.snack import Snack
from database import db
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
db.init_app(app)

@app.route("/snack", methods=['POST'])
def create_snack():
    data = request.json
    name = data.get("name")
    description = data.get("description")
    time = data.get("time")
    date = data.get("date")
    included = data.get("included")
    timeFormated = datetime.strptime(time, "%H:%M:%S").time()
    dateFormated = datetime.strptime(date, "%Y-%m-%d").date()

    if name:
        snack = Snack(name=name, description=description ,time=timeFormated, date=dateFormated, included=included)
        db.session.add(snack)
        db.session.commit()
        return jsonify({"message": "Refeição cadastrada com sucesso!"})
    
    return jsonify({"message": "Erro ao cadastrar a refeição!"}), 400

if __name__ == "__main__":
    app.run(debug=True)