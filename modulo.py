import cv2
import base64
import numpy as np


class Map_Search:
    def __init__(self) -> None:
        self.original_map = cv2.imread('API/Felucca.png')


    def verifica_resultado(self, string: str):
        image_to_verify = base64.b64decode(string)
        png_as_np = np.frombuffer(image_to_verify, dtype=np.uint8)
        image_to_verify_decoded = cv2.imdecode(png_as_np, flags=1)
        original_map = self.original_map
        try:
            result = []
            metod = cv2.TM_CCOEFF_NORMED
            result.append(cv2.matchTemplate(original_map, image_to_verify_decoded, method=metod))
            for a in result:
                (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(a)
                (startX, startY) = maxLoc
                endX = startX + image_to_verify_decoded.shape[1]
                endY = startY + image_to_verify_decoded.shape[0]
                x = int(((startX + endX)/2)-20)
                y = int(((startY + endY)/2)-15)
        except:
            print('ERRO 404', 'Mapa não encontrado')
            x = 0
            y = 0
        return (x , y)

