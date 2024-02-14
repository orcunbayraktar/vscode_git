class Library :
    global f

    def __init__(self): # constructer mrtod
        self.f = open("books.txt","a+")

    def listBooks(self):     #liste listeleme bookData->satır bilgiler,bookValues->kitabın özellileri
        self.f = open("books.txt","r")
        bookData = self.f.read().splitlines()
          
        for bookValues in bookData :
            bookNameAuthor = bookValues.split(",")
            print("Books name : " + bookNameAuthor[0] + " - Book author : " + bookNameAuthor[1])
        self.f.close()

    def addBook(self): #dosyada kitap ekleme
        self.f = open("books.txt","a+")
        bookName = input("Enter book name : ")
        bookAuthor = input("Enter book Author : ")
        bookReleaseDate = input("Enter book ReleaseDate : ")
        bookNumberOfPages = input("Enter book NumberofPages : ")
        
        bookDetails =  bookName + "," + bookAuthor + "," + bookReleaseDate + "," + bookNumberOfPages + "\n" 
        self.f.write(bookDetails)
        self.f.close()
    

    def removeBook(self): #dosyada kitap silme
        self.f = open("books.txt","r+")
        bookDatasList = self.f.read().splitlines()
        inputBookName=input("Enter the book you want to delete: ")
        
        for index,bookValues in enumerate(bookDatasList) : #enumate index değeri tutar
            bookValuesList= bookValues.split(",")           
            if(inputBookName == bookValuesList[0]) : 
                bookDatasList.pop(index)              
        with open("books.txt","w") as filee :
            for i in bookDatasList :
                filee.write(i + "\n")
        self.f.close()
        

    def isThere(self,str): #dosyada var mı?
        self.f = open("books.txt","r+")
        bookDatasList = self.f.read().splitlines()
        for bookValues in bookDatasList :
            bookValuesList= bookValues.split(",")
            if(str == bookValuesList[0]) :
                return True
            else : 
                return False
          
        
    def menuSelect(self): #menu
        print("*************************")
        print("1-List Books")
        print("2-Add Books")
        print("3-Remove Books")
        print("4-Exits")
        print("*************************")
        select = input("Enter the Select(1-4): ")
        if select == "1" :
            self.listBooks()
            self.menuSelect()
        elif select == "2" :
            self.addBook()
            self.menuSelect()
        elif select == "3" :
            self.removeBook()
            self.menuSelect()
        elif select == "4" :
            exit()
        else :
            print("You made a wrong choice")
            self.menuSelect()
    
    def destructorFile(self) : #dosya kapatma metotodu
        self.f.close()
        exit()


lib = Library()
lib.menuSelect()
lib.destructorFile()



