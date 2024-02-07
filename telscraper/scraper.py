from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import PeerChannel
import re

class TelScraper:

    USER_CHOICES = {
            1 : 'no download',
            2 : 'audio download only',
            3 : 'video download only',
            4 : 'picture download only',
            5 : 'audio and video download only',
            6 : 'audio and picture download only',
            7 : 'picture and video download only',
            8 : 'download all',
            9 : 'download pdf only',
        }

    def __init__(self, api_id, api_hash, username, phone):
        self.api_id = api_id
        self.api_hash = api_hash
        self.username = username
        self.phone = phone
        # Create the client and connect
        self.client = TelegramClient(username, api_id, api_hash)
        self.me = None
        self.channel = None

    async def connect(self):
        await self.client.start()
        print("Client Created")
        # ensure you are authorized
        if await self.client.is_user_authorized() == False:
            await self.client.send_code_request(self.phone)
            try:
                await self.client.sign_in(self.phone, input('enter the code: '))
            except SessionPasswordNeededError:
                await self.client.sign_in(password=input('password: '))

        self.me = await self.client.get_me()


    async def set_channel(self, user_input_channel):
        if user_input_channel.isdigit():
            entity = PeerChannel(int(user_input_channel))
        else:
            entity = user_input_channel
        channel = await self.client.get_entity(entity)
        self.channel = channel


    def get_operation_type(self):


        while True:
            print('Please Enter operation type - enter the number from list blow')
            for choice_id, description in TelScraper.USER_CHOICES.items():
                print(f'{choice_id} - {description}')
            user_input = input('>>>')
            if not user_input.isdigit():
                print('Enter a valid input')
                continue
            user_input = int(user_input)
            user_choice = TelScraper.USER_CHOICES.get(user_input, None)
            if not user_choice :
                print('Enter a valid input')
                continue
            return user_input


    async def rich_scrap(self, total_count_limit, limit, url, operation_type=None, downloads_dir='downloads'):
        await self.connect()
        await self.set_channel(url)
        if not self.channel:
            raise Exception('No channel set for this object')
        offset_id = 0
        all_messages = []
        downloaded_messages = []

        if not TelScraper.USER_CHOICES.get(operation_type, None):
            operation_type = self.get_operation_type()

        while True:
            history = await self.client(GetHistoryRequest(
                peer=self.channel,
                offset_id=offset_id,
                offset_date=None,
                add_offset=0,
                limit=limit,
                max_id=0,
                min_id=0,
                hash=0
            ))
            if not history.messages:
                break
            messages = history.messages
            for message in messages:
                all_messages.append(message.to_dict())
                if operation_type == 2 and message.audio:
                    path = await self.client.download_media(message.media, downloads_dir)
                    print(f'downloaded to {path}')
                    downloaded_messages.append(message.to_dict())
                elif operation_type == 3 and message.video:
                    path = await self.client.download_media(message.media, downloads_dir)
                    print(f'downloaded to {path}')
                    downloaded_messages.append(message.to_dict())
                elif operation_type == 4 and message.photo:
                    path = await self.client.download_media(message.media, downloads_dir)
                    print(f'downloaded to {path}')
                    downloaded_messages.append(message.to_dict())
                elif operation_type == 5 and (message.audio or message.video):
                    path = await self.client.download_media(message.media, downloads_dir)
                    print(f'downloaded to {path}')
                    downloaded_messages.append(message.to_dict())
                elif operation_type == 6 and (message.audio or message.photo):
                    path = await self.client.download_media(message.media, downloads_dir)
                    print(f'downloaded to {path}')
                    downloaded_messages.append(message.to_dict())
                elif operation_type == 7 and (message.video or message.photo):
                    path = await self.client.download_media(message.media, downloads_dir)
                    print(f'downloaded to {path}')
                    downloaded_messages.append(message.to_dict())
                elif operation_type == 8 and (message.video or message.photo or message.audio):
                    path = await self.client.download_media(message.media, downloads_dir)
                    print(f'downloaded to {path}')
                    downloaded_messages.append(message.to_dict())
                elif operation_type == 9 and message.file and message.file.name and re.search(r"\.pdf$", message.file.name, re.IGNORECASE):
                    path = await self.client.download_media(message.media, downloads_dir)
                    print(f'downloaded to {path}')
                    downloaded_messages.append(message.to_dict())


            offset_id = messages[len(messages) - 1].id
            total_messages = len(all_messages)
            if total_count_limit != 0 and total_messages >= total_count_limit:
                break

        return all_messages, downloaded_messages


    def run(self, total_count_limit, limit, url, operation_type=None, downloads_dir='downloads'):
        with self.client:
            res = self.client.loop.run_until_complete(self.rich_scrap(total_count_limit, limit, url, operation_type, downloads_dir))
        return res
