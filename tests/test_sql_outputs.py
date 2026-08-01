import sqlite3
import pandas as pd
def test_kpi_view_exists():
    conn=sqlite3.connect('data/processed/student_wellbeing.db')
    count=conn.execute('SELECT COUNT(*) FROM vw_student_kpi').fetchone()[0]; conn.close()
    assert count==900
def test_privacy_design():
    df=pd.read_csv('data/processed/student_kpi_view.csv')
    prohibited={'name','email','address','phone','student_number'}
    assert prohibited.isdisjoint(df.columns)
    assert df['student_key'].str.startswith('STU-').all()
