# flask --app data_server run
from flask import Flask
from flask import render_template
import json
from flask import request

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


    life_sum = 0
    yearAmt = 0
    for country in data:
        for year in years:
            life_sum += data[country][year]
            yearAmt+=1
    universalAvg = life_sum/yearAmt 
    print("universalAvg", universalAvg)

    

    for i in range(len(increment_years)-1): # make it easy to dynamically generate a line graph
        start_x = increment_years[i] #generate endpoints for each line segment
        stop_x = increment_years[i+1]
        canada_line_endpoints.append([canada[start_x],canada[stop_x]])
        mexico_line_endpoints.append([mexico[start_x],mexico[stop_x]])
        usa_line_endpoints.append([usa[start_x],usa[stop_x]])

    increment_life = [55, 62, 69, 76, 83]


    print("c_e",canada_line_endpoints)
    return render_template('index.html', years = sorted(data["Canada"].keys()), increment_years = increment_years, canada_endpoints = canada_line_endpoints, mexico_endpoints = mexico_line_endpoints, usa_endpoints = usa_line_endpoints, increment_life = sorted(increment_life, reverse=True), universalAvg = universalAvg)

@app.route('/year')
def year():
    #load a current view of the data
    f = open("data/life_expectancy.json", "r")
    data = json.load(f)
    f.close()


    
    requested_year = request.args.get("year")
    print("requested_year", requested_year)

    canada_life = data["Canada"][requested_year]
    mexico_life = data["Mexico"][requested_year]
    usa_life = data["United States"][requested_year]

    
    if 55 < canada_life <= 57.25:
        canada_color = 231, 220, 250
    if 57.25 < canada_life <= 59.5:
        canada_color = 226, 209, 255
    if 59.5 < canada_life <= 61.75:
        canada_color = 213, 189, 252
    if 61.75 < canada_life <= 64:
        canada_color = 206, 176, 255
    if 64 < canada_life <= 66.25:
        canada_color = 187, 146, 252
    if 66.25 < canada_life <= 68.5:
        canada_color = 178, 130, 255
    if 68.5 < canada_life <= 70.75:
        canada_color = 169, 115, 255
    if 70.75 < canada_life <= 73:
        canada_color = 155, 93, 252
    if 73 < canada_life <= 75.25:
        canada_color = 143, 73, 252
    if 75.25 < canada_life <= 77.5:
        canada_color = 135, 59, 255
    if 77.5 < canada_life <= 79.75:
        canada_color = 122, 38, 255
    if 79.75 < canada_life <= 83:
        canada_color = 105, 10, 255

    if 55 < mexico_life <= 57.25:
        mexico_color = 231, 220, 250
    if 57.25 < mexico_life <= 59.5:
        mexico_color = 226, 209, 255
    if 59.5 < mexico_life <= 61.75:
        mexico_color = 213, 189, 252
    if 61.75 < mexico_life <= 64:
        mexico_color = 206, 176, 255
    if 64 < mexico_life <= 66.25:
        mexico_color = 187, 146, 252
    if 66.25 < mexico_life <= 68.5:
        mexico_color = 178, 130, 255
    if 68.5 < mexico_life <= 70.75:
        mexico_color = 169, 115, 255
    if 70.75 < mexico_life <= 73:
        mexico_color = 155, 93, 252
    if 73 < mexico_life <= 75.25:
        mexico_color = 143, 73, 252
    if 75.25 < mexico_life <= 77.5:
        mexico_color = 135, 59, 255
    if 77.5 < mexico_life <= 79.75:
        mexico_color = 122, 38, 255
    if 79.75 < mexico_life <= 83:
        mexico_color = 105, 10, 255

    if 55 < usa_life <= 57.25:
        usa_color = 231, 220, 250
    if 57.25 < usa_life <= 59.5:
        usa_color = 226, 209, 255
    if 59.5 < usa_life <= 61.75:
        usa_color = 213, 189, 252
    if 61.75 < usa_life <= 64:
        usa_color = 206, 176, 255
    if 64 < usa_life<= 66.25:
        usa_color = 187, 146, 252
    if 66.25 < usa_life <= 68.5:
        usa_color = 178, 130, 255
    if 68.5 < usa_life <= 70.75:
        usa_color = 169, 115, 255
    if 70.75 < usa_life <= 73:
        usa_color = 155, 93, 252
    if 73 < usa_life <= 75.25:
        usa_color = 143, 73, 252
    if 75.25 < usa_life <= 77.5:
        usa_color = 135, 59, 255
    if 77.5 < usa_life <= 79.75:
        usa_color = 122, 38, 255
    if 79.75 < usa_life <= 83:
        usa_color = 105, 10, 255


    return render_template('year.html', years = sorted(data["Canada"].keys()), requested_year = requested_year, canada_color = canada_color, mexico_color = mexico_color, usa_color = usa_color, canada_life = canada_life, mexico_life = mexico_life, usa_life = usa_life)

app.run(debug=True)
