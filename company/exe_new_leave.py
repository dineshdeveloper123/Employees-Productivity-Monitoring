#!C:/Users/dell/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgi,cgitb,pymysql,os
import datetime

cgitb.enable()
con=pymysql.connect(host='localhost',user='root',password='',database='company')
cur=con.cursor()

f=cgi.FieldStorage()
userid=f.getvalue("id")
q="""select * from empreg where id='%s'""" % (userid)
cur.execute(q)

rec=cur.fetchall()

name =rec[0][1]
department =rec[0][11]
role =rec[0][10]

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Executive new leave</title>
     <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/css/bootstrap.min.css">
     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/js/bootstrap.bundle.min.js"></script>
     
     <!--
     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>

     -->
     <link
     rel="stylesheet"
     href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" />
 
     <!--executive dash style-->
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

     <!--exe leave form style-->
     <style>

.container-fluid{
        margin: 0;
        padding: 0;
        font-family:Arial, Helvetica, sans-serif;
        font-weight:550;
        }
        
        .form1{
        background-color: rgb(249, 240, 238);
        padding:40px;
        border-color: rgb(212, 233, 250);
        border-width:3px;
        border-style:solid;
        border-radius:10px;
        box-shadow: 1px 1px 11px 4px rgb(134, 157, 170);
        
        }
        .form-control{
        margin: 10px;
        }
        #button1{
        margin-left:30px;
        }
        
        </style>
</head>""")

print("""

