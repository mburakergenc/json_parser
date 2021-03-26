### json_parser

- json_parser is a pipeline where a given json input is mapped to a certain format and saved back to postgres table

# How to run the code

- First create the database using the given make file
  `make run-db` <br>
  To run this succesfully you need to have docker installed in your environment. More information can be found on [https://docs.docker.com/engine/install/.](https://docs.docker.com/engine/install/. "https://docs.docker.com/engine/install/.")

- Then, install dependencies; <br>
  `pip install -r requirements.txt`

- Then run models.py to create a new database using sqlalchemy as the ORM; <br>
  `python -m src.models`

- We can now run our parser to parse the data and save it in Postgres <br>
  `python -m src.parser` <br>
  The parser can be written in pure Python to reduce the package size, but Pandas is fun and gives a lot of out of the box methods for rapid development.

# How to run the tests

- In the current format there is only one requirement tested. This is open to improvement. For example we can also try to test the datetime fileds before parsing to make sure they are type of a datetime object. <br>
  `python -m unittest tests.test_pipeline`
