# imports
from datetime import date, timedelta

import requests
from bs4 import BeautifulSoup

# 'https://pogoda.meta.ua/ua/Kyivska/Kyivskiy/Kyiv/'

# main list with all data
list_all_day = []


def getDataFromSiteNow():
    """
    func which take data from  site that describe above
    and return dict with today`s weather data
    :return:
    dictionary with weather data
    """
    dict_today = {}
    # getting site data
    r = requests.get('https://pogoda.meta.ua/ua/Kyivska/Kyivskiy/Kyiv/')
    soup = BeautifulSoup(r.text, 'lxml')
    divs = soup.find('main', class_='main').find_all('table', {'class': 'city__table active'})
    # searching by attr 'data-id' in html
    res = [x['data-id'] for x in divs]
    # establishing today date and adding to the dict
    dict_today['date'] = res[0]
    # searching temp data
    temp = soup.find('main', class_='main'). \
        find('table', class_='city__table active').find('div', class_='temperature')
    # getting out the text with temp data
    temp = temp.get_text()
    # adding temp data to the dict
    dict_today['temp'] = temp
    # searching description data by attr that was pointed at that test task
    desc_data = soup.find('main', class_='main'). \
        find('table', class_='city__table active'). \
        find('div', class_='right').find('div', class_='img').find_all('img')
    # catching then adding to the dict
    desc = [x['title'] for x in desc_data]
    dict_today['descript'] = desc[0]
    return dict_today


def getDataFromSite():
    """
    func which take data from  site that describe above
    and return list with in a 5 days`s weather data
    :return:
    list with in a 5 days`s  weather data
    """
    date_now = date.today()
    """launching loop to define range for days 
    which need to take from the weather site """
    for date_ in range(0, 5):
        dict_all = {}
        date_ += 1
        end_date = str(date_now + timedelta(days=date_))
        # getting site data
        r = requests.get(f'https://pogoda.meta.ua/ua/Kyivska/Kyivskiy/Kyiv/{end_date}/ajax/')
        soup = BeautifulSoup(r.text, 'lxml')
        divs = soup.find_all('table', {'class': 'city__table active'})
        res = [x['data-id'] for x in divs]
        dict_all['date'] = res[0]
        temp = soup.find('table', class_='city__table active').find('div', class_='temperature')
        temp = temp.get_text()
        dict_all['temp'] = temp
        desc_data = soup.find('table', class_='city__table active'). \
            find('div', class_='right').find('div', class_='img').find_all('img')
        desc = [x['title'] for x in desc_data]
        dict_all['descript'] = desc[0]
        # adding all the data to main list
        list_all_day.append(dict_all)
    return list_all_day


def main():
    """ main func that need to start all this script
    and adding data from the getDataFromSiteNow()
    :return:
    list with all the data
    """
    res_ = getDataFromSiteNow()
    # adding info from getDataFromSiteNow()
    list_all_day.append(res_)
    getDataFromSite()
    return list_all_day


if __name__ == '__main__':
    main()
