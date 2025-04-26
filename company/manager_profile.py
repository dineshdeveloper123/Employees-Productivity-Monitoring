#!C:/Users/dell/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgi,cgitb,pymysql,os
import datetime

cgitb.enable()
con=pymysql.connect(host='localhost',user='root',password='',database='company')
cur=con.cursor()

f=cgi.FieldStorage()
userid=f.getvalue("id")


print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Manager Dashboard</title>
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
</head> """)
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




q="""select * from empreg where id='%s'""" % (userid)
cur.execute(q)
con.commit()
rec=cur.fetchall()
for i in rec:
     fn="user/"+i[18]
     print("""      <main class="content px- py-">
                <div class="container-fluid">
                    <div class="row">
                        <div class="col-3 col-sm-2 col-md-3 col-lg-3"></div>
                        <div class="col-6 col-sm-8 col-md-6 col-lg-6">
                          <br>
                          <h4><b style="color:green;">PROFILE</b></h4>
                          <div class="card" style=" background-color: rgb(215, 243, 251);box-shadow: 1px 1px 1px 2px rgba(82, 190, 240, 0.702); "> <center><br>
                            <img class="card-img-top rounded-circle" src='%s' alt="profile image" style="width:161px ; height:161px">
                            <div class="card-body">
                             
                              <h4 class="card-title">%s %s</h4>
                               <h5 class="card-text">%s %s</h5>
                                <h5 class="card-text">%s</h5>
                                <h5 class="card-text">%s</h5></center>
                                <button type="button" class="btn btn-secondary " data-bs-toggle="modal" data-bs-target="#passchange" >Change password <i class="fa fa-pencil-square" aria-hidden="true"></i></button>
                               
                            </div>
                          </div>
                            
                        </div>
                    </div>               
                 </div>
            </main>
       
        </div>
    </div>"""% (fn,i[1],i[2],i[11],i[10],i[6],i[7]))
     print("""
      
            <!--Modal password change-->
    <div class="modal" id="passchange">
      <div class="modal-dialog">
        <div class="modal-content">
          
         
          <div class="modal-header">
            <h4 class="modal-title"><b style="color: rgb(10, 169, 243);">CHANGE PASSWORD</b></h4>
            <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
          </div>
               
          <form class="form-group" method="post" enctype="multipart/form-data" >
          <div class="modal-body">
                    
                  <center>
                    
                  <input type="text" class="form-control" name="newpass" placeholder="Enter new password"><br>
                  <input type="text" class="form-control" name="repass" placeholder="Re-Enter new password">
              
                  </center>
                    
          </div>
          <div class="modal-footer d-flex justify-content-between">
            <input type="submit" value="update" class="btn btn-primary " name="update" > 
           <button type="button" class="btn btn-danger" data-bs-dismiss="modal">Close</button>
          
          </div>
            </form>
     </div>
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
""" )



pnewpass=f.getvalue("newpass")
prepass=f.getvalue("repass")
psubmit=f.getvalue("update")

if psubmit != None:
     if pnewpass == prepass:
          q ="""Update empreg set password='%s' where id='%s' """ % (pnewpass,userid)
          cur.execute(q)
          con.commit()
          print("""<script>
               alert("password updated")
               </script>""")

     else:
          print("""<script>
               alert("missmatch password")
               </script>""")
