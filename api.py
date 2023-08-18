import date;

def putData( subject, duedate, details ):
	# Initialise the data file
	with dataFile = open( "homework-" + date.today(), "a" ):
		# Write data into file in CSV
		data = f"{subject}, {duedate}, {details}";
		dataFile.write( data );
		print( f"Wrote data \"{data}\"" );
	pass
