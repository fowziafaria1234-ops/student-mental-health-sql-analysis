# Data dictionary and privacy design

The repository intentionally excludes direct identifiers. `student_key` is a synthetic pseudonymous key.

| Table | Grain | Purpose |
|---|---|---|
| programmes | one row per programme | Programme and faculty dimensions |
| students | one row per student key | Demographic and study attributes |
| wellbeing_assessments | one row per student and term | Stress, sleep, wellbeing and loneliness measures |
| support_engagement | one row per support interaction summary | Support route, sessions and status |
| vw_student_kpi | one row per student key | Reusable analytical view |

External reporting should apply a minimum cohort size, suppress small groups and avoid re-identification through combinations of attributes.
