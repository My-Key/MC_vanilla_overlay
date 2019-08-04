# Tools

## Reqires Python 3 and [Pillow](https://pillow.readthedocs.io/en/stable/ "Pillow")

#### Overlay Maker
- apply alpha from already created set of overlay tiles to applied tile

**Parameters:**
1. tile - path to tile file
2. index of first source tile
3. index of first output tile

**Example:**
python overlayMaker.py red_sand.png 0 17
It will create tiles from 17.png to 33.png based on alpha from tiles from 0.png to 16.png with colors form red_sand.png

------------

#### Palette Swap
- apply palette from tile to already created set of overlay tiles

**Parameters:**
1. tile - path to tile file, source of palette
2. index of first source tile
3. index of first output tile

**Example:**
python paletteSwap.py red_sandstone.png 0 17
It will create tiles from 17.png to 33.png based on  tiles from 0.png to 16.png with applied palette form red_sandstone.png