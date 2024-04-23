<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../assets/substyles.css">
    <title>View Teams</title>
</head>
<body>
    <div class="options-box">
        <h1>View Teams</h1>
        <form action="view_teams_by_confrence.php" method="post">

            <div class="form-group">
                <label for="confrence">Confrence:</label>
                <input type="text" id="confrence" name="confrence" required><br><br>
            </div>

            <button type="submit">Submit</button>

        </form>
    </div>
    <a href="home.html">Home</a>

    <script>
        function validateForm() {
            var form = document.getElementById("findTeamsbyConfrenceForm");
            var inputs = form.getElementsByTagName("input");
            for (var i = 0; i < inputs.length; i++) {
                if (inputs[i].value.trim() === "") {
                    alert("Please fill out all the fields.");
                    return false;
                }
            }
            return true;
        }
    </script>
</body>
</html>


<?php
if (isset($_POST['submit'])) 
{
    // add ' ' around multiple strings so they are treated as single command line args
    $data = escapeshellarg($_POST['confrence']); #data

    // build the linux command that you want executed;  
    $command = 'python3 view_teams_by_confrence.py ' . $data;

    // remove dangerous characters from command to protect web server
    $command = escapeshellcmd($command);
 
    // echo then run the command
    echo "command: $command <br>";
    system($command);           
}
?>