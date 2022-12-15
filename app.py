import json
import os


from flask import Flask

app = Flask(__name__)


def get_data():
    path = os.path.join(app.root_path, 'static', 'data.json')
    return json.load(open(path))


@app.route('/<year>')
def get(year):
    data = get_data()

    if year not in data:
        return {}, 404

    return {
        year: data[year],
        "Country Name": "Panama",
        "Country Code": "PAN",
        "Indicator Name": "Immunization, measles (% of children ages 12-23 months)",
        "Indicator Code": "SH.IMM.MEAS"
    }


@app.route('/')
def index():
    return get_data()


if __name__ == '__main__':
    app.run()
