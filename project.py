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
        choices=['build', 'make', 'update'],
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
    elif arguments.command == 'build':
        build()
    elif arguments.command == 'update':
        update(arguments.version, arguments.get)

def make(location, version, get=None):
    if location == '':
        print('Please make sure that both the project name is given')
        sys.exit()
    if version == None:
        with request.urlopen('https://raw.githubusercontent.com/mrRachar/AElfi-tools/master/rsc/latestaelfi.txt') as versionfile:
            version = versionfile.read().decode('utf-8')
    v, r = re.match(r'v?(\d+\.\d+\.\d)(?:[\-\_\/\\]?r(\d+))?', version).groups()
    version = '{}'.format(v) if not r else '{}-r{}'.format(v, r)

    print('starting download ...')
    if not get:
        zip_file = request.urlopen('https://github.com/mrRachar/AElfi/archive/v{v}.zip'.format(v=version))
    else:
        zip_file = request.urlopen(get)

    os.makedirs(os.path.dirname(location + '_make_temp' '/AElfi.zip'), exist_ok=True)
    temporary_zip = open(location + '_make_temp' '/AElfi.zip', 'wb')
    temporary_zip.write(zip_file.read())
    zip_file.close()
    temporary_zip.close()
    print('download complete ...')
    
    temporary_zip = zipfile.ZipFile(location + '_make_temp' '/AElfi.zip', 'r')
    temporary_zip.extractall(location + '_make_temp' '/AElfi')
    temporary_zip.close()
    print('extracted zip ...')
    os.remove(location + '_make_temp' '/AElfi.zip')
    print('removed zip ...')

    if not os.path.exists(location + '/'):
        os.replace(location + '_make_temp' + '/AElfi/AElfi-{v}'.format(v=version), location + '/')
    else:
        for file in os.listdir(location + '_make_temp'):
            if os.path.exists(location + '/' + file):
                try:
                    shutil.rmtree(location + '/' + file)
                except NotADirectoryError:
                    os.remove(location + '/' + file)
            shutil.move(location+'_make_temp/'+file, location + '/')

    shutil.rmtree(location + '_make_temp')
    print('set up in', location + '/', '...')

    print('cleaning up', '...')
    for dirname, dirs, files in os.walk(location + '/'):
        for file in files:
            os.chmod(dirname + '/' + file, 0o755)
    print('finished make!')
    

def build():
    subprocess.call([python_name, './_aelfi/build.py'])


def update(location, version, get=None):
    aelfi_project_folder = os.getcwd().rstrip('/').split('/')[-1]
    os.chdir('../')
    save_paths = (
        'modules',
        'templating',
    )
    if os.path.exists(r'./__aelfi_temp_for_aelfi_tools_update_cache__/'):
        shutil.rmtree(r'./__aelfi_temp_for_aelfi_tools_update_cache__/', ignore_errors=True)
    for save_path in save_paths:
        if os.path.exists(r'./{}/_aelfi/'.format(aelfi_project_folder) + save_path):
            shutil.copytree(r'./{}/_aelfi/'.format(aelfi_project_folder) + save_path, r'./__aelfi_temp_for_aelfi_tools_update_cache__/' + save_path)
    print('preserved modules and templates', '...')
    shutil.rmtree(r'./{}/_aelfi/'.format(aelfi_project_folder), ignore_errors=True)
    print('removed old aelfi version', '...')

    make(r'./{}'.format(aelfi_project_folder), version)

    print('reinstating modules and templates', '...')
    if os.path.exists(r'./__aelfi_temp_for_aelfi_tools_update_cache__/modules'):
        shutil.move(r'./__aelfi_temp_for_aelfi_tools_update_cache__/modules', r'./{}/_aelfi/'.format(aelfi_project_folder) + 'modules')

    if os.path.exists(r'./__aelfi_temp_for_aelfi_tools_update_cache__/templating'):
        for file in os.listdir(r'./__aelfi_temp_for_aelfi_tools_update_cache__/templating'):
            shutil.move(
                        r'./__aelfi_temp_for_aelfi_tools_update_cache__/templating/' + file,
                        r'./{}/__aelfi/'.format(aelfi_project_folder) + r'templating/' + file
                )
        shutil.rmtree(r'./__aelfi_temp_for_aelfi_tools_update_cache__/', ignore_errors=True)

    print('finished update!')
