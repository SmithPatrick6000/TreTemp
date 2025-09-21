
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import os

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(title = "Select CSV File", filetypes=[("CSV Files", "*.csv")])

if file_path:
    book = pd.read_csv(file_path, sep="\t", encoding='utf-16')

    skip_one = book.columns[1]
    cleaned_val = []


    for val in book[skip_one]:
        if isinstance(val, str):
            stripped = val.strip()
            if stripped and stripped[-1].isalpha():
                try:
                    num = float(stripped[:-1])
                    cleaned_val.append(num)
                except ValueError:
                    continue
        elif isinstance(val, (int, float)):
            cleaned_val.append(val)


    if cleaned_val:

        max_val = max(cleaned_val)
        min_val = min(cleaned_val)

        num_columns = len(book.columns)
        book['Max'] = None
        book['Min'] = None

        book.at[1, 'Max'] = max_val
        book.at[1, 'Min'] = min_val



        book.to_csv(file_path, index=False, encoding='utf-16', sep='\t')

        os.startfile(file_path)
    else:
        print("No valid data found")
else:
    print("No file selected")
