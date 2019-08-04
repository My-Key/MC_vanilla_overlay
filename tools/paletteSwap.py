import os, sys
from PIL import Image

targetImage = Image.open( sys.argv[1] )

if targetImage.mode != 'RGB':
    targetImage = targetImage.convert('RGB')

targetIndexed = targetImage.convert("P", palette=Image.ADAPTIVE) 
targetPalette = targetIndexed.getpalette()

fromS = int(sys.argv[2])
fromO = int(sys.argv[3])

for i in range(0, 17):
	if os.path.exists(str(fromS + i) + ".png"):
		pattern = Image.open( str(fromS + i) + ".png" )
		rm,gm,bm,am = pattern.split()
		
		pattern = Image.merge("RGB", (rm, gm, bm))
			
		pattern = pattern.convert("P", palette=Image.ADAPTIVE)
		
		pattern.putpalette(targetPalette)
		
		pattern = pattern.convert('RGB')
		r,g,b = pattern.split()
		
		im = Image.merge("RGBA", (r, g, b, am))
		im.save(str(fromO + i) + ".png")