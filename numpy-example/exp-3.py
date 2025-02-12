"""
Имя проекта: Boring-numpy
Номер версии: 1.0
Имя файла: exp-3.py
Автор: 2019 © В.В. Костерин, Челябинск

Дата создания: 06/12/2019
Дата последней модификации: 06/12/2019

Связанные файлы/пакеты: numpy, opencv, matplotlib

Описание: загружаем картинку из файла и транспонируем её (поворачиваем на 90)
           всякими разными способаи

#версия Python: 3.6
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

I = cv2.imread('susu-new-year.jpg')[:, :, ::-1]
flg = plt.figure(num=None, figsize=(15, 15), dpi=80, facecolor='w', edgecolor='k')
plt.imshow(I)
plt.show()
flg.savefig('./output-images/ext-31.jpg')

I_ = I.reshape(I.shape[0] // 2, 2, I.shape[1] // 2, 2, -1)
print(I_.shape)
flg = plt.figure(num=None, figsize=(15, 15), dpi=80, facecolor='w', edgecolor='k')
plt.imshow(I_[:, 0, :, 0])
plt.show()
flg.savefig('./output-images/ext-32.jpg')

I_ = np.transpose(I, (1, 0, 2))
flg = plt.figure(num=None, figsize=(15, 15), dpi=80, facecolor='w', edgecolor='k')
plt.imshow(I_)
plt.show()
flg.savefig('./output-images/ext-33.jpg')

I_ = np.swapaxes(I, 0, 1)
flg = plt.figure(num=None, figsize=(15, 15), dpi=80, facecolor='w', edgecolor='k')
plt.imshow(I_)
plt.show()
flg.savefig('./output-images/ext-34.jpg')


