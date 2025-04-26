#!C:/Users/dell/AppData/Local/Programs/Python/Python311/python.exe
import cgi
import cgitb
import random
import string
import pymysql,os
import smtplib
import datetime
print("content-type:text/html \r\n\r\n")
cgitb.enable()
con=pymysql.connect(host='localhost',user='root',password='',database='company')
cur=con.cursor()
print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add employee</title>
     <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/css/bootstrap.min.css">
     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/js/bootstrap.bundle.min.js"></script>
     <!--
     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>

     -->
     <link
     rel="stylesheet"
     href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" />
   
     <link rel="stylesheet" href="path/to/font-awesome/css/font-awesome.min.css">
    <!--Admin dash style-->
  <style>  
  *{
  font-family:'Times New Roman', Times, serif;
 }   
*,::after,::before {
  box-sizing: border-box;
}

body {
  font-family:sans-serif;
  font-size: 0.875rem;
  opacity: 1;
  overflow-y: scroll;
  margin: 0;
}

a {
  cursor: pointer;
  text-decoration: none;

}

li {
  list-style: none;
}



/* Layout for admin dashboard skeleton */

.wrapper {
  align-items: stretch;
  display: flex;
  width: 100%;
}

#sidebar {
  max-width: 264px;
  min-width: 264px;
  background-color: #deeaf5;
  transition: all 0.35s ease-in-out;
}

.main {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  min-width: 0;
  overflow: hidden;
  transition: all 0.35s ease-in-out;
  width: 100%;
  background-color: #ecf5fb;
  color: rgb(16, 16, 16);
}

/* Sidebar Elements Style */

.sidebar-logo {
  padding: 1.15rem;
}

.sidebar-nav {
  flex-grow: 1;
  list-style: none;
  margin-bottom: 0;
  padding-left: 0;
  margin-left: 0;
}

.sidebar-header {
  color: black;
  font-size: 0.75rem;
  padding: 1.5rem 1.5rem 0.375rem;
}
.sidebar-dropdown .sidebar-item{
  background-color: rgb(202, 225, 246);
  transition: all 0.2s ease-out;
}

a.sidebar-link {
  padding: 0.625rem 1.625rem;
  
  color:black;
  position: relative;
  display: block;
  font-size: 0.875rem;
}
a.sidebar-link:hover{
  background-color:white;
  transition: all 0.2s ease-out;
}

.sidebar-link[data-bs-toggle="collapse"]::after {
  border: solid;
  border-width: 0 0.075rem 0.075rem 0;
  content: "";
  display: inline-block;
  padding: 2px;
  position: absolute;
  right: 1.5rem;
  top: 1.4rem;
  transform: rotate(-135deg);
  transition: all 0.2s ease-out;
}

.sidebar-link[data-bs-toggle="collapse"].collapsed::after {
  transform: rotate(45deg);
  transition: all 0.2s ease-out;
}
.sidebar-item i{
  padding-right: 8px;
  
}
.navbar-expand .navbar-nav {
  margin-left: auto;
}

.content {
  flex: 1;
  max-width: 100vw;
  width: 100vw;
}


.content {
    max-width: auto;
    width: auto;
}


/* Sidebar Toggle */

#sidebar.collapsed {
  margin-left: -264px;
}

.modal-content{
  background-color: rgb(236, 249, 255);
  color:black;
}
@media (max-width:767.98px) {

  .js-sidebar {
      margin-left: -264px;
  }

  #sidebar.collapsed {
      margin-left: 0;
  }


  }
  </style>

<!--employee form style-->
  <style>
    .container-fluid{
    margin: 0;
    padding: 0;
    font-family:Arial, Helvetica, sans-serif;
    font-weight:550;
    
    
}

.text{
    padding: 30px;
  
    font-weight: 400;

    
}
#form{
    background-color: rgb(249, 240, 238);
    padding:30px;
    border-color: rgb(212, 233, 250);
    border-width:3px;
    border-style:solid;
    border-radius:10px;
    box-shadow: 1px 1px 11px 4px rgb(134, 157, 170);
  
}
#form label{
    margin:10px;
}
#button1{
    margin-left:30px;
}


  </style>
