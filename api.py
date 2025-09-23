import json
import sqlite3
import os
from openai import OpenAI

dir = os.path.dirname(__file__)
setupPath = os.path.join(dir, 'food.sql')
dbPath = os.path.join(dir, 'food.db')
addDataPath = os.path.join(dir, 'addFood.sql')
configPath = os.path.join(dir, 'config.json')
schema: str

db_init = True
cursor: sqlite3.Cursor

# Client config
with open(configPath, 'r') as f:
  config = json.load(f)
client: OpenAI = OpenAI(api_key=config['key'])

def setup_db():
  global cursor, schema
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

def gpt(query: str):
  global client
  response = client.responses.create(
    model=config['model'],
    input=query,
  )
  print(response)
  return response.output_text

def send_api(text: str) -> str:
  global db_init
  if db_init:
    setup_db()
    db_init = False
  try:
    response = gpt(text)
    return response
  except Exception as e:
    print(e)

  return "Error encountered"