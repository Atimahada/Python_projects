from bs4 import BeautifulSoup
import requests
import csv

with open('accra_avail_hotels.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Name', 'Price', 'Rating'])
    url = 'https://www.booking.com/searchresults.html?label=gen173nr-1FCAEoggI46AdIM1gEaKcBiAEBmAExuAEXyAEM2AEB6AEB-AECiAIBqAIDuAKB2PaYBsACAdICJGIxZTc4YmRiLTZmZTgtNDEyZS1iZjIwLTU1NDQ2NDQ5NjliY9gCBeACAQ&sid=e0ac1b1e04591a768e23eaf246419b7e&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.html%3Flabel%3Dgen173nr-1FCAEoggI46AdIM1gEaKcBiAEBmAExuAEXyAEM2AEB6AEB-AECiAIBqAIDuAKB2PaYBsACAdICJGIxZTc4YmRiLTZmZTgtNDEyZS1iZjIwLTU1NDQ2NDQ5NjliY9gCBeACAQ%26sid%3De0ac1b1e04591a768e23eaf246419b7e%26sb_price_type%3Dtotal%26%26&ss=Accra%2C+Greater+Accra%2C+Ghana&is_ski_area=&checkin_year=2022&checkin_month=9&checkin_monthday=16&checkout_year=2022&checkout_month=9&checkout_monthday=18&efdco=1&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&ss_raw=ghana&ac_position=0&ac_langcode=en&ac_click_type=b&dest_id=-2067935&dest_type=city&iata=ACC&place_id_lat=5.600427&place_id_lon=-0.187796&search_pageview_id=dade43806e2e01b5&search_selected=true&search_pageview_id=dade43806e2e01b5&ac_suggestion_list_length=5&ac_suggestion_theme_list_length=0'
    no_of_pages = 1
    offset = 25
    while no_of_pages < 15:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

        source = requests.get(url, headers=headers)
        soup = BeautifulSoup(source.content, 'lxml')

        properties = soup.find('div', class_='d4924c9e74').find_all('div', class_='a826ba81c4')

        for property_ in properties:
            try:
                name = property_.find('div', class_='fcab3ed991 a23c043802').text
                price = property_.find('span', class_="fcab3ed991 bd73d13072").text
                rating = property_.find('div', class_="b5cd09854e d10a6220b4").text

            except AttributeError:
                rating = None
            print('------------')

            csv_writer.writerow([name, price, rating])
            print(name, price, rating)

        url = f'https://www.booking.com/searchresults.html?label=gen173nr-1FCAEoggI46AdIM1gEaKcBiAEBmAExuAEXyAEM2AEB6AEB-AECiAIBqAIDuAKB2PaYBsACAdICJGIxZTc4YmRiLTZmZTgtNDEyZS1iZjIwLTU1NDQ2NDQ5NjliY9gCBeACAQ&sid=e0ac1b1e04591a768e23eaf246419b7e&aid=304142&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.html%3Flabel%3Dgen173nr-1FCAEoggI46AdIM1gEaKcBiAEBmAExuAEXyAEM2AEB6AEB-AECiAIBqAIDuAKB2PaYBsACAdICJGIxZTc4YmRiLTZmZTgtNDEyZS1iZjIwLTU1NDQ2NDQ5NjliY9gCBeACAQ%26sid%3De0ac1b1e04591a768e23eaf246419b7e%26sb_price_type%3Dtotal%26%26&ss=Accra%2C+Greater+Accra%2C+Ghana&is_ski_area=&checkin_year=2022&checkin_month=9&checkin_monthday=16&checkout_year=2022&checkout_month=9&checkout_monthday=18&efdco=1&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&ss_raw=ghana&ac_position=0&ac_langcode=en&ac_click_type=b&dest_id=-2067935&dest_type=city&iata=ACC&place_id_lat=5.600427&place_id_lon=-0.187796&search_pageview_id=dade43806e2e01b5&search_pageview_id=dade43806e2e01b5&search_selected=true&ac_suggestion_list_length=5&ac_suggestion_theme_list_length=0&offset={offset}'
        offset += 25
        print(f'Page num {no_of_pages}')
        no_of_pages += 1
        print('+++++++++++')
