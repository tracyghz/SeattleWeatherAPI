import csv
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# use the actual path to this csv file in your working dir if want to test without running in container
CSV_FILE_PATH = '/app/static/seattle-weather.csv'

class DatabaseClient:

    def get_all(self):
        content = []
        try:
            # Specify the path to your CSV file
            # Open and read the CSV file
            with open(CSV_FILE_PATH, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    content.append(row)
        except IOError as e:
            logger.exception(f'Error when reading CSV: {str(e)}')
        return content

    def get_by_query(self, args):
        limit = args.get('limit', type=int)
        date = args.get('date', type=str)
        weather = args.get('weather', type=str)

        content = self.get_all()
        result = []
        for row in content:
            if date and weather:
                if row['date'] == date and row['weather'] == weather: result.append(row)
            elif date:
                if row['date'] == date: result.append(row)
            elif weather:
                if row['weather'] == weather == weather: result.append(row)
            else:
                result.append(row)
        if limit:
            result = result[0:limit]
        return result
