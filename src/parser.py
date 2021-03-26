import json
import pandas as pd
import psycopg2
import io

from sqlalchemy import create_engine
from .models import Obj
from .database import engine
from sqlalchemy.orm import sessionmaker


def create_session():

    Session = sessionmaker(bind=engine)
    Session = Session()
    return Session


def parse_data(json_input):

    Session = create_session()

    df_normalized = pd.json_normalize(json_input)

    items_list = df_normalized['content.marks'][0]

    df_normalized['created'] = pd.to_datetime(df_normalized['created'])
    df_normalized['updated'] = pd.to_datetime(df_normalized['updated'])
    df_normalized['created_date'] = [str(d.date())
                                     for d in df_normalized['created']]
    df_normalized['created_time'] = [str(d.time())
                                     for d in df_normalized['created']]
    df_normalized['updated_date'] = [str(d.date())
                                     for d in df_normalized['updated']]
    df_normalized['updated_time'] = [str(d.time())
                                     for d in df_normalized['updated']]
    df_normalized['counters_total'] = df_normalized['counters.mistakes'] + \
        df_normalized['counters.score']
    df_normalized['items'] = [[d['text'] for d in items_list if 'text' in d]]
    df_normalized.drop(['created', 'updated', 'counters.score',
                        'counters.mistakes', 'type', 'content.marks'], axis=1, inplace=True)

    df_normalized.rename(columns={"address": "path", 'content.description': 'body',
                                  "author.username": "author_name", "author.id": "author_id"}, inplace=True)

    required_fields = ['address', 'id', 'author_name', 'author_id',
                       'created_date', 'created_time', 'counters_total']

    schema = df_normalized.to_json(orient='table', index=False)
    schema_dict = json.loads(schema)
    schema_dict['schema']['required'] = required_fields
    schema_dict = json.dumps(schema_dict)

    return schema_dict


def commit_data(schema_dict, Session):

    blueprint = Obj(obj=schema_dict)

    Session.add(blueprint)
    Session.commit()

    return "Successfully pushed data"


schema_dict = parse_data(json_input={
    "address": "https://www.google.com ",
    "content": {
        "marks": [
            {
                "text": "marks"
            },
            {
                "text": "season"
            },
            {
                "text": "querie"
            },
            {
                "text": "autumn"
            }
        ],
        "description": "Some description"
    },
    "updated": "2021-02-26T08:21:20+00:00",
    "author": {
        "username": "Bob",
        "id": "68712648721648271"
    },
    "id": "543435435",
    "created": "2021-02-25T16:25:21+00:00",
    "counters": {
        "score": 3,
        "mistakes": 0
    },
    "type": "main"
}
)

Session = create_session()
commit_data(schema_dict, Session)
