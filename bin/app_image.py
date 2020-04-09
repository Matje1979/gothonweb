import web

import os

urls = (
        '/images/(.*)', 'images'
        ) #this is where the image folder is located
        
app_image = web.application(urls, globals())

class images:
    def GET(self,name):
        ext = name.split(".")[-1] # Gather extension
        
        
        cType = {
            "png":"image/png",
            "jpg":"image/jpeg",
            "gif":"image/gif",
            "ico":"image/x-icon"           
            }

        if name in os.listdir('.\images\\'):  # Security
            web.header("Content-Type", cType[ext]) # Set the Header
            return open('images/%s'%name,"rb").read() # Notice 'rb' for reading images
        else:
            raise web.notfound()

if __name__ == "__main__":
    app_image.run()