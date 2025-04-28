from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET', 'POST'])
def predict():
    a = float(request.args.get('a', 0) or request.json.get('a', 0))
    b = float(request.args.get('b', 0) or request.json.get('b', 0))
    suma = a + b
    prediction = 1 if suma > 5.8 else 0
    return jsonify({
        "prediction": prediction,
        "features": {
            "a": a,
            "b": b,
            "sum": suma
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)