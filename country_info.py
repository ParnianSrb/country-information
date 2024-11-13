import requests, csv
from bs4 import BeautifulSoup

response = requests.get('https://www.scrapethissite.com/pages/simple/')
soup = BeautifulSoup(response.content, 'html.parser')
div_countries = soup.find_all('div', attrs={'class': 'col-md-4 country'})

with open('Country-Info.csv', 'w') as f:
    writer = csv.writer(f)

    for index in range(20):
        country_name = div_countries[index].h3.text.strip()
        country_capital = div_countries[index].div.find('span', attrs={'class': 'country-capital'}).text
        country_population = int(div_countries[index].div.find('span', attrs={'class': 'country-population'}).text)
        country_area = div_countries[index].div.find('span', attrs={'class': 'country-area'}).text

        country_info = [f'Name = {country_name}', f'\nCapital = {country_capital}', f'\nPopulation = {country_population}', f'\nArea = {country_area}\n\n\n']

        writer.writerow(country_info)



    # print(country_name, country_capital, country_population, country_area)