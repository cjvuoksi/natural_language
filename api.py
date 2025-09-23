
import sqlite3
import os
from openai import OpenAI as ai

dir = os.path.dirname(__file__)
setupPath = os.path.join(dir, 'food.sql')
dbPath = os.path.join(dir, 'food.db')
addDataPath = os.path.join(dir, 'addFood.sql')

db_init = True
cursor: sqlite3.Cursor

def setup_db():
  global cursor
  if os.path.exists(dbPath):
    os.remove(dbPath)
  conn = sqlite3.connect(dbPath)
  cursor = conn.cursor()
  with (
    open(setupPath) as setupFile,
    open(addDataPath) as addFile
  ):
    cursor.executescript(setupFile.read())
    cursor.executescript(addFile.read())

def query_db(query: str):
  return cursor.execute(query).fetchall()

def send_api(text: str) -> str:
  global db_init
  if db_init:
    setup_db()
    db_init = False
  print(text)
  value = query_db(text)
  return str(value)