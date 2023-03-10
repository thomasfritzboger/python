import requests
from bs4 import BeautifulSoup
import textwrap

def get_toc_dict():
    # Hent indholdet af oversigten på Wikipedia-siden
    response = requests.get("https://en.wikipedia.org/wiki/Alan_Turing")
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find overskrifterne på siden og opbyg toc_dict
    toc_dict = {}
    headings = soup.select('div.vector-toc-text')
    striped_list = []
    for heading in headings:
        heading_text = ''
        for child in heading.children:
            if child.name != 'span':
                heading_text += str(child)
        striped_list.append(heading_text.strip())

    striped_list.pop(0)

    for key, heading in enumerate(striped_list):
        href = f'#{heading.replace(" ", "_")}'
        toc_dict[heading] = href

    return toc_dict

def search_toc(dictionary, word, soup):
    search_words = word.lower().split()
    for key in dictionary.keys():
        if all(search_word in key.lower() for search_word in search_words):
            link = dictionary[key]
            section = soup.find(id=link[1:])
            content = ''
            for elem in section.find_all_next():
                if elem.name == 'h3':
                    break
                elif elem.name == 'p':
                    content += '\n' + elem.get_text()
            return content.strip()
    return f"No section found matching '{word}'"

def main():
    toc_dict = get_toc_dict()
    response = ''
    while response.lower() != 'quit':
        response = input('Enter a keyword to search for a section, or "quit" to exit: ')
        if response.lower() == 'quit':
            break
        result = search_toc(toc_dict, response, soup)
        if result:
            lines = textwrap.wrap(result, width=80)
            print(f"Content for section related to '{response}':")
            for line in lines:
                print(line)
        else:
            print(f"No section found matching '{response}'.")

if __name__ == '__main__':
    # Hent indholdet af siden
    response = requests.get("https://en.wikipedia.org/wiki/Alan_Turing")
    soup = BeautifulSoup(response.content, 'html.parser')
    main()
