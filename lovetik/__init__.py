from aiohttp import ClientSession
from requests import post,get
from .type import LinkResult,DownloadResult
import os

class client:
    def __init__(self) -> None:
        pass

    def get(self,link:str) -> "LinkResult":

        """
            Get Info about the link & get link for video and audio. (sync function)

            Args:
                link: str : Link the video

            Returns:
                LinkResult: Info the video : _mp4_mp3_link_   name,username the author    etc...
        """

        try:
            _result = post( "https://lovetik.com/api/ajax/search", data = { "query" : link } , headers = { "user-agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0" } ).json()   
        except Exception as e:
            raise BaseException(e)
        return LinkResult.parse(_result, link)

    def save(self,link: str, type: str, name: str = 'momolove') -> "DownloadResult":

        """
            Save the video in    VDownloads/    directory

            Args:
                link (str): real link (mp4 , mp3, jpeg, png)
                type (str): download type (mp4, mp3, jpeg, png)
                name (str, optional): name vid/audio . Defaults to 'momolove'.

            Raises:
                Exception1: this exception if there's problem in code (maybe i will update it soon... >_<)
                Exception2:  this exception if the user enters his values, and values not (mp4 or mp3 or jpeg, png)

            Returns:
                DownloadResult: Info about download 
        """

        if not os.path.exists('VDownloads'):   os.makedirs('VDownloads')

        if type.lower() in ['mp4','mp3','png','jpg','jpeg']:
            try:
                with open('VDownloads/'+name+'.'+type.lower(), "wb") as f:
                    size = f.write(get(link).content)
                
                return DownloadResult.parse({'status':'ok','link':link,'size':size,'type':type.lower(),'path':'VDownloads/'+name+'.'+type.lower()})
            except Exception as e:
                raise Exception(e)
        else:
            raise Exception('Just Type : mp3 or mp4 or jpeg, png')

class async_client:
    def __init__(self) -> None:
        pass

    async def get(self,link) -> "LinkResult":
        """
            Get Info about the link & get link for video and audio. (async function)

            Args:
                link: str : Link the video

            Returns:
                LinkResult: Info the video : _mp4_mp3_link_   name,username the author    etc...
        """
        try:

            async with ClientSession() as session:
                async with session.post('https://lovetik.com/api/ajax/search',data={ "query" : link } , headers = { "user-agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0" } ) as response:
                    result = await response.json()

        except Exception as e:
            raise BaseException(e)
        
        return LinkResult.parse(result, link)


    async def save(self,link: str, type: str, name: str = 'momolove') -> "DownloadResult":

        """
            Save the video in    VDownloads/    directory    (async function)

            Args:
                link (str): real link (mp4 , mp3 , jpeg, png)
                type (str): download type (mp4, mp3)
                name (str, optional): name vid/audio . Defaults to 'momolove'.

            Raises:
                Exception1: this exception if there's problem in code (maybe i will update it soon... >_<)
                Exception2:  this exception if the user enters his values, and values not (mp4 or mp3 , jpeg, png)
            
            Returns:
                DownloadResult: Info about download 
        """

        if not os.path.exists('VDownloads'):
            os.makedirs('VDownloads')

        if type.lower() in ['mp4','mp3','png','jpg','jpeg']:
            try:
                async with ClientSession() as session:
                    x = await session.get(link)
                    xx = await x.read()
                    with open('VDownloads/'+name+'.'+type.lower(), "wb") as f:
                        size = f.write(xx)
                    return DownloadResult.parse({'status':'ok','link':link,'size':size,'type':type.lower(),'path':'VDownloads/'+name+'.'+type.lower()})

            except Exception as e:
                raise Exception(e)
        else:
            raise Exception('Just Type : mp3 or mp4')
        
