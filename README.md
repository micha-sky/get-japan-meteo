# get-japan-meteo
saves weather data from Japan Meteorogical Agency web-site
http://www.data.jma.go.jp/
usage:
python jma-reader.py interval station_id year start_month end_month

interval - (hourly, 10min) - hourly or 10 minute weather data
station_id - weather station id. (Haramachi=0288; Iitate=1130; Soma=0285; Tsushima=1150)
year - year
start_month - month to start from
end_month - month to end

Assumes there's 31 day in month, so you need to delete
one file if there is only 30 days (like in June and September)
example gets hourly data for Haramachi station from May to October 2011
python jma-reader.py hourly 0288 2011 05 10
