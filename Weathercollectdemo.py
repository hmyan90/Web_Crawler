#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding=utf8
from ParserWeather import ParserWeather
import csv
import sys
from decimal import Decimal
import numpy as np
reload(sys)
sys.setdefaultencoding('utf8')


f = open('weatherData_' + '90245' + '_' + '2014-2015' +'.csv', 'w')
for i in range(2014,2016):
    for t in range(1,13):
        if t==1 or t==3 or t==5 or t==7 or t==8 or t==10 or t==12:
            for k in range(1,32):
               ParserWeather(i,t,k,90245,f)
        elif t==2:
            for k in range(1,29):
                ParserWeather(i, t, k, 90245, f)
        else:
            for k in range(1,31):
                ParserWeather(i, t, k, 90245, f)

f.close()
openfile = open('weatherData_90245_2014-2015.csv')
writefile= open('modifiedweatherData_90245_2014-2015.csv','w')
writer=csv.writer(writefile)
csv_f= csv.reader(openfile)
temprow=[]
for row in csv_f :
    if len(row) ==12 and row[0]!='Time(PDT)':
        if len(temprow)==0:
            temprow.append(row)

        elif row[0][:2]!=temprow[-1][0][0:2] or row[0][-2:]!=temprow[-1][0][-2:]:
            if len(temprow[0][0])==8:
                write_to_file=temprow[0][0][0:3]+'00'+temprow[0][0][5:]+','
            else:
                write_to_file=temprow[0][0][0:2]+'00'+temprow[0][0][4:]+','
            temptemp=0
            tempdew=0
            temphum=0
            temppre=0
            tempvis=0
            tempevent=''
            count=0
            for i in temprow:
                if i[1] == '-':
                    temptemp += 0
                else:
                    temptemp+=float(i[1][0:4])
                if len(i[2])==9:
                    tempdew+=float(i[2][0:4])
                elif i[2]=='-':
                    tempdew+=0
                else:
                    tempdew += float(i[2][0:2])
                if len(i[3]) == 3:
                    temphum += float(i[3][0:2])
                elif len(i[3]) == 2:
                    temphum += float(i[3][0:1])
                elif len(i[3]) ==4 and i[3][0]=='1':
                    temphum+= float(i[3][0:3])
                else:
                    temphum += 0
                if i[4]=='-':
                    temppre+=0
                else:
                    temppre+=float(i[4][0:5])
                if len(i[5])==8:
                    tempvis+=float(i[5][0:4])
                elif i[5]=='-':
                    tempvis+=0
                else:
                    tempvis +=float(i[5][0:3])
                if i[10]!='':
                    tempevent=i[10]
                count+=1
            temptemp=round(temptemp/count,1)
            tempdew =round(tempdew / count,1)
            temphum=round(temphum/count,2)
            temppre=round(temppre/count,2)
            tempvis=round(tempvis/count,2)
            write_to_file+=str(temptemp)+temprow[0][1][-5:]+','+str(tempdew)+temprow[0][2][-5:]+','+str(temphum)+temprow[0][3][-1:]+','+str(temppre)+temprow[0][4][-4:]+','+str(tempvis)+temprow[0][5][-4:]+','
            for t in range(6,10):
                write_to_file+=temprow[0][t]+','
            write_to_file+=str(tempevent)+','+temprow[0][-1]+'\n'
            writefile.write(write_to_file)
            temprow=[]
            temprow.append(row)
        elif row[0][:2]==temprow[-1][0][0:2] and row[0][-2:]==temprow[-1][0][-2:]:
            temprow.append(row)
    else:
        if len(temprow)==0:
            writer.writerow(row)
        else:
            if len(temprow[0][0])==8:
                write_to_file=temprow[0][0][0:3]+'00'+temprow[0][0][5:]+','
            else:
                write_to_file=temprow[0][0][0:2]+'00'+temprow[0][0][4:]+','
            temptemp=0
            tempdew=0
            temphum=0
            temppre=0
            tempvis=0
            tempevent=''
            count=0
            for i in temprow:
                if i[1] == '-':
                    temptemp += 0
                else:
                    temptemp+=float(i[1][0:4])
                if len(i[2])==9:
                    tempdew+=float(i[2][0:4])
                elif i[2]=='-':
                    tempdew+=0
                else:
                    tempdew += float(i[2][0:2])
                if len(i[3]) == 3:
                    temphum += float(i[3][0:2])
                elif len(i[3])==2:
                    temphum += float(i[3][0:1])
                else:
                    temphum+=0
                if i[4]=='-':
                    temppre+=0
                else:
                    temppre+=float(i[4][0:5])
                if len(i[5])==8:
                    tempvis+=float(i[5][0:4])
                elif i[5]=='-':
                    tempvis+=0
                else:
                    tempvis +=float(i[5][0:3])
                if i[10]!='':
                    tempevent=i[10]
                count+=1
            temptemp = round(temptemp / count, 1)
            tempdew = round(tempdew / count, 1)
            temphum = round(temphum / count, 2)
            temppre = round(temppre / count, 2)
            tempvis = round(tempvis / count, 2)
            write_to_file+=str(temptemp)+temprow[0][1][-5:]+','+str(tempdew)+temprow[0][2][-5:]+','+str(temphum)+temprow[0][3][-1:]+','+str(temppre)+temprow[0][4][-4:]+','+str(tempvis)+temprow[0][5][-4:]+','
            for t in range(6,10):
                write_to_file+=temprow[0][t]+','
            write_to_file+=str(tempevent)+','+temprow[0][-1]+'\n'
            writefile.write(write_to_file)
            writer.writerow(row)
            temprow = []
openfile.close()
writefile.close()