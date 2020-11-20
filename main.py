import Helpers as h
import Constants as c

def generateDESKeys(key):
    primaryKey = h.createKeystring(key, 10)
    primaryKey = h.permuteKey(primaryKey, c.P10)
    primaryKey = h.leftShift(primaryKey[:5], 1) + h.leftShift(primaryKey[5:], 1)
    key1 = h.permuteKey(primaryKey, c.P8)
    primaryKey = h.leftShift(primaryKey[:5], 2) + h.leftShift(primaryKey[5:], 2)
    key2 = h.permuteKey(primaryKey, c.P8)
    return key1, key2

def SBox(input, matrix):
    row = int(input[0]+input[3], 2)
    column = int(input[1:3], 2)
    return bin(matrix[row][column])[2:].zfill(2)

def cycleF(input, keystring):
    expandedInput = h.permuteKey(input, c.EP)
    bits = bin(int(expandedInput, 2) ^ int(keystring, 2))[2:].zfill(8)

    leftBits = bits[:4]
    rightBits = bits[4:]

    left_out = SBox(leftBits, c.S0)
    right_out = SBox(rightBits, c.S1)

    return h.permuteKey(left_out+right_out, c.P4)

def complexF(left, right, keystring):
    leftBit = int(left, 2)
    leftOut = leftBit ^ int(cycleF(right, keystring), 2)
    return bin(leftOut)[2:].zfill(4), right

def encrypt(bits, key1, key2, decrypt=False):
    if decrypt:
        key2, key1 = key1, key2

    bits = h.permuteKey(bits, c.IP)
    left,right = complexF(bits[:4], bits[4:], key1)
    left,right = complexF(right, left, key2)
    return h.permuteKey(left + right, c.inversedIP)

def encryptor(src, key, decrypt = False):
    assert 0 <= key < 1023, "key must be a 10 bit binary"
    key1,key2 = generateDESKeys(key)

    for byte in h.getBytes(src):
        bits = bin(h.byteToBits(byte))[2:].zfill(8)
        cipherString = encrypt(bits, key1, key2, decrypt)
        cipherBit = int(cipherString, 2)
        yield h.bitsToByte(cipherBit)

def encryptFile(src, dest, key, decrypt):
    h.writeBytes(dest, encryptor(src, key, decrypt))

if __name__=="__main__":

    # 2

    #encryptFile("input.txt", "output.txt", int("0000000000", 2), decrypt=False)
    #encryptFile("input.txt", "output.txt", int("0000000001", 2), decrypt=False)
    #encryptFile("input.txt", "output.txt", int("0000000010", 2), decrypt=False)
    #encryptFile("input.txt", "output.txt", int("0000000100", 2), decrypt=False)
    #encryptFile("input.txt", "output.txt", int("0000001000", 2), decrypt=False)
    #encryptFile("input.txt", "output.txt", int("0000010000", 2), decrypt=False)
    #encryptFile("input.txt", "output.txt", int("0000100000", 2), decrypt=False)
    #encryptFile("input.txt", "output.txt", int("0001000000", 2), decrypt=False)
    #encryptFile("input.txt", "output.txt", int("0010000000", 2), decrypt=False)
    #encryptFile("input.txt", "output.txt", int("0100000000", 2), decrypt=False)
    #encryptFile("input.txt", "output.txt", int("1000000000", 2), decrypt=False)
    #encryptFile("output.txt", "input.txt", 1000, decrypt=True)

    # Results:

    # & ô££)\ * )(£
    #
    # §""hCh¤"Ì
    #
    # R @ ÓÓëì(ë * Ó=
    #
    # ab9d cece a4f1 4fa4 8dce 00
    #
    # `Vþ:œK
    #
    # ëõNN¤°¤
    # Ne
    #
    # ætcc©Üê©¨c
    #
    # `Vþ:.K
    #
    # ÎØ««©p‚©e«¥
    #
    # Ð££    x
    # £­
    #
    # "R§§?Ì:?.§


    # 3

    # encryptFile("input.txt", "output.txt", 1020, decrypt=False)

    # Results

    # 4
    #
    # 4
    #
    # 4
    #
    # 4
    #
    # 4
    #
    # 4
    #
    # 4
    #
    # 4
    #
    # 4
    #
    # 4

    # 4

    encryptFile("input.txt", "output.txt", 1020, decrypt=False)

    # Results

    # [[[[[[[[[[
    #
    # [[[[[[[[[[
    #
    # [[[[[[[[[[
    #
    # [[[[[[[[[[
    #
    # [[[[[[[[[[
    #
    # [[[[[[[[[[
    #
    # [[[[[[[[[[
    #
    # [[[[[[[[[[
    #
    # [[[[[[[[[[
    #
    # [[[[[[[[[[
    #
    # ����������
    #
    # ����������
    #
    # ����������
    #
    # ����������





