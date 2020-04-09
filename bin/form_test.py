import web

urls = (
    '/','Foo'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Foo(object):
    def GET(self):
        form = web.input(name="Mirko", last_name = "Spasic")
        greeting = "%s %s" % (form.name, form.last_name)
        return render.index(greeting = greeting)
       
        
if __name__ == "__main__":
    app.run()
        
        