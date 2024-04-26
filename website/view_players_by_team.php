<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../assets/substyles.css">
    <title>View Players By Team</title>
</head>
<body>
    <h1>Players on NFL Team</h1>

    <label for="teamSelect">Select a Team:</label>
    <select id="teamSelect" name="team" onchange="updateSelectedTeam()">
        <option value="" disabled selected>Select a team</option>
        <option value="49ers">San Francisco 49ers</option>
        <option value="bears">Chicago Bears</option>
        <option value="bengals">Cincinnati Bengals</option>
        <option value="bills">Buffalo Bills</option>
        <option value="broncos">Denver Broncos</option>
        <option value="browns">Cleveland Browns</option>
        <option value="buccaneers">Tampa Bay Buccaneers</option>
        <option value="cardinals">Arizona Cardinals</option>
        <option value="chargers">Los Angeles Chargers</option>
        <option value="chiefs">Kansas City Chiefs</option>
        <option value="colts">Indianapolis Colts</option>
        <option value="cowboys">Dallas Cowboys</option>
        <option value="dolphins">Miami Dolphins</option>
        <option value="eagles">Philadelphia Eagles</option>
        <option value="falcons">Atlanta Falcons</option>
        <option value="giants">New York Giants</option>
        <option value="jaguars">Jacksonville Jaguars</option>
        <option value="jets">New York Jets</option>
        <option value="lions">Detroit Lions</option>
        <option value="packers">Green Bay Packers</option>
        <option value="panthers">Carolina Panthers</option>
        <option value="patriots">New England Patriots</option>
        <option value="raiders">Las Vegas Raiders</option>
        <option value="rams">Los Angeles Rams</option>
        <option value="ravens">Baltimore Ravens</option>
        <option value="redskins">Washington Football Team</option>
        <option value="saints">New Orleans Saints</option>
        <option value="seahawks">Seattle Seahawks</option>
        <option value="steelers">Pittsburgh Steelers</option>
        <option value="texans">Houston Texans</option>
        <option value="titans">Tennessee Titans</option>
        <option value="vikings">Minnesota Vikings</option>
    </select>    

    <button type="submit" form="playersForm">View Players</button>

    <form id="playersForm" action="view_players_by_team.php" method="POST">
        <input type="hidden" name="submit" value="1"> <!-- Adding a hidden input field named "submit" -->
        <input type="hidden" name="team_id1" id="selectedTeam">
    </form>

    <button onclick="location.href='home.html';" class="back-btn">Home</button>

    <script>
        function updateSelectedTeam() {
            var teamSelect = document.getElementById("teamSelect");
            var selectedTeam = teamSelect.options[teamSelect.selectedIndex].value;
            document.getElementById("selectedTeam").value = selectedTeam;
        }
    </script>
</body>
</html>


<?php
if (isset($_POST['submit'])) 
{
    // add ' ' around multiple strings so they are treated as single command line args
    $data = escapeshellarg($_POST['team_id1']); #data

    // build the linux command that you want executed;  
    $command = 'python3 view_players_by_team.py ' . $data;

    // remove dangerous characters from command to protect web server
    //$command = escapeshellcmd($command);
 
    // echo then run the command
    echo "command: $command <br>";
    system($command);           
}
?>