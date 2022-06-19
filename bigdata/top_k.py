import os
import string
import random
import hashlib
import collections

K = 10


def rand_num():
    length = random.choice(range(1, len(string.digits)))
    return str(int(''.join(random.sample(string.digits, length))))


def create_data_if_not_exist(f=None, size=10000000):
    if not os.path.exists(f):
        with open(f, 'w') as f:
            while size:
                f.write(rand_num + '\n')
                size -= 1


def divide_data(f=None, num=K):
    with open(f, 'r') as f:
        tmp_files = []
        for i in range(num):
            tmp_files.append(open(str(i), 'w'))
        for s in f:
            tmp_files[int(hashlib.md5(s.encode('utf-8')).hexdigest(), 16) % num].write(s)
        for tf in tmp_files:
            tf.close()


def record_tmp_res(f=None, num=K, reverse=True):
    with open(f, 'r') as f:
        count = collections.defaultdict(int)
        for i in f:
            count[i.strip()] += 1
        tmp = sorted(count.items(), key=lambda x: (x[1], x[0]), reverse=reverse)
        tmp_res = {}
        for i in range(num):
            tmp_res[tmp[i][0].strip()] = tmp[i][1]
        return tmp_res


def main():
    test_file = 'test.data'
    create_data_if_not_exist(test_file)
    divide_data(test_file)
    res = {}
    for i in range(K):
        res.update(record_tmp_res(str(i)))
    tmp = sorted(res.items(), key=lambda x: (x[1], x[0]), reverse=True)
    for i in range(K):
        print(tmp[i])


if __name__ == "__main__":
    main()
