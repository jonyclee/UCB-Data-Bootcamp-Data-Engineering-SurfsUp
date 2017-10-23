# Dependencies
from flask import Flask, jsonify
import pandas as pd
from sqlalchemy import *
from sqlalchemy.ext.automap import automap_base
from datetime import date
from sqlalchemy.orm import Session

# Create instance of Flask app
app = Flask(__name__)

# Create route /api/v1.0/precipitation
@app.route('/api/v1.0/precipitation')
def prcp():
	# Create an engine to connecting to hawaii.sqlite
	engine = create_engine("sqlite:///hawaii.sqlite")

	# Reflect Database into ORM classes
	Base = automap_base()
	Base.prepare(engine, reflect=True)
	Base.classes.keys()

	Measurement = Base.classes.hawaii_measurement

	# Create a session for the engine
	session = Session(engine)

	prcp_data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > '2016-08-18').all()

	# Save the data into lists
	Date = [pd.to_datetime(x[0]) for x in prcp_data]
	prcp = [x[1] for x in prcp_data]

	prcp_date = pd.DataFrame({'date': Date, 'prcp': prcp})

	prcp_date_dict = prcp_date.to_dict(orient='record')

	return jsonify(prcp_date_dict)

# Create route /api/v1.0/stations
@app.route('/api/v1.0/stations')
def station():
	# Create an engine to connecting to hawaii.sqlite
	engine = create_engine("sqlite:///hawaii.sqlite")

	# Reflect Database into ORM classes
	Base = automap_base()
	Base.prepare(engine, reflect=True)
	Base.classes.keys()

	Station = Base.classes.hawaii_station

	# Create a session for the engine
	session = Session(engine)

	station_info = session.query(Station.station, Station.name, Station.latitude, Station.longitude, Station.elevation).all()

	station = [x[0] for x in station_info]
	name = [x[1] for x in station_info]
	lat = [x[2] for x in station_info]
	longitude = [x[3] for x in station_info]
	elevation = [x[4] for x in station_info]

	station_df = pd.DataFrame({'station': station, 'name': name, 'latitude': lat, 'longitude': longitude, 'elevation': elevation})

	station_dict = station_df.to_dict(orient='record')

	return jsonify(station_dict)

# Create route /api/v1.0/tobs
@app.route('/api/v1.0/tobs')
def tobs():
	# Create an engine to connecting to hawaii.sqlite
	engine = create_engine("sqlite:///hawaii.sqlite")

	# Reflect Database into ORM classes
	Base = automap_base()
	Base.prepare(engine, reflect=True)
	Base.classes.keys()

	Measurement = Base.classes.hawaii_measurement

	# Create a session for the engine
	session = Session(engine)

	tobs_data = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date > '2016-08-18').all()

	# Save the data into lists
	Date = [pd.to_datetime(x[0]) for x in tobs_data]
	tobs = [x[1] for x in tobs_data]

	tobs_date = pd.DataFrame({'date': Date, 'tobs': tobs})

	tobs_date_dict = tobs_date.to_dict(orient='record')

	return jsonify(tobs_date_dict)

# Create route /api/v1.0/<start>
@app.route('/api/v1.0/<start>')
def start(start):
	# Create an engine to connecting to hawaii.sqlite
	engine = create_engine("sqlite:///hawaii.sqlite")

	# Reflect Database into ORM classes
	Base = automap_base()
	Base.prepare(engine, reflect=True)
	Base.classes.keys()

	Measurement = Base.classes.hawaii_measurement

	# Create a session for the engine
	session = Session(engine)

	start_info = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= start).all()

	# Save the data into lists
	Date = [pd.to_datetime(x[0]) for x in start_info]
	tobs = [x[1] for x in start_info]

	start_data = pd.DataFrame({'tobs': tobs})

	tobs_max = start_data.max()
	tobs_min = start_data.min()
	tobs_avg = start_data.mean()

	summary_df = pd.DataFrame({'Max. Temperature': tobs_max, 'Min. Temperature': tobs_min, 'Average Temperature': tobs_avg})

	summary_dict = summary_df.to_dict(orient='record')

	return jsonify(summary_dict)


if __name__ == "__main__":
    app.run(debug=True)