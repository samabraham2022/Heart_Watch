<?php
$servername = "localhost";
$username = "root";
$password = "samgeorge";
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
    $Heart_attack = "False";


    $sql = "INSERT INTO patreg (Room_No, fname, lname, gender, email, contact, Heart_Rate,Heart_Attack) VALUES ('$room_no', '$fname', '$lname', '$gender', '$email', '$contact', '$heart_rate','$Heart_Attack')";

// Execute the query
    if ($conn->query($sql) === TRUE) {
        echo "Record inserted successfully";
        header("Location:admin-panel1.php");
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }

    // if($result){
    //     header("Location:admin-panel1.php");
        
    // }
    $conn->close();
}
