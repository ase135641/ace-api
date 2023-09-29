from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/temp', methods=['GET'])
def convert_temperature():
    celsius_str = request.args.get('celsius')
    if celsius_str is None:
        return jsonify({'error': 'Celsius parameter is missing'}), 400

    try:
        celsius = float(celsius_str)
        kelvin = celsius + 273.15
        response = {
            'kelvin': kelvin,
            'celsius': celsius
        }
        return jsonify(response)
    except ValueError:
        return jsonify({'error': 'Invalid value for Celsius parameter'}), 400


@app.route('/api/prime', methods=['GET'])
def generate_primes():
    limit = int(request.args.get('limit'))

    def sieve_eratosthenes(n):
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        primes = []
        for p in range(2, int(n**0.5) + 1):
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
        for i in range(2, n + 1):
            if is_prime[i]:
                primes.append(i)
        return primes

    primes = sieve_eratosthenes(limit)
    response = {'primes': primes}
    return jsonify(response), 200, {'Content-Type': 'application/json; charset=utf-8', 'indent': 2}


@app.route('/api/number', methods=['GET'])
def calculate_number():
    n = int(request.args.get('n'))
    
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(n - 1):
                a, b = b, a + b
            return b
    
    number = fibonacci(n)
    response = {'number': number}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
