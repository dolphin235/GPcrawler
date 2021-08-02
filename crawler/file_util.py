#!/bin/user/python3

def wrtie_text_to_file(file_path, text):
    f = open(file_path, mode='x', encoding='utf-8')
    f.write(text)
    f.close()


def write_list_to_file(file_path, input_list):
    f = open(file_path, 'w')
    text = list_to_csv(input_list)
    f.write(text)
    f.close()


def list_to_csv(input_list):
    res_text = ''
    for l in input_list:
        res_text = res_text + l + ','
    return res_text[:-1]