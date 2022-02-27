from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/qn1")
def qn1():
    options = ['Accountancy', 'Arts', 'Business', 'Computer Science', 
                'Communication Studies', 'Engineering','History', 'Mathematics', 
                'Pyschology', 'Science', 'Sociology', 'Select']
    return render_template("question1.html", options=options, npage="qn2")

@app.route("/qn2")
def qn2():
    options = ['Australia', 'China', 'Canada', 'Indonesia', 'Malaysia',
                'Singapore', 'Thailand', "United Kingdom", 'USA', 'Select']
    return render_template("question2.html", options=options, npage="qn3", bpage="qn1")

@app.route("/qn3")
def qn3():
    options = ['Full Time', 'Part Time', 'Summer Internship',
               'Credit-Bearing Internship', 'Select']
    return render_template("question3.html", options=options, npage="qn4", bpage="qn2")

@app.route("/qn4")
def qn4():
    options = ['< $1000', '$1000 to $2000', '$2000 to $3000',
               '$3000 to $4000', '$4000 to $5000', '> $5000', 'Select']
    return render_template("question4.html", options=options, npage="qn5", bpage="qn3")

@app.route("/qn5")
def qn5():
    options = ['Banking & Finance', 'Chemical Manufacturing', 'Consulting and Management', 
                'Engineering and Manufacturing', 'Healthcare', 'IT', 'Marketing', 'Media and Internet', 'Select']
    return render_template("question5.html", options=options, npage="qn6", bpage="qn4")

@app.route("/qn6")
def qn6():
    options = ['Team-player', 'Independent-worker',
               'Fast-learner', 'Leader', 'Select']
    return render_template("question6.html", options=options, npage="qn7", bpage="qn5")

@app.route("/qn7")
def qn7():
    return render_template("question7.html", npage="jobmatchsuccess", bpage="qn6")

@app.route("/job1")
def job1():
    return render_template("job1.html", page="job2", joblink="https://careers.shopee.sg/job-detail/2336")

@app.route("/job2")
def job2():
    return render_template("job2.html", page='job3', fpage="job1", joblink="https://capps.com.sg/career")

@app.route("/job3")
def job3():
    return render_template("job3.html", page="job4", fpage="job2", joblink="https://www.mycareersfuture.gov.sg/job/information-technology/embedded-software-engineer-anotech-energy-singapore-01547dadab80df96decb05f6d4aeb534?source=MCF&event=Search&utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic")

@app.route("/job4")
def job4():
    return render_template("job4.html", page="job5", fpage="job3", joblink="https://www.linkedin.com/jobs/view/2924080444?showGuestApplyModal=true")

@app.route("/job5")
def job5():
    return render_template("job4.html", page="home", fpage="job4", joblink="https://www.mycareersfuture.gov.sg/job/sciences/rd-software-engineer-edf-lab-singapore-c2e94f7ca343c9ff88a02f9be9f69e8e?source=MCF&event=Search")

@app.route("/jobmatchsuccess")
def jobmatchsuccess():
    return render_template("jobmatchsuccess.html")


if __name__ == "__main__":
    app.run(debug= True)