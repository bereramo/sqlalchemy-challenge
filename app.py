# Import the dependencies.
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
base= automap_base()

base.prepare(autoload_with=engine)
# reflect the tables


# Save references to each table
measurement= base.classes.measurement
station = base.classes.station

# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return (
        f"Hawaii<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>" 
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
       
    )
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Starting from the most recent data point in the database. 
    most_recent= (session.query(measurement.date).order_by(measurement.date.desc()).first())
    most_recent_date = dt.datetime.strptime(most_recent[0], '%Y-%m-%d').date()
    # Calculate the date one year from the last date in data set.

    year = most_recent_date - dt.timedelta(days=365)

    # Perform a query to retrieve the data and precipitation scores
    data_prp = session.query(measurement.date, measurement.prcp).filter(measurement.date >= year)
    data= data_prp.filter(measurement.date <= most_recent[0]).order_by(measurement.date).all()
    return jsonify(data)

@app.route("/api/v1.0/stations")
def stations():
    stations= session.query(station.name).all()
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    active_results= [func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)]
    stuff= session.query(active_results).\
    order_by(measurement.id.desc())
    results =stuff.first()
    return jsonify(stations)


@app.route("/api/v1.0/start")
def start():
    session = session(engine)
    start_results = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).\
              filter(measurement.date <'start').all()
    session.close()

    temperature = []
    for min, max, average in start_results:
        temps = {}
        temps['Minimum Temperature'] = min
        temps['Maximum Temperature'] = max
        temps['Average Temperature'] = average
        temps.append(temps)

    return jsonify(temps)
    

@app.route("/api/v1.0/start/end")
def starteend(start, end):
   def tobs():
    session = session(engine)
    end_results = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).\
              filter(measurement.date <= 'end').all()
    session.close()

    temperature = []
    for min, max, average in end_results:
        temps = {}
        temps['Minimum Temperature'] = min
        temps['Maximum Temperature'] = max
        temps['Average Temperature'] = average
        temps.append(temps)

    return jsonify(temps)