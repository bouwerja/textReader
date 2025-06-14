import os 
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

import easyocr
from datetime import datetime
import warnings
import logging

start_time = datetime.now()

os.environ['CUDA_VISIBLE_DEVICES'] = ''
reader = easyocr.Reader(['en'], gpu=False)

warnings.filterwarnings("ignore", message = "'pin_memory' argument is set as true but no accelerator is found")
logging.getLogger('easyocr').setLevel(logging.ERROR)

result = reader.readtext('test.png')
if result:
    detected_text = result[0][1]
    print(f"Your text is: {detected_text}")
else:
    print("No text detected")

end_time = datetime.now()
delta_time = end_time - start_time
delta_formatted = delta_time.total_seconds()
print(f"Total seconds: {delta_formatted}")
