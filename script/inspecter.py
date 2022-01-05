#!/bin/user/python3

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import crawler.file_util as fu

DIR_PATH = '../dataset/raw_data'

def check_perm(perm_list):
    if perm_list == []:
        return True
    
    for perm in perm_list:
        if len(perm.split(':')[0]) == 0:
            print("[DEBUG] permission= "+str(perm))
            return False

def main():
    files = os.listdir(DIR_PATH)
    for file_name in files:
        file_path = DIR_PATH+'/'+file_name
        try:
            pn,ct,dc,pm,pp = fu.read_raw_file(file_path)
            if check_perm(pm) == False:
                print("[INFO] remove ["+file_path+"]")
                os.remove(file_path)
        except Exception as e:
            print(e)
            with open(file_path, 'r') as f:
                if(f.read() == 'None'):
                    print("[INFO] remove ["+file_path+"]")
                    os.remove(file_path)


if __name__=="__main__":
    main()


