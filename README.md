# TelScraper


#### Description:
This Python application is built to interact with the Telegram API using the Telethon library. The Telethon library provides a simple and
efficient way to perform various tasks, such as retrieving chat history, downloading media, and more. With this application, you can easily
perform a wide range of operations with ease. Whether you want to download media from a channel or
retrieve chat history, this application has got you covered

this is a simple Telegram scraper built with teleton module to easily scrap and download data from an Telegram channel to your local machine

I Also created an example app using this scraper to show you how to work with it

it has 9 options you can use
-  no download
-  audio download only
-  video download only
-  picture download only
-  audio and video download only
-  audio and picture download only
-  picture and video download only
-  download all
-  download pdf only

Before running this application, you need to obtain the following information from the Telegram API:

-   `api_id`: Your application's API ID.
-   `api_hash`: Your application's API hash.
-   `phone`: Your Telegram account's phone number.
-   `username`: Your Telegram account's username (optional).

you can find your `api_id` and `api_hash` from [here](https://my.telegram.org/auth)

if you run this scraper for first time you need ro provide your phone number so it can create a client
but after that it will store your client data in a session so you won't need to do the same, twice


## how does it work ?
The code starts by importing the necessary libraries and defining a class called TelScraper. The class has a dictionary called USER_CHOICES which maps the user’s choice to a string that describes the choice. The class has an __init__ method that initializes the api_id, api_hash, username, and phone variables. The method creates a TelegramClient object and sets the me and channel variables to None.

The connect method connects to the Telegram client and ensures that the user is authorized. If the user is not authorized, the method sends a code request to the user’s phone number and prompts the user to enter the code. If the user has a password, the method prompts the user to enter the password.

The set_channel method sets the channel that the user wants to download media from. The method takes a user input channel and checks if it is a digit. If it is a digit, the method creates a PeerChannel object. Otherwise, the method sets the entity to the user input channel. The method then gets the channel entity and sets the channel variable to the channel.

The get_operation_type method prompts the user to enter the operation type and displays the choices available in the USER_CHOICES dictionary.

The rich_scrap method is an asynchronous method that takes in several parameters such as total_count_limit, limit, url, operation_type, and downloads_dir. The method connects to the Telegram client and sets the channel to the specified URL. The method then downloads media based on the user’s choice of operation_type. The operation_type variable is set to None by default, but if it is not in the USER_CHOICES dictionary, the method prompts the user to enter the operation type. The method then iterates through the messages in the channel and downloads the media based on the user’s choice of operation_type.


Here's an updated version of the text:

## Dependencies

If you cloned this repository, you can easily install all dependencies at once with the following command:

```
pip install -r requirements.txt
```

If you prefer to install the dependencies manually, you only need the `telethon` library. You can install it with the following command:

```
pip install telethon
```

However, for better download performance, it is recommended to install `cryptg` as well. You can use the following command to install it:

```
pip install cryptg
```
