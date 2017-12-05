This is a FireEye Deployment Tool - Platinum Deluxe Edition

I never intended to release this, but after talking with several people at FireEye Summit, I was convinced that this would be helpful to others. 

The purpose of this tool is to remotely manage multiple FireEye appliances from a single interface. FireEye does not provide an API for device management, so I made my own. It utilizes pexpect and requires that you script out each command into a function. This provides speed and accessibility that the FireEye CMS does not offer. This tool will work on all NX devices as well as HX. 

I may add more features in the future. I may not. Feel free to fork and add your own.

Install dependencies.
Place all files a the local folder.
Run fedeploy.py.
Enjoy!