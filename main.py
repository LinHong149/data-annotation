# This is method 2, where I get the data on document by scraping. 
# I utilize beautiful soup, prune the unnecessary data, 
import requests
from bs4 import BeautifulSoup

# url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
url = input("Enter url: ")
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
paragraphs = soup.find_all("p")

data = []
def prune(paragraphs):
    while paragraphs[0].get_text() != "y-coordinate":
        paragraphs.remove(paragraphs[0])
    paragraphs.remove(paragraphs[0])
    return paragraphs

paragraphs = prune(paragraphs)
max_x = 0
max_y = 0

# organize data
for i in range(0,len(paragraphs)-2,3): # loops thorough the lines in intervals of 3
    x = int(paragraphs[i].get_text())
    y = int(paragraphs[i+2].get_text())
    max_x = max(x, max_x)
    max_y = max(y, max_y)
    data.append([x, paragraphs[i+1].get_text(), y])


# store data
grid = [[" " for x in range(max_x+1)] for y in range(max_y+1)]
for set in data:
    grid[set[2]][set[0]] = set[1]
grid.reverse()

# print out data
for line in grid:
    for letter in line:
        print(letter, end="")
    print("")

