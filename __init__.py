#import pips :
import requests,json
#creat new class with TikTok Name :
class TikTok: 
    #creat function with Vid Name
    def Vid(self,link):
        #send Request To https://lovetik.com With Link vid to get Response {
        #headers :
        self.headers = {"referer":"https://lovetik.com/sa/video/","origin":"https://lovetik.com","user-agent":"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0"}
        
        #data :
        self.payload = {"query":link}

        #send req :
        url =requests.post("https://lovetik.com/api/ajax/search",headers = self.headers,data=self.payload).json()

        #try if good response and with-out any proplem return json data on "respones" var 
        #try:
        self.respones=json.loads('{"ok":"true","Video":{"authorUser":"'+url['author']+'","authorName":"'+url['author_name']+'","authorImage":"'+url['author_a']+'","cover":"'+url['cover']+'","vidID":"'+url['vid']+'","desc":"'+url["desc"]+'","link":"'+url['links'][4]['a']+'","audioName":"'+url['links'][5]['s']+'","audioLink":"'+url['links'][5]['a']+'"}}')		
        
        #except return error message data 
        #except:self.respones =json.loads('{"ok":"false","error":"There is an error in the link"}')
        
        return self.respones
        