from Downloader import Downloader
from Gui import Gui

import threading
import time
from tkinter import messagebox



class Controller:

    def __init__(self):
        self.downloader = Downloader()
        self.gui = Gui()
        self.program_running = True
        self.while_loop_thread = threading.Thread(target=self.start_program_loop)
        self.while_loop_thread.start()
        self.gui.window.protocol("WM_DELETE_WINDOW", self.close_program_loop)
        self.gui.start_interface()

    def start_program_loop(self):
        while self.program_running:
            time.sleep(.25)
            if self.check_run_button_press():
                self.run_downloader()
                self.gui.set_run_btn_pushed_false()

    def close_program_loop(self):
        self.program_running = False
        self.gui.stop_interface()

    def check_run_button_press(self):
        run_button_state = self.gui.get_run_btn_state()
        return run_button_state
    
    def run_downloader(self):
        self.gui.change_run_button_state('disabled')
        if self.gui.get_target_url().get() == '':
            messagebox.showinfo("ERROR", "Target Webpage URL is a required field.  Click okay and enter a valid URL")
            self.gui.change_run_button_state('normal')
            return False 
        else:
            self.target_url = self.gui.get_target_url().get()
            print(self.target_url)

            if self.gui.get_download_directory().get() == '':
                messagebox.showinfo("ERROR", "Download Directory is a required field.  Click okay and enter a valid directory path")
                self.gui.change_run_button_state('normal')
                return False 
            else:
                self.download_directory = self.gui.get_download_directory().get()
                print(f"This is the original download directory: {self.download_directory}")
                if self.download_directory[-1] != '\\':
                    self.download_directory = self.download_directory + "\\"
                    print(f"This is what it looks like after: {self.download_directory}")
        self.downloader.set_target_webpage(self.target_url)
        self.downloader.set_download_directory(self.download_directory)
        number_of_docs = self.downloader.get_doc_ids()
        if type(number_of_docs) is int:
            if number_of_docs > 0:
                self.downloader.run_downloader(self.gui)
            else:
                number_of_docs = 0
                messagebox.showinfo("ERROR", "No Google Docs were found on that webpage.  Make sure you point to a URL with links to Google Docs")
        self.gui.stop_progressbar(number_of_docs)
        self.gui.change_run_button_state('normal')