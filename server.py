from flask import Flask;
from flask import request;
from flask import render_template;
import api;

app = Flask(__name__);

@app.route( "/", methods = ["GET", "POST"] )
def onIndexGetOrPost():
	"""Handle HTTP requests to the main route"""
	if request.method == "GET":
		# send the submit page
		return render_template( "index.html" );
		
	elif request.method == "POST":
		# form data
		# TODO: put in new form data ids
		subject = request.form["sel-subject"];
		duedate = request.form["inp-duedate"];
		details = request.form["inp-details"];
		api.putData( subject, duedate, details );
		render_template( "index.html", submitted = true );

@app.route( "/data", methods = ["GET"] )
def onDataGet():
	if not request.method == "GET":
		return
	
	return "Not implemented";
	

@app.errorhandler( 404 )
def notFound( error ):
	return render_template( "errors/error.html", error=error, code=404 ), 404

@app.errorhandler(500)
def serverError( error ):
	return render_template( "errors/error.html", error=error, code=500 ), 500