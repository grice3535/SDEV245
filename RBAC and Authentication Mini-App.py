'''
Program Name: RBAC and Authentication Mini-App
Author: Gillian Rice
Date: October 29, 2025
Description:
    This program is a simple script preforming the core topics of authentication,
    roles, and access control.
'''

users = {'admin': 1, 'user': 2}

def backend():
    print("Hello from backend")

def frontend():
    print("Hello from frontend")

def access_route(username, route):
    role = users.get(username)
    if route == "backend" and role == 1:
        backend()
    elif route == "frontend" and role == 2:
        frontend()
    else:
        print("Access denied")

access_route("admin", "backend")
access_route('addin', 'frontend')
access_route('user', 'frontend')
access_route('user', 'backend')