<body>
    <div class="wrapper">
        <div id="sidebar" class="js-sidebar">
            <!-- Content For Sidebar -->
            <div class="h-100">
                <div class="sidebar-logo" style="margin-bottom: -35px;">
                    <p style="color: rgb(165, 27, 27);"><img src="media/techlogo.png"  height="45px"> <b>TECHVOLT SOFTWARE</b></p>
                </div>
                <ul class="sidebar-nav">
                    <li class="sidebar-header">
                        <h4><b style="color: green;">EXECUTIVE</b></h4>
                       
                    </li>
                    <hr>
                  <li class="sidebar-item">
                        <a href="exe_profile.py?id=%s" class="sidebar-link" >
                            <i class="fa fa-user-circle" aria-hidden="true"></i>
                           PROFILE
                        </a>
                    </li>
                   
                    <li class="sidebar-item">
                        <a href="#" class="sidebar-link collapsed" data-bs-target="#timesheet" data-bs-toggle="collapse"
                            aria-expanded="false"><i class="fa fa-table" aria-hidden="true"></i>
                             TIMESHEET
                        </a>
                        <ul id="timesheet" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#sidebar">
                            <li class="sidebar-item">
                                <a href="exe_new_timeS.py?id=%s" class="sidebar-link">New</a>
                            </li>
                            <li class="sidebar-item">
                                <a href="exe_exis_timeS.py?id=%s" class="sidebar-link">Existing</a>
                            </li>
                        </ul>
                    </li>
                   
                    <li class="sidebar-item">
                      <a href="exe_new_anno.py?id=%s" class="sidebar-link">
                          <i class="fa fa-bullhorn" aria-hidden="true"></i>
                         ANNOUNCEMENT
                      </a>
                  </li>
                            <li class="sidebar-item">
                                <a href="#" class="sidebar-link collapsed" data-bs-target="#leave" data-bs-toggle="collapse"
                                    aria-expanded="false"><i class="fa fa-files-o" aria-hidden="true"></i>
                                    LEAVE
                                </a>
                                <ul id="leave" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#sidebar">
                                    <li class="sidebar-item">
                                        <a href="exe_new_leave.py?id=%s" class="sidebar-link">New</a>
                                    </li>
                                    <li class="sidebar-item">
                                        <a href="exe_exis_leave.py?id=%s" class="sidebar-link">Existing</a>
                                    </li>
                           
                                </ul>
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
        </div>"""% (userid,userid,userid,userid,userid,userid))
current = datetime.datetime.now()

print("""
        
        <div class="main">
          <!--nav-->
            <nav class="navbar navbar-expand px-4 border-bottom" style="background-color: #a6c3f8;">
                <button class="btn btn-info" id="sidebar-toggle" type="button" style="background-color: rgb(209, 236, 251);">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="navbar-collapse navbar">
                    
                 <img src="media/logopic.png"  alt="logo" height="35px" style="padding-left: 20px;">
                 
                </div>
            </nav>
                        <div style="text-align:right; color:#637ba8">
                <p><b>%s<b></p><hr>
                </div> """%(current))
print("""
            <main class="content px-3 py-2">
                <div class="container-fluid">
                    <div class="row">
                        <div class="col-3">
                
                        </div>
                        <div class="col-6"><br>
                            <h4 style="color: green;">LEAVE APPLICATION</h4><br>
                            <form name="myform" method="post" enctype="multipart/form-data" class="form1" style="overflow: hidden;">
                                                           
                                <div class="form-group">
                                  <label for="start">Start Date:</label>
                                  <input type="date" class="form-control" id="start"  name="start" required>
                                  <div class="valid-feedback">Valid.</div>
                                  <div class="invalid-feedback">Please fill out this field.</div>
                                </div>
                        
                                <div class="form-group">
                                   <label for="end">End Date:</label>
                                  <input type="date" class="form-control" id="end"  name="end" onchange="cal_leave()" required>
                                  <div class="valid-feedback">Valid.</div>
                                  <div class="invalid-feedback">Please fill out this field.</div>
                                </div>
                        
                                <div class="form-group">
                                  <label for="NoOfdays">No.of Days:</label>
                                 <input type="number"  class="form-control" id="NoOfdays"  name="noofdays" readonly required>
                                 <div class="valid-feedback">Valid.</div>
                                 <div class="invalid-feedback">Please fill out this field.</div>
                               </div>
                                
                                <div class="form-group">
                                  <label for="reason">Leave Reason:</label>
                                  <select class="form-control" name="reason" id="reason" required>
                                    <option value="Madical Leave"> Madical Leave </option>
                                    <option value="Personal Leave">Personal Leave</option>
                                    <option value="Annual Leave">Annual Leave</option>
                                  </select>
                                  <div class="valid-feedback">Valid.</div>
                                  <div class="invalid-feedback">Please fill out this field.</div>
                                </div>
                        
                             
                                <input type="submit" value="Submit" name="request"  class="btn btn-primary" id="button1" >
                                <input type="reset" value="Cancel" class="btn btn-secondary" id="button2">
                                
                            
                              </form>
                
                        </div>
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
    
          function cal_leave(){
            let start_date=document.getElementById("start").value
            let end_date=document.getElementById('end').value
            start_date=new Date(start_date)
            end_date=new Date(end_date)

            var time_diff=end_date.getTime()-start_date.getTime()
            if(time_diff>0){
              var time_diff=time_diff/(1000*60*60*24)
              document.getElementById("NoOfdays").value=time_diff
            }
            else{
              alert("Choose Correct Date")
            }
          }                            
    </script>
</body>

</html>
""")
psubmit=f.getvalue('request')

if psubmit != None:
    startdate=f.getvalue("start")
    enddate=f.getvalue("end")
    noofdays=f.getvalue("noofdays")
    reason=f.getvalue("reason")
    print(reason)
    # c_m=datetime.datetime.now().month
    # month=calendar.month_name[c_m]
    # con2 = pymysql.connect(host="localhost", user="root", password="", database="company")
    # cur2 = con2.cursor()

    q="""select sum(noofdays) from leavet where status='Approve' and eid='%s'"""%(userid)
    cur.execute(q)
    t=cur.fetchall()
    print(t)
    total_leave=0
    for i in t:

        if i[0]==0:
            total_leave=0
        else:
            total_leave=i[0]
        print(total_leave)
    status='new'
    con = pymysql.connect(host="localhost", user="root", password="", database="company")
    cur = con.cursor()
    q3="""insert into leavet (eid,name,department,role,startdate,enddate,noofdays,reason,totalleave,status) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""%(userid,name,department,role,startdate,enddate,noofdays,reason,total_leave,status)
    cur.execute(q3)
    con.commit()
    print("""<script>alert("ok")</script>""")
