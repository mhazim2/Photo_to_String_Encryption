import base64
from twofish import Twofish
import glob
import h5py
import sys

if __name__ == "__main__":
    dir_image_encrypt = glob.glob('uploads\image.encrypt.txt')
    # print dir_image_encrypt
    # open binary file in read mode
    image_encrypt_with_padding_ext = open(dir_image_encrypt[0], 'rb')
    image_encrypt_read_with_padding_ext = image_encrypt_with_padding_ext.read()
    image_encrypt_split_with_padding_ext = image_encrypt_read_with_padding_ext.split('.')
    image_encrypt_without_padding = image_encrypt_split_with_padding_ext[0]
    padding = image_encrypt_split_with_padding_ext[1]
    image_encrypt_decode = base64.decodestring(image_encrypt_without_padding)
    # print padding
    # print image_encrypt_without_padding

    # algo decrypt
    T = Twofish(sys.argv[1])  # keynya
    # decrypt

    # ngebagi string cipher per 16 sama kek awal
    n = 16
    list_cipher = [''.join(image_encrypt_decode[i:i + n]) for i in range(0, len(image_encrypt_decode), n)]
    # print list_cipher
    plain = ""
    result_FIX = ""
    for i in range(0, len(list_cipher)):
        plain += T.decrypt(list_cipher[i]).decode()
    # print plain
    # ngilangin padding yang ditambah diawal
    # for i in range(0, len(plain) - int(padding)):
    result_FIX += plain[:-int(padding)]
    # print "Plain Textnya : " + result_FIX

    extension = image_encrypt_split_with_padding_ext[2]
    image_decrypt = open('downloads/image.'+extension, 'wb')  # create a writable Image
    image_decrypt.write(base64.decodestring(result_FIX))
    image_decrypt.close()
