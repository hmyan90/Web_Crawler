#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding=utf8
'''This code used to parse the HTML page of weatherground.com to scrape the weather data by using BeautifulSoup'''
import csv
import requests
import re
import urllib2
import sys
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')
def ParserWeather(y,m,d,z,f):


    year = str(y)
    month = str(m)
    day = str(d)
    date = year + '/' + month + '/' + day
    zip = z
    # Set the webpage here. For batch work, read the webpage from file or etc
    weatherUrl = 'https://www.wunderground.com/history/airport/KLAX/'+date+'/DailyHistory.html?req_city=El%20Segundo&req_state=CA&reqdb.zip='+str(zip)+'&reqdb.magic=1&reqdb.wmo=99999'
    request = requests.get(weatherUrl)
    if request.status_code == 200:
        print('Web site exists')
    else:
        print('Web site does not exist')
    page = urllib2.urlopen(weatherUrl)
    soup = BeautifulSoup(page)

    # Find the table from the HTML
    table = soup.find("div", {"id": "observations_details"})

    # Open a file to store the parsed record
    # Write the title to csv file
    write_to_file = str(zip) + ' ' + date + '\n'
    f.write(write_to_file)
    write_to_file = 'Time(PDT)' + ',' + 'Temp.°F' + ',' + 'Dew Point°F' + ',' + 'Humidity%' + ',' + 'Pressure(in)' + ',' + 'Visibility(mi)' + ',' + 'Wind Dir' + ',' + 'Wind Speed' + ',' + 'Gust Speed' + ',' + 'Precip' + ',' + 'Events' + ',' + 'Conditions' + '\n'
    f.write(write_to_file)

    # Traverse each row of the table
    for row in table.findAll("tr"):
        cells = row.findAll("td")
        if len(cells) == 12:
            record_each_day = []
            record_each_day.append(cells[0].find(text=True))
            # Due to the special format of the HTML 2-11 columns need another treatment
            for i in range(1, 11):
                tmp = cells[i].find(text=False)
                if len(re.split('[> <]', str(tmp))) > 3:
                    record_each_day.append(unicode(re.split('[> <]', str(tmp))[6] + re.split('[> <]', str(tmp))[11]))
                else:
                    tmp2 = cells[i].find(text=True)
                    tmp2 = unicode(tmp2)
                    tmp2 = tmp2.strip()
                    # tmp2 = tmp2.strip('%')
                    record_each_day.append(tmp2)
            # The 21st column need special treatment
            Events = cells[11].find(text=True)
            record_each_day.append(re.split(',', Events)[0])
            write_to_file = record_each_day[0].strip() + ','
            for i in range(1, 11):
                write_to_file += str(record_each_day[i]).strip().replace('\n', '').replace('\t', '').replace(',',
                                                                                                             ' and ') + ','
            write_to_file += (record_each_day[11].strip() + '\n')
            f.write(write_to_file)
        if len(cells) == 13:
            record_each_day = []
            record_each_day.append(cells[0].find(text=True))
            # Due to the special format of the HTML 2-11 columns need another treatment
            for i in range(1, 12):
                if i == 2:
                    continue
                tmp = cells[i].find(text=False)
                if len(re.split('[> <]', str(tmp))) > 3:
                    record_each_day.append(unicode(re.split('[> <]', str(tmp))[6] + re.split('[> <]', str(tmp))[11]))
                else:
                    tmp2 = cells[i].find(text=True)
                    tmp2 = unicode(tmp2)
                    tmp2 = tmp2.strip()
                    # tmp2 = tmp2.strip('%')
                    record_each_day.append(tmp2)
            # The 21st column need special treatment
            Events = cells[12].find(text=True)
            record_each_day.append(re.split(',', Events)[0])
            write_to_file = record_each_day[0].strip() + ','
            for i in range(1, 11):
                write_to_file += str(record_each_day[i]).strip().replace('\n', '').replace('\t', '').replace(',',
                                                                                                             ' and ') + ','
            write_to_file += (record_each_day[11].strip() + '\n')
            f.write(write_to_file)