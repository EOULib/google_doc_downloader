import requests
import gdown
from bs4 import BeautifulSoup
from tkinter import messagebox

class Downloader:
  def __init__(self):
    self.target_webpage = ''
    self.gdoc_url = ''
    self.gdoc_id = ''
    self.download_directory = ''
    self.gdoc_id_list = []
    self.gdrive_url_prefix = 'https://drive.google.com/uc?export=download&id='
    self.gdoc_domain = 'docs.google.com'

  def set_target_webpage(self, url):
    self.target_webpage = url

  def set_download_directory(self, path):
    self.download_directory = path

  def get_doc_urls(self):
    try:
      grab_urls = requests.get(self.target_webpage)
      if grab_urls.status_code == 200:
        self.soup = BeautifulSoup(grab_urls.text, 'html.parser')
        return "Success"
      else:
        messagebox.showinfo("HTTP ERROR", f"HTTP Request Failed for url {self.target_webpage} with status code: {grab_urls.status_code}")
        return "HTTP ERROR"
    except Exception as e:
      messagebox.showinfo("ERROR", f"HTTP Request Failed for url {self.target_webpage} with the following exception: {e}")
      return "Exception"

  def get_doc_ids(self):
    get_doc_urls_value = self.get_doc_urls()
    if get_doc_urls_value == "Success":
      self.total_docs = 0
      for link in self.soup.find_all("a"):
        self.gdoc_url = link.get('href')
        try:
          if self.gdoc_url.split('/')[2] == self.gdoc_domain:
            self.gdoc_id = self.gdoc_url.split('/')[-2]
            self.gdoc_id_list.append(self.gdoc_id)
            self.total_docs += 1
        except Exception as e:
          continue 
    else:
      return get_doc_urls_value
    
    return self.total_docs

  def run_downloader(self, gui):
    count = 0
    for id in self.gdoc_id_list:
      count += 1
      gui.update_progressbar(self.total_docs, count)
      full_download_url = self.gdrive_url_prefix + id
      try:
          print(f"URL is: {full_download_url} and the directory is: {self.download_directory}")
          gdown.download(full_download_url, self.download_directory)
      except Exception as e:
        messagebox.showinfo("EXCEPTION", f"Download failed for the following reason: {e}")
        self.gdoc_id_list.clear()
        self.total_docs = 0
        gui.update_progressbar(self.total_docs, count)
        return False
    self.gdoc_id_list.clear()