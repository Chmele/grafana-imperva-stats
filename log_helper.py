import csv
import os
from itertools import groupby
from influxdb import InfluxDBClient
from datetime import datetime


client = InfluxDBClient(database='imperva')
#filenames = [_ for _ in os.listdir('stats')]


def timeSplit(file, measurement):
    sect = groupby(csv.DictReader(file), lambda x: x["TimeStamp"])
    for i in sect:
        rework(measurement, *i)


def rework(measurement, time, data):
    fields = {i["IndicationName"]: i for i in data}
    ret = nullPayload(time, measurement)
    for f, v in fields.items():
        ret[0]['fields'].update(
            {
                f+'Max': int(v['MaxValue']),
                f+'Avg': int(v['AverageValue']),
            })
    client.write_points(ret)


def nullPayload(time, measurement='8th'):
    return [{
        'measurement': measurement,
        'time': datetime.strptime(time, '%Y-%m-%d %H:%M:%S').isoformat()+'Z',
        'fields': {}
    }]

if __name__ == "__main__":
    for i in filenames:
        timeSplit(open("stats/"+i))
