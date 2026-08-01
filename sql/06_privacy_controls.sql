-- The analytical layer uses only pseudonymous student keys.
-- Direct identifiers such as names, emails, addresses and student numbers are excluded.
-- Example minimum-cell rule for external reporting:
SELECT programme, gender, COUNT(*) AS cohort_size, ROUND(AVG(avg_wellbeing),1) AS avg_wellbeing
FROM vw_student_kpi
GROUP BY programme, gender
HAVING COUNT(*) >= 10;