</head>  
""")
current = datetime.datetime.now()
print("""
<body>
    <div class="wrapper">
        <div id="sidebar" class="js-sidebar" >
            <!-- Content For Sidebar -->
            <div class="h-100 ">
                <div class="sidebar-logo" style="margin-bottom: -35px;">
                    
                    <p style="color: rgb(165, 27, 27);"><img src="media/techlogo.png"  height="45px"> <b>TECHVOLT SOFTWARE</b></p>
                </div>
                <ul class="sidebar-nav">
                    <li class="sidebar-header">
                         <b style="color: green;">Admin</b>
                    </li>
                    <hr>
                    <li class="sidebar-item">
                        <a href="#" class="sidebar-link collapsed" data-bs-target="#employee" data-bs-toggle="collapse"
                            aria-expanded="false"><i class="fa fa-address-card-o" aria-hidden="true"></i>
                            EMPLOYEE
                        </a>
                        <ul id="employee" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#sidebar">
                            <li class="sidebar-item">
                                <a href="admin_add_emp.py"  class="sidebar-link">New</a>
                            </li>
                            <li class="sidebar-item">
                                <a href="admin_exis_emp.py" class="sidebar-link">Existing</a>
                            </li>
                        </ul>
                    </li>
                    <li class="sidebar-item">
                        <a href="#" class="sidebar-link collapsed" data-bs-target="#timesheet" data-bs-toggle="collapse"
                            aria-expanded="false"><i class="fa fa-table" aria-hidden="true"></i>
                            TIMESHEET
                        </a>
                        <ul id="timesheet" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#sidebar">
                            <li class="sidebar-item">
                                <a href="admin_new_timeS.py" class="sidebar-link">New</a>
                            </li>
                            <li class="sidebar-item">
                                <a href="admin_exis_timeS.py" class="sidebar-link">Existing</a>
                            </li>
                        </ul>
                    </li>
                    <li class="sidebar-item">
                        <a href="#" class="sidebar-link collapsed" data-bs-target="#history" data-bs-toggle="collapse"
                            aria-expanded="false"><i class="fa fa-history" aria-hidden="true"></i>
                           HISTORY
                        </a>
                        <ul id="history" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#sidebar">
                            <li class="sidebar-item">
                                <a href="admin_manager_his.py" class="sidebar-link">Manager History</a>
                            </li>
                            <li class="sidebar-item">
                                <a href="admin_exe_his.py" class="sidebar-link">Executive History</a>
                            </li>
                        
                        </ul>
                    </li>
                    <li class="sidebar-item">
                        <a href="#" class="sidebar-link collapsed" data-bs-target="#announcement" data-bs-toggle="collapse"
                            aria-expanded="false"><i class="fa fa-bullhorn" aria-hidden="true"></i>
                            ANNOUNCEMENT
                        </a>
                        <ul id="announcement" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#sidebar">
                            <li class="sidebar-item">
                                <a href="admin_new_anno.py" class="sidebar-link">New</a>
                            </li>
                            <li class="sidebar-item">
                                <a href="admin_exis_anno.py" class="sidebar-link">Existing</a>
                            </li>
                        </ul>
                            <li class="sidebar-item">
                                <a href="#" class="sidebar-link collapsed" data-bs-target="#leave" data-bs-toggle="collapse"
                                    aria-expanded="false"><i class="fa fa-files-o" aria-hidden="true"></i>
                                    LEAVE
                                </a>
                                <ul id="leave" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#sidebar">
                                    <li class="sidebar-item">
                                        <a href="admin_new_leave.py" class="sidebar-link" >New</a>
                                    </li>
                                    <li class="sidebar-item">
                                        <a href="admin_exis_leave.py" class="sidebar-link">Existing</a>
                                    </li>
                           
                                </ul>
                                
                                
                                <li class="sidebar-item">
                                  <a href="admin_request.py" class="sidebar-link" >
                                      <i class="fa fa-unlock-alt" aria-hidden="true"></i>
                                     PASSWORD REQUEST
                                  </a>
                              </li>
                              
                                <li class="sidebar-item">
                                    <a href="homeLogin.py" class="sidebar-link" style="color:red">
                                        <i class="fa fa-sign-out" aria-hidden="true"></i>
                                       LOGOUT
                                    </a>
                                </li>
                    </li>

                </ul>
            </div>
        </div>
        
        <div class="main">
          <!--nav-->
            <nav class="navbar navbar-expand px-4 border-bottom" style="background-color: #a6c3f8;">
                <button class="btn btn-light" id="sidebar-toggle" type="button" style="background-color: rgb(209, 236, 251);">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="navbar-collapse navbar">
                    
                 <img src="media/logopic.png"  alt="logo" height="35px" style="padding-left: 40px;">
                 
                </div>
            </nav>
             <div style="text-align:right; color:#637ba8">
                <p><b>%s<b></p><hr>
                </div> """%(current))

print("""
            <main class="content px-3 py-2">
              <div class="container-fluid"  >
                <div class="row" >
                    <div class="col-1 col-sm-2 col-md-2 col-lg-3">
                     
                       </div>
                       <div class="col-10 col-sm-8 col-md-8 col-lg-6">
                    <h3 class="text" style="color:green;">Employee Registration</h3>
                
                    <form name="myform" id="form" method="post" enctype="multipart/form-data" onsubmit="return ValidateEmail(email)"  style="overflow: hidden;">
                      <div class="form-group">
                        <label for="fname">First Name:</label>
                        <input type="text" class="form-control" id="fname"  name="fname" required>
                        <div class="valid-feedback">Valid.</div>
                        <div class="invalid-feedback">Please fill out this field.</div>
                      </div>
            
                      <div class="form-group">
                        <label for="lname">Last Name:</label>
                        <input type="text" class="form-control" id="lname"  name="lname" required>
                        <div class="valid-feedback">Valid.</div>
                        <div class="invalid-feedback">Please fill out this field.</div>
                      </div>
            
                      <div class="form-group">
                        <label for="dob">DOB:</label>
                        <input type="date" class="form-control" id="dob"  name="dob" required>
                        <div class="valid-feedback">Valid.</div>
                        <div class="invalid-feedback">Please fill out this field.</div>
                      </div>
            
                      <div class="form-group">
                        <label for="gender">Gender:</label>
                        <input type="radio"  id="gender"  name="gender" value="Male" required>Male
                        <input type="radio"  id="gender"  name="gender" value="Female" required>Female
                        <div class="valid-feedback">Valid.</div>
                        <div class="invalid-feedback">Please fill out this field.</div>
                      </div>
            
                      <div class="form-group">
                        <label for="join">Joining Date:</label>
                        <input type="date" class="form-control" id="join"  name="join" required>
                        <div class="valid-feedback">Valid.</div>
                        <div class="invalid-feedback">Please fill out this field.</div>
                      </div>
            
                      
            
                      <div class="form-group">
                        <label for="email">Email:</label>
                        <input type="text" class="form-control" id="Email"  name="email">
                        <div class="valid-feedback">Valid.</div>
                        <div class="invalid-feedback">Please fill out this field.</div>
                      </div>
            
                      <div class="form-group">
                        <label for="number">Phone Number:</label>
                        <input type="tel" class="form-control" id="number" name="phone" required>
                        <div class="valid-feedback">Valid.</div>
                        <div class="invalid-feedback">Please fill out this field.</div>
                      </div>
            
                      <div class="form-group">
                        <label for="qual">Qualification:</label>
                        <select class="form-control" name="qual" id="qual" required>
                          <option value="B.E">B.E </option>
                          <option value="B.Tech ">B.Tech</option>
                          <option value="BCA">BCA </option>
                          <option value="B.Sc ">B.Sc</option>
                          <option value="BBA ">BBA</option>
                          <option value="M.E">M.E </option>
                          <option value="MCA ">MCA</option>
                          <option value="MBA ">MBA</option>
                          <option value="M.Sc">M.Sc </option>
                          <option value=" Others ">Others</option>
                        </select>
                        <div class="valid-feedback">Valid.</div>
                        <div class="invalid-feedback">Please fill out this field.</div>
                      </div>
            
                      <div class="form-group">
                        <label for="exper">Experience:</label>
                        <input type="number" class="form-control" id="exper" placeholder="In year" name="experience" required>
                        <div class="valid-feedback">Valid.</div>
                        <div class="invalid-feedback">Please fill out this field.</div>
                      </div>
            
                      <div class="form-group">
                        <label for="role">Job Role:</label>
                        <select class="form-control" name="role" id="role" required>
                          <option value="executive"> Executive level </option>
                          <option value="manager ">Manager level</option>
                        </select>
                        <div class="valid-feedback">Valid.</div>
                        <div class="invalid-feedback">Please fill out this field.</div>
                      </div>
            
                      <div class="form-group">
                        <label for="department">Department:</label>
                        <select class="form-control" name="dep" id="department" required>
                          <option value="Sales"> Sales Department</option>
                          <option value="technical"> Technical Department</option>
                        </select>
                        <div class="valid-feedback">Valid.</div>
                        <div class="invalid-feedback">Please fill out this field.</div>
                      </div>
            
                      <div class="form-group">
                        <label for="hours">Working hours:</label>
                        <select class="form-control" name="timing" id="hours" required>
                          <option value="12-hours"> 12-hours</option>
                          <option value="10-hours"> 10-hours</option>
                          <option value="8-hours"> 8-hours</option>
                        </select>
                        <div class="valid-feedback">Valid.</div>
                        <div class="invalid-feedback">Please fill out this field.</div>
                      </div>
            
                      <div class="form-group">
                        <label for="address">Address:</label>
                        <textarea class="form-control" name="address" id="address" rows="3" cols="30"  required></textarea>
                        <div class="valid-feedback">Valid.</div>
                        <div class="invalid-feedback">Please fill out this field.</div>
                      </div>
            
                      <div class="form-group">
                        <label for="city">City:</label>
                        <input type="text" class="form-control" id="city" name="city" required>
                        <div class="valid-feedback">Valid.</div>
                        <div class="invalid-feedback">Please fill out this field.</div>
                      </div>

                      <div class="form-group">
                        <label for="State">State:</label>
                        <select class="form-control" name="state" id="state" required>
                          <option value="Tamil Nadu"> Tamil Nadu</option>
                          <option value="Karnataka">Karnataka</option>
                          <option value="Kerala"> Kerala</option>
                        </select>
                        <div class="valid-feedback">Valid.</div>
                        <div class="invalid-feedback">Please fill out this field.</div>
                      </div>
            
                      <div class="form-group">
                        <label for="pincode">Pincode:</label>
                        <input type="text" class="form-control" id="pincode"  name="pincode" required>
                        <div class="valid-feedback">Valid.</div>
                        <div class="invalid-feedback">Please fill out this field.</div>
                      </div>

                      <div class="form-group">
                        <label for="aadhar">Aadhar Number:</label>
                        <input type="text" class="form-control" id="aadhar"  name="aadhar" required>
                        <div class="valid-feedback">Valid.</div>
                        <div class="invalid-feedback">Please fill out this field.</div>
                      </div>
            
                      <div class="form-group">
                        <label for="photo">Photo:</label>
                        <input type="file" class="form-control" id="image"  name="photo" required>
                        <div class="valid-feedback">Valid.</div>
                        <div class="invalid-feedback">Please fill out this field.</div>
                      </div> <br>
                   
                      <input type="submit" value="Register" name="register" class="btn btn-primary" id="button1" >
                      <input type="reset" value="Cancel" class="btn btn-secondary" id="button2">
                      
                    </div>
                    </form>
                    <script>
                      function ValidateEmail(email){
                            if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(myform.email.value))
                           {
                               return (true)
                            }
                            else{
                              alert("You have entered an invalid email address!")
                              email.focus()
                              return (false)
                            }
                            }
                    </script> 
                    
                  </div>
                </div>

            </main>
       
        </div>
    </div>

   
    <script >
        sidebarToggle = document.querySelector("#sidebar-toggle");
        sidebarToggle.addEventListener("click",function(){
                   document.querySelector("#sidebar").classList.toggle("collapsed");
                                                });
                                 
    </script>
