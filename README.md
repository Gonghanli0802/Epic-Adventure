# Epic Games Scraper 

Summary:
This Python program scrapes all the useful info about each of the free games that Epic Games sends out weekly.
Then it retrives the review of each of the free games in Metacriti.
Finally the program stores all the infomation in Excel and send a copy to the user.

Tools used:
Window Task Schudler: is used so that this program can be run automatically daily.
Selenium: is used becuase each of the free games are dynicmally generated using Javascript.
Pandas: is used to store and organzie all the data scraped.
Twiloi:  is used to send a copy of the info to user's phone. 


A Simple Walk Through:
Firstly, this program first visits the Epic Games and scrapes the name, date, price, and genres of all the free weekly games.
![Screenshot 2023-04-12 195604](https://user-images.githubusercontent.com/90666615/231624729-ca16de6c-0361-4a6b-a464-a9bd7412a489.png)

Then it naigets to Metacritic to scrape the Meta Score and User Score of each free game.
Finally, it stores all the information it get into an Excel docemetn while sending a copy of the info to the user's phone.
