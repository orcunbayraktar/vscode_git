class Library :
    global f

    def __init__(self):         # constructer metod
        self.f = open("books.txt","a+") 

    def listBooks(self):        # Show Liblary  and Listed with book name in order
        with  open("books.txt","r") as self.f :
            booksDataList = self.f.read().splitlines()
            if booksDataList == list() :
                print("The Library is Empty")
            for bookValues in booksDataList :
                bookValueList = bookValues.split(",")
                print("Book name : " + bookValueList[0].ljust(24," ") + "Author : " + bookValueList[1].ljust(24," "))

    def listBooksAllContents(self):        # Show Liblary  all contents
        with  open("books.txt","r") as self.f :
            booksDataList = self.f.read().splitlines()
            if booksDataList == list() :
                print("The Library is Empty")
            for bookValues in booksDataList :
                bookValueList = bookValues.split(",")
                print("Book name : " + bookValueList[0].ljust(24," ") + "Author : " + bookValueList[1].ljust(24," ") + "Release Year : " + bookValueList[2].ljust(7," ") + "Number of Pages : " + bookValueList[3].ljust(7," "))            
                
        
    def addBook(self):          # Adding a book to the end of library
        with  open("books.txt","a+") as self.f :
            bookDetails =  input("Enter the book name : ") + "," + input("Enter the author : ") + ","
            
            releaseYear = input("Enter the release year : ")           
            while releaseYear.isnumeric() == False :                      # numeric value control on releaseYear 
                print("The value you entered is not numeric, try again")
                releaseYear = input("Enter the release year : ")
            
            numberOfPages = input("Enter the number of pages : ")
            while numberOfPages.isnumeric() == False :                    # numeric value control on number of page 
                print("The value you entered is not numeric, try again")
                numberOfPages = input("Enter the number of pages : ")
            
            bookDetails += releaseYear  + "," + numberOfPages + "\n"
            self.f.write(bookDetails)
           
    def removeBook(self):       #delete books from library
        with  open("books.txt","r+") as self.f :
            booksDataList = self.f.read().splitlines()
            inputBookName=input("Enter the book name to delete: ")
            if self.isThereBookContents(inputBookName,booksDataList) :
                for index,bookValues in enumerate(booksDataList) : 
                    bookValueList= bookValues.split(",")          
                    if(inputBookName == bookValueList[0]) : 
                        booksDataList.pop(index)
                        break              
                
                with open("books.txt","w") as filee :
                    for i in booksDataList :
                        filee.write(i + "\n")
            else :
                print("Enter to remove  book name ((" + inputBookName + ")) is not found in the Library")
    
    def authorInfo(self):       # gives the author's books and releaseOfYear
        with  open("books.txt","r") as self.f :
            booksDataList = self.f.read().splitlines()
            inputAuthorName = input("Enter to Author in the library :  ")

            if self.isThereBookContents(inputAuthorName,booksDataList,1) :
                
                listAuthorDetailsBooks = self.contentsInfo(booksDataList,inputAuthorName)
                listAuthorDetailsRelaseOfYear = self.contentsInfo(booksDataList,inputAuthorName,1,2)
                print("Author information in the library\n*********************************")
                print(inputAuthorName + "'s books are as follows:")
                for i in range(len(listAuthorDetailsBooks)) :
                    print(f" {i+1}.book : {listAuthorDetailsBooks[i]} (" + listAuthorDetailsRelaseOfYear[i] + ")")    
                     
            else :
                print("Enter to remove  Author name ((" + inputAuthorName + ")) is not found in the Library")
        
    def contentsInfo(self,listOfLibrary,queriedInfo,queriedInfoIndex=1,desiredContentIndex =0): # **get Other contents of the queried information**
        list1= list()                                                                           # 0->name , 1-> author , 2->Number of pages , 3-> release year
        for bookValues in listOfLibrary :                                                       # default(Authername,1,0) auther's books name
            bookValueList= bookValues.split(",")                                                # Authername,1,2 -> book release yer                                  
            if(bookValueList[queriedInfoIndex] == queriedInfo) :                
                list1.append(bookValueList[desiredContentIndex])
        return list1

    
    def dataFix(self):          # Edit any book content entered incorrectly
        with  open("books.txt","r+") as self.f :
            booksDataList = self.f.read().splitlines()
            inputBookName = input("Enter the book name of the content you want to **Edit** : ")
            if self.isThereBookContents(inputBookName,booksDataList) :
                inputChoiceContentsIndex=input("What content will you edit? \n1-Book name 2-Author 3-Release of year 4-number of pages : ")
                inputFixedContents=input("Enter the content  you want to Edit : ")
                
                if (inputChoiceContentsIndex == "3" or inputChoiceContentsIndex == "4") : # numeric value control on releaseYear and number of page 
                    while inputFixedContents.isnumeric() == False :
                        print("The value you entered is not numeric, try again")
                        inputFixedContents = input("Enter the release year : ")
                    newBookDataList = self.dataFixCalc(booksDataList,inputBookName,inputFixedContents,int(inputChoiceContentsIndex)-1) #return to list
                    self.f.seek(0)    #cursor reset
                    for i in newBookDataList :
                        self.f.write(i+ "\n")
                    print("Correction has been made.")
                
                elif(inputChoiceContentsIndex == "1" or inputChoiceContentsIndex == "2") :
                    newBookDataList = self.dataFixCalc(booksDataList,inputBookName,inputFixedContents,int(inputChoiceContentsIndex)-1) #return to list
                    self.f.seek(0)    #cursor reset
                    for i in newBookDataList :
                        self.f.write(i+ "\n")
                    print("Correction has been made.")
                
                else :
                    print("Wrong selection made, returns to menu")
                    
            else :
                print("You entered the wrong book name")

    def dataFixCalc(self,booksDataList,inputBookName,inputFixedContents,inputChoiceContentsIndex):  # Calc edit books content
        str = ""
        for count,bookValues in enumerate(booksDataList) :
            bookValueList= bookValues.split(",")
            if(inputBookName == bookValueList[0]) :                                          
                bookValueList[inputChoiceContentsIndex] = inputFixedContents # bookValueList is list

                # To add the list to the main list, convert it to string and add it
                for i in bookValueList :
                    str+=i +","
                str=str[:len(str)-1]    #   "1,2,3,4," convert "1,2,3,4"
                booksDataList[count] = str       
        return booksDataList                                                                     
         
    def sortedBooks(self) : # sorted metod
        with  open("books.txt","r+") as self.f :
            bookDataList = self.f.read().splitlines()
            inputSelectAction=input("How should you sort?? \n1-Book name 2-Release of year 3-Number of pages : ")      
            inputSelectSortBy=input("Sort by ?? 1-Low to High or 2-High-to-Low\nSelect 1 or 2 : ")
            if((inputSelectAction == "1" or inputSelectAction == "2" or inputSelectAction == "3") and (inputSelectSortBy == "1" or inputSelectSortBy =="2")) :
                if inputSelectAction == "1" : 
                    if  inputSelectSortBy == "1":                         
                        bookDataList.sort(key = str.lower)
                    else :
                        bookDataList.sort(key = str.lower,reverse = True)        
                else :
                    if inputSelectSortBy == "1" :
                        bookDataList=self.bubbleSort(bookDataList,int(inputSelectAction))
                    else :
                        bookDataList=self.bubbleSort(bookDataList,int(inputSelectAction))
                        bookDataList.reverse()
                
                self.f.seek(0)
                for i in bookDataList :
                    self.f.write(i + "\n" )
                print("Book library sorting...")
                self.f.seek(0)
                self.listBooksAllContents()
            else :
                print("Choose wrong action, try again ")


    def bubbleSort(self,bookDataList,inputSelectAction):     # bubbleSort returns list        
            for i in range (len(bookDataList)) :                     
                for j in range (len(bookDataList) - i - 1) :
                    bookSplit = bookDataList[j].split(",")
                    nextBookSplit = bookDataList[j+1].split(",")
                    if int(bookSplit[inputSelectAction]) > int(nextBookSplit[inputSelectAction]) :    
                        bookDataList[j],bookDataList[j+1] = bookDataList[j+1], bookDataList[j]      # swaping
            return bookDataList          
     
    def isThereBookContents(self,queriedContent,booksDataList,indexOfNameOrAuthor = 0): # Is there any content in question? return true and false
        for bookValues in booksDataList :                                               # default bookname 
            bookValueList= bookValues.split(",")                                        # 0->name , 1-> author , 2->Number of pages , 3-> release date
            if(queriedContent == bookValueList[indexOfNameOrAuthor]) :
                return True 
        return False           

    def destructorFile(self) :  # file closing method
        self.f.close()
        
    def menuSelect(self):       # menu
        print("*******MENU*******")
        print("1-List Books(name,auther)")
        print("2-List All Contents Books")
        print("3-Add Books")
        print("4-Remove Book")
        print("5-Sort By Content")
        print("6-Author Information")           # Lists all books and release year in the library
        print("7-DataFix")                      # Edit any book content entered incorrectly  
        print("8-Quit")                         # exit
        print("******************")
        select = input("Enter your choice (1-8) : ")
        if select == "1" :
            self.listBooks()
            self.menuSelect()
        elif select == "2" :
            self.listBooksAllContents()
            self.menuSelect()
        elif select == "3" :
            self.addBook()
            self.menuSelect()
        elif select == "4" :
            self.removeBook()
            self.menuSelect()
        elif select == "5" :
            self.sortedBooks()
            self.menuSelect()
        elif select == "6" :
            self.authorInfo()
            self.menuSelect()
        elif select == "7" :
            self.dataFix()
            self.menuSelect()
        elif select == "8" :
            self.destructorFile()
        else :
            print("You made a wrong choice")
            self.menuSelect()
   
lib = Library()
lib.menuSelect()
lib.destructorFile() 








