from flask import Flask, request, jsonify, render_template
from ski import Ski
from snowboard import Snowboard

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ski', methods=['POST'])
def ski_recommend():
    data = request.json
    try:
        ski = Ski(
            height=data.get('height'),
            weight=data.get('weight'),
            shoe_size=data.get('shoe_size'),
            skill_level=data.get('skill_level'),
            terrain=data.get('terrain'),
            style=data.get('style'),
            preferred_type=data.get('preferred_type'),
            age=data.get('age')
        )
        recommendation = ski.recommend()
        return jsonify({"success": True, "recommendation": recommendation})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@app.route('/snowboard', methods=['POST'])
def snowboard_recommend():
    data = request.json
    try:
        board = Snowboard(
            height=data.get('height'),
            weight=data.get('weight'),
            shoe_size=data.get('shoe_size'),
            skill_level=data.get('skill_level'),
            terrain=data.get('terrain'),
            style=data.get('style'),
            preferred_type=data.get('preferred_type'),
            age=data.get('age')
        )
        recommendation = board.recommend()
        return jsonify({"success": True, "recommendation": recommendation})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
