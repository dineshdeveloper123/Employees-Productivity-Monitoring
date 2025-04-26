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
con.commit()
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
    <title>Manager new timeSheet</title>
     <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/css/bootstrap.min.css">
     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/js/bootstrap.bundle.min.js"></script>
     <!--
     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>

     -->
     <link
     rel="stylesheet"
     href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" />
       
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
  .table{
    overflow:auto;
    text-wrap:nowrap;
    text-align: center;
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
                        <h4><b style="color: green;">MANAGER</b></h4>
                         <b style="color: green;">PERSONAL</b>
                    </li>
                    <li class="sidebar-item">
                        <a href="manager_profile.py?id=%s" class="sidebar-link" >
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
                                <a href="manager_new_timeS.py?id=%s" class="sidebar-link">New</a>
                            </li>
                            <li class="sidebar-item">
                                <a href="manager_exis_times.py?id=%s" class="sidebar-link">Existing</a>
                            </li>
                        </ul>
                    </li>
                   
                            <li class="sidebar-item">
                        <a href="manager_new_anno.py?id=%s" class="sidebar-link" >
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
                                        <a href="manager_new_leave.py?id=%s" class="sidebar-link">New</a>
                                    </li>
                                    <li class="sidebar-item">
                                        <a href="manager_exis_leave.py?id=%s" class="sidebar-link">Existing</a>
                                    </li>
                           
                                </ul>
                            </li>
                                <li class="sidebar-header">
                                     <b style="color: green;">ROLE</b>
                                </li>

                                <li class="sidebar-item">
                                  <a href="#" class="sidebar-link collapsed" data-bs-target="#timesheetE" data-bs-toggle="collapse"
                                      aria-expanded="false"><i class="fa fa-table" aria-hidden="true"></i>
                                      TIMESHEET
                                  </a>
                                  <ul id="timesheetE" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#sidebar">
                                      <li class="sidebar-item">
                                          <a href="manager_role_new_timeS.py?id=%s" class="sidebar-link">New</a>
                                      </li>
                                      <li class="sidebar-item">
                                          <a href="manager_role_exis_timeS.py?id=%s" class="sidebar-link">Existing</a>
                                      </li>
                                  </ul>
                              </li>

                        <li class="sidebar-item">
                        <a href="manager_role_his.py?id=%s" class="sidebar-link" >
                            <i class="fa fa-history" aria-hidden="true"></i>
                           EXECUTIVE HISTORY
                        </a>
                    </li>

                                <li class="sidebar-item">
                                    <a href="#" class="sidebar-link collapsed" data-bs-target="#leaveE" data-bs-toggle="collapse"
                                        aria-expanded="false"><i class="fa fa-files-o" aria-hidden="true"></i>
                                        LEAVE
                                    </a>
                                    <ul id="leaveE" class="sidebar-dropdown list-unstyled collapse" data-bs-parent="#sidebar">
                                        <li class="sidebar-item">
                                            <a href="manager_role_new_leave.py?id=%s" class="sidebar-link">New</a>
                                        </li>
                                        <li class="sidebar-item">
                                            <a href="manager_role_exis_leave.py?id=%s" class="sidebar-link">Existing</a>
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
        </div>"""%(userid,userid,userid,userid,userid,userid,userid,userid,userid,userid,userid))
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
                        <div class="col-12"><br>
                            <h4 style="color: green;">NEW TIMESHEET</h4><hr>
              
                            <div class="table" style="display: fixed;">
                              <form method="post" enctype="multipart/form-data">
                            <table class="table table-responsive table-bordered table-striped" border="1" cellpadding="5" style="overflow: auto; text-align: center;" >
                                
                                <tr style="background-color:rgb(152, 248, 192);">
                                    <th> Date</th> <th style="padding-left: 50px; padding-right: 50px;">Day </th> <th <th style="padding-left: 50px; padding-right: 50px;">Timing</th>
                                     <th style="padding-left: 30px; padding-right: 30px;">Hours</th>  <th>Work status</th> <th>Acknowledgement</th>

                                </tr>
                                
                                <tr>
                                  <td >  <input type="date" id="dateInput" name="date1" class="form-control" onchange="disDay()" required style="background: transparent; "></td>
                                <td style="background: transparent;"><input type="text"  class="form-control" id="dayInput" name="day1"  readonly required style="background: transparent;"> </td>
                                <td> <select class="form-control" name="timing" style="background: transparent;" >
                                  <option value="10am to 10pm">10am to 10pm</option>
                                  <option value="10am to 8pm">10am to 8pm</option>
                                  <option value="10am to 6pm">10am to 6pm</option>
                                </select></td>

                                <td> <select class="form-control" name="hours" style="background: transparent; ">
                                  <option value="12">12</option>
                                  <option value="10">10</option>
                                  <option value="8">8</option>
                                </select></td>

                                <td ><textarea id="work"  class="form-control" name="work" rows="3" cols="10" style="background: transparent; " required> </textarea></td>
                              
                                <td ><input type="submit" class="btn btn-success" name="send" value="Send"> </td>
                                </tr>
                                
                              
                            </table>
                          </form>
                          </div>
                            
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
        
          function disDay(){
            var selectDate= new Date(document.getElementById("dateInput").value);
            var daysOfWeek= ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
            var selectDay = daysOfWeek[selectDate.getDay()];

            document.getElementById("dayInput").value=selectDay;
          }
    </script>
</body>

</html>
""")

pdate=f.getvalue('date1')
pday=f.getvalue('day1')
ptiming=f.getvalue('timing')
phours=f.getvalue('hours')
pwork=f.getvalue('work')
psubmit = f.getvalue('send')
if psubmit != None:

    q="""select sum(hours) from timesheet where status='approved' and empid='%s'"""%(userid)
    cur.execute(q)
    t=cur.fetchall()

    total_hours=0
    for i in t:

        if i[0]==0:
            total_hours=0
        else:
            total_hours=i[0]


    q2="""insert into timesheet (empid,name,department,role,date,day,timing,hours,workstatus,totalhours) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""%(userid,name,department,role,pdate,pday,ptiming,phours,pwork,total_hours)
    cur.execute(q2)
    con.commit()
    print("""
    <script> alert("TimeSheet sent")</script>
    """)
