#!/usr/bin/python3

import os
import sys
import pandas as pd

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import crawler.file_util as fu
import dataset.permission.perm_list as pl

SRC_DIR_PATH = '../dataset/raw_data/'
DES_DIR_PATH = '../dataset/description/'
PERM_DIR_PATH = '../dataset/permission/'


def make_dir(dir_path):
    try:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
    except OSError:
        pass


def make_description_file():
    print('[INFO] make description.')
    make_dir(DES_DIR_PATH)
    filenames = os.listdir(SRC_DIR_PATH)
    for filename in filenames:
        try:
            package_name, category, description, permission, privacy_policy = fu.read_raw_file(SRC_DIR_PATH+filename)
            with open(DES_DIR_PATH+package_name, 'w', encoding='utf-8') as f:
                f.writelines(description)

        except Exception as e:
            print(e)
            continue

def make_perm_list():
    print('[INFO] make permission list.')
    make_dir(PERM_DIR_PATH)
    perm_list = list()
    filenames = os.listdir(SRC_DIR_PATH)
    for filename in filenames:
        try:
            package_name, category, description, permission, privacy_policy = fu.read_raw_file(SRC_DIR_PATH+filename)
            perm_list.extend(permission)
        except Exception as e:
            print(e)
            continue
    perm_list = list(set(perm_list))
    perm_list.sort()

    with open(PERM_DIR_PATH+'perm_list.py', 'w', encoding='utf-8') as f:
        f.write('PERMISSION_LIST = [\n')
        for perm in perm_list:
            f.write('"')
            f.write(perm)
            f.write('",\n')
        f.write(']')
    

def get_permission_df():
    print('[INFO] make permission DataFrame.')
    features = ['packageName', 'category', 'numOfPerms']
    features.extend(pl.PERMISSION_LIST)
    res_list = list()
    filenames = os.listdir(SRC_DIR_PATH)
    for filename in filenames:
        try:
            package_name, category, description, permission, privacy_policy = fu.read_raw_file(SRC_DIR_PATH+filename)
            tmp_list = list()
            tmp_list.append(package_name)
            tmp_list.append(category)
            tmp_list.append(len(permission))
            for i in range(3,len(features)):
                if features[i] in permission:
                    tmp_list.append(1)
                else:
                    tmp_list.append(0)
            res_list.append(tmp_list)
        except Exception as e:
            print(e)
            continue
    df = pd.DataFrame(res_list, columns=features)
    return df


def save_perm_df(df):
    make_dir(PERM_DIR_PATH)
    df.to_csv(PERM_DIR_PATH+'perm_df.csv', index=False)


def main():
    make_description_file()
    make_perm_list()
    df = get_permission_df()
    save_perm_df(df)

if __name__ == '__main__':
    main()
