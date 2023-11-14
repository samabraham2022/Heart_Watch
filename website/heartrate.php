<?php
// Connect to database
$servername = "localhost";
$username = "root";
$password = "samgeorge";
$dbname = "myhmsdb";

$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

// Retrieve data from the database
$sql = "SELECT * FROM patreg";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  $data = array();
  // Loop through the results and add each row to the data array
  while ($row = $result->fetch_assoc()) {
    $data[] = $row;
  }
  // Close database connection
  $conn->close();
  // Return data as JSON
  header('Content-Type: application/json');
  echo json_encode($data);
} else {
  // Close database connection
  $conn->close();
  // Return error message as JSON
  header('Content-Type: application/json');
  echo json_encode(array('error' => 'No data found.'));
}
?>
