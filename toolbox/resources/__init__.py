# %%
from toolbox import get_directory
from pathlib import Path
from pprint import pprint

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

    xml_dict = {}
    for name in path.glob('**/*.xml'):
        xml_dict[name.name] = name
    
    urdf_dict = {}
    for name in path.glob('**/*.urdf'):
        urdf_dict[name.name] = name

    asset_path = dict(xml=xml_dict, urdf=urdf_dict)
    print(f"Available assets for {name}:")
    pprint(asset_path)
    return asset_path


# %%
if __name__ == '__main__':
    robot_names = get_robot_names()
    name = robot_names[0]

    get_asset_from_name(name)
    