import os
from unittest import TestCase
from api import send_api

directory = os.path.dirname(__file__)
setupPath = os.path.join(directory, 'food.sql')
with open(setupPath) as f:
  schema = f.read()
common = "Give an sqlite select statement that answers the associated question based on the provided schema. Only provide the sqlite syntax. Do not add any other content."
questions = [
  "What is the most purchased food?",
  "Which employees are not customers?",
  "In which states do employees live?"
]

tests = [
  {
    "name": "zero-shot",
    "text": ""
  },
  {
    "name": "double-shot, single domain",
    "text": ""
  },
  {
    "name": "double-shot, single domain",
    "text": ""
  }
]

class Test(TestCase):

  def test_suite(self):
    for test in tests:
      print(test['name'])
      query = "\n".join([schema, common, test['text']])
      value = send_api(query)
      print(value)
      assert value != "Error encountered"


