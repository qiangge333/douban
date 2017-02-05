from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///douban.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

# 下面三行是套路, 用来增加迁移的命令
# 迁移就是要这样, 使用是在命令行
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


class ReprMixin(object):
    def save(self):
        db.session.add(self)
        db.session.commit()

    # def __repr__(self):
    #     class_name = self.__class__.__name__
    #     properties = ('{0} = {1}'.format(k, v) for k, v in self.__dict__.items())
    #     return '<{0}: \n  {1}\n>'.format(class_name, '\n  '.join(properties))

    def __repr__(self):
        class_name = self.__class__.__name__
        properties = ('{} = ({})'.format(k, v) for k, v in self.__dict__.items())
        return '\n<{}:\n  {}\n>'.format(class_name, '\n  '.join(properties))


class Movie(db.Model, ReprMixin):
    __tablename__ = 'Top250'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text())
    score = db.Column(db.Integer())
    reviews = db.Column(db.Integer())
    ranking = db.Column(db.Integer())
    quote = db.Column(db.Text())
    cover_url = db.Column(db.Text())

    def __init__(self):
        # 电影类有 4 个属性
        self.name = ''
        self.score = 0
        self.reviews = 0
        self.ranking = 0
        self.quote = ''
        self.cover_url = ''


class Comedy(db.Model, ReprMixin):
    __tablename__ = 'comedy'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text())
    score = db.Column(db.Integer())
    reviews = db.Column(db.Integer())
    information = db.Column(db.Integer())
    cover_url = db.Column(db.Text())

    def __init__(self):
        # 电影类有 4 个属性
        self.name = ''
        self.score = 0
        self.reviews = 0
        self.information = ''
        self.cover_url = ''


if __name__ == '__main__':
    manager.run()
