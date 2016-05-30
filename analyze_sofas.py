import json

with open('sofas.json') as f:

    lines = f.readlines()
    for line in lines:
        x = json.loads(line)

        print x['info']['name'], x['info']['dimensions'], x['info']['price']
