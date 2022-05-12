import subprocess

# test = subprocess.Popen(["docker run -d --name selenium_chrome -p 4444:4444 -p 5900:5900 -v /dev/shm:/dev/shm selenium/standalone-chrome-debug"], stdout=subprocess.PIPE)
# output = test.communicate()[0]

# import os
# os.system("docker run -d --name selenium_chrome -p 4444:4444 -p 5900:5900 -v /dev/shm:/dev/shm selenium/standalone-chrome-debug")

# subprocess.run("docker run -d --name selenium_chrome -p 4444:4444 -p 5900:5900 -v /dev/shm:/dev/shm selenium/standalone-chrome-debug",shell=True, check=True)


subprocess.run("docker", shell=True,check=True)