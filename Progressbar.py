import tkinter as tk
from tkinter import ttk

class Progressbar:
	def __init__(self, frame):
		self.target_frame = frame
		self.progressbar = ttk.Progressbar(self.target_frame, orient="horizontal", value=0, length=200, mode="determinate")
		self.progress_update = tk.StringVar()
		self.progressbar.grid(row=2, column=1, sticky="we")
		self.progressbar_message = ttk.Label(self.target_frame, textvariable=self.progress_update)
		self.progressbar_message.grid(row=3, column=1)

	def start_display(self):
		self.progressbar.start()

	def stop_display(self, number_of_docs):
		self.progressbar.stop()
		self.progress_update.set("Done Downloading " + str(number_of_docs) + " Documents")

	def update_display(self, number_of_docs, doc_number):
		if number_of_docs > 0:
			increase_value = doc_number/number_of_docs
		elif number_of_docs == 0:
			increase_value = 0

		self.progressbar['value'] = increase_value * 100
		self.progress_update.set(str(doc_number) + " of " + str(number_of_docs) + " Google Docs Downloaded")