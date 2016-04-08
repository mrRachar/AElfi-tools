#!/usr/bin/env python3
#-*- coding: UTF-8 -*-

import argparse, re, subprocess, urllib.request as request, zipfile, shutil, os, sys

python_name = 'python3'
aelfi_tools_folder = os.path.dirname(__file__)

def run(args):
    arg_parser = argparse.ArgumentParser(
        prog='aelfi project',
        description='Making and building aelfi projects'
        )

    arg_parser.add_argument(
        'command',
        type=str,
        choices=['build', 'make'],
        help='whether to build an aelfi project or make a new one'
        )
    arg_parser.add_argument(
        'name',
        type=str,
        default='',                                                     # Empty string so no error later when stripping it
        help='the name of the new project, if installing a new one',
        nargs='?'
        )
    arg_parser.add_argument(
        '--version', '-v',
        type=str,
        help='if installing, the aelfi version to install',
        default=None
        )
    arg_parser.add_argument(
        '--get', '-g',
        type=str,
        help='if installing, the aelfi repository to install from. This will override the version that has been chosen',
        default=None
        )

    arguments = arg_parser.parse_args(args)

    if arguments.command == 'make':
        make(arguments.name.rstrip('/'), arguments.version, arguments.get)
    if arguments.command == 'build':
        build()

def make(location, version, get=None):
    if version is None or location == '':
        print('Please make sure that both the project name and AElfi version are given')
        sys.exit()
    v, r = re.match(r'v?(\d+\.\d+\.\d)+(?:[\-\_\/\\]?r(\d+))?', version).groups()
    version = '{}'.format(v) if not r else '{}-r{}'.format(v, r)
    
    if not get:
        zip_file = request.urlopen('https://github.com/mrRachar/AElfi/archive/v{v}.zip'.format(v=version))
    else:
        zip_file = request.urlopen(get)

    os.makedirs(os.path.dirname(location + '_make_temp' '/AElfi.zip'), exist_ok=True)
    temporary_zip = open(location + '_make_temp' '/AElfi.zip', 'wb')
    temporary_zip.write(zip_file.read())
    zip_file.close()
    temporary_zip.close()
    
    temporary_zip = zipfile.ZipFile(location + '_make_temp' '/AElfi.zip', 'r')
    temporary_zip.extractall(location + '_make_temp' '/AElfi')
    temporary_zip.close()

    os.replace(location + '_make_temp' '/AElfi/AElfi-{v}'.format(v=version), location + '/')
    shutil.rmtree(location + '_make_temp')

    for dirname, dirs, files in os.walk(location + '/'):
        for file in files:
            os.chmod(file, 0o755)
    

def build():
    subprocess.call([python_name, 'AElfi/build.py'])

    
