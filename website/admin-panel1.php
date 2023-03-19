<!DOCTYPE html>

<head>
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

</head>
<?php
$con = mysqli_connect("localhost", "root", "", "myhmsdb");

include('newfunc.php');

if (isset($_POST['docsub'])) {
  $doctor = $_POST['doctor'];
  $dHeart_Rate = $_POST['dHeart_Rate'];
  $demail = $_POST['demail'];
  $spec = $_POST['special'];
  $docFees = $_POST['docFees'];
  $query = "insert into doctb(username,Heart_Rate,email,spec,docFees)values('$doctor','$dHeart_Rate','$demail','$spec','$docFees')";
  $result = mysqli_query($con, $query);
  if ($result) {
    echo "<script>alert('Doctor added successfully!');</script>";
  }
}


if (isset($_POST['docsub1'])) {
  $demail = $_POST['demail'];
  $query = "delete from doctb where email='$demail';";
  $result = mysqli_query($con, $query);
  if ($result) {
    echo "<script>alert('Doctor removed successfully!');</script>";
  } else {
    echo "<script>alert('Unable to delete!');</script>";
  }
}


?>
<html lang="en">

<head>


  <!-- Required meta tags -->
  <meta charset="utf-8">
  <link rel="shortcut icon" type="image/x-icon" href="images/favicon.png" />
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <link rel="stylesheet" type="text/css" href="font-awesome-4.7.0/css/font-awesome.min.css">
  <link rel="stylesheet" href="style.css">
  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="vendor/fontawesome/css/font-awesome.min.css">
  <link href="https://fonts.googleapis.com/css?family=IBM+Plex+Sans&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css" integrity="sha384-/Y6pD6FV/Vv2HJnA6t+vslU6fwYXjCFtcEpHbNJ0lyAFsXTsjBbfaDjzALeQsN6M" crossorigin="anonymous">
  <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top">

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <a class="navbar-brand" href="#"><i class="fa fa-user-plus" aria-hidden="true"></i> Hospital </a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <script>
      var check = function() {
        if (document.getElementById('dHeart_Rate').value ==
          document.getElementById('cdHeart_Rate').value) {
          document.getElementById('message').style.color = '#5dd05d';
          document.getElementById('message').innerHTML = 'Matched';
        } else {
          document.getElementById('message').style.color = '#f55252';
          document.getElementById('message').innerHTML = 'Not Matching';
        }
      }

      function alphaOnly(event) {
        var key = event.keyCode;
        return ((key >= 65 && key <= 90) || key == 8 || key == 32);
      };
    </script>

    <style>
      .bg-primary {
        background: -webkit-linear-gradient(left, #3931af, #00c6ff);
      }

      .col-md-4 {
        max-width: 20% !important;
      }

      .list-group-item.active {
        z-index: 2;
        color: #fff;
        background-color: #342ac1;
        border-color: #007bff;
      }

      .text-primary {
        color: #342ac1 !important;
      }

      #cpass {
        display: -webkit-box;
      }

      #list-app {
        font-size: 15px;
      }

      .btn-primary {
        background-color: #3c50c1;
        border-color: #3c50c1;
      }

      form {
        display: flex;
        flex-direction: column;
        align-items: center;
      }

      .label-group {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        width: 100%;
        margin-bottom: 0.5rem;
      }

      .label-group label {
        font-size: 1.2rem;
        font-weight: bold;
        width: 45%;
        margin-bottom: 0;
      }

      .input-group {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        width: 100%;
        margin-bottom: 1rem;
      }

      .input-group input,
      .input-group select {
        width: 45%;
        padding: 0.5rem;
        border-radius: 0.5rem;
        border: 1px solid #ccc;
        font-size: 1rem;
        margin-bottom: 0;
      }

      button[type="submit"] {
        background-color: #007bff;
        color: #fff;
        padding: 0.5rem 1rem;
        border: none;
        border-radius: 0.5rem;
        font-size: 1rem;
        cursor: pointer;
        transition: all 0.2s ease-in-out;
      }

      button[type="submit"]:hover {
        background-color: #0062cc;
      }
    </style>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item">
          <a class="nav-link" href="logout1.php"><i class="fa fa-sign-out" aria-hidden="true"></i>Logout</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#"></a>
        </li>
      </ul>
    </div>
  </nav>
</head>
<style type="text/css">
  button:hover {
    cursor: pointer;
  }

  #inputbtn:hover {
    cursor: pointer;
  }
</style>

