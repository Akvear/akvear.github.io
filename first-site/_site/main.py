import requests
from bs4 import BeautifulSoup
from googlesearch import search
import os

url = "https://motorsporttickets.com/blog/10-greatest-formula-1-drivers-in-history/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
else:
    print("Failed!")
    exit()

driver_elements = soup.select("h2")
driver_elements.pop(0)
driver_elements.reverse()

drivers = [" ".join(driver.text.split()[-2:]) for driver in driver_elements if driver.text.strip()]

# Print extracted names
print("Top 11 Formula 1 Drivers:")
for i, driver in enumerate(drivers, 1):
    print(f"{i}. {driver}")

index_md = '---\n\nlayout: post\n\n---\n\n'

# Generate main page (index.md)
index_md += "# Top 11 Greatest Formula 1 Drivers\n\n"
index_md += "Over the years there's been nearly 1000 different drivers fighting for the world championship.\n\n"
index_md += "The biggest question is who is the best?\n\n"
index_md += "| Rank | Driver |\n"

for i, driver in enumerate(drivers, 1):
    slug = driver.lower().replace(" ", "-") 
    index_md += f"| {i} | [{driver}](pages/{slug}.html) |\n"

# Save the main markdown file
with open("index.markdown", "w", encoding="utf-8") as f:
    f.write(index_md)

print("Main page created: index.markdown")

# Generate sub-pages for each driver
for driver in drivers:
    slug = driver.lower().replace(" ", "-")  # Convert to URL-friendly format
    driver_md = f"---\ntitle: {driver}\nlayout: post\n---\n\n"
    driver_md += f"# {driver}\n\nMore information about {driver} will be added here.\n"

    # Save driver markdown file
    with open(f"pages/{slug}.markdown", "w", encoding="utf-8") as f:
        f.write(driver_md)

    print(f"Sub-page created: {slug}.markdown")
