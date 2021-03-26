import unittest
import json
import src.parser as parser


class TestPipeline(unittest.TestCase):

    def test_processing(self):
        json_input = {
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
        result = parser.parse_data(json_input)

        expected_dict = {"schema": {"fields": [{"name": "path", "type": "string"}, {"name": "id", "type": "string"}, {"name": "body", "type": "string"}, {"name": "author_name", "type": "string"}, {"name": "author_id", "type": "string"}, {"name": "created_date", "type": "string"}, {"name": "created_time", "type": "string"}, {"name": "updated_date", "type": "string"}, {"name": "updated_time", "type": "string"}, {"name": "counters_total", "type": "integer"}, {
            "name": "items", "type": "string"}], "pandas_version": "0.20.0", "required": ["address", "id", "author_name", "author_id", "created_date", "created_time", "counters_total"]}, "data": [{"path": "https://www.google.com ", "id": "543435435", "body": "Some description", "author_name": "Bob", "author_id": "68712648721648271", "created_date": "2021-02-25", "created_time": "16:25:21", "updated_date": "2021-02-26", "updated_time": "08:21:20", "counters_total": 3, "items": ["marks", "season", "querie", "autumn"]}]}
        self.assertEqual(json.dumps(expected_dict), result)
