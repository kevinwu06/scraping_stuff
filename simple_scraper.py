import time

from main import models
from main.mechanizehelper import create_browser
from lxml.html.soupparser import fromstring as parse_html


def get_or_create_espnid(espn_id, date):
    espn_id_object, created = models.EspnId.objects.get_or_create(value=espn_id)
    if len(models.EspnId.objects.filter(value=espn_id)) == 2:
        espn_id_object.delete()
        print 'duplicate'
    else:
        print espn_id_object


def espn_schedule():
    for year in [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]:
        time.sleep(30)
        for month in [3, 4, 5, 6, 7, 8, 9, 10]:
            for day in [1, 8, 15, 22, 29]:
                if month == 3:
                    if day != 29:
                        continue
                time.sleep(2)
                if day < 10:
                    day = '0%s' % (day)
                if month < 10:
                    month = '0%s' % (month)
                date = int('%s%s%s' % (year, month, day))
                browser = create_browser()
                page = browser.open('http://espn.go.com/mlb/schedule?date=%s' % date)
                html = parse_html(page.read())
                for tr in html.cssselect('.mod-content tr'):
                    for a in tr.cssselect('td a'):
                        link = a.get('href')
                        print link
                        try:
                            espn_id = int(link.split('?id=')[1])
                            print espn_id
                            get_or_create_espnid(espn_id=espn_id, date=date)
                        except:
                            continue
                        break