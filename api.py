import cv2
import base64
import numpy as np
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

class B64(BaseModel):
    b64_image: str

app = FastAPI()

@app.post('/maps/')
async def verifica_resultado(b64: B64):
    image_to_verify = base64.b64decode(b64.b64_image)
    png_as_np = np.frombuffer(image_to_verify, dtype=np.uint8)
    image_to_verify_decoded = cv2.imdecode(png_as_np, flags=1)
    original_map = cv2.imread('Felucca.png')
    try:
        result = []
        metod = cv2.TM_CCOEFF_NORMED
        result.append(cv2.matchTemplate(original_map, image_to_verify_decoded, method=metod))
        for a in result:
            x = int(cv2.minMaxLoc(a)[3][0] + 50)
            y = int(cv2.minMaxLoc(a)[3][1] + 50)
            output = list((x, y, 'sucess'))
    except:
        x = 0
        y = 0
        output = list((x, y, 'error'))
    return output

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)