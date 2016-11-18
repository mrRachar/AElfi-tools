
<p align="center"><img src='http://campars.net/AElfi/logo tools.svg'/></p>

A simple application manager for [AElfi](https://github.com/mrRachar/AElfi)

#### Commands
```bash
aelfi project make $YOUR-NEW-PROJECT-NAME$          # Make a new aelfi web-app from the latest AElfi version
aelfi project build                                 # Build the aelfi project (in the cwd)
aelfi tools info                                    # Get info about aelfi
aelfi -h                                            # AElfi command tool help
aelfi project update                                # Update project to latest AElfi version
aelfi project -d /var/www/myproject build           # Build a project at the given directory 
                                                    #  (same can be done with make)
aelfi get mrRachar/gloss                            # Install module "gloss"
                                                    #  repository "exampleProject" as a module
```

#### Install
Download current project from GitHub directly here.
 
If you use the Linux command line, you could also do it with the following commands:
```bash
wget https://github.com/mrRachar/AElfi-tools/archive/master.zip
unzip master.zip
```

Then use the instructions below to install it.

##### Linux
Run `sudo python3 install.py` which will do everything for you!
