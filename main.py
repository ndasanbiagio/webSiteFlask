from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
  print("Get request string")
  return render_template('index.html')


@app.route('/', methods = ['POST'])
def home_post():
  dim1 = request.form['first_dim']
  dim2 = request.form['second_dim']
  dim3 = request.form['third_dim']
  volume = float(dim1) * float(dim2) * float(dim3)
  print()

  print("Get post request")
  return render_template('index.html', output=volume, dim_1=dim1, dim_2=dim2, dim_3=dim3)

app.run(host='0.0.0.0')


# This is a Python script using the Flask web framework. Let's go through it step by step:

# Import Statements:

# from flask import Flask, render_template, request: This imports the necessary modules from Flask. 
# Flask is the main class we use to create our web application. render_template is used to render 
# HTML templates, and request is used to access incoming request data.
# Create Flask App:

# app = Flask(__name__): This creates a Flask application instance. __name__ is a special variable in 
# Python that represents the name of the current module. This is needed so that Flask knows where to
# look for templates and static files.
# Define Routes:

# @app.route('/'): This is a decorator that defines the route for the home page ('/'). The function 
# below this decorator (home()) will be called when a GET request is made to the root URL.
# @app.route('/', methods=['POST']): This is another route decorator for the home page, but this one 
# specifically handles POST requests. The function below (home_post()) will be called when a POST request is made to the root URL.
# Home Route (GET):

# def home():: This function handles GET requests to the root URL. It simply renders the index.html template.
# Home Route (POST):

# def home_post():: This function handles POST requests to the root URL. It retrieves the dimensions 
# entered by the user from the form using request.form, calculates the volume, and then renders the 
# index.html template again, passing the calculated volume (output) and the dimensions (dim_1, dim_2, dim_3) back to the template.
# Run the App:

# app.run(host='0.0.0.0'): This line runs the Flask application. Setting host='0.0.0.0' makes the app 
# accessible from any IP address on the machine's network.
# Overall, this script creates a simple web application using Flask that calculates the volume based 
# on user input from a form in the index.html template and displays the result back to the user.