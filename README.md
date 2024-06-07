 # READING LOG AND BOOK TRACKER WITH API
    #### Video Demo:  <https://www.youtube.com/watch?v=9jWcqzijw18>
    #### Description: This is a program that allows the user to search books from the Open Library API and add them to their reading lists. It can recommend books from the user reading list and list them as a table in the terminal.

 ## **The main function**
   * The first thing that the user gets when openning the program is the welcoming message. Using **INQUIRER**, the user will get in the command line these choices :

      1. **Search book**
      1. **Add read book**
      1. **Add to Want to Read**
      1. **Check read books list**
      1. **Check Want to read list**
      1. **Recommend a book from my reading list**

---
 ## **Function 1: Search book**
   * By selecting in the command line prompt the first option **Search Book**,
   the user will be asked to input the ***title*** and the name of the ***author*** of a book. No need to type the whole name of the book or the whole name of the author. In most cases a word from the title and the first name of the author are enough to get a result.
   * The progress will be animated with **YASPIN** and the text *...Loading...*
   * Then the program will use the **Open Library API** to get the information *name of the book, all the authors names if they are 2 or more, and the year it was first published* from its database.
   * If by chance there is no result from the search, the user will be prompted again for the *name of the book and the title*, until the user will input valid books and authors name.
   * After being prompted the result from the search, the user will have two options :
      * to search again for another book
      * to exit the program
   * If the first option is chosen, the whole process will be repeated, until the user decides to exit the program.

---
 ## **Function 2: Add book**
   * By selecting this option the user will have the option to create a new CSV file with the name ***read.csv*** in which the user can add all the book he/she read.
   * The file will be created automatically if the file does not exist in the program directory.
   * If the file does not exist or it's empty, the program will create it, and if the user wants to add a book that he/she read, the program will create a header automatically.
   * If the file exists, but does not contain any information or its empty, the program will add new books to the list, will create a header,but will not create a new header each time a book it's added.
   * If the file exists and contains information or it contains the header at least, and the user wants to add a book to his/hers read books list, the program will detect that and will not create a new header if one exists.
   * After adding a book to the reading list, the user will have the option to continue to add books to the list, or just exit the program.
   * The list of books can be viewed in the ***read.csv*** file. Every time the user adds a book to the list, the informations from the book will be written in the csv file.

---
  ## **Function 3: Add to reading list**
   * By selecting this option the user will have the option to create a new CSV file with the name ***want_to_read.csv*** in which the user can add all the book he/she wants to read.
   * The file will be created automatically if the file does not exist in the program directory.
   * If the file does not exist or it's empty, the program will create it, and if the user wants to add a book that he/she read, the program will create a header automatically.
   * If the file exists, but does not contain any information or its empty, the program will add new books to the list, will create a header,but will not create a new header each time a book it's added.
   * If the file exists and contains information or it contains the header at least, and the user wants to add a book to his/hers reading list, the program will detect that and will not create a new header if one exists.
   * After adding a book to the reading list, the user will have the option to continue to add books to the list, or just exit the program.
   * The list of books can be viewed in the ***want_to_read.csv*** file. Every time the user adds a book to the list, the informations from the book will be written in the csv file.

   ---

 ## **Function 4: Check Read Books**
  * When selecting this function the program opens the ***read.csv*** file and and it creates an easy to read table in the command line using **TABULATE**.
  * This function is used to make it easier for the user to handle the program, so the user doesn't have to go into the ***read.csv*** everytime he/she wants to view the read books list.

---
 ## **Function 5: Check Want To Read List**
  * When selecting this function the program opens the ***want_to_read.csv*** file and and it creates an easy to read table in the command line using **TABULATE**.
  * This function is used to make it easier for the user to handle the program, so the user doesn't have to go into the ***want_to_read.csv*** everytime he/she wants to view the reading list.

---

 ## **Function 6: Recommend a Book**
  * When selecting this function the program opens the ***want_to_read.csv*** file and and it returns a random book from the  reading list using **TABULATE**.
  * This function helps choose a book to read from the reading list when the user is in doubt about what to read next.

