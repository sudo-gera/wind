# wind
comfortable variant of wslpath
converts all file arguments to windows path
# [requirements]
python3
# [insallation]
./install.py
# [usage]
wind {command}
# [example]
wind notepad.exe /mnt/d/somedir/sonefile.txt
# this example will run
notepad.exe D:/somedir/somefile.txt
# [example]
wind notepad.exe ~/wind/README.md
# this example will run
notepad.exe \<some prefix\>/\<$HOME\>/wind/README.md
# note that command
notepad.exe /mnt/d/somedir/somefile.txt
# will cause error, so with windows apps you should run commands with wind prefix.
