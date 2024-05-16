# Install:
```commandline
git clone https://github.com/mooamel/lovetik.git
```

# About this project:
- lovetik is use:
- lovetik ( [lovetik.com](https://lovetik.com) )
- Supporting Sync & Async.
- Thanks to [@zaid505](https://github.com/zaid5o5) cuz i'm get the idea for type.py file from him ( [Source](https://github.com/zaid5o5/trengine/blob/main/trengine/types.py) ).

# How to use?
- Here an example to use it:
```python
from lovetik import client

cli = client()
url = 'https://vm.tiktok.com/ZMMj9fmyS/'

info    =  cli.get(url) # Result : info about video as :  Dict {}
download = cli.save(link = info.mp3, type = 'mp3', name = 'audio') # Result : info about downloading status as  :   Dict {}.  NOTE: u can use save method with (cover , avater , mp3 , mp4 , mp4_rights). ex : info.avatar

```
- Here an async example:
```python
from lovetik import async_client
import asyncio

cli = async_client()
url = 'https://vm.tiktok.com/ZMMj9fmyS/'

async def main():
    info = await cli.get(url) # to get the info about vid
    print(
        await cli.save(info.cover,'jpg') # to save the cover of vid
    )

asyncio.run(main())
```
