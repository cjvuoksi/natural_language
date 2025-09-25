import os
from unittest import TestCase
from api import send_api

directory = os.path.dirname(__file__)
setupPath = os.path.join(directory, 'food.sql')
with open(setupPath) as f:
  schema = f.read()
common = "Use the following schema and respond with sqlite syntax: "
questions = [
  "What is the most purchased food?",
  "Where can you purchase beef?",
  "In which states do employees live?",
  "Which employees live in the same state as the store they work at and what is their role?"
]

tests = [
  {
    "name": "zero-shot",
    "text": ""
  },
  {
    "name": "double-shot, single domain",
    "text": "Which employees are also customers?\nSelect first_name, last_name from employee join person on employee.id = person.id join customer on person.id = customer.id;",
  },
  {
    "name": "single-shot, cross domain",
    "text": "Example database: create table person (\n    person_id integer primary key,\n    name varchar(20) not null\n);\n\ncreate table phone (\n    phone_id integer primary key,\n    person_id integer not null,\n    area_code int not null,\n    number int not null,\n    can_recieve_sms tinyint not null,\n    foreign key (person_id) references person (person_id)\n);\n\ncreate table address (\n    address_id integer primary key,\n    person_id integer not null,\n    street varchar(50),\n    zip integer not null\n);\n\ncreate table zip (\n    zip integer primary key,\n    city varchar(35),\n    state_two_letter_code char(2)\n);\n\ncreate table dog (\n    dog_id integer primary key,\n    name varchar(35),\n    breed varchar(35),\n    birth_date date\n);\n\ncreate table award (\n    award_id integer primary key,\n    dog_id integer not null,\n    event_date date,\n    award_name varchar(25) not null,\n    foreign key (dog_id) references dog (dog_id)\n);\n\ncreate table person_dog (\n    dog_id integer,\n    person_id integer,\n    foreign key (dog_id) references dog (dog_id),\n foreign key (person_id) references person (person_id)\n);\n" +
            "Who doesn't have a way for us to text them?  \nSELECT p.person_id, p.name\nFROM person p\nLEFT JOIN phone ph ON p.person_id = ph.person_id AND ph.can_recieve_sms = 1\nWHERE ph.phone_id IS NULL;"
  }
]

class Test(TestCase):

  def test_suite(self):
    for test in tests:
      print(test['name'])
      print('================================================================')
      for question in questions:
        query = "\n".join([common, schema, test['text'], question])
        print(f'Query: {query}')
        value = send_api(query, question, schema)
        print(f'Natural Question and Answer: {question} {value}')
        print('----------------------------------------------------------------------')



