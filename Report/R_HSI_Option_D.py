import datetime, urllib3
from bs4 import BeautifulSoup
urllib3.disable_warnings()

class R_HSI_Option_D:

    url_prefix = "https://www.hkex.com.hk/chi/stat/dmstat/dayrpt/hsioc%y%m%d.htm"

    def __init__(self, report_date, isExport):
        self.report_date = report_date

    def __del__(self):
        print("Destroy: ", self.__class__.__name__)

    def downloadData(self):
        if datetime.date.today().isoweekday() > 5:
            self.report_date += datetime.timedelta(days=(datetime.date.today().isoweekday() - 5)*-1)
        url = self.report_date.strftime(self.url_prefix)
        #print("Path: ", url)
        conn = urllib3.connection_from_url(url)
        response = conn.urlopen('GET', url)
        html_doc = response.read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        for x in soup.find_all('27000'):
            print(x.string())


if __name__ == '__main__':
    print("Main")
    opt_report = R_HSI_Option_D(datetime.date.today(), True)
    opt_report.downloadData()