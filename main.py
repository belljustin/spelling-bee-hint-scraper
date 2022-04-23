from bs4 import BeautifulSoup
from datetime import date
import requests

URL_FORMAT = "https://www.nytimes.com/{}/crosswords/spelling-bee-forum.html"

class Grid:
    def __init__(self, header, letter_to_values):
        self.header = header
        self.letter_to_values = letter_to_values

    def __str__(self):
        output = ' \t' + '\t'.join(self.header) + '\n'
        for letter, values in self.letter_to_values.items():
            values = [str(v) for v in values]
            output += letter + '\t' + '\t'.join(values) + '\n'
        return output

if __name__ == '__main__':
    today = date.today()
    formatted_date = today.strftime("%Y/%m/%d")
    url = URL_FORMAT.format(formatted_date)

    r = requests.get(url, headers= {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})

    soup = BeautifulSoup(r.text, 'html.parser')
    grid = soup.body.find(text="Spelling Bee Grid").parent.next_sibling.next_sibling.next_sibling.next_sibling

    grid_text = grid.text
    end_of_header_index = grid_text.index('Σ')
    header = list(filter(lambda x: x, grid_text[:end_of_header_index].split(' ')))

    letter_to_values = dict()
    rows = grid_text[end_of_header_index+1:].split(':')
    next_letter = rows[0][-1]
    for row in rows[1:-1]:
        parsed_row = []

        values = list(filter(lambda x: x, row.split(' ')))
        for v in values[:-1]:
            parsed_row.append(0 if v == '-' else int(v))

        last_value = values[-1][:-1]
        parsed_row.append(0 if last_value == "-" else int(last_value))

        letter_to_values[next_letter] = parsed_row

        next_letter = values[-1][-1]

    grid = Grid(header, letter_to_values)
    print(grid)
