
"""
  sync client :
"""

from lovetik import client

cli = client()
url = 'https://vm.tiktok.com/ZMMj9fmyS/'

info    =  cli.get(url) # Result : info about video as :  Dict {}
download = cli.save(link = info.mp3, type = 'mp3', name = 'audio') # Result : info about downloading status as  :   Dict {}.  NOTE: u can use save method with (cover , avater , mp3 , mp4 , mp4_rights). ex : info.avatar


"""
  async client :
"""
from lovetik import async_client
import asyncio

cli = async_client()
url = 'https://vm.tiktok.com/ZMMj9fmyS/'

async def main():
    info = await cli.get(url) # to get the info about vid
    print(
        await cli.save(info.cover,'jpg') # to save the cover of vid, u can use (cover , avater , mp3 , mp4 , mp4_rights) also
    )

asyncio.run(main())
