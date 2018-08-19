from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

# Hier wird der Pfad zum Verzeichnis des ».py«-Files gesetzt
# Erspart einem das Herumgehample in TextMate mit dem os.getcwd()
# und os.path.join()
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

me = Image.open("images/jkantel2.jpg")
arr = np.array(me.getdata(), np.uint8).reshape(me.size[1], me.size[0], 3)

plt.imshow(arr)
plt.colorbar()
plt.show()
