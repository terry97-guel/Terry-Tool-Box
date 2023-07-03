# %%
from toolbox import get_directory
from pathlib import Path
# from pprint import pprint

RESOURCE_PATH = get_directory(__file__)

ROBOT_PATH = RESOURCE_PATH / 'assets/robots'

def get_robot_names():
    path = ROBOT_PATH
    names = []
    for path_ in path.iterdir():
        names.append(path_.name)
    print(f'Available robots: {names}')
    return names
    
    
def get_asset_from_name(name:str):
    path = ROBOT_PATH / name

    robot_names = get_robot_names()
    if name not in robot_names:
        raise FileNotFoundError(f"Can not find {name} from robot names {robot_names}.")

    names = []
    for path_ in path.iterdir():
        if path_.suffix in ['.xml', '.urdf']:
            names.append({path_.name: path_.absolute()})
    print(f"Available assets for {name}: {names}")
    return names


# %%
if __name__ == '__main__':
    robot_names = get_robot_names()
    name = robot_names[0]

    get_asset_from_name(name)