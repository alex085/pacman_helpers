# pacman_helpers
Helper scripts for pacman

## uncomment_mirrolist.py
Script to uncomment "#Server = " strings in a mirrorlist file that you can generate by https://archlinux.org/mirrorlist/. You can also sort servers by countries.
```
python uncomment_mirrorlist.py mirrorlist Japan Germany "United states"
```
Or you can get just uncommented file without sorting
```
python uncomment_mirrorlist.py mirrorlist
```

The script doesn't change input file. Instead it just generates uncommented and sorted ouput into stdout.
