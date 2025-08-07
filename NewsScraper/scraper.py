import requests
from bs4 import BeautifulSoup

# Function to scrape news headlines
def scrape_headlines(url):
    # Send a GET request to the website
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all <h2> tags (or adjust based on the website structure)
        headlines = soup.find_all('h2')
        
        # Extract text from each headline and save to a list
        headlines_text = [headline.text for headline in headlines]
        
        # Save headlines to a .txt file
        with open('headlines.txt', 'w') as file:
            for headline in headlines_text:
                file.write(headline + '\n')
        
        print("Headlines have been successfully scraped and saved to headlines.txt")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# Main execution
if __name__ == "__main__":
    # URL of the news website to scrape
    news_url = 'https://www.bbc.com/news'  # Replace with the actual news website URL
    scrape_headlines(news_url)
