# %%
import pandas as pd
import numpy as np 

# %%
def CombineStateChildPlan (StatefileName, ChildfileName, PlanfileName):
    #df = pd.merge(PlanfileName, ChildfileName, how="left", on=["f1_title_iv_agency", "reporting_period_name", "child_record_id"])
    df = pd.merge(StatefileName, ChildfileName, how="left", on=["f1_title_iv_agency"])
    #df = pd.merge(df, PlanfileName, how="outer", on=["f1_title_iv_agency", "child_record_id"])
    df = pd.merge(df, PlanfileName, how="outer", on=["f1_title_iv_agency", "child_record_id","f2_child_identifier","prevention_plan_id"])

    
    return(df)


# %% 
def AddSummerizedFcCounts (df,FC_DF):
    df = pd.merge(FC_DF,df,how="left",on=["f1_title_iv_agency", "child_record_id","f2_child_identifier"])
    return(df)

# %%
if __name__ == '__main__':
    Comb = CombineStateChildPlan(State_df,Child_df, PreventionPlan_df)
    Comb_df = AddSummerizedFcCounts(Comb,Fostercare_df)
    print(Comb['f1_title_iv_agency'].value_counts())
    print(Child_df['f1_title_iv_agency'].value_counts())

# %%

