from datetime import datetime

def query_date():
    this_day = datetime.today()
    print('Today is', this_day.strftime("%A, %d %B %Y"), '\n')