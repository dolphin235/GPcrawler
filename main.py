#!/usr/bin/python3
import argparse
import os

import crawler.common as cm
import crawler.applist.android_rank_list as android_rank
import crawler.file_util as fu


DATASET_DIR_NAME = 'dataset/'
g_home_path = ''

LISTRANGE_TYPE = ['all', 'popular']


def print_soup(soup):
    print("\n|title|\n", soup.title)
    print("\n|title.name|\n", soup.title.name)
    print("\n|title.string|\n", soup.title.string)
    print("\n|title.parent.name|\n", soup.title.parent.name)
    print("\n|p|\n", soup.p)
    #print("\n|p['class']|\n", soup.p['class'])
    print("\n|a|\n", soup.a)
    print("\n|find_all('a')|\n", soup.find_all('a'))
    print("\n|find(id='link3')|\n", soup.find(id='link3'))


def init():
    global g_home_path
    g_home_path = os.path.dirname(os.path.realpath(__file__))


def get_package_lists(args):
    if package_list_exist(args.listpath) == True:
        return

    if args.listrange == 'all':
        fu.write_list_to_file(g_home_path+'/'+args.listpath, android_rank.AndroidrankListCollector.get_all_list())
    elif args.listrange == 'popular':
        fu.write_list_to_file(g_home_path+'/'+args.listpath, android_rank.AndroidrankListCollector.get_popular_list())



def package_list_exist(file_path):
    if os.path.isfile(file_path):
        return True

    if not os.path.isdir(g_home_path+'/'+DATASET_DIR_NAME):
        os.makedirs(g_home_path+'/'+DATASET_DIR_NAME)

    return False


def read_package_list(args):
    return fu.read_csv_to_list(args.listpath)


def set_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--list-path', type=str, default='dataset/popular_apps', dest='listpath',
                        help='enter package list file path')
    parser.add_argument('--list-range', type=str, default='popular', dest='listrange', choices=LISTRANGE_TYPE,
                        help='choose range of list')

    return parser.parse_args()


def main():
    print("[INFO] run main")
    init()
    args = set_argparser()

    # Get package list to file
    get_package_lists(args)

    # Read package list
    package_list = read_package_list(args)




    print("[INFO] finish successfully")


if __name__=="__main__":
    main()

