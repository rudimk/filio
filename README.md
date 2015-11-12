# filio
A dead-simple UI which you can use to quickly upload/download files to and from a cloud instance. It's essentially a [Flask-Admin](https://flask-admin.readthedocs.org/en/latest/introduction/) app with the File Manager enabled, and basic HTTP auth through [Flask-BasicAuth](http://flask-basicauth.readthedocs.org/).

## Why?
...I don't like using ```scp``` much. 

## How do I use it?

First, clone this repo:

```git clone https://github.com/rudimk/filio.git```

I use [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/) to manage Python environments. You're free to use [virtualenv](https://virtualenv.readthedocs.org/en/latest/), or install filio's dependencies to your system's Python libraries. Your call. 

Next, install dependencies:

```cd filio/```
```pip install -r requirements.txt```

Good job, young padawan. The force of Python is strong in you. But a final test remains. Time to declare your true allegiance...*cough*, your HTTP credentials. Open up ```creds.py``` and add a username and password, like this:

```python
username='johndoe'
password='myfancypassword123'
```

Good. Now, time to run the app:

```python app.py```

Visit ```http://<YOUR_SERVER_IP_OR_DOMAIN:9500``` and log in with the credentials you supplied earlier.

## Issues

1. Since this app uses HTTP auth, it's obviously not very strong. Anyone sniffing your packets will be able to access your server. SSL helps, as does *not* having HTTP auth. I'm thinking of adding Unix-based auth here, but it's a bitch to figure out if you use SSH keys instead of passwords. 
2. Uploading and downloading can be a little slow here. But hey, it works.

## Stuff I plan to add

1. Better auth mechanisms.
2. A nice web terminal. Who needs Xterm and iTerm2 and Cmder?
3. Feel free to add something you want.

##License

[Copyright (c) 2015 Rudraksh MK](https://github.com/rudimk/filio/blob/master/LICENSE)


