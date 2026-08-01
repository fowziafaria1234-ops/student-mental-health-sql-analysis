from pathlib import Path
import numpy as np
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
def main():
    rng=np.random.default_rng(202603)
    programmes=pd.DataFrame({'programme_id':['P01','P02','P03','P04','P05','P06'],'programme':['Computing','Business','Engineering','Health','Arts','Social Sciences'],'faculty':['Technology','Business','Engineering','Health','Humanities','Social Sciences']})
    n=900; keys=[f'STU-{i:05d}' for i in range(1,n+1)]
    students=pd.DataFrame({'student_key':keys,'programme_id':rng.choice(programmes.programme_id,n,p=[.20,.18,.18,.16,.14,.14]),'gender':rng.choice(['Female','Male','Non-binary','Prefer not to say'],n,p=[.48,.43,.05,.04]),'international_flag':rng.choice([0,1],n,p=[.67,.33]),'study_level':rng.choice(['Undergraduate','Postgraduate'],n,p=[.72,.28]),'length_of_stay_months':rng.integers(1,49,n),'age_band':rng.choice(['18-20','21-24','25-34','35+'],n,p=[.35,.38,.20,.07])})
    assessments=[]
    for key,prog,international,stay in students[['student_key','programme_id','international_flag','length_of_stay_months']].itertuples(index=False):
        base=64+min(stay,24)*.35-international*3+{'P01':0,'P02':1,'P03':-2,'P04':2,'P05':3,'P06':1}[prog]
        for term,date in [('T1','2025-10-15'),('T2','2026-02-15'),('T3','2026-05-15')]:
            stress=np.clip(rng.normal(55-base*.15+(4 if term=='T2' else 0),12),5,95); sleep=np.clip(rng.normal(6.7-stress*.012,.8),3.5,9.5); wellbeing=np.clip(base+sleep*2.1-stress*.28+rng.normal(0,7),10,95); loneliness=np.clip(rng.normal(45+max(0,10-stay)*.5,13),5,95); assessments.append([key,term,round(stress,1),round(sleep,1),round(wellbeing,1),round(loneliness,1),date])
    assessments=pd.DataFrame(assessments,columns=['student_key','term','stress_score','sleep_hours','wellbeing_score','loneliness_score','assessment_date'])
    # Select exactly 67 students (7.4% of 900) using risk-weighted sampling.
    # This keeps the portfolio result stable while preserving a relationship
    # between lower wellbeing / higher stress and support engagement.
    risk=assessments.groupby('student_key').agg(well=('wellbeing_score','mean'),stress=('stress_score','mean')).reset_index()
    risk['weight']=np.clip((70-risk.well)+(risk.stress-35),1,None)
    chosen=set(rng.choice(risk.student_key,size=67,replace=False,p=(risk.weight/risk.weight.sum()).to_numpy()))
    support=[]
    for key in chosen:
        support.append([key,rng.choice(['Counselling','Peer support','Academic adviser','Wellbeing workshop']),int(rng.integers(1,7)),rng.choice(['Completed','Ongoing','Referred'])])
    support=pd.DataFrame(support,columns=['student_key','support_type','sessions','status'])
    out=ROOT/'data/raw'; out.mkdir(parents=True,exist_ok=True); programmes.to_csv(out/'programmes.csv',index=False); students.to_csv(out/'students.csv',index=False); assessments.to_csv(out/'wellbeing_assessments.csv',index=False); support.to_csv(out/'support_engagement.csv',index=False)
if __name__=='__main__': main()
