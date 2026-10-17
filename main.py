## Imports ## 

import os

from newsapi import NewsApiClient

from rich.console import Console 
from rich.table   import Table
from rich.prompt  import Prompt

## Imports ##

## Article ## 

class Article: 
    source = ""
    author = ""

    title = ""
    desc  = ""

    url  = ""
    date = ""

    def __init__(self, source, author, title, desc, url, date):
        self.source = source 
        self.author = author 

        self.title = title 
        self.desc  = desc 

        self.url  = url 
        self.date = date

## Article ##

## Functions ## 

def gather_news(api):
    # Gather the information of the top headlines

    headlines = api.get_top_headlines(language="en", category="general", page_size=50)
    articles  = []

    for article in headlines["articles"]:
        source_name = article["source"]["name"]
        author_name = article["author"]

        title = article["title"]
        desc  = "No description"

        if article["description"]:
         desc = article["description"]

        url  = article["url"]
        date = article["publishedAt"]

        articles.append(Article(source_name, author_name, title, desc, url, date))
   
    # Done!
    return articles

def display_news(console, articles):
    # Clear the console from all previous clutter 
    console.clear()

    # Make a table for the news

    table = Table(title="[white on red]Header[/white on red][black on white]News[/black on white]: Get your latest news from your console!", show_lines=True, style="red", highlight=True)

    table.add_column("Source")
    table.add_column("Author")
    
    table.add_column("Date")

    table.add_column("Title")
    table.add_column("Description")

    # Add the news to the table

    for article in articles: 
        table.add_row(article.source, article.author, article.date, f"[link={article.url}][white underline]{article.title}[/white underline][/link]", article.desc)

    # Print 
    console.print(table)

def get_api_key(console, path):
    key = ""

    # Query the user for the API key 

    console.print("[red][ERROR]: Could not find the API key for NewsAPI[/red]")
    console.print("[green][INFO]: Go to [link=https://newsapi.org/][white underline]NewsAPI[/white underline][/link] to generate a new API key[/green]")

    key = Prompt.ask("Enter the API key")

    # Write the new key to the file 

    with open(path, "w") as file: 
        file.write(key)

    # Done!
    return key

## Functions ##

# Create a TUI console 
console = Console() 

# Load the API key

api_file_path = "api_key.txt"
api_key       = ""

if not os.path.exists(api_file_path):
    api_key = get_api_key(console, api_file_path)
else: 
    with open(api_file_path, "r") as file:
        api_key = file.read().strip()

# Load the API 
api = NewsApiClient(api_key=api_key)

# Gather and display the news 

articles = gather_news(api)
display_news(console, articles)
