from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app) 
api = Api(app)

class TextModel(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)

    def __repr__(self): 
        return f'{self.text}'

text_args = reqparse.RequestParser()
text_args.add_argument('text', type=str, required=True, help="Text can not be blank")

textFields = {
    'id':fields.Integer,
    'text':fields.String,
}

class Text(Resource):
    @marshal_with(textFields)
    def get(self):
        texts = TextModel.query.all() 
        return texts 
    
    @marshal_with(textFields)
    def post(self):
        args = text_args.parse_args()
        text = TextModel(text=args["text"])
        db.session.add(text) 
        db.session.commit()
        text = TextModel.query.all()
        return text, 201
    

api.add_resource(Text, '/text/')

@app.route('/')
def home():
    return '<h1>Flask REST API</h1>'

if __name__ == '__main__':
    app.run(debug=True) 