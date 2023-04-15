# Epic Games Scraper 

![Epic_Scraper](https://user-images.githubusercontent.com/90666615/231628758-31352eb0-3121-4a50-b258-06f82e354451.png)

<p>This Python program scrapes all the useful information about each free weekly games of Epic Games.
It retrieves the review of each free games on Metacritic. Then stores the information in Excel and sends a copy to the user. </p>

## Tools used:
- Python/Selenium: is used because each free games is dynamically generated using Javascript.
- Pandas: is used to store and organize all the data scraped.
- Pickle: is used to store and load cookies to avoid pop up alerts.
- Twilio:  is used to send a copy of the info to the user's phone. 
- Window Task Scheduler: is used so that this program can execute automatically.


## A Simple Walk Through:
**Firstly, this program visits Epic Games and scrapes the name, date, price, and genres of each free games.**
![Screenshot 2023-04-12 195604](https://user-images.githubusercontent.com/90666615/231624729-ca16de6c-0361-4a6b-a464-a9bd7412a489.png)

**Then it navigates to Metacritic to scrape the Meta Score and the User Score of each free game.**
![Screenshot 2023-04-12 214142](https://user-images.githubusercontent.com/90666615/231625332-726b2ecb-ba86-44e7-972e-eb7343eafbe0.png)


**It stores all the information it get into an Excel document.**
![Screenshot 2023-04-12 200417](https://user-images.githubusercontent.com/90666615/231625379-75cbe3b7-4781-423a-8973-ac2fdf3f57e0.png)

**Finally, it sends a copy to the user's phone.**
![IMG_2795](https://user-images.githubusercontent.com/90666615/231625426-e577f961-752d-41c9-8c95-cd119fe5f466.jpeg)
