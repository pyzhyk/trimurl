# trimurl
Website for trimming URLs. Stack: Python, Django


## Setup

1. Clone repository
```bash
git clone git@github.com:pyzhyk/trimurl.git
```
2. Change directory
```bash
cd trimurl
```
3. Install prerequisites
```bash
apt update
apt install python3 python3-pip mariadb
pip3 install -r requirements.txt
```

4. Log in as root user
```bash
sudo su
```

5. Set up database and log out from root user
```bash
systemctl start mysql
cat init.sql | mysql
exit
````

6. Run server
```bash
python3 manage.py runserver
```
7. Go to url: `http://127.0.0.1:8000/`


## Result

![Home](https://i.ibb.co/b1crCK0/Screenshot-2022-07-13-at-12-48-42-Home.png)
![SignUp](https://i.ibb.co/pvtLfDd/Screenshot-2022-07-13-at-12-48-59-Sign-Up.png)
![LogIn](https://i.ibb.co/h1MjgWn/Screenshot-2022-07-13-at-12-49-16-Login.png)
![Home](https://i.ibb.co/dcKM2Wz/Screenshot-2022-07-13-at-12-48-29-Home.png)
![NewUrl](https://i.ibb.co/5MqPZJ2/Screenshot-2022-07-13-at-12-57-59-Home.png)
![MyLinks](https://i.ibb.co/LC0pfwq/Screenshot-2022-07-13-at-12-48-15-Home.png)

