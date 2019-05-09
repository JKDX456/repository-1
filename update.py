import subprocess
#subprocess.Popen('powershell.exe git add .')
up_comment = input("Enter update info: ")
subprocess.Popen('powershell.exe git add -u; powershell.exe git status; powershell.exe git commit -m "' + up_comment + '"; powershell.exe git push')
