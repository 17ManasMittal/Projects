<?php
session_start();
include('../includes/connection.php');
if (isset($_POST['create_task'])) {
    $query = "insert into tasks values(null,$_POST[id],'$_POST[description]','$_POST[start_date]','$_POST[end_date]','Not Started')";
    $query_run = mysqli_query($connection, $query);
    if ($query_run) {
        echo "<script type='text/javascript'>
            alert('Task Assigned Successfully...');
            window.location.href='admin_dashboard.php';
            </script>
            ";
    } else {
        echo "<script type='text/javascript'>
            alert('Please Try Again...');
            window.location.href='admin_dashboard.php';
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
    <title>Admin Dashboard</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.0/jquery.min.js"></script>
    <link rel="stylesheet" type="text/css" href="../css/styles.css">
    <!-- jquery code starts to open create_task file on same window without refreshing-->
    <script type="text/javascript">
        $(document).ready(function() {
            $("#manage_task").click(function() {
                $("#right_sidebar").load("manage_task.php");
            });
        });
        $(document).ready(function() {
            $("#create_task").click(function() {
                $("#right_sidebar").load("create_task.php");
            });
        });
    </script>
</head>

<body>
    <!-- Header code -->
    <div class="row" id="header">
        <div class="col-md-12">
            <div class="col-md-4" style="display: inline-block;">
                <h3>Task Management Application</h3>
            </div>
            <div class="col-md-6" style="display: inline-block;text-align: right;">
                <b>Email: </b><?php echo $_SESSION['email']; ?>
                <span style="margin-left: 25px;"><b>Name: </b><?php echo $_SESSION['name']; ?></span>
            </div>
        </div>
    </div>
    <!-- Header code end -->
    <div class="row">
        <div class="col-md-2" id="left_sidebar">
            <table class="table">
                <tr>
                    <td style="text-align: center;">
                        <a href="admin_dashboard.php" type="button" id="logout_link">Dashboard</a>
                    </td>
                </tr>
                <tr>
                    <td style="text-align: center;">
                        <a type="button" style="text-decoration: none;" class="link" id="create_task">Create Task</a>
                    </td>
                </tr>
                <tr>
                    <td style="text-align: center;">
                        <a type="button" style="text-decoration: none;" class="link" id="manage_task">Manage Task</a>
                    </td>
                </tr>
                <tr>
                    <td style="text-align: center;">
                        <a href="../logout.php" type="button" id="logout_link">Logout</a>
                    </td>
                </tr>
            </table>
        </div>
        <div class="col-md-10" id="right_sidebar">

        </div>
    </div>
</body>

</html>