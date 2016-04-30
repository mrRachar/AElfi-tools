# AElfi-tools
A simple application manager for [AElfi](https://github.com/mrRachar/AElfi)

#### Commands
```bash
aelfi project make $YOUR-NEW-PROJECT-NAME$          # Make a new aelfi web-app from AElfi version 0.3.1
aelfi project build                                 # Build the aelfi project (in the cwd)
aelfi tools info                                    # Get info about aelfi
aelfi -h                                            # AElfi command tool help
aelfi project -d /var/www/myproject build           # Build a project at the given directory 
                                                    # (same can be done with make)
aelfi get gloss                                     # Install module "gloss"
aelfi get g/exampleuser/exampleProject              # Install GitHub user "exampleuser"'s repository "exampleProject" as a module
```

#### Install
Download current project from GitHub directly here.
 
If you use the Linux command line, you could also do it with the following commands:
```bash
wget https://github.com/mrRachar/AElfi-tools/archive/master.zip
unzip master.zip
```

Then use the instructions below to install it.


##### Windows
Run `install_windows.bat` and follow the instructions

*or with administrator privilages run `python3 install.py`*.

##### Linux
Run `sudo python3 install.py` which will do everything for you!
