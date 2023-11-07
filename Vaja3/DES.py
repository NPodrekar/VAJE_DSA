from DES_funkcije import *
import sys
sys.path.append('.')






def prepare_keys(kljuc):
    bin_key=text2bin(kljuc)
    bin_key = permute(bin_key,keyp,56)
    left = bin_key[0:28]
    right = bin_key[28:56]
    keys = []
    for i in range(16):
        left = shift_left(left, shift_table[i])
        right = shift_left(right, shift_table[i])
        combined_str = left +right
        combined_str = permute(combined_str, key_comp, 48)
        keys.append(combined_str)
    return keys

def encrypt(cistopis, kljuc):
    keys=prepare_keys(kljuc)
    
    binary = text2bin(cistopis)
    binary = permute(binary,initial_perm,64)
    left = binary[0:32]
    right = binary[32:64]
    

    for i in range(16):
        str_right=F(right, keys[i])
        left = xor(left, str_right)

        if i < 15:
            temp = left
            left = right
            right = temp
    combined = left + right
    koncni_bin = permute(combined, final_perm,64)
    return bin2text(koncni_bin)


print(encrypt("skrivnost", "geslogeslo"))

def decrypt(sifropis,kljuc):
    keys=prepare_keys(kljuc)
    
    binary = text2bin(sifropis)
    binary = permute(binary,initial_perm,64)
    left = binary[0:32]
    right = binary[32:64]
    

    for i in range(16):
        str_right=F(right, keys[15-i])
        left = xor(left, str_right)
        if i < 15:
            temp = left
            left = right
            right = temp
    combined = left + right
    koncni_bin = permute(combined, final_perm,64)
    return bin2text(koncni_bin)

print(decrypt(encrypt("skrivnost", "geslogeslo"), "geslogeslo"))

def ECB(cistopis,kljuc, smer):
    for i in range(0, len(cistopis), 8):
        block = cistopis[i:8+i]
        izhod = ""
        if smer == 0:
            block = block(8, '0')
            izhod += encrypt(block, kljuc)
        else:
            cistopis_block = decrypt(block, kljuc)
            izhod= cistopis_block.rstrip('0')
    return izhod

print(ECB("skrivnostskrivnost","geslogeslo", 0))