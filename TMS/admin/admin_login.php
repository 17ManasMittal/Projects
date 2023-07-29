<?php
session_start();
include('../includes/connection.php');
//if register button is set
if (isset($_POST['adminlogin'])) {
    $query = "select email,password,name from admins where email='$_POST[email]' AND password='$_POST[password]'";
    $query_run = mysqli_query($connection, $query);
    if (mysqli_num_rows($query_run)) {
        while ($row = mysqli_fetch_assoc($query_run)) {
            $_SESSION['email'] = $row['email'];
            $_SESSION['name'] = $row['name'];
        }
        echo "<script type='text/javascript'>
            window.location.href='admin_dashboard.php';
            </script>
            ";
    } else {
        echo "<script type='text/javascript'>
            alert('Please Enter Correct Details...');
            window.location.href='admin_login.php';
            </script>
            ";
    }
}
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Task Management Application | Admin Login</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>
    <link rel="stylesheet" type="text/css" href="../css/styles.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.0/jquery.min.js"></script>
</head>

<body>
    <div class="row">
        <div class="col-md-3 m-auto" id="login_home_page">
            <center>
                <h3 style="background-color: #5abf7b;padding: 5px;width:15vw;">Admin Login</h3>
            </center>
            <form action="" method="post">
                <div class="form-group">
                    <input type="email" name="email" class="form-control" placeholder="Enter Email" required>
                </div><br>
                <div class="form-group">
                    <input type="password" name="password" class="form-control" placeholder="Enter Password" required>
                </div><br>
                <div class="form-group">
                    <center><input type="submit" name="adminlogin" value="Login" class="btn btn-warning"></center>
                </div>
            </form>
            <br>
            <center><a href="../index.php" class="btn btn-danger">Go To Home Page</a></center>
        </div>
    </div>
</body>

</html>