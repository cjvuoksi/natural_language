from api import send_api

common = "Give an sqlite select statement that answers the associated question. Only provide the sqlite syntax. Do not add any other content."
questions = [
  "What is the most purchased food?",
  "Which employees are not customers?",
  "In which states do employees live?"
]

tests = {

}

def test_suite():
  for test in tests:
    test_single(test)

def test_single(input):
  value = send_api(input)
  print(value)