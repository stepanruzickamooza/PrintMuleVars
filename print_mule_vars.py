#!/Users/stepanruzicka/.pyenv/versions/3.8.7/bin

# author        : Stepan Ruzicka
# date          : 2022.08.22
# email         : stepan@mooza.io

import argparse
import yaml
import re

def read_yaml_file_as_dict(file_path):
   with open(file_path) as f:
       data = yaml.load(f, Loader=yaml.FullLoader)
   return data

def updatecurrentkey(currentkey, key, delimiter = '.'):
    if currentkey:
        return currentkey + delimiter + key
    else:
        return key

def flatten_dict(dictionary, currentkey=""):
    children={}
    for key, value in dictionary.items():
        new_key = updatecurrentkey(currentkey, key)
        if isinstance(value, dict):
            grandchildren=flatten_dict(value, new_key)
            children = {**children, **grandchildren}
        else:
            children[new_key] = value
    return children

def main():
   parser = argparse.ArgumentParser()
   parser.add_argument(
        "-d", "--debug", dest="debug",
        help="Debug mode", action="store_true")

   parser.add_argument(
        "-f", "--file", dest="file",
        help="Input yaml file", required=True)

   parser.add_argument(
        "-i", "--item", dest="item",
        help="Item", required=False)

   parser.add_argument(
        "-r", "--replace-regular-expression", dest="regularexpression",
        help="Regular expression", default=r"\1=\2", required=False)

   parser.add_argument(
        "-s", "--output-separator", dest="separator",
        help="Output separator", default="\n", required=False)

   args = parser.parse_args()

   yaml_dict = read_yaml_file_as_dict(args.file)

   yaml_flatten_dict = {}
   yaml_flatten_dict = flatten_dict(yaml_dict)

   result_array = []
   result = ""
   for key, value in yaml_flatten_dict.items():
      if (args.item and key.startswith(args.item)) or (args.item is None): 
         if isinstance(value, list):
           result = re.sub('^([^|]+)\|\|\|\|(.+)$', r"{}".format(args.regularexpression), key + "||||" + args.separator.join(value))
         else:
           result = re.sub('^([^|]+)\|\|\|\|(.+)$', r"{}".format(args.regularexpression), key + "||||" + value)
         result_array.append(result)

   print(args.separator.join(result_array))

if __name__ == "__main__":
   main()
