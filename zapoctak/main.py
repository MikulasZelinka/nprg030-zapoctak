from zapoctak import napis_zapoctak
import os

DATA_PATH = '../data/'
ZAPOCTAK_PATH = 'zapoctak.txt'

os.makedirs(DATA_PATH, exist_ok=True)
with open(os.path.join(DATA_PATH, ZAPOCTAK_PATH), 'w') as f:
    print(napis_zapoctak(jazyk='python', zajimavost=17), file=f)
