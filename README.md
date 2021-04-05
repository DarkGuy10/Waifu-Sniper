<h1 align="center">Waifu Sniper</h1>
<p align="center">A Discord self-bot for sniping mudae waifus/husbandos, written in Python3.</p>

![Waifu with sniper](https://raw.githubusercontent.com/DarkGuy10/Waifu-Sniper/master/assets/waifu.jpg)

## Warning!
Self bots like this break Discord's TOS and hence your account may get **banned**. <br>
I do not endorse these in anyway, this code is just a *proof of concept*.

## Criteria for sniping
```
A. Kakera >= min_kakera # this can be changed, check line#7 of main.py
B. In someone's wishlist
```

## Description
The bot uses embed color values (**HARDCODED VALUES**) to filter unclaimed waifus/husbandos and if either of the above conditions are satsified, adds a '❤️' reaction to claim.<br>
#### Note: Server kakera must be enabled

## Environment variable
The token for the self bot must be stored in an environment variable named `TOKEN`.<br>
Alternatively, you can edit `line #6` of `main.py`

## Deploying
The repo is ready to be deployed on heroku.<br>
###### Make sure to edit the config vars properly!

##### Code with ❤️ at GitHub.