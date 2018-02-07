# Program: Run Length Encoding
# Class:   CS 251
# Author:  Joel Ristvedt

import struct

infile_path = "assets/picture.bmp" # initial file
comp_path = "assets/picture_comp.raw" # compressed file
outfile_path = "assets/picture_out.bmp" # decompressed file
MAX_LEN = 255

def encode_bmp(inf, outf):
    inf = open(inf, "rb")
    outf = open(outf, "wb")
    bcount = 0
    byte = inf.read(1)
    last_byte = b''
    same_byte_count = 1
    outbcount = 0
    while byte != b'':
        if(byte == last_byte and same_byte_count < MAX_LEN):
            same_byte_count += 1
        elif last_byte != b'':
            outf.write(struct.pack(">B", same_byte_count))
            outf.write(last_byte)
            same_byte_count = 1
            outbcount += 1
        bcount += 1
        last_byte = byte
        byte = inf.read(1)
    outf.write(struct.pack(">B", same_byte_count))
    outf.write(last_byte)

    print("Number of bytes = ", bcount)
    print("Number of bytes out = ", outbcount)
    comp_rate = (bcount - outbcount) / bcount
    print("Rate of Compression: {:.1%}".format(comp_rate))
    print()
    inf.close()
    outf.close()

    return bcount


def decode_bmp(inf, outf):
    inf = open(inf, "rb")
    outf = open(outf, "wb")
    byte = inf.read(1)
    data_info = {'freq': struct.unpack('B',byte)[0], 'data': ''} # index 0 = freq, index 1 = data
    byte = inf.read(1)
    data_info['data'] = byte
    outbcount = 0
    bcount = 0
    while byte != b'':
        i = 0
        while i < data_info['freq']: # write out data
            outf.write(data_info['data'])
            i += 1
            outbcount += 1
        byte = inf.read(1)
        if byte != b'':
            data_info['freq'] = struct.unpack('B',byte)[0]
            byte = inf.read(1)
            data_info['data'] = byte
            bcount += 1
    print("Number of bytes = ", bcount)
    print("Number of bytes out = ", outbcount)
    print()
    inf.close()
    outf.close()
    return outbcount

def Main():
    print()
    bytes_init = encode_bmp(infile_path, comp_path)
    bytes_final = decode_bmp(comp_path, outfile_path)
    if bytes_init == bytes_final:
        print("No data lost!")
    else:
        print("Data lost during compression!")
    print()


Main()
