import requests
import csv
from io import StringIO

class Site(object):
    def __init__(self, name, county, aqi):
        super().__init__()
        self.site_name = name
        self.county = county
        try:
            self.aqi = int(aqi)
        except:
            self.aqi = 999

    def __repr__(self):
        return f"站點:{self.site_name},城市:{self.county},aqi:{self.aqi}"


class Taiwan_AQI():

    API_KEY = "657f239f-f6e5-49fb-b8e0-966c8f789a5b"

    @classmethod
    
    def download_AQI(cls) -> list:
        
        response = requests.get(f"https://data.epa.gov.tw/api/v2/aqx_p_432?api_key={cls.API_KEY}&limit=1000&sort=ImportDate desc&format=CSV")
        
        if(response.ok):            
            #print(response.text)
            #file = open("./Lesson17/aqi.csv", encoding = "utf-8", mode = "w")
            #file.write(response.text)
            #file.close()

            file = StringIO(response.text, newline = "")
            csvReader = csv.reader(file)
            next(csvReader)

            dataList = []
            for item in csvReader:
                site = Site(item[0], item[1], item[2])
                dataList.append(site)
            return dataList
            

                     
        
            """
            for item in csvReader:
                print(item[0], item[1])
            """

        else:
            raise Exception("下載失敗")
