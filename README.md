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
# will run
notepad.exe D:/somedir/somefile.txt
# note that command
notepad.exe /mnt/d/somedir/somefile.txt
# will cause error, so with windows apps you should run commands with wind prefix.
# note that editing files in linux dir using windows apps can damage not the file only but the whole distro and you will have to reinstall it. So wind does not support convertation local filepathes.
