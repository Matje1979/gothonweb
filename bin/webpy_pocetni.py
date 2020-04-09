    
        #if form.operation == "+" or form.operation.lower() == "sabiranje":
            #greeting = int(form.greet) + int(form.name)
        #elif form.operation == "-":
            #greeting = int(form.greet) + int(form.name)
        #elif form.operation == "*":
            #greeting = int(form.greet) * int(form.name)
        #elif form.operation == "/":
            #greeting = int(form.greet) / int(form.name)
        #else:
            #greeting = "Sorry, I cannot recognize that operation."
        #greeting = "%s %s" % (form.greet, form.name)
       # print greeting
        
        #return render.index_laid_out(greeting = greeting)
            
        
        #y = open(data.myfile, "r")
        #z = y.read()
        #return render.index_laid_out(z = z)
        
        
        #filename = web.debug(data['myfile'].filename) # This is the filename
        #return render.index(filename)   
        #web.debug(data['myfile'].value) # This is the file contents
        #x = web.debug(data['myfile'].file.read()) # Or use a file(-like) object

        #filedir = 'C:/projects/gothonweb' # change this to the directory you want to store the file in.
        #if 'myfile' in x:
        
        #x = web.input(myfile={})
        #if x == True:
            #file_name = x['myfile'].filename
            #print file_name
        
            #with open('C:/projects/dan_brazila/fotke/' + file_name, 'wb') as saved:
                #shutil.copyfileobj(x['myfile'].file, saved)
            #return render.index_laid_out(file_content = file_content)
            #filepath = x.myfile.filename.replace('\\','/')
            
            #filename = filepath.split('\\')[-1] # splits the and chooses the last part (the filename with extension)
            #fout = open(filedir +'/'+ filename,'w') # creates the file where the uploaded file should be stored
            #fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
            #fout.close() # closes the file, upload complete.
        #raise web.seeother('C:\projects\gothonweb')
            
        #else:
            #return render.index_laid_out(greeting = greeting, file_name="you have not chosen a file")