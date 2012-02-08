#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import hashlib
import pymongo

class User:
    def __init__(self, uid, username, password, email):
        self.uid = uid
        self.username = username
        self.password = password
        self.email = email
    def verify(self, password):
        return self.password == hashlib.sha1(password).hexdigest()
    def change_password(self, password):
        self.password = hashlib.sha1(password).hexdigest()
    def change_email(self, email):
        self.email = email
    def save(self, db): # 1=duplicate key, 2 = other errors, 0 = ok
        db.users.ensure_index('username', unique = True)
        if self.uid == None:
            try:
                uid = db.users.insert(
                        {
                            'username' : self.username,
                            'password' : self.password,
                            'email' : self.email
                        }, safe = True)
            except pymongo.errors.DuplicateKeyError:
                return 1
            except Exception:
                return 2
            self.uid = uid
            return 0
        else:
            try:
                db.users.update({'username' : username},
                        {
                            'username' : self.username,
                            'password' : self.password,
                            'email' : self.email
                        }, safe = True)
            except Exception:
                return 2
            return 0
    def User_from_uid(uid, db):
        k = db.users.find_one({'id' : uid})
        if k != None:
            return User(k['id'], k['username'], k['password'], k['email'])
        else:
            return None
    def User_from_username(username, db):
        k = db.users.find_one({'username' : username})
        if k != None:
            return User(k['id'], k['username'], k['password'], k['email'])
        else:
            return None

