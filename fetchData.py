import sys
import wget

'''
fetch data from yahoo finance
example, this link will fetch CRM's historical data from yahoo finance
from Jan 23 2014 - Dec 29 2014 -->
http://real-chart.finance.yahoo.com/table.csv?s=CRM&a=00&b=23&c=2014&d=11&e=29&f=2014&g=d&ignore=.csv
'''

tickSymbol = sys.argv[1]

def getStartDate (date):
    dates = date.split('.')
    print dates
    return '&a=' + getMonthStr(dates[0]) + 'b=' + dates[1] + '&c=' + dates[2] 

def getEndDate (date):
    dates = date.split('.')
    return '&d=' + getMonthStr(dates[0]) + 'e=' + dates[1] + '&f=' + dates[2] 

def getMonthStr(month):
    return str(int(month) - 1).zfill(2)

url = 'http://real-chart.finance.yahoo.com/table.csv?s=' + tickSymbol + getStartDate(sys.argv[2]) + getEndDate(sys.argv[3]) + '&g=d&ignore=.csv'

print url

filename = wget.download(url)

