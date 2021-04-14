import argparse
import os


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--lang', type=str, required=True)
    parser.add_argument('--domain_nums', type=int, required=True)
    return parser.parse_args()


def file_name(prefix, lang):
    fname = prefix
    if lang is not None:
        fname += ".{lang}".format(lang=lang)
    return fname

def split_ted(lang):
    trainpref = file_name("dataset/iwslt14.tokenized.en-de/train", lang)
    with open(trainpref, 'r') as f:
        ted_total_lines = sum(1 for line in f)
    domain_nums = args.domain_nums
    lines_per_file = ted_total_lines // (domain_nums - 1)
    smallfile = None
    domain_file_list = []
    with open(trainpref) as bigfile:
        for lineno, line in enumerate(bigfile):
            if lineno % lines_per_file == 0:
                if smallfile:
                    smallfile.close()
                domain_index = (lineno // lines_per_file) + 1
                pathdir = "dataset/ted_domains/{}".format(domain_nums)
                if not os.path.exists(pathdir):
                    os.makedirs(pathdir)
                small_filename = pathdir + "/train" + '.domain{}'.format(domain_index) + ".{}".format(lang)
                domain_file_list.append(small_filename)
                smallfile = open(small_filename, "w+")
            smallfile.write(line)
        if smallfile:
            smallfile.close()
    return domain_file_list

if __name__ == '__main__':
    args = get_args()
    split_ted(args.lang)
