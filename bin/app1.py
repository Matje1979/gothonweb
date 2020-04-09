import web
import shutil

urls = (
'/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base='layout', operation="+")

class Index(object):
    def GET(self):
        return render.hello_form_laid_out(greet="55", name="44")
    
    def POST(self):
        
        x = web.input(myfile={})
        file_name = x['myfile'].filename
        file_content = x['myfile'].value.read()
        with open('C:\projects\dan_brazila\fotke' + file_name, 'wb') as saved:
            shutil.copyfileobj(x['myfile'].file, saved)
            return render.index_laid_out(file_content = file_content)