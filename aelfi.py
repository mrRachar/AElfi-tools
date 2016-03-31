#!/usr/bin/env python3
#-*- coding: UTF-8 -*-

import argparse, os
from importlib.machinery import SourceFileLoader

# AElfi tool information            ✓
# AElfi project version update
# AElfi tool setup script           ✓
# AElfi dependencies install

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(
        prog='aelfi',
        description='AElfi tools to allow you to start new projects and build them, as well as use other utilities'
        )

    arg_parser.add_argument(
        'utility',
        type=str,
        help='the utility to use (project, ...)'
        )
    arg_parser.add_argument(
        '--directory', '--dir', '-d',
        type=str,
        help='the aelfi project directory to run the script in',
        default=None
        )

    arguments, utility_arg_list = arg_parser.parse_known_args()
    
    utility = SourceFileLoader('utility_' + arguments.utility, os.path.dirname(os.path.abspath(__file__)) + '/{}.py'.format(arguments.utility)).load_module()

    if arguments.directory != None:
        #os.chdir(os.path.abspath(arguments.directory))
        os.chdir(arguments.directory)

    utility.run(utility_arg_list)

def run(args):
    print(r"""\nYou found him!


                                       |\      /|
                                       | \____/ |
            AElfi the Cat              |  /\/\  |
                                      .'___  ___`.
                                     /  \|/  \|/  \
                    _.--------------(              )
                 .-' \  -. | | | | | \ ----\/---- /
               .'\  | | / \` | | | |  `.  -'`-  .'
              /`  ` ` '/ / \ | | | | \  `------'\
             /-  `-------.' `-----.       -----. `---.
            (  / | | | |  )/ | | | )/ | | | | | ) | | )
             `._________.'_____,,,/\_______,,,,/_,,,,/

He thought he was good at hiding ...
""")
