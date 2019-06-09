import json
import os


class Jsonwork:
    def jsonwrite(self, data, file):
        with open(file, 'w') as write_file:
            json.dump(data, write_file)
        return file

    def jsonread(self, file):
        with open(file, 'r') as read_file:
            data = json.load(read_file)
        return data

    def jsoncombine(self, file1, file2, newfile):
        with open(file1, 'r') as read_file:
            data1 = json.load(read_file)
        with open(file2, 'r') as read_file:
            data2 = json.load(read_file)
        newdata = json.dumps(data1) + json.dumps(data2)
        with open(newfile, 'w') as write_file:
            json.dump(newdata, write_file)
        return newfile

    def absolute(self, file):
        abspath = os.path.abspath(file)
        return abspath

    def relative(self, file):
        relpath = os.path.relpath(file)
        return relpath


c = Jsonwork()
print(c.jsonread('data_file.json'))
data = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
c.jsonwrite(data, 'newdata.json')
c.jsoncombine('data_file.json', 'newdata.json', 'newfile.json')
print(c.absolute('data_file.json'))
print(c.relative('data_file.json'))
