#!/bin/bash
#This is a bash script that can be included inside of cron to automatically start downloading files.
#My current recommendation is to create two cron jobs to execute every 30 minutes
#Example 30 * * * * root cd /scriptdirectory/ && /scriptdirectory/vturlwrapper.sh
#Example 00 * * * * root cd /scriptdirectory/ && /scriptdirectory/vturlwrapper.sh
#Run the Python script to download the files
python urlvt.py
#Create a variable with a date timestamp to allow unique files
stamp=$(date "+%s")
#Run the parser to find all the higher positives
python myparse.py
#Move the output file to a unique filename
mv newoutput.txt newoutput.$stamp.txt
