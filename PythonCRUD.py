#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 21:20:53 2023

@author: alexwells_snhu
"""
from pymongo import MongoClient
from bson.objectid import ObjectId


class AAC_Database():

    def __init__(self, username=None, password=None):
        if username is None:
            USER = 'aacuser'
        else:
            USER = username
        if password is None:
            PASS = 'StarfieldLover2023'
        else:
            PASS = password

        DB = 'AAC'
        COL = 'animals'
        PORT = 30323
        HOST = 'nv-desktop-services.apporto.com'

        self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}')
        self.database = self.client[f'{DB}']
        self.collection = self.database[f'{COL}']

        self.collection = self.database[f'{COL}']

    def create(self, data):
        if data is not None:
            result = self.database.animals.insert_one(data).acknowledged
            return result

        raise Exception("Nothing to save no data recieved")

    def retrieve(self, query):
        try:
            cursor = self.database.animals.find(query)
            result = [document for document in cursor]
            return result
        except Exception as e:
            print(f"Error : {e}")

    def update(self, query, new_values):
        try:
            result = self.database.animals.update_many(query, new_values)
            return result.modified_count
        except Exception as e:
            print(f"Error : {e}")

    def delete(self, query_to_delete):
        try:
            result = self.database.animals.delete_many(query_to_delete)
            return result.deleted_count
        except Exception as e:
            print(f"Error : {e}")

    def close(self):
        self.client.close()
