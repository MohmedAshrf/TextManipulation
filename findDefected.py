import re
import os
def newest(path):
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    return max(paths, key=os.path.getctime)

def find_Instance(in_line):
    out = in_line.split(':')# i.e casi02 - oss5: JBOD_5_6_SLOT_42 will be splitted at the ':'
    split = out[1].strip()# remove all unwanted spaces
    prefixes = ['JBOD', 'casi', 'raidz', 'mirror']
    if (any(split.startswith(x) for x in prefixes)):
        return str(out[1].strip())

def find_nums(in_line):
    return (re.findall('[0-9]+', in_line))

def convert_int(in_list):
    return list(map(int, in_list))# convert all to integers


Result = []
with open(newest("/admin/tmp/")) as f: #find the newest file to detect errors from
    for line in f:
        Instance_line = find_Instance(line)# find our targets to check
        if (Instance_line != None):
            numbers = convert_int(find_nums(Instance_line))
            if (len(numbers) > 10):
                if numbers[-8] > 0: #errors in line -8
                    print(line)
