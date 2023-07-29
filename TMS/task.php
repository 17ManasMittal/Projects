<?php
include('includes/connection.php');
session_start();
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.0/jquery.min.js"></script>
    <link rel="stylesheet" type="text/css" href="css/styles.css">
</head>

<body>
    <center>
        <h3 style="color: white;">Your Tasks</h3>
    </center>
    <table class="table" style="background-color: whitesmoke;width: 75vw;">
        <tr>
            <th>S.No</th>
            <th>Taks ID</th>
            <th>Description</th>
            <th>Start Date</th>
            <th>End Date</th>
            <th>Status</th>
            <th>Action</th>
        </tr>
        <?php
        $sno = 1;
        $query = "select * from tasks where uid= $_SESSION[uid]";
        $query_run = mysqli_query($connection, $query);
        while ($row = mysqli_fetch_assoc($query_run)) {
        ?>
            <tr>
                <td><?php echo $sno ?></td>
                <td><?php echo $row['tid'] ?></td>
                <td><?php echo $row['description'] ?></td>
                <td><?php echo $row['start_date'] ?></td>
                <td><?php echo $row['end_date'] ?></td>
                <td><?php echo $row['status'] ?></td>
                <td><a href="update_status.php?id=<?php echo $row['tid']; ?>">Update</a></td>
            </tr>
        <?php
            $sno = $sno + 1;
        }
        ?>
    </table>
</body>

</html>