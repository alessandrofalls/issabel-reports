import pymongo, csv
from pymongo import MongoClient

with open("lista.csv", encoding="utf8") as csv_file:
	csv_reader = csv.reader(csv_file)
	next(csv_reader)
	next(csv_reader)
	lista = []
	for linha in csv_reader:
		post = {"usuario": linha[0], "centro_custo": linha[1], "funcao": linha[2]}
		lista.append(post)
	else:
		print("Finally finished!") 
		print(lista)

cluster = MongoClient("mongodb+srv://dbadmin:Jackoff2019@cluster0-blkbq.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["ad0718"]
collection = db["colaboradores"]
collection.insert_many(lista)

#post = {"usuario": "Alex", "centro_custo": "Sureg", "funcao": "Técnico"}
#collection.insert_one(post)


#collection.delete_many({}) #apagar todos os documentos da coleção
'''
{usuario: {$regex: 'alessandro'}}
db.test.find({A: {$regex: 'Star Wars'}})

'''