from marshmallow import fields, validate,pre_load
from employee_service import db, ma

class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    mobile = db.Column(db.String(10), nullable=False,unique=True)
    title = db.Column(db.String(50), nullable=False)
    department = db.Column(db.String(50), nullable=False)
    created_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, email, mobile,title,department):
        self.email = email
        self.mobile = mobile
        self.title = title
        self.department= department
    def __repr__(self) -> str:
        return f"{self.id=} {self.created_date=}"

class PositonSchema(ma.Schema):
    title = fields.String(required=True, validate=[validate.Length(min=1, max=20)])
    department = fields.String(required=True, validate=[validate.Length(min=1, max=20)])

class EmployeeSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    email = fields.Email(required=True)
    mobile = fields.String(required=True, validate=validate.Length(10))
    created_date = fields.DateTime()
    positonSchema = ma.Nested(PositonSchema)


class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    key = db.Column(db.String(50), nullable=False)
    
    def __init__(self, username,key):
        self.username = username
        self.key = key
        
    def __repr__(self) -> str:
        return f"{self.username=}"

class AdminSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True,validate=[validate.Length(min=8, max=50)])
    key = fields.String(required=True,validate=[validate.Length(min=8, max=50)])
    
    
    



    

