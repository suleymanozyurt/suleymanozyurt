import base64
p=base64.b64encode(open('photo.jpg','rb').read()).decode()
s=open('index.src.html',encoding='utf-8').read().replace('__PHOTO__','data:image/jpeg;base64,'+p)
open('index.html','w',encoding='utf-8').write(s)
