from pathlib import Path
import sqlite3
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
def main():
    db=ROOT/'data/processed/student_wellbeing.db'; db.parent.mkdir(parents=True,exist_ok=True)
    conn=sqlite3.connect(db)
    for file,table in [('programmes.csv','programmes'),('students.csv','students'),('wellbeing_assessments.csv','wellbeing_assessments'),('support_engagement.csv','support_engagement')]:
        pd.read_csv(ROOT/'data/raw'/file).to_sql(table,conn,index=False,if_exists='replace')
    conn.executescript((ROOT/'sql/03_kpi_view.sql').read_text())
    pd.read_sql_query('SELECT * FROM vw_student_kpi',conn).to_csv(ROOT/'data/processed/student_kpi_view.csv',index=False)
    conn.close()
if __name__=='__main__': main()
