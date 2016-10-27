import ruamel.yaml as yaml

with open("vdm.yaml") as stream:
    try:
        print(yaml.load(stream))
    except yaml.YAMLError as exc:
        print(exc)
