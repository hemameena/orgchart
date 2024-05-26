from . import db


class ChartData(db.Model):
    __tablename__ = 'chartdata'

    EmpID = db.Column(db.Integer, primary_key=True)
    EmpName = db.Column(db.String(255), nullable=False)
    UserName = db.Column(db.String(255), nullable=False)
    Designation = db.Column(db.String(255), nullable=False)
    BusinessUnit = db.Column(db.String(255), nullable=False)
    Reportee = db.Column(db.String(255), nullable=True)
    Reporter = db.Column(db.String(255), nullable=True)

    def to_dict(self):
        return {
            'EmpID': self.EmpID,
            'EmpName': self.EmpName,
            'UserName': self.UserName,
            'Designation': self.Designation,
            'BusinessUnit': self.BusinessUnit,
            'Reportee': self.Reportee,
            'Reporter': self.Reporter
        }
