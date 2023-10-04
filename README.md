#Scrap_to_drive 🌐

## WebScraper class 🤖

The WebScraper class is a Python-based web scraper that searches the web for a specified query and uploads the results to a Google Drive folder. It uses the googlesearch library to perform the web search and the pydrive library to interact with Google Drive.

## Installation 🛠

Before using the WebScraper class, you need to install the required Python libraries. You can do this with the following command:

\`\`\`bash
pip install googlesearch-python pydrive
\`\`\`

You also need to set up OAuth2 credentials for the Google Drive API. You can follow the instructions in the PyDrive documentation to do this.

## Usage 🚀

To use the WebScraper class, you first need to create an instance of the class with the search query and the ID of the Google Drive folder where you want to save the results:

\`\`\`python
scraper = WebScraper("cats facts", "your_folder_id")
\`\`\`

You can find the ID of the Google Drive folder in the URL of the folder when you open it in a web browser.

After creating the WebScraper instance, you can start the web scraping process by calling the search_web method:

\`\`\`python
scraper.search_web()
\`\`\`

The search_web method will continue to search the web for the query and upload the results to the Google Drive folder until the script is manually stopped.

## Methods 🛠

The WebScraper class has the following methods:

- \_\_init\_\_(self, query, folder_id): This is the constructor method that is called when you create a new instance of the WebScraper class. It takes the search query and the ID of the Google Drive folder as arguments.
- authenticate_drive(self): This method authenticates with the Google Drive API using OAuth2 credentials. It is called automatically when you create a new instance of the WebScraper class.
- search_web(self): This method searches the web for the query and adds the results to the file data. It also checks the size of the file data and uploads it to Google Drive if necessary.
- check_file_size_and_upload(self): This method checks the size of the file data and uploads it to Google Drive if it is larger than a certain size (10MB by default).
- upload_to_drive(self): This method uploads the file data to the Google Drive folder. It is called automatically by the check_file_size_and_upload method when the file data is larger than a certain size.

Please note that the WebScraper class does not actually scrape the content of the webpages in the search results. It only retrieves the URL and the title of each search result. If you want to scrape the content of the webpages, you would need to modify the code to send a GET request to each URL and parse the response with a library like BeautifulSoup.
