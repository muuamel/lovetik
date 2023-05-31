<h1 align="center">lovetiklib</h1>
<p align="center">With This Package Can You Download Any TikTok Video from lovetik.com</p>

## Installation :
```bash
pip install lovetiklib
```
### Example
```python
import lovetiklib
from lovetiklib import *#to import the lib

a = TikTok().Vid("https://vm.tiktok.com/ZM2FdEuwu/?t=2") #Creat Var To send data-Link To Vid Function

print(a) #Shows All List

#print(a['Video']) #Get Video List

print(a['Video']['cover']) #Get Cover Vid

print(a['Video']['vidID']) #Get ID The Vid

print(a['Video']['desc']) #Get Descrption

print(a['Video']['link']) #Get MP4 File Link

print(a['Video']['audioName']) #Get Audeo Name

print(a['Video']['audioLink']) #Get Audio Link

print(a['Video']['authorUser']) #Get author UserName

print(a['Video']['authorName']) #Get author Name

print(a['Video']['authorImage']) #Get author Photo

```
#
### Follow us on social media accounts

* telegram : @s_y_e
* github : https://github.com/MuamleAmeer
