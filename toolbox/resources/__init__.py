# %%
from toolbox import get_directory
from pathlib import Path
from pprint import pprint
from enum import Enum

RESOURCE_PATH = get_directory(__file__)

ROBOT_PATH = RESOURCE_PATH / 'assets/robots'
MANAGERIE_PATH = RESOURCE_PATH / 'assets/mujoco_menagerie'


    
class ASSET_SRC(Enum):
    CUSTOM = 0
    MENAGERIE = 1

def get_asset_from_name(name:str, TYPE=ASSET_SRC.CUSTOM, XML=True):
    if TYPE is ASSET_SRC.CUSTOM:
        path = ROBOT_PATH
    elif TYPE is ASSET_SRC.MENAGERIE:
        path = MANAGERIE_PATH
    else:
        raise ValueError(f"Unknown asset type {TYPE}")
    
    if XML:
        xml_dict = {}
        for name in path.glob('**/*.xml'):
            xml_dict[name.name] = name
        
        pprint(xml_dict)
        return xml_dict
    else:
        urdf_dict = {}
        for name in path.glob('**/*.urdf'):
            urdf_dict[name.name] = name
        pprint(urdf_dict)
        return urdf_dict

    # asset_path = dict(xml=xml_dict, urdf=urdf_dict)
    # print(f"Available assets for {name}:")
    # pprint(asset_path)
    # return asset_path


# %%
if __name__ == '__main__':
    name = 'go1'
    get_asset_from_name(name, ASSET_SRC.MENAGERIE)
    