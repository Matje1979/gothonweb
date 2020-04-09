import web

urls = (
'/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="db_layout.html")

class Index(object):
    def GET(self):
        return render.db_layout(content)
    
    def POST(self):
        form = web.input(password = "Nobody", username = "Hello")
        greeting = "%s %s" % (form.password, form.username)
        return render.index(greeting = greeting)
    
if __name__ == "__main__":
    app.run()