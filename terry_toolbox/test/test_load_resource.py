# %%
from terry_toolbox.resources import get_asset_dict, ASSET_SRC

def test_get_asset_dict():
    get_asset_dict(ASSET_SRC.CUSTOM)

get_asset_dict(ASSET_SRC.CUSTOM)