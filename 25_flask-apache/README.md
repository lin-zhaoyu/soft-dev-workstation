# how-to :: CREATE A DIGITAL OCEAN DROPLET WITH UBUNTU AND APACHE
---
## Overview
Guide to creating an ubuntu 20.04 virtual machine ("droplet") and installing Apache2 web server on it.

### Estimated Time Cost: 20 minutes

### Prerequisites:
- Have a [droplet](https://docs.digitalocean.com/products/droplets/how-to/create/)
- Be able to access it with [ssh](https://docs.digitalocean.com/products/droplets/how-to/connect-with-ssh/)
- Install pip3 with sudo
``sudo apt-get install python3-pip```
- Install virtual environment and flask with sudo
- Create a new [sudo enabled user](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-sudo-enabled-user-on-ubuntu-20-04-quickstart)
1. Install apache with
  ```
  $ sudo apt-get update
  $ sudo apt-get install apache2
  ```
2. Install wsgi library
  ```
  $ sudo apt-get install libapache2-mod-wsgi-py3
  ```
  and make sure it's enabled/enable it
  ```
  $ sudo a2enmod wsgi
  ```
3. Set up a file structure which you host your __init__.py file
  in my case I hosted it inside
  /var/www/FlaskApp/FlaskApp
4. Put something in the file
  key thing:
  ```
  if __name__ == "__main__":
    app.run(host = "0.0.0.0")
  ```
5. Configure the config file
  open it with
  ```
  $ sudo nano /etc/apache2/sites-available/FlaskApp.conf
  ```
  then paste in
  ```
  <VirtualHost *:80>
  ServerName digital ocean ip address
  ServerAdmin youemail@email.com
  WSGIScriptAlias / /var/www/FlaskApp/flaskapp.wsgi
  <Directory /var/www/FlaskApp/FlaskApp/>
    Order allow,deny
    Allow from all
  </Directory>
  Alias /static /var/www/FlaskApp/FlaskApp/static
   <Directory /var/www/FlaskApp/FlaskApp/static/>
    Order allow,deny
    Allow from all
  </Directory>
  ErrorLog ${APACHE_LOG_DIR}/error.log
  LogLevel warn
  CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
  ```
  EXAMPLE:
  ```
  <VirtualHost *:80>
  ServerName 62.227.2.199 *digital ocean ipv4
  ServerAdmin zlin20@stuy.edu *email
  WSGIScriptAlias / /var/www/FlaskApp/flaskapp.wsgi *location leaidng to flaskapp
  <Directory /var/www/FlaskApp/FlaskApp/> *where __init__>py is
    Order allow,deny
    Allow from all
  </Directory>
  Alias /static /var/www/FlaskApp/FlaskApp/static
   <Directory /var/www/FlaskApp/FlaskApp/static/>
    Order allow,deny
    Allow from all
  </Directory>
  ErrorLog ${APACHE_LOG_DIR}/error.log
  LogLevel warn
  CustomLog ${APACHE_LOG_DIR}/access.log combined
  </VirtualHost>
  ```
6. enable the flaskapp with:
  ```
  $ sudo a2ensite 000-default.conf
  ```
  restart apache with
  ```
  $ service apache2 restart
  ```
7. configure the wsgi file
  cd into where the flaskapp.wsgi is
  ```
  sudo nano flaskapp.wsgi
  ```

restart apache again, and everytime you change a py file
### Resources
https://www.thegeeksearch.com/setup-flask-with-apache-and-wsgi/

https://www.digitalocean.com/community/tutorials/how-to-create-a-new-sudo-enabled-user-on-ubuntu-20-04-quickstart
(please verify ; some of these are old links)

---

Accurate as of (last update): 2022-01-20

#### Contributors:  
Zhao Yu Lin pd1  
