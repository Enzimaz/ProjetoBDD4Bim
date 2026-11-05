import os
from pathlib import Path
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv(Path(__file__).with_name('.env'))
uri = os.getenv('MONGO_URI' , 'mongodb+srv://root:root@cluster0.58o4d2w.mongodb.net/')
cliente = MongoClient(uri, serverSelectionTimeoutMS=5000)
cliente.admin.command('ping')
banco = cliente['laboratorio_python']