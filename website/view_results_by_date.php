<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Results by Date</title>
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../assets/substyles.css">
</head>
<body>
    <h1>Results on a Given Date</h1>

    <label for="dateSelect">Select a Date:</label>
    <input type="date" id="date" name="date">
    
    <button type="submit" form="gamesForm">View Results</button>

    <form id="gamesForm" action="view_results_by_date.php" method="POST" onsubmit="updateSelectedDate()">
        <input type="hidden" name="submit" value="1"> 
        <input type="hidden" name="date" id="dateSelect"> 
    </form>

    <button onclick="location.href='home.html';" class="back-btn">Home</button>

    <script>
        function updateSelectedDate() {
            var dateSelect = document.getElementById("date");
            var selectedDate = dateSelect.value;
            document.getElementById("dateSelect").value = selectedDate;
        }
    </script>
</body>
</html>

<?php
if (isset($_POST['submit'])) 
{
    // replace ' ' with '\ ' in the strings so they are treated as single command line args
    $date = escapeshellarg($_POST['date']);

    $command = 'python3 view_results_by_date.py ' . $date;

    // remove dangerous characters from command to protect web server
    $escaped_command = escapeshellcmd($command);
    echo "<p>command: $command <p>"; 
    // run insert_new_item.py
    system($escaped_command);           
}
?>