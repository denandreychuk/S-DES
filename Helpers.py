import struct

def createKeystring(key, size):
    return bin(key)[2:].zfill(size)

def permuteKey(key, permutation):
    rstring=""
    for i in permutation:
        rstring+=key[i]
    return rstring

def leftShift(key, shift):
    return key[shift:]+key[:shift]

import struct

def getBytes(filename):
    with open(filename, 'rb') as fileobject:
        byte=fileobject.read(1)
        while byte != b'':
            yield byte
            byte=fileobject.read(1)

def writeBytes(filename, byte_generator):
    with open(filename, 'wb') as fileobject:
        for byte in byte_generator:
            fileobject.write(byte)

def byteToBits(byte):
    return ord(byte)

def bitsToByte(bits):
#   The "B" option ensure the input is packed with 8 bits
    return struct.pack("B", bits)