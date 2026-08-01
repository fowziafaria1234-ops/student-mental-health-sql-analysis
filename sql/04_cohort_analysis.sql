-- Programme comparison
SELECT programme, ROUND(AVG(avg_wellbeing),1) AS avg_wellbeing,
       ROUND(AVG(avg_stress),1) AS avg_stress,
       ROUND(AVG(avg_sleep),1) AS avg_sleep,
       COUNT(*) AS students
FROM vw_student_kpi
GROUP BY programme
ORDER BY avg_wellbeing DESC;

-- Length-of-stay cohorts
WITH cohorts AS (
  SELECT *, CASE WHEN length_of_stay_months<=6 THEN '0-6 months'
                 WHEN length_of_stay_months<=12 THEN '7-12 months'
                 WHEN length_of_stay_months<=24 THEN '13-24 months'
                 ELSE '25+ months' END AS stay_group
  FROM vw_student_kpi
)
SELECT stay_group, ROUND(AVG(avg_wellbeing),1) AS avg_wellbeing, COUNT(*) AS students
FROM cohorts GROUP BY stay_group ORDER BY MIN(length_of_stay_months);
