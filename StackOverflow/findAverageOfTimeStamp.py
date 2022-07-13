import datetime
import pandas as pd

date_times = ["2020-01-02 10:00:00", "2020-01-02 10:10:00", "2020-01-02 10:20:00",
         "2020-01-03 10:00:00", "2020-01-03 10:10:00", "2020-01-03 10:20:00",
         "2020-01-04 10:00:00", "2020-01-04 10:10:00", "2020-01-04 10:20:00"]

values = [10, 20, 16, 
          31, 56, 25,
          15, 17, 18]

df = pd.DataFrame({
    "date": pd.to_datetime(date_times),
    "value_": values
})

data_combinded = ["2020-01-02 10:00:00 10", "2020-01-02 10:10:00 30", "2020-01-02 10:20:00 10",
         "2020-01-03 10:00:00 20", "2020-01-03 10:10:00 10", "2020-01-03 10:20:00 50",
         "2020-01-04 10:00:00 39", "2020-01-04 10:10:00 2", "2020-01-04 10:20:00 6"]


def find_last_2days_mean(time, df):
    time = time - datetime.timedelta(days=1)
    test = df.loc[pd.date_range(end=time, periods=2, freq='1D')]
    # print(test)
    return df[df.date.isin(pd.date_range(end=time, periods=2, freq='1D'))].value_.mean()


def find_mean(ref_date: str, df: int):

    for date_s in date_times:
        date = datetime.datetime.strptime(date_s, '%Y-%m-%d %H:%M:%S')
        print(date_s, date)



if __name__ == '__main__':
    # find_mean()
    df['last_2_days_avg'] = df['date'].apply(lambda x: find_last_2days_mean(x, df))
    average = df[df['date'] == "2020-01-03 10:00:00"].value_.mean()
    print(average)