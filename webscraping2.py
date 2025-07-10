from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://www.gla.ac.uk/undergraduate/degrees/").text
soup = BeautifulSoup(html_text, "lxml")

select_tag = soup.find("select", id = "refinebysubjectselect")
options = select_tag.find_all("option")[1:]
degrees = [opt.get_text(strip = True) for opt in options]

for degree in degrees:
    print(f"- {degree}")


degree_input = input("Please enter the degree you want to do: ")
degree_input = degree_input.replace(" ", "").lower()

html_text = requests.get(f"https://www.gla.ac.uk/undergraduate/degrees/{degree_input}").text
soup = BeautifulSoup(html_text, "lxml")

a_level = "A-level standard entry requirements"
target = None
for p in soup.find_all('p'):
    if a_level in p.get_text():
        target = p

ul = target.find_next_sibling("ul")
requirements = []
for li in ul.find_all("li"):
    text = li.get_text(strip = True)
    requirements.append(text)

print(f"\n{a_level}:")
for req in requirements:
    print(f"- {req}")