import os, sys
from PIL import Image

main = Image.open( sys.argv[1] )

if main.mode != 'RGBA':
    main = main.convert('RGBA')

fromS = int(sys.argv[2])
fromO = int(sys.argv[3])

r,g,b,a = main.split();

for i in range(0, 17):
	if os.path.exists(str(fromS + i) + ".png"):
		mask = Image.open( str(fromS + i) + ".png" )
		rm,gm,bm,am = mask.split()
		im = Image.merge("RGBA", (r, g, b, am))
		im.save(str(fromO + i) + ".png")
    
