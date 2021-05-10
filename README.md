# LavaExe
----------

* Just a simple python program to start latest Lavalink.
* You can use `lavaexe.py` to download and run the latest available Lavalink at the time.
* Option to choose the Master build or the dev build. 
	* Dev relies on teamcity ci. I can't get the latest url unless updating the script on every new dev build. So the latest version before the current commit time is available for dev build. Master build is always latest.

## Settings
------------

* In application.yml
	* Default Port : 4488 
	* Change your password.
	* Uncomment Ratelimit block and use your IP block to avoid Ratelimits.
	* Sources can be turned to True based on your requirements. 

## Requirements
---------------

* Make sure you have the right version of Java mentioned in https://github.com/freyacodes/lavalink .
