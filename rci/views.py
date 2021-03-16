from django.shortcuts import render

def index(self):
    return render(self, 'index.html')

def user(self):
    return render(self, 'user.html')