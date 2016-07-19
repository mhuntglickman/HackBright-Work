from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show the index/Welcome page."""

    return render_template("index.html")


@app.route('/application-form')
def make_application():
    """Display open postions at UberMelon"""

    return render_template("application-form.html")

@app.route('/application-response', methods=["POST"])
def app_response():
	"""Display open postions at UberMelon"""

	firstname = request.form.get("firstname")
	lastname = request.form.get("lastname")
	salary_req = request.form.get("salary_req")
	job = request.form.get("job")

	return render_template("application-response.html", 
							firstname=firstname,
							lastname=lastname,
							salary_req=salary_req,
							job=job)

if __name__ == "__main__":
    app.run(debug=True)
