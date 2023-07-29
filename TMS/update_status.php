<?php
include('includes/connection.php');
if (isset($_POST['update'])) {
    $query = "update tasks set status='$_POST[status]' where tid=$_GET[id]";
    $query_run = mysqli_query($connection, $query);
    if ($query) {
        echo "<script type='text/javascript'>
            alert('Status Updated Successfully...');
            window.location.href='user_dashboard.php';
            </script>
            ";
    } else {
        echo "<script type='text/javascript'>
            alert('Please Try Again...');
            window.location.href='user_dashboard.php';
            </script>
            ";
    }
}
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Task Management Application</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.0/jquery.min.js"></script>
    <link rel="stylesheet" type="text/css" href="css/styles.css">
</head>

<body>
    <!-- Header code starts here -->
    <div class="row" id="header">
        <div class="col-md-12">
            <h3><i class="fa fa-solid fa-list" style="padding-right: 15px;"></i>Task Management Application</h3>
        </div>
    </div>
    <div class="row">
        <div class="col-md-4 m-auto" style="color: white;">
            <h3 style="color: white;">Update The Task</h3><br>
            <?php
            $query = "select * from tasks where tid=$_GET[id]"; //id fetched from URL using GET
            $query_run = mysqli_query($connection, $query);
            while ($row = mysqli_fetch_assoc($query_run)) {
            ?>
                <form action="" method="post">
                    <div class="form-group">
                        <input type="hidden" name="id" value="" required class="form-control">
                    </div>
                    <div class="form-group">
                        <select name="status" class="form-control">
                            <option>-Select-</option>
                            <option>In-Progress</option>
                            <option>Completed</option>
                        </select>
                    </div>
                    <br>
                    <input type="submit" class="btn btn-warning" name="update" value="Update">
                </form>
            <?php
            }
            ?>
        </div>
    </div>
</body>

</html>