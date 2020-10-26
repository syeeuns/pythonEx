from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbjungle

target_movie = db.movies.find_one({'title':'알라딘'})
print(target_movie['rate'])

targets = list(db.movies.find({'rate':target_movie['rate']}))
for a in targets:
    print(a['title'])

db.movies.update_one({'title':'매트릭스'},{'$set' : {'rate':0}})
matrix = db.movies.find_one({'title':'매트릭스'})

print(matrix)
