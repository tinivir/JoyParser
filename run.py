from subprocess import check_output

a = check_output(["python", "main.py","--tag=best"])
print "a:", a