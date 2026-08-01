CREATE VIEW IF NOT EXISTS vw_student_kpi AS
SELECT s.student_key,p.programme,p.faculty,s.gender,s.international_flag,s.study_level,s.length_of_stay_months,
       ROUND(AVG(a.wellbeing_score),2) AS avg_wellbeing,
       ROUND(AVG(a.stress_score),2) AS avg_stress,
       ROUND(AVG(a.sleep_hours),2) AS avg_sleep,
       ROUND(AVG(a.loneliness_score),2) AS avg_loneliness,
       CASE WHEN se.student_key IS NULL THEN 0 ELSE 1 END AS used_support
FROM students s
JOIN programmes p ON p.programme_id=s.programme_id
JOIN wellbeing_assessments a ON a.student_key=s.student_key
LEFT JOIN (SELECT DISTINCT student_key FROM support_engagement) se ON se.student_key=s.student_key
GROUP BY s.student_key,p.programme,p.faculty,s.gender,s.international_flag,s.study_level,s.length_of_stay_months,se.student_key;