</body>

</html>
""")

form = cgi.FieldStorage()
q="""select max(id) from empreg"""
cur.execute(q)
rec=cur.fetchone()
if rec[0] !=None:
    n=rec[0]
else:
    n=0

z=""
if n<9:
    z="000"
elif n==10 or n<99:
    z="00"
elif n>99 or n<=999:
    z="0"

empid="emp24"+z+str(n+1)

N=6
emppass=''.join(random.choices(string.ascii_uppercase+string.digits, k=N))
pwrd= "EMP"+emppass


pregister=form.getvalue('register')

if pregister != None:
    if len(form) !=0:
        pfname=form.getvalue("fname")
        plname=form.getvalue('lname')
        pdob=form.getvalue('dob')
        pgender=form.getvalue('gender')
        pjoindate=form.getvalue('join')
        pemail=form.getvalue('email')
        pphone=form.getvalue('phone')
        pqual=form.getvalue('qual')
        pexperience=form.getvalue('experience')
        prole=form.getvalue('role')
        pdep=form.getvalue('dep')
        ptiming=form.getvalue('timing')
        paddress=form.getvalue('address')
        pcity=form.getvalue('city')
        pstate=form.getvalue('state')
        ppincode=form.getvalue('pincode')
        paadhar=form.getvalue('aadhar')
        pimage=form['photo']

        if pimage.filename:
            fn=os.path.basename(pimage.filename)
            open("user/"+fn,"wb").write(pimage.file.read())

            q="""Insert Into empreg (firstname,lastname,dob,gender,joindate,email,phone,qualification,experience,role,department,timing,address,city,state,pincode,aadhar,photo,userid,password) 
            values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') """ %(pfname,plname,pdob,pgender,pjoindate,pemail,pphone,pqual,pexperience,prole,pdep,ptiming,paddress,pcity,pstate,ppincode,paadhar,fn,empid,pwrd)
            cur.execute(q)
            con.commit()

            print("""<script> alert("register successfully") </script>""")

            fromadd = "dinesh.sivakumar.c@gmail.com"
            password="wnwiicwvetrjbnsf"
            toadd=pemail
            subject="Employee Register "
            body="Welcome {}{} Your Joined new employee of this Company ,\n EMPLOYEE ID :{} & PASSWORD :{}".format(pfname,plname,empid,pwrd)

            msg="subject : {} \n\n{}".format(subject,body)
            server=smtplib.SMTP("smtp.gmail.com:587")
            server.ehlo()
            server.starttls()
            server.login(fromadd,password)
            server.sendmail(fromadd,toadd,msg)
            server.quit()

            print("""<script> alert("Mail sended") </script>""")
