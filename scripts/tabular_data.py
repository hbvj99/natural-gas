datapackage = '''{
    "profile": "tabular-data-package",
    "name": "Natural Gas prices",
    "title": "Henry Hub Natural Gas Spot prices at https://www.eia.gov/dnav/ng/hist/rngwhhdm.htm",
    "resources": [
        {
            "path": "data/price_daily.csv",
            "format": "csv",
            "mediatype": "text/csv",
            "name": "daily",
            "schema": {
                "fields": [
                    {
                        "format": "default",
                        "name": "Date",
                        "type": "date"
                    },
                    {
                        "format": "default",
                        "name": "Price",
                        "type": "number"
                    }
                ],
        "missingValues": [
          ""
        ]
            }
        },
        {
            "path": "data/price_weekly.csv",
            "format": "csv",
            "mediatype": "text/csv",
            "name": "daily",
            "schema": {
                "fields": [
                    {
                        "format": "default",
                        "name": "Week",
                        "type": "date"
                    },
                    {
                        "format": "default",
                        "name": "Price",
                        "type": "number"
                    }
                ],
        "missingValues": [
          ""
        ]
            }
        },
        {
            "path": "data/price_montly.csv",
            "format": "csv",
            "mediatype": "text/csv",
            "name": "montly",
            "schema": {
                "fields": [
                    {
                        "format": "default",
                        "name": "Date",
                        "type": "date"
                    },
                    {
                        "format": "default",
                        "name": "Price",
                        "type": "float"
                    }
                ],
        "missingValues": [
          ""
        ]
            }
        },
        {
            "path": "data/price_annual.csv",
            "format": "csv",
            "mediatype": "text/csv",
            "name": "daily",
            "schema": {
                "fields": [
                    {
                        "format": "default",
                        "name": "Year",
                        "type": "date"
                    },
                    {
                        "format": "default",
                        "name": "Price",
                        "type": "number"
                    }
                ],
        "missingValues": [
          ""
        ]
            }
        }
    ]
}
'''
