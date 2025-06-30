from flask import Flask, render_template, request

app = Flask(__name__)

def factorial(n):
    a = 1
    for i in range(1, n + 1):
        a *= i
    return a

@app.route('/factorial', methods=['GET', 'POST'])
def index1():
    result = None
    if request.method == 'POST':
        try:
            number1 = request.form.get('number1')
            number2 = request.form.get('number2') 
            if number1:
                number = int(number1)
                result = factorial(number)
            elif number2:
                number = int(number2)
                result = factorial(number)
        
        except:
            result = ("Invalid input")
    else:
         try:
            number = int(request.args.get('number', ''))
            result = factorial(number)
         except:
            result = ("Invalid input")
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
