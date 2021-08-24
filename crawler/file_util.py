#!/bin/user/python3

def wrtie_text_to_file(file_path, text):
    f = open(file_path, mode='w', encoding='utf-8')
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


def read_csv_to_list(file_path):
    res_list = []
    f = open(file_path, 'r')
    while True:
        line = f.readline().rstrip('\n')
        if line:
            line_list = line.split(',')
            res_list.extend(line_list)
        else:
            break
    return res_list

