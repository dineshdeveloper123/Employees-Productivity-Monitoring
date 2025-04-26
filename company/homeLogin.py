#!C:/Users/dell/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgi,cgitb,pymysql,os


cgitb.enable()
con=pymysql.connect(host='localhost',user='root',password='',database='company')
cur=con.cursor()


print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>home</title>

  <style>
    
#login{
    padding-right: 55px;
}
#bodycolor{
    background-color: rgb(232, 234, 250);
  }
  
.form{
    background-color: rgb(224, 240, 252);
    padding:20px;
    border-color: rgb(249, 245, 220);
    border-width:3px;
    border-style:solid;
    border-radius:10px;
    box-shadow: 1px 1px 11px 4px rgb(134, 157, 170);
  
}


#dialog{
    font-family: cursive;
    margin-top: 20px;
    margin-bottom: 39px;
    text-align: center;
    color: green;
    padding: 15px;
    box-shadow: 3px 3px 3px rgba(0,0,0,.3),inset 1px 1px 1px white;
    border-radius: 15px;
   
}


#img{
    box-shadow: 1px 2px 9px 2px rgb(129, 215, 255);
    padding: 10px;
}
#dinesh{
    margin-top: 25px;
    margin-left: 15px;
    margin-right: 15px;
    text-align: center;
    color:green;
   box-shadow: 15px 20px 20px rgba(0,0,0,.3),inset 4px 4px 10px white;
   border-radius: 5px;
   align-items: center;
   font-family:cursive ;
   padding: 22px;
   color: rgba(12, 12, 13, 0.978);
}
#dinesh:hover{
     box-shadow: inset 5px 5px 10px rgba(0,0,0,.3),inset -4px -4px 10px white;
}
#marque{
    font-size: 13px;
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    color: red;
}



