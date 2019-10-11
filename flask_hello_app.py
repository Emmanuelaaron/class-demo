from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:comforter@localhost:5432/example'

db = SQLAlchemy(app)

class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Person ID: {self.id}, name: {self.name}>'

db.create_all()
print('\n\n\n\n\n\n')
all_people = Person.query.all()
print(all_people)
bob = Person.query.filter_by(name="Bob").first()
print(bob)
like_query = Person.query.filter(Person.name.like('B%')).all()
limit_5 = Person.query.limit(5).all()
case_ses_like_query = Person.query.filter(Person.name.ilike('b%')).all()
bob_count = Person.query.filter(Person.name.ilike('B%')).count()
print('bob_count', bob_count)
print('limit_5', limit_5)
print('like_query', like_query)
print('case_ses_like_query', case_ses_like_query)
print('\n\n\n\n\n\n')
@app.route('/')
def index():
    person = Person.query.first()
    return "Hello " + person.name

if __name__ == '__main__':
    app.run()