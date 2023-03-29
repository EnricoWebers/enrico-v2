from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db
# import easygui

app = Flask(__name__)
  
@app.route("/")
def hello_world():
    jobs = load_jobs_from_db()
    return render_template("home.html", 
                           jobs=jobs,
                           company_name='Enrico Company')
  
@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not Found", 404
  else:
    return render_template("jobpage.html", job=job)

@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  # print('ID', id)
  data = request.form
  job = load_job_from_db(id)
  print('job', job['id'])
  add_application_to_db(job['id'],data)
  return render_template("applicationsubmit.html", 
                         application=data,
                         job=job)
  # return job

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)