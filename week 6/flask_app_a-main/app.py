from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Route for the home page (index.html)
@app.route('/')
def home_page():
    return render_template('index.html')

# Route for performing math operations based on form data (POST method)
@app.route('/math', methods=['POST'])
def math_ops():
    if request.method == 'POST':
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        
        if ops == 'add':
            r = num1 + num2
            result = "The sum of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        elif ops == 'subtract':
            r = num1 - num2
            result = "The difference of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        elif ops == 'multiply':
            r = num1 * num2
            result = "The product of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        elif ops == 'divide':
            r = num1 / num2
            result = "The division of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        else:
            result = "Invalid operation"

        return render_template('results.html', result=result)


# Route for performing math operations based on JSON data (POST method)
@app.route('/postman_action', methods=['POST'])
def math_ops1():
    if request.method == 'POST':
        ops = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        
        if ops == 'add':
            r = num1 + num2
            result = "The sum of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        elif ops == 'subtract':
            r = num1 - num2
            result = "The difference of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        elif ops == 'multiply':
            r = num1 * num2
            result = "The product of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        elif ops == 'divide':
            r = num1 / num2
            result = "The division of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        else:
            result = "Invalid operation"

        return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0")