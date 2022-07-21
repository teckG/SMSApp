from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique= True)
    password = db.Column(db.String(200))
    first_name =  db.Column(db.String(150))


class Student(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name =  db.Column(db.String(150))
    last_name =  db.Column(db.String(150))
    email =  db.Column(db.String(150))
    dads_name =  db.Column(db.String(150))
    dads_contact =  db.Column(db.String(150))
    dads_occu =  db.Column(db.String(150))
    moms_name =  db.Column(db.String(150))
    moms_contact =  db.Column(db.String(150))
    moms_occu =  db.Column(db.String(150))
    dob  =  db.Column(db.String(150))
    addr =  db.Column(db.String(150))
    forms =  db.Column(db.String(150))
    gender =  db.Column(db.String(150))
    admfees = db.Column(db.String(150))
    fees = db.Column(db.String(150))
    tfees = db.Column(db.String(150))




class Staff(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name =  db.Column(db.String(150))
    last_name =  db.Column(db.String(150))
    email =  db.Column(db.String(150))
    dads_name =  db.Column(db.String(150))
    dads_contact =  db.Column(db.String(150))
    dads_occu =  db.Column(db.String(150))
    moms_name =  db.Column(db.String(150))
    moms_contact =  db.Column(db.String(150))
    moms_occu =  db.Column(db.String(150))
    dob  =  db.Column(db.String(150))
    addr =  db.Column(db.String(150))
    gender =  db.Column(db.String(150))
    forms =  db.Column(db.String(150))
    maritalstate =  db.Column(db.String(150))
    images =  db.Column(db.LargeBinary)
    bankname =  db.Column(db.String(150))
    accountnum =  db.Column(db.String(150))
    nameonaccount =  db.Column(db.String(150))
    momonum =  db.Column(db.String(150))
    network =  db.Column(db.String(150))
    nameonmomo =  db.Column(db.String(150))



class Event(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title =  db.Column(db.String(150))
    date =  db.Column(db.String(150))
    description =  db.Column(db.String(500))
    eventtime =  db.Column(db.String(150))
    artwork =  db.Column(db.LargeBinary)


class Assessment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name =  db.Column(db.String(5))
    form =  db.Column(db.String(5))
    term =  db.Column(db.String(5))
    engcl =  db.Column(db.String(5))
    engex =  db.Column(db.String(5))
    engtot =  db.Column(db.String(5))
    enggr =  db.Column(db.String(5))
    mathcl =  db.Column(db.String(5))
    mathex =  db.Column(db.String(5))
    mathtot =  db.Column(db.String(5))
    mathgr =  db.Column(db.String(5))
    scicl = db.Column(db.String(5))
    sciex = db.Column(db.String(5))
    scitot = db.Column(db.String(5))
    scigr = db.Column(db.String(5))
    soccl = db.Column(db.String(5))
    socex = db.Column(db.String(5))
    soctot = db.Column(db.String(5))
    socgr = db.Column(db.String(5))
    rmecl = db.Column(db.String(5))
    rmeex = db.Column(db.String(5))
    rmetot = db.Column(db.String(5))
    rmegr = db.Column(db.String(5))
    bdtcl = db.Column(db.String(5))
    bdtex = db.Column(db.String(5))
    bdttot = db.Column(db.String(5))
    bdtgr = db.Column(db.String(5))
    ictcl = db.Column(db.String(5))
    ictex = db.Column(db.String(5))
    icttot = db.Column(db.String(5))
    ictgr = db.Column(db.String(5))
    ghlangcl = db.Column(db.String(5))
    ghlangex = db.Column(db.String(5))
    ghlangtot = db.Column(db.String(5))
    ghlanggr = db.Column(db.String(5))
    frcl = db.Column(db.String(5))
    frex = db.Column(db.String(5))
    frtot = db.Column(db.String(5))
    frgr = db.Column(db.String(5))
    date = db.Column(db.DateTime(timezone=True), default = func.now())



    
class Fees(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name =  db.Column(db.String(150))
    form =  db.Column(db.String(150))
    amount =  db.Column(db.String(500))
    stid =  db.Column(db.Integer, db.ForeignKey('student.id'))
    date = db.Column(db.DateTime(timezone=True), default = func.now())