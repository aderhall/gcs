# gcs
## Git Commit Suicide! A tool for dealing with git quickly.

Git is very easy to work with. However, programmers are lazy and want to be as efficient as possible. One command to do multiple tasks is nice. That's what gcs does. Basically it uses git for you so you can spend less time on git and more time on your project.

Note: gcs does not do everything git does. It will not replace git. Just help you out with it.

## Requires:
+ Python 3
+ Unix type shell
+ git

## Installation:
### Linux/OSX
For now, all the 'installation' is is putting an alias in your bashrc/profile/whatever that sets gcs equal to "python3 ~/gcs/gcs.py"
For reference, its:
```
cd && curl -O https://raw.githubusercontent.com/aderhall/gcs/master/gcs.py && touch ~/.bash_profile && echo ";alias gcs=\"python3 ~/gcs/gcs.py\"" | cat >> ~/.bash_profile && cd - && source ~/.bash_profile;
```
That will automatically set it up. Once done, type gcs to use the command.

### Windows
Why would you want to use windows for git projects? Well, just run the python script (but it won't work, i'm warning you), get fed up and install linux. I mean seriously, unless you're gaming there's no reason to have a pc.

## Usage:
Type ''gcs''
It will check your status and guide you through the process of *gitting*
Here's what it would look like after you just changed something in the repo:
```
bash-3.2$ gcs
Found git data!
You may have some unstaged changes. Stage them? [y/n]: y
Staged all changes!
Commit these changes? [y/n]: y
Please enter the commit message for this action: Update README with message: Update README with message: Update README with message...
Checking status...
Found git data!
Your code appears to be up to date with your last commit. Checking remotes...
Checking remote: origin
Differences found between local and remote: origin
Push these changes? [y/n]: y
All remotes checked, found no changes. My work here is done!
bash-3.2$ Yay!
```
Yes the messages are cheesy. Deal with it.

## Modification:
I really don't care how much you modify this.
