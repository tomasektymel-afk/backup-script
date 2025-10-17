from pathlib import Path
import json
from datetime import datetime
import getpass
import shutil

def log() -> None: # makes a log in log file
    tmp = datetime.now()
    user = getpass.getuser()
    time = tmp.strftime("%Y-%m-%d-%H-%M-%S")
    with open("config.json","r") as file:
        config = json.load(file)
    with open(config["log_file"], "a") as log:
        log.write(time + " " + user + " " + config["log_file"] + "\n")

def rec_backup(source: Path , destination: Path):
    for item in source.iterdir():
        if item.is_file():
            shutil.copy2(item, destination)
        else:
            (destination / item.name).mkdir()
            rec_backup(source / item.name, destination / item.name )

def make_backup()-> None: # makes a directiory, sets the name and calls recursive function to copy all the files
    with open("config.json","r") as file:
        config = json.load(file)
    source = Path(config["source"])
    tmp = datetime.now()
    destination = Path(config["destination"] + "/ backup "+ tmp.strftime("%Y-%m-%d-%H-%M-%S"))
    destination.mkdir()
    rec_backup(source , destination)



def main ():
    log()
    make_backup()

if __name__ == "__main__":
    main()