import requests
import json
import csv
import inquirer
from yaspin import yaspin
import os
from tabulate import tabulate
import random



def main():

    welcome = inquirer.list_input("Welcome to Book Tracker" , choices= ['Search book', 'Add read book', 'Add to Want to Read' , 'Check read books list', 'Check Want to read list', 'Recommend a book from my reading list'])

    if welcome == "Search book":
        search_book()
    if welcome == "Add read book":
        add_book()

    if welcome == "Add to Want to Read":
        add_to_reading_list()

    if welcome == "Check read books list":
        check_read_books()

    if welcome == "Check Want to read list":
        check_want_read_books()

    if welcome == "Recommend a book from my reading list":
        recommend_book()


def search_book():
    while True:
        title = input("Enter the book title: ").lower()
        author = input("Enter the author name: ").lower()

        try:
            with yaspin(text="...Loading..."):

                url = f"https://openlibrary.org/search.json?title={title}&author={author}"
                response = requests.get(url)


                if response.status_code == 200:
                    data = response.json()


                    if data['docs']:

                        for book in data['docs'][:1]:
                            author_name = book.get("author_name", ["Unknown author"])
                            title_book = book.get('title', 'No title')
                            first_publish_year = book.get('first_publish_year', 'Unknown year')

                            print()
                            print(f"Author: {', '.join(author_name)}, Title: {title_book}, First Publish Year: {first_publish_year}")
                            print()

                            question = inquirer.list_input("Search for another book? " , choices= ['Yes, I want to search for another book', 'No, exit the program'])

                        if question == "Yes, I want to search for another book":
                            continue
                        if question == "No, exit the program":
                            break

                    else:
                        print("Sorry, the book that you are searching for cannot be found, please try again: ")
                else:
                    print(f"Error {response.status_code}")

        except requests.RequestException:
            print("No results found.")


def add_book():

    while True:

        title_read = input("Enter the book title: ").lower()
        author_read  = input("Enter the author name: ").lower()

        try:
            url = f"https://openlibrary.org/search.json?title={title_read}&author={author_read}"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()

                if data['docs']:

                    file_exists = os.path.exists("read.csv")
                    write_header = not file_exists or os.stat("read.csv").st_size == 0

                    with open("read.csv", mode = "a", newline="") as csvfile:
                        fieldnames = ["Title", " Author's Name", " Publish Year"]
                        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

                        if write_header:
                            writer.writeheader()

                        for book in data['docs'][:1]:
                            titlex = book.get('title', 'N/A')
                            author_name = ', '.join(book.get('author_name', ['N/A'])).replace('"' , "")
                            first_publish_year = book.get('first_publish_year', 'N/A')
                            writer.writerow({
                                "Title" : titlex,
                                " Author's Name" : author_name,
                                " Publish Year" : first_publish_year
                                })
                            print(f"Written to Read Books List: {titlex}, {author_name}, {first_publish_year}")
                            question = inquirer.list_input("Add another book? " , choices= ['Yes, I want to add another book', 'No, exit the program'])

                        if question == "Yes, I want to add another book":
                            continue
                        if question == "No, exit the program":
                            break

                else:
                    print("Sorry, the book that you are trying to add to your read books list cannot be found, please try again: ")
            else:
                print(f"Error {response.status_code}")

        except requests.RequestException:
            print("No results found.")



def add_to_reading_list():
     while True:

        title_to_read = input("Enter the book title: ").lower()
        author__to_read  = input("Enter the author name: ").lower()

        try:
            url = f"https://openlibrary.org/search.json?title={title_to_read}&author={author__to_read}"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()

                if data['docs']:

                    file_exists = os.path.exists("want_to_read.csv")
                    write_header = not file_exists or os.stat("want_to_read.csv").st_size == 0

                    with open("want_to_read.csv", mode = "a", newline="") as csvfile:
                        fieldnames = ["Title", " Author's Name", " Publish Year"]
                        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

                        if write_header:
                            writer.writeheader()

                        for book in data['docs'][:1]:
                            titlex = book.get('title', 'N/A')
                            author_name = ', '.join(book.get('author_name', ['N/A'])).replace('"' , "")
                            first_publish_year = book.get('first_publish_year', 'N/A')
                            writer.writerow({
                                "Title" : titlex,
                                " Author's Name" : author_name,
                                " Publish Year" : first_publish_year
                                })

                            question = inquirer.list_input("Add another book to reading list? " , choices= ['Yes, I want to add another book to my reading list', 'No, exit the program'])

                        if question == "Yes, I want to add another book to my reading list":
                            continue
                        if question == "No, exit the program":
                            break

                else:
                    print("Sorry, the book that you are trying to add to your reading list cannot be found, please try again: ")
            else:
                print(f"Error {response.status_code}")

        except requests.RequestException:
            print("No results found.")

def check_read_books(csv_file="read.csv"):

    with open("read.csv", newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)

    if data:
        headers = data[0]
        rows = data[1:]
        print(tabulate(rows, headers=headers, tablefmt="grid"))
    else:
        print("File is empty")


def check_want_read_books(csv_file_want="want_to_read.csv"):

    with open("want_to_read.csv", newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)

    if data:
        headers = data[0]
        rows = data[1:]
        print(tabulate(rows, headers=headers, tablefmt="grid"))
    else:
        print("File is empty")

def recommend_book(csv_file="want_to_read.csv"):

    with open("want_to_read.csv", newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)

    if data:
        headers = data[0]
        rows = random.choices(data[1:-1])
        print(tabulate(rows, headers=headers, tablefmt="grid"))
    else:
        print("Cannot give recommendation")



if __name__ == "__main__":
    main()






