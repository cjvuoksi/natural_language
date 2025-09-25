import json
import sqlite3
import os
from openai import OpenAI

directory = os.path.dirname(__file__)
setupPath = os.path.join(directory, 'food.sql')
dbPath = os.path.join(directory, 'food.db')
addDataPath = os.path.join(directory, 'addFood.sql')
configPath = os.path.join(directory, 'config.json')
schema: str
common = "Use the following schema and respond with sqlite syntax: "

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
    schema = setupFile.read()
    cursor.executescript(schema)
    cursor.executescript(addFile.read())

def query_db(query: str):
  return cursor.execute(query).fetchall()

def gpt(query: str):
  global client
  client.models.list()
  response = client.responses.create(
    model=config['model'],
    input=query,
    service_tier="flex"
  )
  return response.output_text

def parse_sql(response: str):
  gpt_start_sql_marker = "```sql"
  gpt_end_sql_marker = "```"
  if gpt_start_sql_marker in response:
    response = response.split(gpt_start_sql_marker)[1]
  if gpt_end_sql_marker in response:
    response = response.split(gpt_end_sql_marker)[0]

  return response

def gpt_(text):
  try:
    response = gpt(text)
    return response
  except Exception as e:
    print(e)
    return ""

def send_to_api(query: str):
  global db_init
  if db_init:
    setup_db()
    db_init = False
  text = "\n".join([common, schema, query])
  return send_api(text, query, schema)

def send_api(text: str, query: str | None = None, schema: str | None = None) -> str:
  global db_init
  if db_init:
    setup_db()
    db_init = False
  response = gpt_(text)
  sql = parse_sql(response)
  print(f'Sql response: {sql}')
  try:
    results = query_db(sql)
    print(f'Database results: {results}')
    if query is None:
      query = text.split(';')[-1]
    if schema is None:
      schema = ""
    else:
      schema = f" about this db ${schema}"
    final = gpt_(f'This question was asked ${query}${schema}. Answer it using the results of a query (${results}) in one short sentence')
    return final
  except Exception as e:
    print(e)
    return "Error"