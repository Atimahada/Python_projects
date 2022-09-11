from bs4 import BeautifulSoup
import requests
import csv

try:
    site = requests.get('https://www.imdb.com/chart/top/')
    site.raise_for_status()

    soup = BeautifulSoup(site.text, 'html.parser')
    movies = soup.find('tbody', class_="lister-list").find_all('tr')

    with open('imdb_top_movies.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['rank', 'title', 'year', 'rating'])
        for movie in movies:
            rank = movie.find('td', class_="titleColumn").get_text(strip=True).split('.')[0]
            title = movie.find('td', class_="titleColumn").a.text
            year = movie.find('td', class_="titleColumn").span.text[1:-1]
            rating = movie.find('td', class_ = "ratingColumn imdbRating").strong.text

            csv_writer.writerow([rank, title, year, rating])
            print(rank, title, year, rating)

except Exception as e:
    print(e)


