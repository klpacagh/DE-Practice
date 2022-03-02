from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

# Flask is for developing web apps, creating api's easily
# running flask starts a web server that the api is running on (requests are sent there)

app = Flask(__name__)
api = Api(app) # wrap the app inside an API

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_kev.db' # db file in current directory
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self): # string representation
        return f"Video(name={name}, views={views}, likes={likes})" # wrapper method

# db.create_all() # creates the db - only want to do this once - comment out after

'''
names = {"kevin": {"age": 30, "gender": "male"},
         "tommy": {"age":55, "gender": "male"}}

class HelloWorld(Resource): # make a class that inherits from resource - overwrite methods
    # will define get methods
    def get(self, name):
        # return {"data": name, "test":test} # response should be json serializable (dictionaries work)
        return names[name]

    def post(self):
        return {"data":"Posted!"}

# slash is default location, made api accessible at /helloworld
# api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:test>") # multiple params
api.add_resource(HelloWorld, "/helloworld/<string:name>") # pass in params between <type:param_name> 
'''

# creating mandatory param requirements
video_put_args = reqparse.RequestParser() # auto parse through form/data that is sent and validate it - use over request
video_put_args.add_argument("name", type=str, help="Name of the Video is req", required=True)
video_put_args.add_argument("views", type=int, help="Views of the Video is req", required=True)
video_put_args.add_argument("likes", type=int, help="Likes of the Video is req", required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of the Video is req")
video_update_args.add_argument("views", type=int, help="Views of the Video is req")
video_update_args.add_argument("likes", type=int, help="Likes of the Video is req")


resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer,
}

# version of Video Class that is DB specific
class Video(Resource):
    @marshal_with(resource_fields) # get return value, serialize it using the resource_fields defined above
    def get(self, video_id): # note we use method names that match the http methods
        result = VideoModel.query.filter_by(id=video_id).first() # query that returns an instance/object in a non-serializable format
        if not result:
            abort(404, message="Could not find video with that id!")

        return result

    @marshal_with(resource_fields) 
    def put(self, video_id):
        # request will give us any data that was sent
        # print(request.form['likes']) # insetead of using this, flask comes with reqparse
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result: # check if id already exists
            abort(409, message="Video id already exists")

        video = VideoModel(id=video_id, name =args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video) # adds object to current db session
        db.session.commit()
        return video, 201

    @marshal_with(resource_fields)
    def patch(self, video_id): # used to update
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Video doesn't exist, cannot update")
        
        if  args['name']:
            result.name = args['name']
        if  args['views']:
            result.views = args['views']
        if  args['likes']:
            result.likes = args['likes']

        db.session.commit()

        return result


    # def delete(self, video_id):
    #     abort_if_video_id_doesnt_exist(video_id)
    #     del videos[video_id]
    #     return '',204


'''
# LIST VERSION - NON-DB
videos={}

def abort_if_video_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, message="Video id is not valid!") #specify a status code as well

def abort_if_video_exists(video_id):
    if video_id in videos:
        abort(409, message="Video id already exists!")


class Video(Resource):
    def get(self, video_id): # note we use method names that match the http methods
        abort_if_video_id_doesnt_exist(video_id)
        return videos[video_id]

    def put(self, video_id):
        # request will give us any data that was sent
        # print(request.form['likes']) # insetead of using this, flask comes with reqparse
        abort_if_video_exists(video_id)
        args = video_put_args.parse_args()
        videos[video_id]=args
        return videos[video_id], 201 # can return a status code as well after the data - 201 means created

    def delete(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        del videos[video_id]
        return '',204
'''

api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True) # debug mode allows the server to auto refresh when changes are applied