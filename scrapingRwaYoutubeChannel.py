#error not as mentioned in the repository, update in few days
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL for tenders page
url = 'https://www.jobinrwanda.com/jobs/tender'

# Send request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all tenders on the page
    tenders = soup.find_all('div', class_='views-row')

    # Create lists to hold the tender data
    tender_titles = []
    tender_dates = []
    tender_locations = []
    tender_links = []

    # Loop through each tender and extract details
    for tender in tenders:
        # Get the title of the tender
        title = tender.find('a').text.strip()
        tender_titles.append(title)

        # Get the date of the tender
        date = tender.find('span', class_='field-content').text.strip()
        tender_dates.append(date)

        # Get the location of the tender
        location = tender.find('div', class_='field field--name-field-location field--type-entity-reference field--label-hidden').text.strip()
        tender_locations.append(location)

        # Get the link to the tender details
        link = 'https://www.jobinrwanda.com' + tender.find('a')['href']
        tender_links.append(link)

    # Save the data to a DataFrame
    tenders_data = pd.DataFrame({
        'Title': tender_titles,
        'Date': tender_dates,
        'Location': tender_locations,
        'Link': tender_links
    })

    # Output the DataFrame
    print(tenders_data)
else:
    print(f"Failed to retrieve tenders. Status code: {response.status_code}")
