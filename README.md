
# About Whatsapp-manager💻
Suppose you have a task to send multiple product pictures along with style/Name on whatsapp? 
whatsapp-manager is the best solution for you.



## What Whatsapp-manager Do?🤔
Whatsapp-Manager can send your messeges/pictures to the person or Group chat that you want to

## How it works?
By reading the code you will see first i have provided excel sheet path in dataframe to let the bot knows what texts and images are need to be send along with picture. 
In my excel sheet there were 4 columns and each column had differnt text but i only want to send the values of first column and picture.
So i created a loop where i've provided folder path where i have saved my pictures, Now when the bot enters in the loop it will select the pictures from the folder one by one and match the name of the picture with the values of my fourth column where i have saved pictures names and send it to your desired person

E.g: Excel img name(4th column) = Lion.png and folder img name = Lion.png, if the condition matched the bot will extract the value of 1st column and send it to the person.

The first column values can be anything for example: "This is lion".

Still I have added comments on each line of the code so you can better understand the what this code actually doing




## Installation

###1-Open visual studio code or any code editor select a folder where you want to clone the repo
###2-Clone the Repo

```bash
https://github.com/SaudZafeer/Whatsapp-manager.git
```
###3-Install all the required packages
After cloning the code just open your terminal and copy paste the line below to get the requirement file to run the code.
```bash
pip install -r requirnments.txt
```
#### How To Create Requirnment.txt

```
pip freeze > Requirnment.txt
```

## Challenges:
The worst challenge was to make sure the picture should be match with the name if the excel file column
## If the bot stops workings:
If suddenly the bots stops working while running the code there are high chances that there is an issue with its elements Paths(Xpaths, CSS Selector, ID, etc). These kind of problems you will only face if the website gets updated and coordinates becomes different
