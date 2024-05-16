from dataclasses import dataclass
from json import dumps
from datetime import datetime


class Base:
    """
        This code aims to provide a way to convert an object of type Base into a custom (JSON) string, excluding attributes that start with an underscore and have a None value.
    """
    @staticmethod
    def default(obj: "Base"):
        return {
            **{
                attr: (getattr(obj, attr))
                for attr in filter(lambda x: not x.startswith("_"), obj.__dict__)
                if getattr(obj, attr) is not None
            },
        }
    def __str__(self) -> str:
        return dumps(self, indent=4, default=Base.default, ensure_ascii=False)

@dataclass
class DownloadResult(Base):
    """
        Code for a structured representation of download results that can be easily serialized to (JSON) using custom serialization logic.

        Args:
            Base : inherits from the Base class, which presumably contains the custom serialization logic .

        Returns:
            Dict
    """
    
    status:     str
    date:       str
    file_size:  dict
    path:       str
    type:       str
    link:       str
    @staticmethod
    def parse(dic: dict) -> "DownloadResult":
        try:
            b = int(dic['size'])
            return DownloadResult(
                status =     dic['status'],
                date =       int(datetime.now().timestamp()),
                file_size =  {
                        'B'  : b  ,
                        'KB' :int( b / 1024 ),
                        'MB' : b / ( 1024 * 1024 )       ,
                        'GB' : b / ( 1024 * 1024 * 1024 ),
                    },
                path =       dic['path'],
                type =       dic['type'],
                link =       dic['link'],
            )
        except:
            return {}
        


@dataclass
class LinkResult(Base):
    """
        Like (DownloadResult) function but with new Reterns for info video...
    """
    status:     str
    mess:       str
    url:        str
    vid_id:     str
    cover:      str
    desc:       str
    username:   str
    name:       str
    avatar:     str
    mp4:        str
    mp4_rights: str
    mp3:        str
    title:      str

    @staticmethod
    def parse(d: dict, link: str) -> "LinkResult":
        try:
                
            return LinkResult(
                status =     d['status'],
                mess =       d['mess'],
                url =        link,
                vid_id =     d['vid'],
                cover =      d['cover'],
                desc =       d['desc'],
                username =   d['author'],
                name =       d['author_name'],
                avatar =     d['author_a'],
                mp4 =        [item for item in d['links'] if item['t'] == '<b> MP4 </b>'][0]['a'],
                mp4_rights = [item for item in d['links'] if item['t'] == '<b> MP4 </b>'][1]['a'],
                mp3 =        [item for item in d['links'] if item['t'] == '<b>♪ MP3 Audio</b> '][0]['a'],
                title =      [item for item in d['links'] if item['t'] == '<b>♪ MP3 Audio</b> '][0]['s'],
            )
        except:
            return {}


