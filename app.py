from flask import Flask


app=Flask(__name__)

'''heroku_email='prakhyathb07@gmail.com'
heroku_api_key=''
heroku_app_name='hello-world-prak'
'''
# to build image
'''docker build -t <name in small calse>:<tagname> .'''

# to view image
'''docker images'''

# to run docker
""" docker run -p 5000:5000 -e PORT=5000 <dockerid>"""

# to check running containers
"""docker ps"""

# to stop
"""docker stop <conatiner id>"""




@app.route("/",methods=["GET","POST"])
def index():
    return "Machine Learning project housing price"

if __name__=="__main__":
    app.run(debug=True)