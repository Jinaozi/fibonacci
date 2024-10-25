from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_term = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_term)
    return fib_sequence[:n]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    value = int(request.form['value'])
    action = request.form['action']
    
    if action == 'sequence':
        result = fibonacci(value)
        return jsonify({'result': result})
    elif action == 'spiral':
        # Spiral logic can be added here if needed
        return jsonify({'message': 'Spiral generation not implemented yet.'})

if __name__ == '__main__':
    app.run(debug=True)