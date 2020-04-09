import web
from gothonweb import map

urls = (
'/', 'Openning', '/game', 'GameEngine',
'/index', 'Index','game_over', 'GameOver'
)

app = web.application(urls, globals())

#little hack so that debug mode works with sessions

if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store,
                                  initializer = {'room':None})
    web.config._session = session
else:
    session = web.config._session

render = web.template.render('templates/', base='layout')


class Openning(object):
    def GET(self):
        #creating an oppening page.
        return render.index()
        
class Index(object):
    def GET(self):
        #this is used to "setup" the session with starting values.
        session.room = map.START
        web.seeother('/game')
    
        
class GameEngine(object):
    def GET(self):
        
        if session.room.name == "The End": 
            return render.game_over(room = session.room)
        else:
            return render.show_room(room = session.room)   
    
    
    def POST(self):
        form = web.input(action = "None")
        
        if session.room and form.action:
            print session.room.attempts
            print form.action
            print session.room.right_path
            print session.room.paths.keys()
            if session.room.attempts == 1:
                if form.action not in session.room.right_path and '*'\
                in session.room.paths.keys():
                    print "form.action not in session.room.right_path and '*'\
                in session.room.paths.keys()"
                    session.room = session.room.go('*')
                    web.seeother('/game')
                elif form.action not in session.room.paths.keys():
                    web.seeother('/game')
                else:
                    session.room = session.room.go(form.action)
                    web.seeother('/game')
                    
            else:
                if form.action not in session.room.right_path:
                    session.room.update_attempts(1)
                    session.room = session.room
                    web.seeother('/game')
                else:
                    if form.action in session.room.right_path:
                        session.room = session.room.go(form.action)
                        web.seeother('/game')
                        
class GameOver(object):
    def GET(self):
        return render.game_end()
                        
        
if __name__ == "__main__":
    app.run()