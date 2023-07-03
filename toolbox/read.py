import json

def read_txt(file):
    with open(file) as f:
        return f.read().splitlines()

def read_json(file):
    with open(file) as f:
        return json.load(f)