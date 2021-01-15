# math
![Logo](https://image.prntscr.com/image/oLX0Jnc2SHWXiAs7ZoPs6A.png)

This is a console chat for special lovers of this shit.
The chat will be improved (both the client side and the server side).
Thank you for noticing and trying it!

Original repository:


[![Original repository](https://github-readme-stats.vercel.app/api/pin/?username=Wiskey666&repo=MATH)](https://github.com/Wiskey666/MATH)

# Version info
**Alpha 1_5.5.1**

Commands update...
Ban, kick, mute are here ;3

Some comments in code... 

# Installation
1. Install colorama and win10toast
```no-highlight
pip install colorama
pip install win10toast
pip install psutil
pip install builtins
```

2. Run chat_server.py and enter ip, port and channel name.

3. Run chat_client.py and connect to server..

It's all :3

# Сonfiguration
Consider the main.conf file...
```no-highlight
[General]
Auto: 1
Log: 1
IP: localhost
PORT: 55555
CH_NAME: NAME
RULES: Rules
```

> :warning: **Important:** 
> ALLWAYS USE 1 SPACE BETWEN PARAMETER AND VALUE!
> ALLWAYS RULES MUST BE IN ONE STRING!


`Auto` - auto-init parameter. (1 - enable, 0 - disable)


	`IP` - auto-init host ip
	`PORT` - auto-init host port
	`CH_NAME` - auto-init host name
	
	
`Log` - logging parameter. (1 - enable, 0 - disable) (NOW NOT WORKING!!)


`RULES` - rules of the server... 


> :warning: **Important:** ALLWAYS RULES MUST BE ON ONE LINE!

# Commands

`/q` - Exit from the server


`/rules` - Show server rules


`/kick {user}` - Kick specified user 


`/ban {user}` - Ban specified user


`/unban {user}` - Unban specified user


> Ban until the server is restarted ...


`/mute {user}` - Mute specified user 


`/unmute {user}` - Ummute specified user  

# Error codes
| Code   | Error or status         |
|:------:| ----------------------- |
| 503    | Incorrect nickname.     |
| 409    | Unsupported version.    |
| 403    | Access denied.          |
| 401    | Already exist client.   |
| 400    | Kick from the server.   |
| 1      | Exit, Success.          |
