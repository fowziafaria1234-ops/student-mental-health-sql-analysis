PRAGMA foreign_keys = ON;
CREATE TABLE programmes (programme_id TEXT PRIMARY KEY, programme TEXT NOT NULL, faculty TEXT NOT NULL);
CREATE TABLE students (student_key TEXT PRIMARY KEY, programme_id TEXT NOT NULL, gender TEXT, international_flag INTEGER, study_level TEXT, length_of_stay_months INTEGER, age_band TEXT, FOREIGN KEY(programme_id) REFERENCES programmes(programme_id));
CREATE TABLE wellbeing_assessments (student_key TEXT NOT NULL, term TEXT NOT NULL, stress_score REAL, sleep_hours REAL, wellbeing_score REAL, loneliness_score REAL, assessment_date TEXT, FOREIGN KEY(student_key) REFERENCES students(student_key));
CREATE TABLE support_engagement (student_key TEXT NOT NULL, support_type TEXT, sessions INTEGER, status TEXT, FOREIGN KEY(student_key) REFERENCES students(student_key));
