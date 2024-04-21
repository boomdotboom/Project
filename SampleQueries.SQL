-- Select results by team
SELECT g.Date, t1.Location, t1.Nickname, g.Score1, t2.Location, t2.Nickname, g.Score2, 
        IF(g.Score1>g.Score2, Concat(t1.Nickname," Won"),Concat(t1.Nickname," Lost")) AS Result 
        FROM Game g 
        JOIN Team t1 on t1.TeamId= g.TeamId1 
        JOIN Team t2 on t2.TeamId= g.TeamId2 
            WHERE g.TeamId1= :team_id 
                OR g.teamId2= :team_id;

-- Select results by Date
    SELECT g.Date, t1.Location, t1.Nickname, g.Score1, t2.Location, t2.Nickname, g.Score2, 
        IF(g.Score1>g.Score2, Concat(t1.Nickname," Won"),Concat(t1.Nickname," Lost")) AS Result 
        FROM Game g 
        JOIN Team t1 on t1.TeamId= g.TeamId1 
        JOIN Team t2 on t2.TeamId= g.TeamId2 
            WHERE g.date= :date