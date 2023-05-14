import json
from googlesearch import search
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

class WebScraper:
    def __init__(self, query, folder_id):
        self.query = query
        self.folder_id = folder_id
        self.file_data = []
        self.drive = self.authenticate_drive()

    def authenticate_drive(self):
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()  # Creates local webserver and auto handles authentication
        return GoogleDrive(gauth)

    def search_web(self):
        for url in search(self.query, num_results=100):
            result = {"url": url, "title": url.title()}
            self.file_data.append(result)
            self.check_file_size_and_upload()

    def check_file_size_and_upload(self):
        if len(json.dumps(self.file_data)) > 1024 * 1024 * 10:  # 10MB
            self.upload_to_drive()
            self.file_data = []

    def upload_to_drive(self):
        file = self.drive.CreateFile({"title": "cats_facts.json", "parents": [{"id": self.folder_id}]})
        file.SetContentString(json.dumps(self.file_data))
        file.Upload()

# Usage
scraper = WebScraper("cats facts", "your_folder_id")
scraper.search_web()

