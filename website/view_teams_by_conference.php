<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../assets/substyles.css">
    <title>View Teams</title>
</head>
<body>
    <h1>Players on NFL Team</h1>

    <label for="ConferenceSelect">Select a Conference:</label>
    <select id="ConferenceSelect" name="Conference" onchange="updateSelectedConference()">
        <option value="" disabled selected>Select a Conference</option>
        <option value="NFC">NFC</option>
        <option value="AFC">AFC</option>
    </select>

    <button type="submit" form="playersForm">View Conferences</button>

    <form id="playersForm" action="view_teams_by_conference.php" method="POST">
        <input type="hidden" name="submit" value="1"> <!-- Adding a hidden input field named "submit" -->
        <input type="hidden" name="conference" id="selectedConference">
    </form>

    <button onclick="location.href='home.html';" class="back-btn">Home</button>

    <script>
        function updateSelectedConference() {
            var ConferenceSelect = document.getElementById("ConferenceSelect");
            var selectedConference = ConferenceSelect.options[ConferenceSelect.selectedIndex].value;
            document.getElementById("selectedConference").value = selectedConference;
        }
    </script>
</body>
</html>


<?php
if (isset($_POST['submit'])) 
{
    // add ' ' around multiple strings so they are treated as single command line args
    $data = escapeshellarg($_POST['conference']); #data

    // build the linux command that you want executed;  
    $command = 'python3 view_teams_by_conference.py ' . $data;

    // remove dangerous characters from command to protect web server
    $command = escapeshellcmd($command);
 
    // echo then run the command
    #echo "command: $command <br>";
    system($command);           
}
?>