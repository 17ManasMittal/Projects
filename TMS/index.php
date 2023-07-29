<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Task Management Application</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.0/jquery.min.js"></script>
    <link rel="stylesheet" type="text/css" href="css/styles.css">
</head>

<body>
    <div class="row">
        <!-- m-auto for center -->
        <div class="col-md-4 m-auto" id="home_page">
            <center>
                <h3>Choose login role ?</h3>
            </center><br>
            <!-- Bootstrap  Three Buttons-->
            <a href="user_login.php" class="btn btn-success" style="margin-right: 140px;">User Login</a>
            <a href="register.php" class="btn btn-warning" style="margin-right: 140px;">User Registration</a>
            <!-- admin folder is different -->
            <a href="admin/admin_login.php" class="btn btn-info">Admin Login</a>
        </div>
    </div>
</body>

</html>