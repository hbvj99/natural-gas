datapackage = '''{
    "name": "natural-gas-prices",
    "title": "Henry Hub Natural Gas Spot prices at https://www.eia.gov/dnav/ng/hist/rngwhhdm.htm",
    "resources": [
        {
            "name": "price_daily",
            "path": "data/price_daily.csv",
            "format": "csv",
            "mediatype": "text/csv",
            "schema": {
                "fields": [
                    {
                        "format": "default",
                        "name": "date",
                        "type": "date"
                    },
                    {
                        "format": "default",
                        "name": "price",
                        "type": "number"
                    }
                ]
            }
        },
        {
            "name": "price_weekly.csv",
            "path": "data/price_weekly.csv",
            "format": "csv",
            "mediatype": "text/csv",
            "schema": {
                "fields": [
                    {
                        "format": "default",

                        "name": "date",
                        "type": "date"
                    },
                    {
                        "format": "default",
                        "name": "price",
                        "type": "number"
                    }
                ]
            }
        }
    ]
}
'''
