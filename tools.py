import argparse

def run(args):
    arg_parser = argparse.ArgumentParser(
        prog='aelfi tools',
        description='Information about aelfi tools'
        )
    
    arg_parser.add_argument(
        'command',
        type=str,
        choices = ['info', 'license'],
        help='current version information'
        )

    arguments = arg_parser.parse_args(args)

    if arguments.command == 'info':
        print('''
AElfi tools v0.0.0
built by Matthew Ross Rachar
''')
    if arguments.command == 'license':
        print('''
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>
''')


        
