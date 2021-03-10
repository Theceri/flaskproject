from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    my_name = 'Theceri'
    my_dict = {'Name' : 'Paul Theceri', 'Age' : 'Advanced', 'Location' : 'Roysambu', 'Date of birth' : 'The olden days'}
    my_list = ('Ducati', 'Husqvarna', 'Yamaha', 'Honda', 'Kawasaki', 'Suzuki', 'Aprilia', 'Royal Enfield', 'Bee Em Dablew', 'Harley Davidson', 'Triumph', 'Norton', 'Benelli', 'KTM')
    age = 18
    return render_template('index.html', my_name = my_name, my_dict=my_dict, my_list=my_list, age=age)