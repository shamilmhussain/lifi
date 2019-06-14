
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homeview),
    path('AddStudent/',views.addstudent),
    path('ViewStudent/',views.viewstudent),
    path('DeleteStudent/',views.deletestudent),
    path('AddBook/',views.addbook),
    path('DeleteBook/',views.deletebook),
    path('SearchBookID/',views.searchbyid),
    path('SearchBookName/',views.searchbyname),
    path('SearchBookAuthor/',views.searchbyauthor),
    path('BookIssue/',views.issuebook),
    path('BookRenew/',views.renewbook),
    path('BookReturn/',views.returnbook),
]
