from telscraper.scraper import TelScraper


# you can get telegram development credentials in telegram API Development Tools
API_ID = '+++++++'
API_HASH = '++++++++++++++++++'

# use full phone number including + and country code
PHONE = '++++++++++'
USERNAME = '++++++++++'

# number of messages to recive via each request
# it shuld not be above 100
LIMIT = 100

# number of total messages you want to get from a chanel
# it shuld be bigger than LIMIT and it is better be divisible by LIMIT
TOTAL_COUNT_LIMIT = 200


# you can see what choices you can make
# also if you don't provide a type in here
# you have to provide it via CLI
print(TelScraper.USER_CHOICES)
OPERATION_TYPE = 1


# you can choose where to store your downloads
DOWNLOAD_DIR = './download/'
# channel id or link
URL = '**********************'



# create an object from TelScraper
sc = TelScraper(api_id=API_ID, api_hash=API_HASH, username=USERNAME, phone=PHONE)
# simply run
all_messages, downloaded_messages = sc.run(TOTAL_COUNT_LIMIT, LIMIT, URL, OPERATION_TYPE, DOWNLOAD_DIR)

# all_messages is a python dict that provide a rich data about all messages you crawled in a channel
print(all_messages)
# downloaded_messages is a python dict that provide a rich data about all messages you crawled in a channel
print(downloaded_messages)
