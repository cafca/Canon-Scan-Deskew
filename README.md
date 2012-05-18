# Canon Scan Deskew

Corrects images which are skewed due to a bug in the SANE Mac driver for Canon scanners.


## Requirements

- Python 2
- PIL (Python Image Library) 


## Usage

1. Place deskew.py together with *copies* of the files that you want to correct into an empty directory. The files should be in JPEG format and their filenames should end in '.jpeg'.
2. Run the script in a terminal window with the command
`python deskew.py`
3. All your image files will be corrected in place.