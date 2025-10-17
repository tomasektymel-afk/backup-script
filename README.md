# backup-script


Simple backup tool
------------------
This is a python script which uses recursive function to make a timestamped backup directory.
It copies files and folders from a source directory to a destination, and logs each backup.


Library
--------------------------
pathlib


How to use
--------------------------
Change in config file path to your needs and then just execute to make a backup.


exmaple
Source folder: /home/user/Documents
Destination:   /home/user/Backups

→ Creates: /home/user/Backups/backup 2025-10-17-14-35-21/