footer{
    width:100%;
    
    bottom:0;
    background:linear-gradient(to right,#3fc9fb,#4bc2f9);
    color:black;
    padding:15px;
    font-size:13px;
    line-height:14px;
    font-family: Arial, Helvetica, sans-serif;
   text-align: center;
   border-radius: 3px;
   
}

</style>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</head>
<body id="bodycolor">

    <nav class="navbar navbar-expand-sm bg-info navbar-dark">
        <div class="container-fluid">
          <a class="navbar-brand" href="#">
              <div class="logo">
            <img src="media\homelogo.png" alter="logo" width="440px" height="50px">
           </div> 
        </a> 

        <ul class="navbar-nav" id="login">
          
            <div class="dropdown" >
                <button type="button" class="btn btn-danger dropdown-toggle" data-bs-toggle="dropdown">
                  <img src="media/user.png" width="19px" height="18px">  Login
                </button>
            <ul class="dropdown-menu">
              <li><button type="button" class="btn btn-light" data-bs-toggle="modal" data-bs-target="#emp_login">Executive Login</button></li>
              <li><button type="button" class="btn btn-light" data-bs-toggle="modal" data-bs-target="#manager_login">Manager Login</button></li>
              <li><button type="button" class="btn btn-light" data-bs-toggle="modal" data-bs-target="#admin_login">Admin Login</button></li>
            </ul>
    </div>
    <!-- execute Modal -->
    
   
<div class="modal" id="emp_login">
  <div class="modal-dialog">
    <div class="modal-content">
      
      <div class="form">
      <div class="modal-header">
        <h4 class="modal-title">Executive  Login</h4>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>

      <div class="modal-body">

              <form name="myform" method="post" enctype="multipart/form-data"  id="emp_login" onsubmit="return  executefun()">
                
                <div class="form-group" >
                  <label for="executive"></label>
                  <input type="text" class="form-control" id="executive_usn" name="executiveid"  placeholder="Executive ID" required>
                  <div class="valid-feedback">Valid.</div>
                  <div class="invalid-feedback">Please fill out this field.</div>
                </div>
      
               
                <div class="form-group">
                  <label for="pwd" ></label>
                  <input type="password" class="form-control" id="executive_pass"  name="executivepass" placeholder="Password" required>
                  <div class="valid-feedback">Valid.</div>
                  <div class="invalid-feedback">Please fill out this field.</div>
                </div>
      
                <div class="forgot-pass-remember-me mt-10">
                  <div class="forgot-pass">
                      <a id="forgotpass" data-bs-toggle="modal" data-bs-target="#executive_forgot" href="#"> Forgot Password? </a>
                  </div>
      
                </div>
                <br>
                <center>
                <input type="submit" value="Login" name="executivelogin" class="btn btn-primary" id="button1" >
                <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Close</button>
              </center>
              </div>
              </form>
              </div>
         


    </div>
  </div>
</div>

<!--Forgot executive-->
<div class="modal" id="executive_forgot">
  <div class="modal-dialog">
    <div class="modal-content">
      
      <div class="form">
      <div class="modal-header">
        <h4 class="modal-title">Forgot password</h4>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>

      <div class="modal-body">

              <form name="myform" method="post" enctype="multipart/form-data" >
                
                <div class="form-group" >
                  <label for="executive"></label>
                  <input type="text" class="form-control" id="executive_usn" name="executiveforgot"  placeholder="Enter your Email" required>
                  <div class="valid-feedback">Valid.</div>
                  <div class="invalid-feedback">Please fill out this field.</div>
                </div>
      
       
                <br>
                <center>
                <input type="submit" value="submit" name="eforgot" class="btn btn-primary" id="button1" >
                <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Close</button>
              </center>
              </div>
              </form>
              </div>
         


    </div>
  </div>
</div>

<!--Forgot Manager-->
<div class="modal" id="manager_forgot">
  <div class="modal-dialog">
    <div class="modal-content">
      
      <div class="form">
      <div class="modal-header">
        <h4 class="modal-title">Forgot password</h4>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>

      <div class="modal-body">

              <form name="myform" method="post" enctype="multipart/form-data" >
                
                <div class="form-group" >
                  <label for="manager"></label>
                  <input type="text" class="form-control" id="manager_usn" name="managerforgot"  placeholder="Enter your Email" required>
                  <div class="valid-feedback">Valid.</div>
                  <div class="invalid-feedback">Please fill out this field.</div>
                </div>
      
       
                <br>
                <center>
                <input type="submit" value="submit" name="mforgot" class="btn btn-primary" id="button1" >
                <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Close</button>
              </center>
              </div>
              </form>
              </div>

    </div>
  </div>
</div> 

<!--manager modal-->
  <div class="modal" id="manager_login">
    <div class="modal-dialog">
      <div class="modal-content">
  
          <div class="form">
        <div class="modal-header">
          <h4 class="modal-title">Manager  Login</h4>
          <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
        </div>
  
        <div class="modal-body">
  
          <form name="myform" method="post" enctype="multipart/form-data"  id="form" onsubmit="return managerfun()">
            <div class="form-group">
              <label for="manager"></label>
              <input type="text" class="form-control" id="manager_usn" name="managerid" placeholder="Manager ID" required>
              <div class="valid-feedback">Valid.</div>
              <div class="invalid-feedback">Please fill out this field.</div>
            </div>
  
           
            <div class="form-group">
              <label for="pwd"></label>
              <input type="password" class="form-control" id="manager_pass"  name="managerpass" placeholder="Password" required>
              <div class="valid-feedback">Valid.</div>
              <div class="invalid-feedback">Please fill out this field.</div>
            </div>
  
            <div class="forgot-pass-remember-me mt-10">
              <div class="forgot-pass">
                  <a id="forgotpass" data-bs-toggle="modal" data-bs-target="#manager_forgot" onclick="" href="#">Forgot Password?</a>
              </div>
  
            </div>
            <br>
            <center>
            <input type="submit" value="Login" name="managerlogin" class="btn btn-primary" id="button1" >
            <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Close</button>
          </center>
         
          </form>
        </div>
         </div>
           
  </div>
      </div>
  </div>
<!--admin modal-->
<div class="modal" id="admin_login">
  <div class="modal-dialog">
    <div class="modal-content">

        <div class="form">
      <div class="modal-header">
        <h4 class="modal-title">Admin  Login</h4>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>

      <div class="modal-body">

        <form  method="post" enctype="multipart/form-data"  name="myform" id="forms" >
          <div class="form-group">
            <label for="admin"></label>
            <input type="text" class="form-control" id="adminusn" name="adminid" placeholder="Admin ID" required>
            <div class="valid-feedback">Valid.</div>
            <div class="invalid-feedback">Please fill out this field.</div>
          </div>
         
          <div class="form-group">
            <label for="passw"></label>
            <input type="password" class="form-control" id="adminpass"  name="adminpass" placeholder="Password" required>
            <div class="valid-feedback">Valid.</div>
            <div class="invalid-feedback">Please fill out this field.</div>
          </div>

          <br>
          <center>
          <input type="submit" value="Login" name="adminlogin" class="btn btn-primary" id="button1" >
          <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Close</button>
        </center>
      </form>
    </div>
      </div>
         
</div>


    </div>
  </div>

</div>
</div>
      </nav>
      

     <div class="container-fluid">
      <div class="row">
      <div class="col-2"></div>
        <div class="col-8" id="dialog">
         
            <p> <b> " Your work is going to fill a large part of your life, and the only way to be truly satisfied 
              is to do what you believe is great work. And the only way to do great work is to love what you do. 
              If you haven’t found it yet, keep looking. Don’t settle."</b> </p>
           
          </div>
          <div class="col-2"></div>
        </div>
        </div>
     
       

       <!--image-->
       <script>
        i=0,img=[],time=1700;
       
        img[0]="media/pic5.jpg";
        img[1]="media/pic6.jpg";
        img[2]="media/pic7.jpg";
        function slide(){
          document.images.src=img[i];
          if (i<img.length-1){
            i++;
          }
          else{
            i=0;
          }
          setTimeout(slide,time);
        }
        slide()
        

       
      </script>

      <center>
        <div class="image">
        <img name="images" class="rounded"  id="img" height="200px" width="450px">
        </div>
    
      </center>

      <div class="container-fluid mt-3" id="marque" >
        <marquee behavior="alternate" scrolldelay="150"><b>Employee Productivity Monitor & Management</b></marquee>
      </div>
      
      <!--best emp-->
      <div class="container-fluid">
      <div class="row" id="dinesh">
        
        <div class="col-3">
        
          <img src="media/dinesh.jpg" class="rounded-circle img-responsive" width="100%" >
       
        </div>
        
        <div class="col-8">
          
         <p><b>Dear <strong> Dinesh Sivakumar,</strong>  Congratulations! You are Techvolt software’s <b style="color:green">Best Employee of the month! </b>
           We’ve recognized how hard you’ve been working on multiple project. It took a lot of effort for you and 
            your team to fulfill all the requirements,
             organize all the activities and do it all on a high-quality level. </b></p>
            
        </div>
        
      </div>
    </div>
        <br>

      
      <!--footer-->
      <footer>
        <div class="container-fluid">
           <p>Copyright @2024 Techvolt Software PVT.LTD All right reserved</p>
           <p>www.techvoltcoimbatore.com</p>
           <p><b>Address:</b> 7,1st Floor, Sri Sairam Tower, NSR Rd, Nesavaalar Colony, Saibaba Koil, Coimbatore, Tamil Nadu 641011.</p>
         </div>
        </div>
      </div>
      </footer>
   
</body>
</html>
""")

form=cgi.FieldStorage()

padminid=form.getvalue("adminid")
padminpassword=form.getvalue("adminpass")
padminlogin =form.getvalue("adminlogin")


pmanagerid=form.getvalue("managerid")
pmanagerpass=form.getvalue("managerpass")
pmanagerlogin =form.getvalue("managerlogin")

pexecutiveid=form.getvalue("executiveid")
pexecutivepass=form.getvalue("executivepass")
pexecutivelogin =form.getvalue("executivelogin")

if padminlogin != None:
    q = """select id from admin where adminid='%s' and password='%s'""" % (padminid,padminpassword)
    cur.execute(q)
    rec = cur.fetchone()
    if rec !=None:
        print("""<script>
               alert("login successfully")
               location.href="admin_dash.py?id=%s"
               </script>""" % rec[0])
    else:
        print("""<script>
        alert("Invalid") </script>""")

if pmanagerlogin != None:
    q2 = """select id from empreg where role="manager" and userid='%s' and password='%s'""" % (pmanagerid,pmanagerpass)
    cur.execute(q2)
    rec2 = cur.fetchone()
    if rec2 !=None:
        print("""<script>
               alert("login successfully")
               location.href="manager_dash.py?id=%s"
               </script>""" % rec2[0])
    else:
        print("""<script>
        alert("Invalid") </script>""")

if pexecutivelogin != None:
    q = """select id from empreg where role="executive" and userid='%s' and password='%s'""" % (pexecutiveid,pexecutivepass)
    cur.execute(q)
    rec3 = cur.fetchone()
    if rec3 !=None:
        print("""<script>
               alert("login successfully")
               location.href="executive_dash.py?id=%s"
               </script>""" % rec3[0])
    else:
        print("""<script>
        alert("Invalid") </script>""")

#forgot executive

pexecutiveemail=form.getvalue("executiveforgot")
peforgot=form.getvalue("eforgot")

if peforgot != None:

    q=""" select * from empreg where role="executive" and email='%s' """ % (pexecutiveemail)
    cur.execute(q)
    rec1 = cur.fetchall()
    for i in rec1:

        pfirstname=i[1]
        plastname=i[2]
        pemail=i[6]
        pdep=i[11]
        prole=i[10]
        puserid=i[19]
        ppassword=i[20]

        q=""" insert into forgot (firstname,lastname,email,department,role,userid,password ) values('%s','%s','%s','%s','%s','%s','%s')"""%(pfirstname,plastname,pemail,pdep,prole,puserid,ppassword)
        cur.execute(q)
        con.commit()
        print("""<script> alert("password alert") </script>""")


# manager Forgot password

pmanageremail=form.getvalue("managerforgot")
pmforgot=form.getvalue("mforgot")



if pmforgot != None:

    q=""" select * from empreg where role="manager" and  email='%s' """%(pmanageremail)
    cur.execute(q)
    rec = cur.fetchall()
    for i in rec:
        pfirstname=i[1]
        plastname=i[2]
        pemail=i[6]
        pdep=i[11]
        prole=i[10]
        puserid=i[19]
        ppassword=i[20]

        q=""" insert into forgot (firstname,lastname,email,department,role,userid,password ) values('%s','%s','%s','%s','%s','%s','%s')"""%(pfirstname,plastname,pemail,pdep,prole,puserid,ppassword)
        cur.execute(q)
        con.commit()
        print("""<script> alert("password alert") </script>""")


