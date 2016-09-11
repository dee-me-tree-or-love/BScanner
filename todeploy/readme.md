# Howdy, reader

This is a readme to the deployment directory

## Abstract:

This is a folder with scripts that has to be deployed to the rasbery pi
It has combined the sections of `'bouncer'` - the application to record the visitors
and the `'secretary'` - the app to analyze the data recorded by the bouncer

## Workflow: 

The aplication `'bouncer'` is to be used to record all the visitors at the event.
Once it's done one has to enter the 'secretary' mode and record all the saved data to the database.
Then the process is finished.

## Startup:

The application has to start at FiMain.py in the Raspberry PI's rc.local file.
The application will run while the system is booting by setting python `/home/pi/myscript.py &` - a command with an ampersant so that it will fork the process and keep on loading.
To exit the `'bouncer'` mode and start the `'secreatary'` part (which is done automatically) one has to scan the reserved **`secr`** barcode.

## Killing the bouncer

Entering **`exit`** will just terminate the process
Entering **`secr`** will terminate the process and start the `secreatary` routine

## The build:

The `'bouncer'` runs constantly unless one enters "exit"/"secr" to terminate.
The `'secretary'` runs untill all the records are analyzed and are saved to the database and finsihes then.
The file `dbsetup.txt` stores a json object with db configurations - change accordingly to the requirements

