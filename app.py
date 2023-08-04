from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    "id": 0,
    "name": "Frontend Engineer",
    "location": "Chennai, India",
    "salary": "Rs.1,00,000"
  },
  {
    "id": 1,
    "name": "Fullstack Developer",
    # "location": "Bangalore, India",
    "salary": "Rs.2,00,000"
  },
  {
    "id": 2,
    "name": "Backend Engineer",
    "location": "Chennai, India",
    # "salary": "Rs.1,25,000"
  },
  {
    "id": 3,
    "name": "Data Engineer",
    "location": "Chennai, India",
    "salary": "Rs.1,50,000"
  },
]


@app.route("/")
def home():
  return render_template("Home.html", jobs=JOBS)

@app.route("/api/jobs")
def apiJobs():
  return jsonify(JOBS);


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
