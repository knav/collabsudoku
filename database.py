import pymongo
import math

print("hello")
client = pymongo.MongoClient("mongodb+srv://adminav:<adminav>@cluster0.pfjma.mongodb.net/collab_sudoku?retryWrites=true&w=majority")
db = client["collab_sudoku"]
map_collection = db["sudoku_maps"]
user_collection = db["user"]
