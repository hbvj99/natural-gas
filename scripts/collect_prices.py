import urllib.request
import json
import csv
import pathlib as plib
import tabular_data as tjson
from datetime import datetime

# Create directory
plib.Path('../data', '../archieve').mkdir(parents=True, exist_ok=True)

#EIA API (https://www.eia.gov/opendata/register.php)
KEY = '8227c29aa545b03ce215edf474b6b943'

# Natural Gas AQI data types
daily_dta = 'NG.RNGWHHD.D'      # Daily price
monthly_dta = 'NG.RNGWHHD.M'    # Monthly price


# Create files
gas_prices = {
    daily_dta: '../archieve/price_daily_unformated.csv',
    monthly_dta: '../archieve/price_monthly_unformated.csv'}


# Fetch URL
def requests(url):
    data = urllib.request.urlopen(url)
    dta_loc = json.loads(data.read().decode('utf-8'))
    return dta_loc


# Write to CSV
def writeCSV(dataRows, csv_file):
    header = ['Date',  'Price']
    with open(csv_file, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(dataRows)
        # date_daily = (dataRows[0])[0]         # Daily Gas price date
        # date_monthly = (dataRows[1])[0]       # Monthly Gas price date
        file.close()


# Fetch URI data types and write CSV
def writeData():
    for data_type, csvFileName in gas_prices.items():
        dta_loc = requests(
            f'http://api.eia.gov/series/?api_key={KEY}&series_id={data_type}')
        data = dta_loc['series'][0]['data']
        writeCSV(data, csvFileName)
        dataPackage()


# Format Dates for Monthly, Yearly prices in new file
def formatDate():
    with open('../archieve/price_daily_unformated.csv', 'r') as src:
        with open('../data/price_daily.csv', 'w+') as result:
            writer = csv.writer(result, lineterminator='\n')
            writer.writerow(['Date', 'Price'])
            reader = csv.reader(src)
            src.readline()
            for row in reader:
                ts = datetime.strptime(row[0], '%Y%m%d').date()
                row[0] = ts
                if ts != '':
                    writer.writerow(row)

    with open('../archieve/price_monthly_unformated.csv', 'r') as src:
        with open('../data/price_monthly.csv', 'w+') as result:
            writer = csv.writer(result, lineterminator='\n')
            writer.writerow(['Month', 'Price'])
            reader = csv.reader(src)
            src.readline()
            for row in reader:
                ts = datetime.strptime(row[0], '%Y%m').strftime('%Y-%m')
                row[0] = ts
                if ts != '':
                    writer.writerow(row)

    src.close()
    result.close()


# Create datapackage
def dataPackage():
    fle = open('../datapackage.json', 'w+')
    fle.write(tjson.datapackage)
    fle.close()


# Main
if __name__ == '__main__':
    writeData()
    formatDate()
