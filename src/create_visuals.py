from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
COLORS=['#14B8A6','#38BDF8','#8B5CF6','#F59E0B','#22D3EE','#6366F1']

def style(ax,title):
    ax.set_title(title,fontsize=16,fontweight='bold',color='#0F172A',pad=16)
    ax.spines[['top','right']].set_visible(False)
    ax.grid(axis='y',alpha=.16)

def main():
    df=pd.read_csv(ROOT/'data/processed/student_kpi_view.csv'); out=ROOT/'assets'
    summary=df.groupby('programme').avg_wellbeing.mean().sort_values(ascending=False)
    fig,ax=plt.subplots(figsize=(11,5.6)); summary.plot(kind='bar',ax=ax,color=COLORS[:len(summary)]); ax.set_ylabel('Average wellbeing score'); ax.set_xlabel(''); style(ax,'Wellbeing by study programme'); fig.tight_layout(); fig.savefig(out/'programme-wellbeing.png',dpi=170,facecolor='white'); plt.close(fig)
    fig,ax=plt.subplots(figsize=(11,5.6)); ax.scatter(df.avg_sleep,df.avg_stress,alpha=.28,color='#38BDF8',edgecolors='none'); ax.set_xlabel('Average sleep hours'); ax.set_ylabel('Average stress score'); style(ax,'Sleep and stress relationship'); fig.tight_layout(); fig.savefig(out/'stress-sleep.png',dpi=170,facecolor='white'); plt.close(fig)
if __name__=='__main__': main()
