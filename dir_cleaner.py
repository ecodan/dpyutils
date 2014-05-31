__author__ = 'dan'

import os
import shutil

def clean_dir(dir, target_list):
    for dirname, dirnames, filenames in os.walk(dir):
        print('searching dir ' + dirname)
        for subdirname in dirnames:
            fqdir = os.path.join(dirname, subdirname)
            if subdirname in target_list:
                print('deleting ' + fqdir)
                shutil.rmtree(fqdir)


def main(in_dir, targets):
    print('starting for dir=' + in_dir + ' targets=' + targets)
    target_list = targets.split('|')
    clean_dir(in_dir, target_list)
    print('finished')


if __name__=='__main__':

    args = { 'in_dir':  '/Users/dan/dev/code/icall',
             'targets': 'target|.svn'}
    model = main(**args)
