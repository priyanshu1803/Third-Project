class Library:

    def __init__(self,slist,name):
        self.booklist=slist
        self.name=name
        self.lendict={}

    def displaybook(self):
        print(f"BOOKS AVAILABE IN:  ***{self.name}***")
        for book in self.booklist:
            print(book)

    def lendbook(self,user,book):
        if book not in self.lendict.keys():
            print("BOOK HAS BEEN LENDED TO YOU...")
            self.lendict.update({book:user})
            
        else:
            print("BOOK IS ALREADY LENDED TO SOMEONE...")

     
    def addbook(self,book):
        self.booklist.append(book)
        print("BOOK HAS BEEN ADDED..")

    def returnbook(self,book):
        self.lendict.pop(book)
        print("BOOK HAS BEEN RETURNED...")

if __name__=="__main__":
    harry=Library(['django','c++','python'],"CODE WITH HARRY")
    while(True):
        print("WELCOME OF THE WORLD'S BEST LIBRARY")
        print("ENTER YPUR CHOICES")
        print("1. DISPLAY A BOOK")
        print("2. LEND A BOOK")
        print("3. ADD A BOOK")
        print("4. RETURN A BOOK")
        userchoice=int(input(""))
        if userchoice==1:
            harry.displaybook()
        elif userchoice==2:
            book=input("enter the book you want to lend:\n")
            user=input("enter your name:\n")
            harry.lendbook(user,book)
        elif userchoice==3:
            book=input("enter the book you want to add:\n")
            harry.addbook(book)

        elif userchoice==4:
            book=input("enter the book you want to return:\n")
            harry.returnbook(book)
        
        else:
            print(" not a valid option")

        print("press q to quit and c to continue")
        user1=input("")
        while user1!='c' and user1!='q':
            if user1=='q':
                print("thanks for coming")
                exit()
            elif user1=='c':
                continue
