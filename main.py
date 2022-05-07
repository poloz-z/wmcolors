from json_parser import validate_json, parse_json_to_dict

def main():
 if validate_json():
  parse_json_to_dict("./doc/test.json")
 else:
   print("The config file is corrupt nor doesn't exists.")


main()