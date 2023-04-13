# Epic Games Scraper 

Summary:
This python program scrapes all the useful information about all the free weekly games that Epic Games give out.
It retrives the review of each of the free games in Metacriti. Stores all the infomation in Excel and sends a copy to the user.

##Tools used:
- Window Task Schudler: is used so that this program can be run automatically daily.
- Selenium: is used becuase each of the free games are dynicmally generated using Javascript.
- Pandas: is used to store and organzie all the data scraped.
- Twiloi:  is used to send a copy of the info to user's phone. 


A Simple Walk Through:
Firstly, this program first visits the Epic Games and scrapes the name, date, price, and genres of all the free weekly games.
![Screenshot 2023-04-12 195604](https://user-images.githubusercontent.com/90666615/231624729-ca16de6c-0361-4a6b-a464-a9bd7412a489.png)

Then it naigets to Metacritic to scrape the Meta Score and User Score of each free game.
![Screenshot 2023-04-12 214142](https://user-images.githubusercontent.com/90666615/231625332-726b2ecb-ba86-44e7-972e-eb7343eafbe0.png)


Finally, it stores all the information it get into an Excel docemetn.
![Screenshot 2023-04-12 200417](https://user-images.githubusercontent.com/90666615/231625379-75cbe3b7-4781-423a-8973-ac2fdf3f57e0.png)

Sends a copy to the user's phone
![IMG_2795](https://user-images.githubusercontent.com/90666615/231625426-e577f961-752d-41c9-8c95-cd119fe5f466.jpeg)
