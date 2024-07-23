from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Raipur, India',
        'salary': 'Rs. 5,00,000'
    },
    {
        'id': 2,
        'title': 'ML Engineer',
        'location': 'Pune, India',
        'salary': 'Rs. 7,00,000'
    },
    {
        'id': 3,
        'title': 'Software Engineer',
        'location': 'Bilaspur, India',
        'salary': 'Rs. 4,50,000'
    },
    {
        'id': 4,
        'title': 'Web Developer',
        'location': 'Raipur, India',
        'salary': 'Rs. 6,50,000'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'remote',
        'salary': 'Rs. 4,20,000'
    },
]


@app.route("/")
def hello_world():
    return render_template("index.html", jobs=JOBS, company_name="JobSearch")


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
