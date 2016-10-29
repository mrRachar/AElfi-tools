#!/usr/bin/env python3
#-*- coding: UTF-8 -*-

import argparse, os, shutil, sys

if __name__ != '__main__':
    print('This module will not run')
    sys.exit()

try:
    print('installing AElfi tools ...')

    arg_parser = argparse.ArgumentParser(
        prog='install.py',
        description='Installing AElfi tools'
        )

    arg_parser.add_argument(
        '--os',
        type=str,
        choices=['posix', 'nt', 'ce', 'java'],
        default=os.name,
        help='what operating system to use, auto-detect by default'
        )
    arg_parser.add_argument(
        '--directory', '--dir', '-d', 
        type=str,
        default=None,
        help='location to store aelfi'
        )

    arguments = arg_parser.parse_args()

    if arguments.os == 'nt':
        print("Error: Windows Not Supported")
        raise SystemExit
    elif arguments.os == 'posix':
        print('installing on Unix/Linux/Posix')
        if arguments.directory is None:
            arguments.directory = r'/usr/bin'
    else:
        if arguments.directory is None:
            raise ValueError('Required directory argument when not on Windows,Unix/Linux/Posix')
    arguments.directory = arguments.directory.rstrip(r'\/')
    print('directory to install in is', arguments.directory, '...')
    
    shutil.rmtree(arguments.directory + '/aelfi-tools/', ignore_errors=True)
    try:
        os.remove(arguments.directory + '/aelfi-tools')
        print('removed old `aelfi\' file ...')
    except:
        pass
    
    shutil.copytree('./', arguments.directory + '/aelfi-tools/')
    print('aelfi tools installed ...')

    if arguments.os == 'posix':
        with open(arguments.directory + '/aelfi', 'w') as command_file:
            command_file.write('python3 "' + arguments.directory + '/aelfi-tools' '/aelfi.py" $@')
        os.chmod(arguments.directory + '/aelfi', 0o755)
        print('aelfi command installed ...')
    else:
        print("Error: Only POSIX Supported")
        raise SystemExit

    input('finished!\n\nclose? [press <Enter>]')
except BaseException as e:
    print('\n---')
    print(repr(e))
    print(e)
    
    input('\nAHHHH!!!! [press <Enter>]')
    
        
        
            
    
