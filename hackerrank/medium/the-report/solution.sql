
select 
case 
    when g.grade >=8 Then S.name
    else 'NULL'
END,
G.grade,s.marks 
from
students S join Grades G
ON S.marks between G.MIN_MArk and G.max_mark
order by G.grade desc ,s.name;
