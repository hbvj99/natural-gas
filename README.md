# Natural Gas Prices

A collection and analysis of Henry Hub Natual Gas Spot Price available at <a href="https://www.eia.gov/dnav/ng/hist/rngwhhdD.htm">EIA</a> (US Energy Information Administration).

Demo data visualization is available <a href="https://hbvj99.github.io/natural-gas/visualization/index.html"> here</a> or view Jupyter Notebook <a href="https://github.com/hbvj99/natural-gas/blob/master/analysis/data.ipynb">analysis</a> of time series data.

## How it works?
- Fetch open data API available at https://www.eia.gov/opendata/
- Download, Format Historical Dataset
- Render in chart using <a href="https://github.com/d3/d3">D3.js</a>

## Data available
- Yearly
- Monthly

Various data types are also <a href="https://www.eia.gov/opendata/qb.php?category=714806">available</a>. Dataset are available from January 1997 and Price are in US dollars.

## Requirements
- D3js for visualization
- Python libraries used in <a href="https://github.com/hbvj99/natural-gas/tree/master/scripts">scripts</a>, <a href="https://github.com/hbvj99/natural-gas/blob/master/analysis/data.ipynb">data</a>

## How to run?
- Execute <a href="https://github.com/hbvj99/natural-gas/blob/master/scripts/collect_prices.py">```collect_prices.py```</a>	to fetch data through API and save CSV document
- Navigate to <a href="https://github.com/hbvj99/natural-gas/blob/master/visualization/daily_prices.js">```visualization```</a> for graph visualization
- Historical dataset availabe at <a href="https://github.com/hbvj99/natural-gas/tree/master/data">```data```</a>
- View <a href="https://github.com/hbvj99/natural-gas/blob/master/analysis/data.ipynb">pattern</a> analysis
- Price Forecast <a href="https://github.com/hbvj99/natural-gas/blob/master/analysis/forecast_year.ipynb">```notebook```</a>using Facebook <a href="https://facebook.github.io/prophet/">Prophet</a>

## About data and usages
Historical Datasets are in the public domain and are not subject to copyright protection, for more info visit offical <a href="https://www.eia.gov/about/copyrights_reuse.php">webpage</a>
