import ruamel.yaml as yaml

with open("test.yaml") as stream:
    try:
        print(yaml.load(stream))
    except yaml.YAMLError as exc:
        print(exc)
