<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>

<body>
    <h3 style="color: white;">Create A New Task</h3>
    <div class="row">
        <div class="col-md-6">
            <form action="" method="post">
                <div class="form-group">
                    <label style="color: white;">Select User:</label>
                    <select class="form-control" name="id">
                        <option>-Select-</option>
                        <?php
                        include('../includes/connection.php');
                        $query = "select name,uid from users";
                        $query_run = mysqli_query($connection, $query);
                        if (mysqli_num_rows($query_run)) {
                            while ($row = mysqli_fetch_assoc($query_run)) {
                        ?>
                                <option value="<?php echo $row['uid']; ?>"><?php echo $row['name']; ?></option>
                        <?php
                            }
                        }
                        ?>
                    </select>
                </div>
                <br>
                <div class="form-group">
                    <label style="color: white;">Description:</label>
                    <textarea class="form-control" rows="3" cols="50" name="description" placeholder="Mention The Task"></textarea>
                </div><br>
                <div class="form-group">
                    <label style="color: white;">Start Date:</label>
                    <input type="date" class="form-control" name="start_date">
                </div><br>
                <div class="form-group">
                    <label style="color: white;">End Date:</label>
                    <input type="date" class="form-control" name="end_date">
                </div><br>
                <input type="submit" class="btn btn-warning" name="create_task" value="Create">
            </form>
        </div>
    </div>
</body>

</html>