<body style="padding-top:50px;">
  <div class="container-fluid" style="margin-top:50px;">
    <h3 style="margin-left: 40%; padding-bottom: 20px;font-family: 'IBM Plex Sans', sans-serif;"> WELCOME RECEPTIONIST </h3>
    <div class="row">
      <div class="col-md-4" style="max-width:25%;margin-top: 3%;">
        <div class="list-group" id="list-tab" role="tablist">
          <a class="list-group-item list-group-item-action active" id="list-dash-list" data-toggle="list" href="#list-dash" role="tab" aria-controls="home">Dashboard</a>

          <a class="list-group-item list-group-item-action" href="#list-pat" id="list-pat-list" role="tab" data-toggle="list" aria-controls="home">Patient List</a>
          <a class="list-group-item list-group-item-action" href="#add-pat" id="list-pat-list" role="tab" data-toggle="list" aria-controls="home">Add Patient</a>




        </div><br>
      </div>
      <div class="col-md-8" style="margin-top: 3%;">
        <div class="tab-content" id="nav-tabContent" style="width: 950px;">



          <div class="tab-pane fade show active" id="list-dash" role="tabpanel" aria-labelledby="list-dash-list">
            <div class="container-fluid container-fullw bg-white">
              <div class="row">

                <div class="col-sm-4" style="left: 35%">
                  <div class="panel panel-white no-radius text-center">
                    <div class="panel-body">
                      <span class="fa-stack fa-2x"> <i class="fa fa-square fa-stack-2x text-primary"></i> <i class="fa fa-users fa-stack-1x fa-inverse"></i> </span>
                      <h4 class="StepTitle" style="margin-top: 5%;">Patient List</h4>

                      <p class="cl-effect-1">
                        <!-- <a href="#app-hist" onclick="clickDiv('#list-pat-list')"> -->
                        View Patients
                        </a>
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="tab-pane fade" id="list-pat" role="tabpanel" aria-labelledby="list-pat-list">

            <div class="col-md-8">
            </div>

            <table class="table table-hover">
              <thead>
                <tr>
                  <th scope="col">ID</th>
                  <th scope="col">Room_Number</th>
                  <th scope="col">First Name</th>
                  <th scope="col">Last Name</th>
                  <th scope="col">Gender</th>
                  <th scope="col">Email</th>
                  <th scope="col">Contact</th>
                  <th scope="col">Heart_Rate</th>
                </tr>
              </thead>
              <script>
                function getData() {
                  setInterval(function() {
                    var xhr = new XMLHttpRequest();
                    xhr.open('GET', 'heartrate.php', true);
                    xhr.onload = function() {
                      if (this.status === 200) {
                        // clear the previous data from the table
                        document.getElementById('table-body').innerHTML = '';
                        // parse the JSON data
                        var data = JSON.parse(this.responseText);
                        console.log('data:', data);
                        // loop through the retrieved data and create table rows
                        data.forEach(function(row) {
                          console.log('row:', row);
                          var tableRow = document.createElement('tr');
                          // loop through each property of the row object and create table cells
                          for (var prop in row) {
                            console.log('cell:', row[prop]);
                            var tableCell = document.createElement('td');
                            tableCell.textContent = row[prop];
                            tableRow.appendChild(tableCell);
                          }
                          if (parseInt(row['Heart_Rate']) < 80) {
                            tableRow.style.backgroundColor = 'red';
                          }
                          // add the row to the table body
                          document.getElementById('table-body').appendChild(tableRow);
                        });
                      } else {
                        console.log('Request failed. Status:', this.status);
                      }
                    };
                    xhr.send();
                  }, 10);
                }

                getData();
              </script>
              <tbody id="table-body">


              </tbody>
            </table>
            <br>
          </div>
          <div class="tab-pane fade" id="add-pat" role="tabpanel" aria-labelledby="list-pat-list">

            <div class="col-md-8">
            </div>
            <form action="addpatient.php" method="POST">
              <div class="label-group">
                <label for="room_no">Room Number</label>
                <label for="fname">First Name</label>

              </div>
              <div class="input-group">
                <input type="text" id="room_no" name="room_no" required>
                <input type="text" id="fname" name="fname" required>

              </div>
              <div class="label-group">
                <label for="lname">Last Name</label>
                <label for="email">Email</label>

              </div>
              <div class="input-group">
                <input type="text" id="lname" name="lname" required>
                <input type="email" id="email" name="email" required>

              </div>
              <div class="label-group">
                <label for="gender">Gender</label>
                <label for="contact">Contact</label>


              </div>
              <div class="input-group">
                <select id="gender" name="gender" required>
                  <option value="">Select Gender</option>
                  <option value="Male">Male</option>
                  <option value="Female">Female</option>
                  <option value="Other">Other</option>
                </select>
                <input type="text" id="contact" name="contact" required>

              </div>

              <button type="submit">Submit</button>
            </form>



          </div>
        </div>
        <!-- Optional JavaScript -->
        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.11.0/umd/popper.min.js" integrity="sha384-b/U6ypiBEHpOf/4+1nzFpr53nxSS+GLCkfwBdFNTxtclqqenISfwAzpKaMNFNmj4" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/js/bootstrap.min.js" integrity="sha384-h0AbiXch4ZDo7tp9hKZ4TsHbi047NrKGLO3SEJAg45jXxnGIfYzk4Si90RDIqNm1" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/limonte-sweetalert2/6.10.1/sweetalert2.all.min.js"></script>
</body>

</html>