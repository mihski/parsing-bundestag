import requests
from bs4 import BeautifulSoup
import json

# person_url_list =[]
# for i in range(0, 760, 20):
#     url = f"https://www.bundestag.de/ajax/filterlist/en/members/863330-863330?limit=20&noFilterSet=true&offset={i}"
#
#     q = requests.get(url)
#     result = q.content
#
#     soup = BeautifulSoup(result,"lxml")
#     persons = soup.find_all("a")
#     for person in persons:
#         person_page_url = person.get("href")
#         person_url_list .append(person_page_url)
#
# with open("person_url_list.txt","a")as file:
#     for line in person_url_list:
#         file.write(f"{line}\n")


with open("person_url_list.txt") as file:
    lines = [line.strip() for line in file.readlines()]

    data_dict = []
    counter = 0
    for line in lines:
        q = requests.get(line)
        result = q.content

        soup = BeautifulSoup(result, "lxml")
        person = soup.find(class_="bt-biografie-name").find("h3").text
        person_name_company = person.strip().split(",")
        person_name = person_name_company[0]
        person_company = person_name_company[1]

        person_social_net = soup.findAll(class_="bt-link-extern")

        person_social_net_url = []
        for item in person_social_net:
            person_social_net_url.append(item.get("href"))

        data = {
            "person_name": person_name,
            "company_name": person_company,
            "social_networks": person_social_net_url
        }
        counter += 1
        print(f"{counter}: {line}")

        data_dict.append(data)

        with open("json_dat", "w") as f:
            json.dump(data_dict, f, indent=4)

# q = requests.get("https://www.bundestag.de/en/members/abdi_sanae-861028")
# result = q.content

# soup = BeautifulSoup(result,"lxml")
# person = soup.find(class_="bt-biografie-name").find("h3").text
# person_name_company = person.strip().split(",")
# person_name = person_name_company[0]
# person_company = person_name_company[1].strip()
#
# print(person)
# print(person_name)
# print(person_company)
