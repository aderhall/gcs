import sys
import os
import subprocess
import traceback
class Git_Commit_Suicide:
    def __init__(self):
        self.arguments = sys.argv
        self.cname = self.arguments[0]
        if len(self.arguments) > 1:
            if self.arguments[1].startswith('-'):
                self.flags = self.arguments[1]
                self.arguments = self.arguments[2:] if len(self.arguments) > 1 else []
            else:
                self.flags = ''
                self.arguments = self.arguments[1:]

    def system_call(self, command, newlines=False):
        """Run system commands and get output"""
        p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        p = p.stdout.read()
        p = str(p).replace('b\'', '')
        p = p.replace('\n', '') if not newlines else p
        return p

    def main(self):
        try:
            """The actual program"""
            # Check if git exists and get status
            self.status = 'FAIL'
            try:
                if 'fatal: Not a git repository (or any of the parent directories): .git' in str(self.system_call('git status')):
                    print('No git here! Try a different folder?')
                    os._exit(1)
                else:
                    print('Found git stuff!')
                    self.status = str(self.system_call('git status'))
            except:
                e = sys.exc_info()[0]
                print('Hmm, I got an error here. Maybe this is the wrong folder?', '\nError: ', e)
                os._exit(1)
            if 'up-to-date' in self.status:
                print('Your code appears to be up to date with your last commit. Checking remotes...')
                self.remotes = self.system_call('git remote', True)
                #print(self.remotes)
                remote = ''
                self.remoteslist = []
                for i in range(len(self.remotes)):
                    #print('Char:', self.remotes[i])
                    if self.remotes[i] == 'n' and self.remotes[i-1] == '\\':
                        self.remoteslist.append(remote[:-1])
                        remote = ''
                    else:
                        remote += self.remotes[i]
                #print(self.remoteslist)
                diffs = []
                for i in self.remoteslist:
                    #print('Checking remote:', i)
                    diffs.append(self.system_call('git --no-pager diff --raw master ' + i + '/master'))
                #print(diffs)
                for i in range(len(diffs)):
                    if len(diffs[i]) > 1:
                        done = False
                        while not done:
                            print('Differences found between local and remote:', self.remoteslist[i])
                            check = input('Push these changes? [y/n]: ').lower()
                            if check == 'y':
                                self.system_call('git push ', self.remoteslist[i])
                                done = True
                            elif check == 'n':
                                done = True
                            else:
                                print('Please type yes/no')
            elif 'unstaged' in self.status:
                print('You may have some unstaged changes.')
            else:
                print('That\'s pretty much it.')

        except KeyboardInterrupt:
            print("Shutdown requested...exiting")
        except Exception:
            traceback.print_exc(file=sys.stdout)


gcs = Git_Commit_Suicide()
if __name__ == "__main__":
    gcs.main()
