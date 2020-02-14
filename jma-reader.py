from urllib.request import urlopen
import sys
from bs4 import BeautifulSoup


def print_usage():
    print("python get_data.py interval station_id year start_month end_month")

def iterate_days(st_id, year, moth_from, month_to):
    for month in range(moth_from, month_to + 1):
        for day in range(1, 32):
            url = form_url(str(st_id), str(year), str(month), str(day))
            response = urlopen(url)

            html = response.read()
            soup = BeautifulSoup(html)
            table = soup.find("table", {"class": "data2_s"})

            f = open('{2}_output_{0}_{1}.csv'.format(month, day, st_id), 'w')
            result = []
            for row in table.findAll("tr"):
                cells = row.findAll("td")

                if len(cells) == 8:
                    val1 = cells[0].find(text=True).encode('utf-8')
                    val2 = cells[1].find(text=True).encode('utf-8')
                    val3 = cells[2].find(text=True).encode('utf-8')
                    val4 = cells[3].find(text=True).encode('utf-8')
                    val5 = cells[4].find(text=True).encode('utf-8')
                    val6 = cells[5].find(text=True).encode('utf-8')
                    val7 = cells[6].find(text=True).encode('utf-8')
                    val8 = cells[7].find(text=True).encode('utf-8')
                    row = [val1, val2, val3, val4,
                           val5, val6, val7, val8]
                    write = "{0},{1},{2},{3},{4},{5},{6},{7}\n".format(str(val1), str(val2),
                                                                       str(val3), str(val4),
                                                                       str(val5), str(val6),
                                                                       str(val7), str(val8))
                    f.write(write)
                print("Processed month {0} day {1}").format(month, day)
                result.append(row)

            f.close()
    return


def form_url(st_id, year, month, day):
    # url = "http://www.data.jma.go.jp/obd/stats/etrn/view/10min_a1.php?prec_no=36&block_no=1150&year=2011&month=" + month + "&day=" + day +"&view=p1s"
    url = "http://www.data.jma.go.jp/obd/stats/etrn/view/{4}_a1.php?prec_no=36&block_no={0}&year={1}&month={2}&day={3}&view=p1s".format(
        st_id, year, month, day, interval)
    return url

if len(sys.argv) == 1:
    print_usage()
else:
    interval = str(sys.argv[1])
    station_id = str(sys.argv[2])
    st_year = int(sys.argv[3])
    start_month = int(sys.argv[4])
    end_month = int(sys.argv[5])

    iterate_days(station_id, 2011, start_month, end_month)
