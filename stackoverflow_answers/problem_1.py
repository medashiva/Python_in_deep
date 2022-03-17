from datetime import datetime
import pandas as pd
class Query:
    XYZ = """ select * from table where date_format(created_at, '%Y-%m-%d') = '{date}' """

current_date = datetime.now().strftime('%Y-%m-%d')


def example():
    print(Query.XYZ.format(date=current_date))
    #df = pd.read_sql(self.db)
    #print(df)



if __name__ == '__main__':
    example()