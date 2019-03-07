from app import app
@app.route('/usr')
def usr():
    user = {'username': 'Miguel'}
    return '''
<html>
    <head>
        <title> Home Page - MyBlog </title>
    </head>
    <body>
            <h1> Hello, ''' + user['username'] + ''' ! </h1>
    </body>
</html>'''
