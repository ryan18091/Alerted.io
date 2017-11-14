from ML_test1 import db

class English_Dict(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    word = db.column(db.String, unique=True, nullable=False)
    word_length = db.Column(db.Integer,unique=False, nullable=False)

    def __init__(self, word, word_length):
        self.session_id = session_id
        self.word = word
        self.word_length = word_length

    def __repr__(self):
        return '<session_id {}'.format(self.session_id)

class Learning_Worsd(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    New_Word = db.Column(db.String,unique=True, nullable=False)
    First_Added = db.Column(db.Date,unique=False, nullable=False)
    Usage = db.Column(db.Integer,unique=False, nullable=True)
    Last_Used = db.Column(db.Date,unique=False, nullable=False)


    def __init__(self, New_word, First_Added, Usage, Last_used):
        self.politician = New_word
        self.screen_name = First_Added
        self.datestamp = Usage
        self.tweet = Last_used


    def __repr__(self):
        return '<User %r>' % self.username

