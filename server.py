# flask --app data_server run
from flask import Flask
from flask import render_template
import json


app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    #load a current view of the data
    f = open("data/life_expectancy.json", "r")
    data = json.load(f)
    f.close()

    canada = data["Canada"]
    mexico = data["Mexico"]
    usa = data["United States"]
    years = sorted(data["Canada"].keys())
    canada_line_endpoints =[]
    mexico_line_endpoints =[]
    usa_line_endpoints =[]
    print("canada",canada)
    years = sorted(data["Canada"].keys())
    increment_years = []

    for year in range(0, len(years), 10):
        increment_years.append(years[year])

    yearAmt = (len(years))*3
    canada_life = 0
    mexico_life = 0
    usa_life = 0

    for life_amt in (data["Canada"].values()):
        canada_life+=life_amt 
    for life_amt in (data["Mexico"].values()):
        mexico_life+=life_amt 
    for life_amt in (data["United States"].values()):
        usa_life+=life_amt 
    universalAvg = (canada_life + mexico_life + usa_life)/yearAmt
    print("universalAvg", universalAvg)

    

    for i in range(len(increment_years)-1): # make it easy to dynamically generate a line graph
        start_x = increment_years[i] #generate endpoints for each line segment
        stop_x = increment_years[i+1]
        canada_line_endpoints.append([canada[start_x],canada[stop_x]])
        mexico_line_endpoints.append([mexico[start_x],mexico[stop_x]])
        usa_line_endpoints.append([usa[start_x],usa[stop_x]])

    print("c_e",canada_line_endpoints)
    return render_template('index.html', years = sorted(data["Canada"].keys()), increment_years = increment_years, canada_endpoints = canada_line_endpoints, mexico_endpoints = mexico_line_endpoints, usa_endpoints = usa_line_endpoints)

@app.route('/map/?year=<year>')
def year(year):
    #load a current view of the data
    f = open("data/life_expectancy.json", "r")
    data = json.load(f)
    f.close()

    canada = data["Canada"]
    mexico = data["Mexico"]
    usa = data["United States"]

    requested_year = year 

    print("year", year)



   


    return render_template('year.html', years = sorted(data["Canada"].keys()), requested_year = requested_year)

app.run(debug=True)
