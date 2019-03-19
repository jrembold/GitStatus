#!/usr/bin/python

# Script to read in git status of folder and output symbol

import subprocess
import argparse

def create_argparse():
    parser = argparse.ArgumentParser(description='Check git folder status')
    parser.add_argument(
            '-f',
            '--folder',
            help='Folder to check status'
            )
    parser.add_argument(
            '-fn',
            '--fname',
            help='Displayed name of folder'
            )
    return parser.parse_args()

def get_status(folder):
    dirty_raw = subprocess.run(['git', '--git-dir='+folder+'.git', '--work-tree='+folder, 'status', '--porcelain=1'], stdout=subprocess.PIPE)

    pushed_raw = subprocess.run(['git', '--git-dir='+folder+'.git', '--work-tree='+folder, 'log', '@{push}..'], stdout=subprocess.PIPE)

    dirty = len(dirty_raw.stdout.decode())>0
    pushed = len(pushed_raw.stdout.decode())<1

    if dirty:
        return '#b03a2e'
    if not dirty and not pushed:
        return '#ca6f1e'
    else:
        return '#1e8449'

message = "<span color='{color}'>⚫<b>{name}</b></span>"
args=create_argparse()
status = get_status(args.folder)
print(message.format(color=status,name=args.fname))
