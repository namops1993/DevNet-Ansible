import yaml

def read_yaml(config_file):
    with open(config_file, 'r') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    print(data)

if __name__ == '__main__':
    name_file = 'config2.ini'
    read_yaml(name_file)
    print('Thanks for using')