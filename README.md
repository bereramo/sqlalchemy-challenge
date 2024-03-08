# sqlalchemy-challenge

Use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database.

Find the most recent date in the dataset.
Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.
Select only the "date" and "prcp" values.
Load the query results into a Pandas DataFrame. Explicitly set the column names.
Sort the DataFrame values by "date".
Plot the results by using the DataFrame plot method, as the following image shows:
Use Pandas to print the summary statistics for the precipitation data.

Design a query to calculate the total number of stations in the dataset.
Design a query to find the most-active stations (that is, the stations that have the most rows). To do so, complete the following steps:
Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.
Design a query to get the previous 12 months of temperature observation (TOBS) data. To do so, complete the following steps:
