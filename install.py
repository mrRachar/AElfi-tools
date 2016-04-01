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
        print('installing on Windows ...')
        if arguments.directory is None:
            arguments.directory = r'C:\Program Files'
    elif arguments.os == 'posix':
        print('installing on Unix/Linux/Posix')
        if arguments.directory is None:
            arguments.directory = r'/usr/bin'
    else:
        if arguments.directory is None:
            raise ValueError('Required directory argument when not on Windows,Unix/Linux/Posix')
    arguments.directory = arguments.directory.rstrip(r'\/')
    print('directory to install in is', arguments.directory, '...')

    #cwd = os.getcwd().rstrip(r'\/').replace('\\', '/').split('/')[-1]
    #print(cwd)
    #os.chdir('../')
    #shutil.copytree('./' + cwd, arguments.directory + '/aelfi-tools')
    
    shutil.rmtree(arguments.directory + '/aelfi-tools/', ignore_errors=True)
    try:
        os.remove(arguments.directory + '/aelfi-tools')
        print('removed old `aelfi\' file ...')
    except:
        pass
    
    shutil.copytree('./', arguments.directory + '/aelfi-tools/')
    print('aelfi tools installed ...')

    if arguments.os == 'nt':
        if not os.path.exists(arguments.directory + '/aelfi-tools' '/cmd'):
            os.makedirs(arguments.directory + '/aelfi-tools' '/cmd')
        with open(arguments.directory + '/aelfi-tools' '/cmd' '/aelfi.bat', 'w') as command_file:
            command_file.write('{} "{}" %*'.format(
                input('What is Python 3 called? (python, python3, python3.6) >> It\'s called '),
                arguments.directory + r'\aelfi-tools\aelfi.py',
                ))
        print('aelfi tools command script ready, but not installed ...')
        
        print('''
-- NOTE: The ``aelfi" command --

Adding a directory to the Windows PATH doesn't work as well from the command line
as it does when done by the user. To install aelfi tools with the ``aelfi" command:

1. Open `Control Panel` (not Settings)
2. Choose `System and Security` by clicking on the title
3. Choose `System` by clicking on the title
4. Click `Advanced System Settings` in the sidebar
5. Click `Environment Variables` down the bottom
6. Find the system variable named `Path`
7. Add the directory '{directory}' to it, and you're done!

--- ---'''.format(directory=arguments.directory + r'\aelfi' r'\cmd')
        )

    elif arguments.os == 'posix':
        with open(arguments.directory + '/aelfi', 'w') as command_file:
            command_file.write('python3 "' + arguments.directory + '/aelfi-tools' '/aelfi.py" $@')
        os.chmod(arguments.directory + '/aelfi', 0o755)
        print('aelfi command installed ...')
    input('\nfinished!\n\nclose? [press <Enter>]')
except BaseException as e:
    print('\n---')
    print(repr(e))
    print(e)
    
    input('\nAHHHH!!!!')
    
        
        
            
    
