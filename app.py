from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        print(f"Name: {name}, Email: {email}, Phone: {phone}")
        return render_template('index.html', message="Form submitted successfully!")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)