from flask import  Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from .models import Student, Staff, Event, Assessment, Fees
from datetime import datetime

auth = Blueprint('auth', __name__)
SQLALCHEMY_TRACK_MODIFICATIONS = False

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user =  User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully! '+str(user.email), category='success')
                login_user(user, remember=True)
                return redirect(url_for('auth.dashboard'))
            else:
                flash('Password is incorrect', category='error')
        else:
            flash('Email does not exist', category='error')
    return render_template("login.html", user=current_user)


@auth.route('/sign_up',  methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user =  User.query.filter_by(email=email).first()
        if user:
            flash('Email already exist', category='error')
        elif len(email) < 7:
            flash('Email must be more than 7 characters', category='error')
        elif len(first_name) < 3:
            flash('Firstname must be greater than 4 characters', category='error')
        elif password1 != password2:
            flash('Password don\'t match', category='error')
        elif len(password1) < 7:
            flash('Password must be a least 7 characters long', category='error')
        else:
            new_user =  User(email = email, first_name = first_name, password = generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            
            flash('Account created successfully', category='success')
            return redirect(url_for('auth.dashboard'))

    return render_template("sign_up.html", user=current_user)


@auth.route('/students',  methods=['GET', 'POST'])
@login_required
def students():
    if request.method == 'POST':
        
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        dadsname = request.form.get('dadsname')
        dadscontact = request.form.get('dadscontact')
        dadsoccu = request.form.get('dadswork')
        momsname = request.form.get('momsname')
        momscontact = request.form.get('momscontact')
        momsoccu = request.form.get('momswork')
        dob = request.form.get('dob')
        homeaddress =  request.form.get('homeaddress')
        gender =  request.form.get('gender')
        forms =  request.form.get('level')
        admis =  request.form.get('admfees')
        sfees =  request.form.get('fees')
        totfees =  request.form.get('Tfees')

        student =  Student(first_name = fname, last_name = lname, email = email, dads_name = dadsname, 
        dads_contact = dadscontact, dads_occu = dadsoccu,
        moms_name = momsname, moms_contact = momscontact,
        moms_occu = momsoccu, dob = dob, addr = homeaddress, forms = forms,
        gender = gender, admfees = admis, fees = sfees,  tfees = totfees )
        db.session.add(student)
        db.session.commit()
        flash('Data inserted successfully', category='success')
    
    return render_template("students.html" , user=current_user)


@auth.route('/staff',  methods=['GET', 'POST'])
@login_required
def staff():
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        dadsname = request.form.get('dadsname')
        dadscontact = request.form.get('dadscontact')
        dadsoccu = request.form.get('dadswork')
        momsname = request.form.get('momsname')
        momscontact = request.form.get('momscontact')
        momsoccu = request.form.get('momswork')
        dob = request.form.get('dob')
        homeaddress =  request.form.get('homeaddress')
        gender =  request.form.get('gender')
        forms =  request.form.get('jhs')
        marital = request.form.get('marital')
        images =  request.form.get('images')
        bankn =  request.form.get('bank')
        acctno =  request.form.get('accountnumber')
        nameofacnt = request.form.get('accountname')
        momono =  request.form.get('momo')
        network =  request.form.get('network')
        nameofmomoacnt = request.form.get('nameonmomo')
        staff =  Staff(first_name = fname, last_name = lname, email = email, dads_name = dadsname, 
        dads_contact = dadscontact, dads_occu = dadsoccu,
        moms_name = momsname, moms_contact = momscontact,
        moms_occu = momsoccu, dob = dob, addr = homeaddress, forms = forms,
        gender = gender, images = images, bankname = bankn, accountnum = acctno, 
        nameonaccount = nameofacnt, momonum = momono, network = network, 
        nameonmomo = nameofmomoacnt, maritalstate = marital )
        db.session.add(staff)
        db.session.commit()
        flash('Data inserted successfully', category='success')
    else:
        pass
    return render_template("staff.html", user=current_user )


@auth.route('/eventlog',  methods=['GET', 'POST'])
@login_required
def event():
    if request.method == 'POST':
        etitle = request.form.get('eventtitle')
        dates = request.form.get('eventdate')
        info = request.form.get('description')
        time = request.form.get('eventtime')
        arts = request.form.get('image')
        event =  Event(title = etitle, date = dates, 
        description = info, eventtime = time, artwork = arts)
        db.session.add(event)
        db.session.commit()
        flash("Event inserted successfully", category='success')

    return render_template("eventlog.html", user=current_user )


@auth.route('/score',  methods=['GET', 'POST'])
@login_required
def score():
    if request.method == 'GET':
        dataset = Student.query.all()
        return render_template("score.html", user=current_user, dataset = dataset)
    elif request.method == 'POST':
        name = request.form.get('studentname')
        form = request.form.get('form')
        term = request.form.get('term')
        englishcl = request.form.get('clswkeng')
        englishex = request.form.get('exameng')
        englishtot = request.form.get('toteng')
        englishgr = request.form.get('eng_grade')
        mathscl = request.form.get('clswkmath')
        mathsex = request.form.get('exammath')
        mathstot = request.form.get('mathtot')
        mathsgr = request.form.get('math_grade')
        sciencecl = request.form.get('clswksc')
        scienceex = request.form.get('examsc')
        sciencetot = request.form.get('totsc')
        sciencegr = request.form.get('sc_grade')
        socialcl = request.form.get('socwkeng')
        socialex = request.form.get('examsoc')
        socialtot = request.form.get('totsoc')
        socialgr = request.form.get('soc_grade')
        rmecl = request.form.get('clswkrme')
        rmeex = request.form.get('examrme')
        rmetot = request.form.get('totrme')
        rmegr = request.form.get('rme_grade')
        basicdcl = request.form.get('clswkbdt')
        basicdex = request.form.get('exambdt')
        basicdtot = request.form.get('totbdt')
        basicdgr = request.form.get('bdt_grade')
        infocl = request.form.get('clswkict')
        infoex = request.form.get('examict')
        infotot = request.form.get('totict')
        infogr = request.form.get('ict_grade')
        ghlngcl = request.form.get('clswkghlang')
        ghlngex = request.form.get('examghlang')
        ghlngtot = request.form.get('totghlang')
        ghlnggr = request.form.get('ghlang_grade')
        frenchcl = request.form.get('clswkfr')
        frenchex = request.form.get('examfr')
        frenchtot = request.form.get('totfr')
        frenchgr = request.form.get('fr_grade')
        score =  Assessment(name = name, form = form, term = term, engcl = englishcl, engex = englishex,
        engtot = englishtot, enggr = englishgr, mathcl = mathscl, mathex = mathsex,
        mathtot = mathstot, mathgr = mathsgr, scicl = sciencecl, sciex = scienceex
        , scitot = sciencetot, scigr = sciencegr, soccl = socialcl, socex = socialex,
        soctot = socialtot, socgr = socialgr, rmecl = rmecl, rmeex = rmeex, rmetot = rmetot, rmegr = rmegr,
        bdtcl =basicdcl, bdtex = basicdex, bdttot = basicdtot, bdtgr = basicdgr,
        ictcl = infocl, ictex = infoex, icttot = infotot, ictgr = infogr,
        ghlangcl = ghlngcl, ghlangex = ghlngex, ghlangtot = ghlngtot, ghlanggr = ghlnggr,
        frcl = frenchcl, frex = frenchex, frtot = frenchtot, frgr = frenchgr)
        db.session.add(score)
        db.session.commit()
        flash("Assessment records inserted successfully", category='success')

    return render_template("score.html", user=current_user)


@auth.route('/dashboard',  methods=['GET', 'POST'])
@login_required
def dashboard():
    
    return render_template("dashboard.html", user=current_user)



@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
        logout_user()
        return redirect(url_for('auth.login'))



@auth.route('/studentreport',  methods=['GET', 'POST'])
@login_required
def studentreport():
    dataset = Student.query.all()
    return render_template("studentreport.html", user=current_user, dataset=dataset)



@auth.route('/staffreport',  methods=['GET', 'POST'])
@login_required
def staffreport():
    dataset = Staff.query.all()
    return render_template("staffreport.html", user=current_user, dataset=dataset)



@auth.route('/event',  methods=['GET', 'POST'])
@login_required
def events():
    dataset = Event.query.all()
    return render_template("event.html", user=current_user, dataset=dataset)
       


@auth.route('/assessment',  methods=['GET', 'POST'])
@login_required
def assessment():
    if request.method == 'GET':
        dataset = Assessment.query.all()
        return render_template("assessment.html", user=current_user, dataset=dataset)
    else:
        return render_template("assessment.html", user=current_user)


#Work on the search button

@auth.route('/individuals',  methods=['GET', 'POST'])
@login_required
def individuals():
    if request.method == 'GET':
        
        dataset = Assessment.query.all()
        return render_template("individuals.html", user=current_user, dataset=dataset)
    else:
        return render_template("individuals.html", user=current_user)



@auth.route('/viewdata',  methods=['GET', 'POST'])
@login_required
def viewdata():
    if request.method == 'POST':
        stdid = request.form["studentID"]
        single = Assessment.query.filter_by(id =stdid).all()
        return render_template("reportcard.html", user=current_user, single = single)
    else:
        return render_template("reportcard.html", user=current_user)        


@auth.route('/fees',  methods=['GET', 'POST'])
@login_required
def fees():
    if request.method == 'POST':
        stdid = request.form["studentID"]
        dataset = Student.query.filter_by(id =stdid).all()
        single  = db.engine.execute(
            "SELECT  name,  sum(amount) as amount from fees WHERE stid ="+stdid+";"
            
        )
        allData  = db.engine.execute(
            "SELECT  * from fees WHERE stid ="+stdid+";"
            
        )
        return render_template("fees.html", user=current_user, single = single, allData = allData, dataset=dataset)
    else:
        return render_template("fees.html", user=current_user) 


@auth.route('/gallery')
@login_required
def gallery():
    return render_template("gallery.html", user=current_user)


@auth.route('/billings',  methods=['GET', 'POST'])
@login_required
def billings():
    if request.method == 'GET':
        dataset = Student.query.all()
        return render_template("billings.html", user=current_user, dataset=dataset)
    elif request.method == 'POST':
        stid = request.form.get('studentID')
        sname = request.form.get('studentName')
        sform = request.form.get('studentForm')
        Fee = request.form.get('feeAmount')
        fee =  Fees(name = sname, form = sform, amount = Fee, stid = stid)
        db.session.add(fee)
        db.session.commit()
        flash("Transaction was successful", category='success')
        return render_template("billings.html", user=current_user)
        
    else:
        return render_template("billings.html", user=current_user)
    


@auth.route('/reportcard',  methods=['GET', 'POST'])
@login_required
def reportcard():
    if request.method == 'GET':
        dataset = Assessment.query.all()
        return render_template("reportcard.html", user=current_user, dataset=dataset)
    else:
        return render_template("reportcard.html", user=current_user)
    