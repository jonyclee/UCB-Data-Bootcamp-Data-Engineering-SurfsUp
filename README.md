# UCB-Data-Bootcamp-Data-Engineering-SurfsUp

### Data Engineering
***
This program imports csv files into a dataframe.

I then cleaned the dataframes by dropping the NaN values and saving the cleaned dataframe into a new csv file.

### Database Engineering
***
This program uses SQLAlchemy and create a sqlite database. It stores the dataframes converted from csv files.

### Climate Analysis and Exploration
***

##### Precipitation Analysis
***
I designed a query to retrieve the last 12 months of precipitation data from the Measurement class and selected only the date and prcp. Then, I plot the prcp against the date. Finally, printed out summary statistics for the data.


##### Station Analysis
***
I designed a query to calculate the total number of stations and another query to find out the frequency of data from each station.

Next, I designed a query to retrieve the last 12 months of temperature observation data (tobs) filtered by the station with the highest observations.

Finally, I plot the results onto a histogram.

##### Temperature Analysis
***
I wrote a function called calc_temps that accepts a start and end date. The start and end date are then subtracted by 1 year as a way to predict the potential temperature for the designated start and end date. The function then return a plot of the average temperature with the error bars indicating the maximum and minimum temperature of the past indicators.

### Climate App
***
I created several Flask api to return information stored as a dictionary in json format.

##### Precipitation
***
route('/api/v1.0/precipitation') <br>
A query of dates and prcp observations for the last year converted into a dictionary.

##### Station
***
route('/api/v1.0/stations') <br>
A query of station information converted into a dictionary.

##### TOBS
***
route('/api/v1.0/tobs') <br>
A query of dates and Temperature observations (tobs) for the last year converted into a dictionary.

##### Start
***
route('/api/v1.0/<\start>') where <\start> is a date in this format YYYY-MM-DD<br>
A query of tobs for the dates starting from the given start date. A simple statistics (Minimum, Maximum, and Average) are shown and converted into a dictionary.

##### Start and End
***
route('/api/v1.0/<\start>/<\end>') where <\start> and <\end> is a date in this format YYYY-MM-DD<br>
A query of tobs for the dates starting from the given start date to a given end date. A simple statistics (Minimum, Maximum, and Average) are shown and converted into a dictionary.

##### Contributors
***
Jonathan Lee [GitHub](https://github.com/jonyclee)

##### Technologies Used:
***
* Python notebook
* Python packages:
	- pandas
	- Flask
	- matplotlib.pyplot
	- sqlalchemy