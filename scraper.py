import requests
from bs4 import BeautifulSoup

base_url = 'https://bluelighttickets.co.uk/'
music = 'https://bluelighttickets.co.uk/category/music'
comedy = 'https://bluelighttickets.co.uk/category/comedy'
theatre = 'https://bluelighttickets.co.uk/category/theatre'
attractions = 'https://bluelighttickets.co.uk/category/family-and-attractions'
other = 'https://bluelighttickets.co.uk/category/other'
URLS = {'MUSIC': music, 'COMEDY': comedy, 'THEATRE': theatre, 'ATTRACTIONS': attractions, 'OTHER': other}

ticket_list =[]

def check_ticket_list():
    for name, URL in URLS.items():  
        print(f"======={name}======")
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        ticket_area = soup.find_all('div', {'class': 'col-lg-4 col-md-6 col-sm-12 text-center event'})
        for index in range(0, len(ticket_area)):
            url = ticket_area[index].select('h3')[0].find('a')['href'].strip('../')
            title = ticket_area[index].select('h3')[0].select('span')[0].text.strip()
            location = ticket_area[index].select('p')[2].text.strip()
            date = ticket_area[index].select('p')[0].text.strip()
            if 'london' in location.lower():
                print(title)
                print(location)
                print(date)
                print(f'{base_url}{url}')
                
           
                ticket_list.append([title, location])
    # print(ticket_list)

check_ticket_list()
