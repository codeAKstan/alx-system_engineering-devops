
# Processes and signals
A project on  Processes

## Image

![App Screenshot](https://journaldev.nyc3.cdn.digitaloceanspaces.com/2020/08/top.png)

## Requirements

### task : 0 
Write a Bash script that displays its own PID.

### task : 1
Write a Bash script that displays a list of currently running processes.

Requirements:

Must show all processes, for all users, including those which might not have a TTY
Display in a user-oriented format
Show process hierarchy

### task : 2
Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.

Requirements:

You cannot use pgrep
The third line of your script must be # shellcheck disable=SC2009 (for more info about ignoring shellcheck error here)

### task : 3
Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.

Requirements:

You cannot use ps