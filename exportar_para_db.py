# encoding: UTF-8
import pymongo, csv
from pymongo import MongoClient

path = "lista.csv"
arquivo = open(path, newline='')
next(arquivo)
next(arquivo)
for linha in arquivo:
	print(linha[1])
	#post = {"usuario": "linha[0]", "src": "", "dst": "", "dcontext": "", "clid": "", "channel": "", "dstchannel": "", "lastapp": "", "calldate": "", "answerdate": "", "hangupdate": "", "duration": "", "billsec": "", "disposition": "", "amaflags": "", "uniqueid": "", "userfield": ""}
	#print(post)
else:
  print("Finally finished!") 

#cluster = MongoClient("mongodb+srv://dbadmin:Jackoff2019@cluster0-blkbq.gcp.mongodb.net/test?retryWrites=true&w=majority")

#db = cluster["issabel0718"]
#collection = db["usuarios"]

#post = {"nome": "Fabio", "sobrenome": "Salesse", "Celular": "4499423161"}
#collection.insert_one(post)