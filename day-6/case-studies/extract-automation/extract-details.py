# name, phone, email, job id


import os, os.path
import re

# get the list of files to process
path = r"."
os.chdir(path)

resumes = [file for file in os.listdir() if os.path.splitext("resume-01.txt")[1][1:] == 'txt']

print(resumes)

# patterns

email_pattern = r""
phone_pattern = r""
jobid_pattern = r""
name_pattern  = r""

# function to extract the data

def extract(file):

    fhandler = open(file)
    content = fhandler.read()
    fhandler.close()

    m = re.search(email_pattern, content)
    if m:
        email = m.group()
    else:
        email = ''
    phone = 'phone'
    name  = 'name'
    jobid = 'jobid'

    return name, phone, email, jobid


# delete the previous "jobapplicants.txt"
# use functions from os.path



# write the data to a file

fhandler = open("jobapplicants.txt", 'w')
for resume in resumes:
    name, phone, email, jobid = extract(resume)
    print(name, phone, email, jobid)
    fhandler.write(','.join([name, phone, email, jobid]) + '\n')

fhandler.close()