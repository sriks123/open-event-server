from app.models import db


class Service(db.Model):
    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Service %r>' % self.name

    def __str__(self):
        try:
            return unicode(self).encode('utf-8')
        except NameError:
            return str(self)

    def __unicode__(self):
        return self.name
