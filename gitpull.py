from os import getcwd
import git

print('')
print("started")
print('')
getcwd = getcwd() 
print('')
print(getcwd, " : Directery")
print('')

repo = git.Repo(getcwd)
repo.git.stash()
repo.git.pull()

print('')
print("stashed and pulled repos")
print('')
print("FINISHED")
