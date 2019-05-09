import subprocess
#subprocess.Popen('powershell.exe git add .')
subprocess.Popen('powershell.exe git add -u; powershell.exe git status; powershell.exe git commit -m "test"; powershell.exe git push')
