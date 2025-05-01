import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.ttk import Style
from tkinter.constants import DISABLED, NORMAL

from Clipboard import Clipboard
from Progressbar import Progressbar

class Gui:

	def __init__(self):
		self.window = tk.Tk()
		self.window.title("Bulk Google Doc Downloader")
		self.window.resizable(True, True)
		self.window.minsize(900, 400)
		self.window.maxsize(1300, 500)
		self.window.columnconfigure(0, weight=1)
		self.window.rowconfigure(0, weight=1)
		self.run_button_pushed = False
		self.build_mainframe()
		self.build_header_frame()
		self.build_user_input_frame()
		self.build_bottom_frame()

	def start_interface(self):
		self.window.mainloop()

	def stop_interface(self):
		self.window.quit()

	def set_run_btn_pushed_true(self):
		self.run_button_pushed = True

	def set_run_btn_pushed_false(self):
		self.run_button_pushed = False

	def change_run_button_state(self, state):
		self.run_button['state'] = state

	def get_run_btn_state(self):
		return self.run_button_pushed

	def select_directory(self):
		directory_path = filedialog.askdirectory(title="Choose the directory to save to")
		self.download_directory_value.set(directory_path)

	def get_target_url(self):
		return self.webpage_url_value

	def get_download_directory(self):
		return self.download_directory_value

	def start_progressbar(self):
		self.progressbar.start_display()

	def update_progressbar(self, number_of_docs, doc_number):
		self.progressbar.update_display(number_of_docs, doc_number)

	def stop_progressbar(self, number_of_docs):
		self.progressbar.stop_display(number_of_docs)

	def build_mainframe(self):
		self.main_frame = ttk.Frame(self.window)
		self.main_frame.grid(row=0, column=0, padx=5, pady=5, sticky='new')
		self.main_frame.columnconfigure(0, weight=1)
		self.main_frame.rowconfigure(2, weight=1)

	def build_header_frame(self):
		header_frame = ttk.Frame(self.main_frame)
		header_frame.grid(row=0, column=0, sticky='nsew')
		header_frame.columnconfigure(0, weight=1)
		header_frame.columnconfigure(1, weight=2)
		header_frame.columnconfigure(2, weight=1)

		header_label = ttk.Label(header_frame, text="Google Doc Downloader", font=('Arial', 22))
		header_label.grid(row=0, column=1, padx=20, pady=30)

	def build_user_input_frame(self):
		user_input_frame = ttk.Frame(self.main_frame)
		user_input_frame.grid(row=1, column=0, padx=10, pady=20, sticky='nsew')
		user_input_frame.columnconfigure(0, weight=0)
		user_input_frame.columnconfigure(1, weight=2)
		user_input_frame.columnconfigure(2, weight=0)
		
		webpage_input_label = ttk.Label(user_input_frame, text="Target Webpage URL:", font=('Arial', 14))
		webpage_input_label.grid(row=1, column=0, padx=(10, 10), pady=5, sticky='w')
		self.webpage_url_value = tk.StringVar()
		target_webpage_entry = ttk.Entry(user_input_frame, textvariable=self.webpage_url_value)
		webpage_entry_clipboard = Clipboard()
		webpage_entry_clipboard.add_menu(self.window, target_webpage_entry, self.webpage_url_value)
		target_webpage_entry.grid(row=1, column=1, sticky='ew')

		download_directory_label = ttk.Label(user_input_frame, text="Download Directory:", font=('Arial', 14))
		download_directory_label.grid(row=2, column=0, padx=(10, 10), pady=5, sticky='w')
		self.download_directory_value = tk.StringVar()
		download_directory_entry = ttk.Entry(user_input_frame, textvariable=self.download_directory_value)
		download_directory_clipboard = Clipboard()
		download_directory_clipboard.add_menu(self.window, download_directory_entry, self.download_directory_value)
		download_directory_entry.grid(row=2, column=1, sticky='ew')
		download_directory_browse = ttk.Button(user_input_frame, width=15, text="Select Directory", command=self.select_directory)
		download_directory_browse.grid(row=2, column=2, padx=10, pady=5)

	def build_bottom_frame(self):
		bottom_frame = ttk.Frame(self.main_frame)
		bottom_frame.grid(row=4, column=0, sticky='nsew')
		bottom_frame.columnconfigure(0, weight=1)
		bottom_frame.columnconfigure(1, weight=1)
		bottom_frame.columnconfigure(2, weight=1)

		run_button_style = ttk.Style()
		run_button_style.configure('run.TButton', font=('Arial', 14))
		self.run_button = ttk.Button(bottom_frame, text="Run Downloader", width=30, style='run.TButton', command=self.set_run_btn_pushed_true)
		self.run_button.grid(row=0, column=1, padx=20, pady=(50, 20))

		self.progressbar = Progressbar(bottom_frame)