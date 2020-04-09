import web

urls = (
    '/', 'index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class index:
    def GET(self):
        form = web.input(name="Nobody", greet = None)
        if form.greet:
            greeting = "Hello, %s %s" % (form.name, form.greet)
            return render.index(greeting = greeting)
        else:
            return "ERROR: greet is required."

if __name__ == "__main__":
    app.run()