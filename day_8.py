# #library management
# books={}
# def add_book(book_id,book_title,author,copies):
#     if book_id in books:
#         print("id existed")
#         return
#     else:
#         books[book_id]={
#             "title":book_title,
#             "author":author,
#             "number of copies":copies
#         }
# print("Book added successfully")
# def search_book(keyword):
#     found=False
#     for book_id,book in books.items():
#         if keyword.lower() in book["title"].lower() or keyword==book_id:
#             print(book_id,book)
#             found=True
#     if not found:
#         print("Book not found")
# def return_book(book_id):
#     if book_id in books:
#         books[book_id]["copies"]+=1
#         print("book returned successfully")
#     else:
#         print("invalid book id")
# while True:
#     print("\n 1.add_book")
#     print("2.search book")
#     print("3.return book")
#     choice=input("enter your choice")

#     if choice=="1":
#         bid=input("book id :")
#         title=input("title :")
#         author=input("author :")
#         copies=int(input("num of copies :"))
#         add_book(bid,title,author,copies)
#     elif choice=="2":
#         keyword=input("enter book id or title")
#         search_book(keyword)
#     elif choice=="3":
#         bid=input("enter book id :")
#         return_book(bid)
#     else:
#         print("invalid")
    
class Duck:
    def walking(self):
        print("Duck is walking")
class Human:
    def walking(self):
        print("human is walking")
class Robort:
    def walking(self):
        print("human is walking")
def walk(obj):
    obj.walking()
walk(Duck())
walk(Human())
walk(Robort())



        