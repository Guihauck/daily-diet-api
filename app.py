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

@app.route("/snack/<int:id_snack>", methods=['GET'])
def read_snack(id_snack):
    snack = Snack.query.get(id_snack)

    if snack:
        return jsonify({
            "message": "Refeição retornada com sucesso!",
            "snack": {
                "nome": snack.name,
                "descrição": snack.description,
                "hora": str(snack.time),
                "data": str(snack.date),
                "incluso": str(snack.included)
            }
        })
    
    return jsonify({"message": "Refeição não encontrada"}), 404

@app.route("/snack/<int:id_snack>", methods=['PUT'])
def update_snack(id_snack):
    data = request.json
    snack = Snack.query.get(id_snack)

    if snack:
        snack.name = data.get("name")
        snack.description = data.get("description")
        snack.time = datetime.strptime(data.get("time"), "%H:%M:%S").time()
        snack.date = datetime.strptime(data.get("date"), "%Y-%m-%d").date()
        snack.included = data.get("included")
        db.session.commit()
        return jsonify({"message": f"A refeição ID: {id_snack} foi alterada!"})
    
    return jsonify({"message": "A refeição não foi encontrada!"})

if __name__ == "__main__":
    app.run(debug=True)