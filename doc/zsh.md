### zsh
 Locate your `thus_completer_zsh.sh` file. 
 If you used `--user` then installing thus, the standard location for `thus_completer_zsh.sh` is in `~/.local/bin/thus_completer_zsh.sh`
 If you did not use `--user` when installing thus, the standard location for `thus_completer_zsh.sh` is in `/usr/bin/thus_comleter_zsh.sh`
 
 Edit the ~/.zshrc file. Add the following lines to the top of the file. It must be before any call to `autoload`
 `$fpath=$fpath:~/.local/bin/thus_completer_zsh.sh`

Restart your terminal for changes to take effect. 
