import subprocess

# subprocess.run("ls",shell=True)

# here we need to go for the capture_output as True which does the same as below 

#another appraoch will be for the capture_output=True
##########################################################
# p1=subprocess.run(["ls","-la"],capture_output=True)

#another approach for printing to the console using CompltedProcess obj
##########################################################################
# p1=subprocess.run("ls -la",shell=True,stdout=subprocess.PIPE,text=True)

#redirecting to the stdout the stderr
################################################################
# p1=subprocess.run("ls -la dne",shell=True,stderr=subprocess.STDOUT,text=True)

#we can also move it to the PIPE as below 
# p1=subprocess.run("ls -la dne",shell=True,stderr=subprocess.PIPE,text=True)

#redirecting to the devnull file 
############################################
p1=subprocess.run("ls -la dne",shell=True,stderr=subprocess.DEVNULL,text=True)



print(p1.returncode)