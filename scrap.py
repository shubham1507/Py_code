import requests
from bs4 import BeautifulSoup

page = requests.get('https://github.com/trending')

# print(page)

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# print(soup)

# get the repo list
repo = soup.find(class_="Box")

# find all instances of that class (should return 25 as shown in the github main page)
repo_list = repo.find_all(class_='Box-row')

print(len(repo))

for repo_list in repo:

    full_repo_name = repo.find('a').text.strip()

    print(full_repo_name)
