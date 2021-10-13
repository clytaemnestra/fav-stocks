# Favourite Stocks App
<!-- TABLE OF CONTENTS -->
 <h2 style="display: inline-block">Table of Contents</h2>
  <ol>
    <li>
      <a href="#about-the-application">About The Application</a>
    </li>
      <ul>
        <li><a href="#functionalities">Functionalities</a></li>
      </ul>    
    <li>
      <a href="#what-have-i-learned">What Have I Learned?</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#heroku">Heroku</a></li>        
        <li><a href="#local-installation">Local installation</a></li>
      </ul>
    </li>
  </ol>


## About The Application

Favourite stocks is an application which I've made for learning purposes. It's a broker system, where users can buy & sell stocks. :bank: Every registered user is given $ 10 000 :moneybag: to start trading. 
![Application Screen Shot](https://user-images.githubusercontent.com/38294198/134824272-fd000470-1ec5-4218-8771-debdc6ab3b4f.png)
![Application Screen Shot](https://user-images.githubusercontent.com/38294198/134824336-6d69ef32-0882-4c20-801a-00749363eb33.png)


### Functionalities
* overview of owned stocks and available balance 
* buy a stock
* sell a stock 
* see history of transactions 
* see all stocks

## What Have I learned? 
* how to set up a Flask app 
* CRUD operations & database transactions in SQAlchemy
* I've used type annotations for the first time
* web scraping with Scrapy  
* how to write decorators 



<!-- GETTING STARTED -->
## Getting Started
### Heroku
The app is available on [this](https://fav-stocks.herokuapp.com/) URI address. Please note that I am using free tier, meaning it takes around 30 seconds for the app to start, if it's not active. 

In case you don't want to register, you can use the following credentials:
* username: example-user
* password: ExampleUser345

### Local Installation
To get a local copy up and running follow the steps below.

<details>
  
1. Clone the repo
```sh
git clone git@github.com:clytaemnestra/fav-stocks.git
```
2. Create a virtual environment and activate it
```sh
python3 -m venv venv
source venv/bin/activate
```
3. Install required packages
```sh
pip install -r requirements.txt
```
4. Create a Postgres database locally and set up environment variables
```sh
sudo -u postgres psql 
CREATE DATABASE database-name
\q 
export TEST_DATABASE_URL="postgres://user:password@localhost:5432/database-name"
```
5. Create tables
```sh
flask db init
flask db migrate
flask db upgrade
```
6. Fill database with stock data 
```sh
\copy stock FROM 'fav-stocks/application/stocks.csv' DELIMITER ',' CSV HEADER
```
7. Run the application
```sh
flask run
```
</details>
