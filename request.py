import cv2
import base64


if __name__ == "__main__":
    image_to_test = cv2.imread('teste.png')
    base64_image = base64.b64encode(cv2.imencode('.png', image_to_test)[1]).decode()
    texto = base64_image
    with open('base64.txt', 'w') as arquivo:
        arquivo.write(texto)
        arquivo.close()
