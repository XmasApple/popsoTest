import getpass

import asyncio
import os

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from . import config

client = TelegramClient(config.phone, config.api_id, config.api_hash)


async def connect():
    await client.connect()

    if not await client.is_user_authorized():
        await client.send_code_request(config.phone)
        try:
            await client.sign_in(config.phone, input('Enter verification code: '))
        except SessionPasswordNeededError:
            await client.sign_in(password=getpass.getpass('Password: '))


async def get_last_messages_from_channel(channel_name, limit=10):
    channel = await client.get_entity(channel_name)
    messages = await client.get_messages(channel, limit=limit)
    return messages


async def download_media(message, tag):
    folder = f'media/{tag}'
    if not os.path.exists(folder):
        os.makedirs(folder)
    path = "None"
    to_download = None
    if message.photo:
        to_download = message.media.photo
    elif message.document:
        to_download = message.media.document
    if to_download:
        path = await client.download_media(to_download)
        ext = path.split('.')[-1]
        new_path = f'{folder}/{message.id}.{ext}'
        if os.path.exists(new_path):
            os.remove(new_path)
        os.rename(path, new_path)
        path = new_path
    return path


async def get_message_data(message, tag):
    photo_path = await download_media(message, tag)
    text = message.message
    date = message.date
    return text, tag, date, photo_path


async def process_channel(channel_name, tag):
    messages = await get_last_messages_from_channel(channel_name)
    tasks = []
    for message in messages:
        tasks.append(get_message_data(message, tag))
    results = await asyncio.gather(*tasks)
    return results


async def parse():
    await connect()
    tasks = []
    for channel_name, tag in config.channels:
        tasks.append(process_channel(channel_name, tag))
    results = await asyncio.gather(*tasks)

    results = [item for sublist in results for item in sublist]
    # get all results with empty text, remove them and delete media files
    empty_texts = [result for result in results if not result[0]]
    for result in empty_texts:
        if result[3]:
            os.remove(result[3])
    results = [result for result in results if result[0]]
    return results


def start():
    with client:
        return client.loop.run_until_complete(parse())


if __name__ == '__main__':
    start()
