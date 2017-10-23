# Dependencies
from flask import Flask, jsonify
import pandas as pd
from sqlalchemy import *
from sqlalchemy.ext.automap import automap_base
from datetime import date
from sqlalchemy.orm import Session

# Create instance of Flask app
app = Flask(__name__)

# Create route /api/v1.0/<start>/<end>
@app.route('/api/v1.0/<start>/<end>')
def start(start, end):
	# Create an engine to connecting to hawaii.sqlite
	engine = create_engine("sqlite:///hawaii.sqlite")

	# Reflect Database into ORM classes
	Base = automap_base()
	Base.prepare(engine, reflect=True)
	Base.classes.keys()

	Measurement = Base.classes.hawaii_measurement

	# Create a session for the engine
	session = Session(engine)

	start_end_info = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= start).filter(Measurement.date <= end).all()

	# Save the data into lists
	Date = [pd.to_datetime(x[0]) for x in start_end_info]
	tobs = [x[1] for x in start_end_info]

	start_end = pd.DataFrame({'tobs': tobs})

	tobs_max = start_end.max()
	tobs_min = start_end.min()
	tobs_avg = start_end.mean()

	summary_df = pd.DataFrame({'Max. Temperature': tobs_max, 'Min. Temperature': tobs_min, 'Average Temperature': tobs_avg})

	summary_dict = summary_df.to_dict(orient='record')

	return jsonify(summary_dict)

if __name__ == "__main__":
    app.run(debug=True)