from subprocess import check_output

a = check_output(["python", "test.py","--tag=best"])
print "a:", a