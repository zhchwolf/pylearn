#!/usr/bin/env python3
# -*- coding:utf-8 -*-

user,passwd = 'horace','123'
login_status = 0

def login(func):
    def inner():
        global login_status
        if login_status == 0:
            user_name = input("user name:")
            password = input("password:")
            if user_name == user and password == passwd:
                print("welcome...")
                login_status = 1
                func()
        else:
            func()
    return inner

def logout():
    print("You have logout the site.")
    global login_status
    login_status = 0

@login
def home():
    print('home...')

@login
def finance():
    print('finance...')

@login
def book():
    print('book...')

def enter_page():
    while True:
        page = input('''choose page you go:
        >>home
        >>finance
        >>book
        >>exit
        >>''')
        if page == 'home':
            home()
        elif page == 'book':
            book()
        elif page == 'finance':
            finance()
        elif page == 'exit':
            logout()
            break

enter_page()


