-- Referential integrity checks
SELECT COUNT(*) AS orphan_assessments
FROM wellbeing_assessments a LEFT JOIN students s ON s.student_key=a.student_key
WHERE s.student_key IS NULL;

-- Range checks
SELECT COUNT(*) AS invalid_wellbeing_scores FROM wellbeing_assessments WHERE wellbeing_score NOT BETWEEN 0 AND 100;
SELECT COUNT(*) AS invalid_sleep_hours FROM wellbeing_assessments WHERE sleep_hours NOT BETWEEN 0 AND 24;

-- Duplicate-grain check
SELECT student_key, term, COUNT(*) duplicates
FROM wellbeing_assessments
GROUP BY student_key, term
HAVING COUNT(*) > 1;
