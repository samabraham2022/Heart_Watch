<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "myhmsdb";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

if($_SERVER["REQUEST_METHOD"] == "POST") {
    $room_no = $_POST['room_no'];
    $fname = $_POST['fname'];
    $lname = $_POST['lname'];
    $gender = $_POST['gender'];
    $email = $_POST['email'];
    $contact = $_POST['contact'];

    // set Heart_Rate to 0
    $heart_rate = "0";

    $stmt = $conn->prepare("INSERT INTO patients (Room_No, fname, lname, gender, email, contact, Heart_Rate) VALUES (?, ?, ?, ?, ?, ?, ?)");
    $query="INSERT INTO patreg (Room_No, fname, lname, gender, email, contact, Heart_Rate) VALUES ('$room_no', '$fname', '$lname', '$gender', '$email', '$contact', '$heart_rate')";
    $result=mysqli_query($conn,$query);
    if($result){
        header("Location:admin-panel1.php");
        
    }
    $conn->close();
}
