from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/soma', methods=['GET'])
def soma():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        resultado = a + b
        return jsonify({"resultado":resultado})
    except (TypeError, ValueError):
        return jsonify({"erro": "Parâmetros inválidos"}), 400

if __name__ == '__main__':
    app.run(debug=True)
