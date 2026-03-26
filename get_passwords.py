import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://lucidar.me/en/security/list-of-100000-most-common-passwords/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    container = soup.find('ol', attrs={'id':'passwordList'})
    
    with open('passwords.txt','wt') as file:
        for item in container.find_all(): # type: ignore
            file.write(item.text)
            file.write('\n')


if __name__ == "__main__":
    main()