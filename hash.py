import time
from bitarray import bitarray
import math
# murmur algorithm


def murmur32(data, seed=0):
    c_2 = 0x1b873593
    length = len(data)
    c_1 = 0xcc9e2d51
    h_1 = seed
    round = (length & 0xfffffffc)
    for i in range(0, round, 4):
      z_1 = (ord(data[i]) & 0xff) | ((ord(data[i + 1]) & 0xff) << 8) | \
           ((ord(data[i + 2]) & 0xff) << 16) | (ord(data[i + 3]) << 24)
      z_1 *= c_1
      z_1 = (z_1 << 15) | ((z_1 & 0xffffffff) >> 17)
      z_1 *= c_2

      h_1 ^= z_1
      h_1 = (h_1 << 13) | ((h_1 & 0xffffffff) >> 19)
      h_1 = h_1 * 5 + 0xe6546b64
    z_1 = 0
    v_len = length & 0x03
    if v_len == 3:
        z_1 = (ord(data[round + 2]) & 0xff) << 16
    if v_len in [2, 3]:
        z_1 |= (ord(data[round + 1]) & 0xff) << 8
    if v_len in [1, 2, 3]:
        z_1 |= ord(data[round]) & 0xff
        z_1 *= c_1
        z_1 = (z_1 << 15) | ((z_1 & 0xffffffff) >> 17)
        z_1 *= c_2
        h_1 ^= z_1
    h_1 ^= length
    h_1 ^= ((h_1 & 0xffffffff) >> 16)
    h_1 *= 0x85ebca6b
    h_1 ^= ((h_1 & 0xffffffff) >> 13)
    h_1 *= 0xc_2b2ae35
    h_1 ^= ((h_1 & 0xffffffff) >> 16)
    return h_1 & 0xffffffff


def read_password(file):
    with open(file,'r') as f:
        data = f.read().splitlines()
    return data


def add_elements(element, k, bloom_filter_size, bit_array):
    for seed in range(k):
        result = murmur32(element, seed) % bloom_filter_size
        bit_array[result] = 1


def look_up_element(data, k, bloom_filter_size, bit_array):
    for seed in range(k):
        result = murmur32(data, seed) % bloom_filter_size
        if bit_array[result] == 0:
            return 0
    return 1


def BloomFilter(passwords1,passwords2):
    k = 7
    bloom_filter_size = 100000000
    bit_array = bitarray(bloom_filter_size)
    bit_array.setall(0)
    start = time.time()
    # add all passwords1 to the filter
    passwords = read_password(passwords1)
    number = len(passwords)
    print(number)
    for password in passwords:
        add_elements(password, k, bloom_filter_size, bit_array)
    # check all passwords2 presence in the filter
    print("----------------------------")
    # passwords = read_password(passwords2)
    n = 0
    for password in passwords:
        if look_up_element(password, k, bloom_filter_size, bit_array):
            n += 1
    p = math.pow((1 - math.e**(-k*number/bloom_filter_size)), k)
    end = time.time()
    # print(read_password(passwords1))
    print('Number of hash function used: ', k)
    print('Number of duplicates detected: ', n)
    print('Probability of false positives: ', p)
    print('Execution time: ', end - start)


if __name__ == "__main__":
    passwords1 = "passwords1.txt"
    passwords2 = "passwords2.txt"
    BloomFilter(passwords1, passwords2)