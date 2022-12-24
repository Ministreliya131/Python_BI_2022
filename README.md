# UNIX tools python3 realisation

## Utilities ##

- **wc.py** - imitates the UNIX **wc** utility. Counts the number of lines, words and bytes in the file. Can take three options: -l (line count), -w (word count), -c (byte count). If options are not specified all of them are considered as True by default;
- **sort.py** - imitates the UNIX **sort** utility. Takes no options. Can take any number of files or read from command line input. Sorts the content lines in alphabetical order ingoring the lettercase;
- **rm.py** - imitates the UNIX **rm** utility. Takes the option -r (recursive). Takes the path to the file or directory. -r option is required to recursively remove the directory;
- **ls.py** - imitates the UNIX **ls** utility. Prints all files and directories in the specified directory. Can take option -a (hidden files/directories shown).

**sort.py** and **wc.py** can work in pipes.

## Installation and usage ##

To get all the functions provided it is recommended to copy the repository to your local machine with the command `git clone git@github.com:Ministreliya131/Python_BI_2022.git` and go to the branch 8 with the command 'git checkout sys_and_os_hw'.

The functions might be executable but it is recommended to make them executable locally using the following command `chmod +x <command_name>`.

The commands could be executed from the folder as following:

`./command_name.py`

To execute the commands from any folder you could add them to your PATH variable or make an alias in your **./bashrc** file.
