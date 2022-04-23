from bs4 import BeautifulSoup
from datetime import date
import requests
import re

URL_FORMAT = "https://www.nytimes.com/{}/crosswords/spelling-bee-forum.html"

class Grid:
    def __init__(self, header, letter_to_values, two_letters_to_value):
        self.header = header
        self.letter_to_values = letter_to_values
        self.two_letters_to_value = two_letters_to_value

    def __str__(self):
        output = ' \t' + '\t'.join(self.header) + '\n'
        for letter, values in self.letter_to_values.items():
            values = [str(v) for v in values]
            output += letter + '\t' + '\t'.join(values) + '\n'

        for two_letters, value in two_letters_to_value.items():
            output += f'{two_letters}-{value}\n'
        return output

if __name__ == '__main__':
    today = date.today()
    formatted_date = today.strftime("%Y/%m/%d")
    url = URL_FORMAT.format(formatted_date)

    r = requests.get(url, headers= {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})

    soup = BeautifulSoup(r.text, 'html.parser')
    grid = soup.body.find(text="Spelling Bee Grid").parent.next_sibling.next_sibling.next_sibling.next_sibling

	# header
    end_of_header_index = grid.text.index('Σ')
    header = list(filter(lambda x: x, grid.text[:end_of_header_index].split(' ')))

	# body
    letter_to_values = dict()
    raw_rows = grid.text[end_of_header_index+1:]
    rows_regex = re.compile('[A-Z]:(?: +[0-9\-]{1,2})*')
    for row in rows_regex.findall(raw_rows):
        letter = row[0]
        values = list(filter(lambda x: x, row[2:].split(' ')))
        letter_to_values[letter] = [0 if v == '-' else int(v) for v in values]

	# two letter list
    two_letter_list = soup.body.find(text="Two letter list:").parent.parent.next_sibling.text
    two_letter_list_regex = re.compile('[A-Z]{2}-[0-9]{1,2}')

    two_letters_to_value = dict()
    for m in two_letter_list_regex.findall(two_letter_list):
        two_letters, value = m.split('-')
        two_letters_to_value[two_letters] = value

	# build grid
    grid = Grid(header, letter_to_values, two_letters_to_value)
    print(grid)
