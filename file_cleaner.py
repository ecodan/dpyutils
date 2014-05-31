__author__ = 'dan'

import os
import shutil

def clean_dir(dir, target_list):
    for dirname, dirnames, filenames in os.walk(dir):
        print('searching dir ' + dirname)
        for filename in filenames:
            fqf = os.path.join(dirname, filename)
            for suffix in target_list:
                if filename.endswith(suffix):
                    print('deleting ' + fqf)
                    os.remove(fqf)


def main(in_dir, targets):
    print('starting for dir=' + in_dir + ' targets=' + targets)
    target_list = targets.split('|')
    clean_dir(in_dir, target_list)
    print('finished')


if __name__=='__main__':

    args = { 'in_dir':  '/BOGUS',
             'targets': '.jar|.war|.ear'}
    model = main(**args)
