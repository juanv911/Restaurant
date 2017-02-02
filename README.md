# Restaurant Menu
Project for a restaurant menu app, where users can add, edit and remove restaurants and menu items to their restaurants. Users can sign in using Facebook via Oauth2, and can only edit and delete their own data.

## Table of contents
* [Requirements](#requirements)
* [Quick start](#quick-start)

## Requirements
* Python 2.7
* Vagrant

## Quick start
* Clone this repo `git clone https://github.com/juanv911/Restaurant` inside your vagrant folder.
* Change to the `/Restaurant` directory.
* In login.html and header.html your Facebook App ID.
* In fb_client_secrets.json include your Facebook App ID and App Secret Key.


* Start vagrant virtual machine with `vagrant up`.
* Run the following code on terminal: `vagrant ssh` to connect to the virtual machine using ssh.
* Run the following code on terminal: `cd /vagrant/Restaurant/` to change directory to this project.
* Run the following code on terminal to populate DB: `python lotsofmenus.py`.
* Run the following code on terminal to run the server locally: `python project.py`.
