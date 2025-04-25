from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
   'id': 1,
    'title': 'Donut Analyst',
    'location': 'Bruges, Belgium',
    'salary': '€100,000'
  },
  {
   'id': 2,
    'title': 'Donut Scientist',
    'location': 'Madrid, Spain',
    'salary': '€150,000'
  },
  {
   'id': 3,
    'title': 'Frontend Donut',
    'location': 'Remote'
  },
  {
   'id': 4,
    'title': 'Backend Donut',
    'location': 'San Francisco, USA',
    'salary': '€200,000'
  }
]

@app.route("/")
def hello_world():
    return render_template("home.html",
                          jobs=JOBS,
                          company_name="Donut")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  

print(__name__)
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)