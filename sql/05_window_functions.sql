-- Rank programmes within faculty and compare with the overall mean
WITH programme_kpi AS (
  SELECT faculty, programme, AVG(avg_wellbeing) avg_wellbeing
  FROM vw_student_kpi GROUP BY faculty, programme
)
SELECT faculty, programme, ROUND(avg_wellbeing,1) avg_wellbeing,
       DENSE_RANK() OVER (PARTITION BY faculty ORDER BY avg_wellbeing DESC) AS faculty_rank,
       ROUND(avg_wellbeing - AVG(avg_wellbeing) OVER (),1) AS variance_from_overall
FROM programme_kpi
ORDER BY faculty, faculty_rank;
