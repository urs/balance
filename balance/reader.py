from os.path import join, dirname, realpath
import csv

def read_transactions(filename, mappings = {}):
    lines = _read_file(filename)
    lines.pop(0)

    if not mappings:
        mappings = _load_default_mappings()

    return [ _map(item, mappings) for item in _parse_csv(lines) ]


def _load_default_mappings():
    filename = join(dirname(realpath(__file__)), 'mappings.json')
    with open(filename) as f:
        return json.loads(f.read())


def _read_file(filename):
    with open(filename, 'r') as f:
        lines = [ line for line in f ]
    return lines


def _parse_csv(iter):
    return [ row for row in csv.reader(iter, delimiter=";") ]


def _map(line, mappings):
    return {
        fieldname: line[index]
        for fieldname, index in mappings
    }

