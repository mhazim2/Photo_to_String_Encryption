import base64
from twofish import Twofish
import glob
import h5py
import sys

if __name__ == "__main__":
    dir_image = glob.glob('uploads\image.*')

    # open binary file in read mode
    image = open(dir_image[0], 'rb')
    image_read = image.read()
    image_encode = base64.encodestring(image_read)

    # algo encrypt
    T = Twofish(sys.argv[1])  # keynya
    # encrypt
    # nambahin padding + ngebagi string per 16, soalnya twofish inputnya 16 byte
    if len(image_encode) % 16 != 0:
        padding = 16 - len(image_encode) % 16
        for i in range(0, padding):
            image_encode += 'X'

    n = 16
    list_plain = [''.join(image_encode[i:i + n]) for i in range(0, len(image_encode), n)]

    cipher = ""
    for i in range(0, len(list_plain)):
        cipher += T.encrypt(list_plain[i])

    extension = dir_image[0].split('.')[1]
    cipher_encoded = base64.encodestring(cipher)
    cipher_encoded = cipher_encoded + '.' + str(padding) + '.' + extension

    image_encrypt = open('downloads\image.encrypt.txt', 'wb')
    image_encrypt.write(cipher_encoded)
    image_encrypt.close()

    # save the feature vector using HDF5
    h5f_image_encrypt = h5py.File('downloads\image.encrypt.hdf5', 'w')
    h5f_image_encrypt.create_dataset('image_encrypt', data=cipher_encoded)
    h5f_image_encrypt.close()

    # print cipher_encoded
