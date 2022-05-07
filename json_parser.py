"""
Project under GPLv3
Repository: https://github.com/poloz-z/wmcolors

"""
# Imports.
import json
import jsonschema
from jsonschema import validate

"""
This function loads the given schema at the root folder.
"""
def get_schema():
    with open('json_schema.json', 'r') as file:
        schema = json.load(file)
    return schema

"""
Function to load the test.json at doc/test.json
"""
def get_test():
  with open('./doc/test.json', 'r') as test:
    test = json.load(test)
  return test

"""
Function to validate the json against 
"""
def validate_json():
    """REF: https://json-schema.org/ """
    # Describe what kind of json you expect.
    execute_api_schema = get_schema()
    # Gets the testing json
    json_for_testing = get_test()

    try:
        validate(
          instance=json_for_testing, 
          schema=execute_api_schema
          )
    except jsonschema.exceptions.ValidationError as err:
        print(err)
        err = "Given JSON data is InValid"
        return False

    message = "Given JSON data is Valid"
    return True

"""
Returns a dictionarie with every key-value inside the json.
"""
def parse_json_to_dict(path):
  with open(path, 'r') as palette:
    json_parsed = json.load(palette)
  return json_parsed

