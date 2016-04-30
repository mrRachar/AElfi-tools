import argparse, urllib.request as request, os, shutil, zipfile, json

def run(args):
    arg_parser = argparse.ArgumentParser(
        prog='aelfi get',
        description='Installing extra modules for use with aelfi'
        )
    arg_parser.add_argument(
        'name',
        type=str,
        help='the name of the new project to install, or a comma-seperated list (e.g. "mymodule" or "example,another-module")',
        )
    '''arg_parser.add_argument(
        '-g', '--gh', '--github',
        help='Download repository from github, name should be "user/project',
        dest='gh',
        action='store_const',
        const=True,
        default=False
        )'''

    arguments = arg_parser.parse_args(args)
    modules = arguments.name.split(',')
    for module in modules:
        download(module)

def download(module: str):
    if module.startswith(('g/', 'gh/', 'github/')):
        name, address = module.split('/')[1], 'https://github.com/{module}/archive/master.zip'.format(module=module)
    else:
        name = module
        with request.urlopen('https://raw.githubusercontent.com/mrRachar/AElfi-tools/master/rsc/get_listings.json') as listings_file:
            listings = json.load(listings_file)
            address = listings['name']

    zip_file = request.urlopen(address)
    os.makedirs(os.path.dirname('AElfi/modules/_temp/download.zip'), exist_ok=True)
    temporary_zip = open('AElfi/modules/_temp/download.zip', 'wb')
    temporary_zip.write(zip_file.read())
    zip_file.close()
    temporary_zip.close()

    temporary_zip = zipfile.ZipFile('AElfi/modules/_temp/download.zip', 'r')
    temporary_zip.extractall('AElfi/modules/_temp/download')
    temporary_zip.close()
    os.remove('AElfi/modules/_temp/download.zip')

    shutil.rmtree('AElfi/modules/{}/'.format(name), ignore_errors=True)
    os.replace('AElfi/modules/_temp/download/{}-master'.format(name), 'AElfi/modules/{}/'.format(name))
    shutil.rmtree('AElfi/modules/_temp/')

    for dirname, dirs, files in os.walk('AElfi/modules/{}/'.format(name)):
        for file in files:
            os.chmod(dirname + '/' + file, 0o755)