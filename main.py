import cv2
import requests
import os
from matplotlib import pyplot as plt


class Histogram:
    @staticmethod
    def from_local_file(image_path: str):
        try:
            image_file = cv2.imread(image_path, 0)
            plt.hist(image_file.ravel(), 256, [0, 256])
            plt.show()

        except AttributeError as err:
            print(f'Application error: {err}')

    @staticmethod
    def from_web(image_url: str):
        try:
            response = requests.get(image_url)
            if response.status_code == 200:
                with open('imagem.jpg', 'wb') as file:
                    file.write(response.content)
                    file.close()

                image_file = cv2.imread('imagem.jpg', 0)
                plt.hist(image_file.ravel(), 256, [0, 256])
                plt.show()
                os.remove('imagem.jpg')

            else:
                print('Request error!')

        except requests.ConnectionError as err:
            print(f'Application error: {err}')


if __name__ == '__main__':
    # Histogram.from_local_file('coisa.png')
    Histogram.from_web('https://blog.emania.com.br/wp-content/uploads/2017/02/2-2.jpg')
