import tkinter as tk #tkinter for GUI
from tkinter import ttk
import pandas as pd

# Dataset
df = pd.read_csv('movies.csv')

def get_recommendations():
    genre = genre_var.get()
    language = language_var.get()
    
    results = df
    if genre:
        results = results[results['Genre'].str.lower() == genre.lower()]
    if language:
        results = results[results['Language'].str.lower() == language.lower()]
    
    results = results[['Title', 'Genre', 'Language', 'Year', 'Rating']].sort_values(by='Rating', ascending=False)
    
    output_text.delete("1.0", tk.END)
    if results.empty:
        output_text.insert(tk.END, "No movies found for the selected criteria.")
    else:
        for _, row in results.iterrows():
            output_text.insert(tk.END, f"{row['Title']} ({row['Year']}) - {row['Genre']} [{row['Language']}] - Rating: {row['Rating']}\n")

# main application window
app = tk.Tk()
app.title("Movie Recommendation System")
app.geometry("600x500")
app.configure(bg="#f0f0f0")

# Title Label
title_label = tk.Label(app, text="🎥 Movie Recommender", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# Genre & Language
genre_var = tk.StringVar()
language_var = tk.StringVar()

input_frame = ttk.Frame(app)
input_frame.pack(pady=10)

ttk.Label(input_frame, text="Genre:").grid(row=0, column=0, padx=5, pady=5)
genre_entry = ttk.Entry(input_frame, textvariable=genre_var)
genre_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(input_frame, text="Language:").grid(row=1, column=0, padx=5, pady=5)
language_entry = ttk.Entry(input_frame, textvariable=language_var)
language_entry.grid(row=1, column=1, padx=5, pady=5)

# Search Button
search_button = ttk.Button(app, text="Get Recommendations", command=get_recommendations)
search_button.pack(pady=10)

# Output
output_text = tk.Text(app, wrap=tk.WORD, height=15, width=70, bg="#ffffff")
output_text.pack(pady=10)

app.mainloop()
