# -*- coding: utf-8 -*-
####################################
# process_main_table module
#----------------------------------#
# 
#
# Author: Malcolm
#----------------------------------#



# %%
import pandas as pd
import numpy as np 

#MH note to self, consider using engine = 'pyarrow' and use_nullabel_dtypes=TRUE to see if it is much faster.

# %%
def load_state_table_csv(inputPath, fileName,FileType =''):
    df = pd.read_csv(inputPath + fileName)
    df['agency_psd_start_date'] = pd.to_datetime(df['agency_psd_start_date'])
    df = df.drop(columns = ['reporting_period_name'])      
    return(df) 

def load_child_table_csv(inputPath, fileName,FileType =''):
    df = pd.read_csv(inputPath + fileName, engine='pyarrow', dtype_backend='pyarrow')

    #Check ID to ensure that there is no duplicates?
    df['Duplicate'] = df.duplicated(subset=['f2_child_identifier'],keep=False)
    #drop duplicate records
    #drop duplicates column

    #Set Date of Birth as a Date Type
    #Should/Could be set up to use a pyarrow data type for speed
    df['f3_date_of_birth'] = pd.to_datetime(df['f3_date_of_birth'])
    
    #Set sex as a categorical variable
    values = [1, 2]
    Labels = ['Male', 'Female']
    df['f4_sex'] = df['f4_sex'].map(dict(zip(values, Labels)))

    #Set race/ethn as a categorical variable
    values = [1, 2, 3, 4, 5, 6, 7, 8]
    Labels = ['Hispanic or Latino', 'Multiracial', 'American Indian or Alaskan Native', 'Asian', 'Black or African American','Native Hawaiian or Other Pacific Islander','White','Unknown']
    df['calc_child_race_ethnicity'] = df['calc_child_race_ethnicity'].map(dict(zip(values, Labels)))

    #Create Age at Prevention Plan (numeric and categorical)
    #Should use a standard function for this
    
    #Set race variables as cat?
    #Should use a standard function for this

    return(df) 


def load_plan_table_csv(inputPath, fileName,FileType =''):
    df = pd.read_csv(inputPath + fileName, engine='pyarrow', dtype_backend='pyarrow')
    df = df.drop('calc_child_record_error_flag',axis = 1) 
    df = df.drop('calc_prevention_plan_error_flag',axis = 1) 
    df = df.drop(columns = ['reporting_period_name'])     
    return(df) 

def load_service_table_csv(inputPath, fileName,FileType =''):
    df = pd.read_csv(inputPath + fileName)
    return(df) 

def load_fcentry_table_csv(inputPath, fileName,FileType =''):
    df = pd.read_csv(inputPath + fileName)
    df['f14a_date_of_entry_into_foster_care'] = pd.to_datetime(df['f14a_date_of_entry_into_foster_care'])
    df = df.drop('calc_child_record_error_flag',axis = 1) 
    df = df.drop('calc_prevention_plan_error_flag',axis = 1)    
    #df = df.drop('calc_foster_care_error_flag',axis = 1)
    df = df.drop(columns = ['reporting_period_name'])  
    df = df.dropna(subset=['f14a_date_of_entry_into_foster_care'])
    df['test'] = df.duplicated(subset=['child_record_id','prevention_plan_id','f14a_date_of_entry_into_foster_care'],keep=False)
    #Check if multiple FC for same child on same day?

    return(df) 

# %%
if __name__ == '__main__':
    rootPath = r"C:\\Users\\malcolm.hale\\Non_Sync\\FF pull 122020224"
    inputPath = rootPath + r"\\Input\\"
    outputPath = rootPath + r"\\Output\\"

    StateTableFileNames = r'106_401_in_stl_171118_241118.csv'
    childTableFileNames = r'106_397_in_clq_171118_241118.csv'
    PPTableFileNames = r'106_398_in_ppl_171118_241118.csv'  
    ServiceTableFileNames = r'106_399_in_sl_171118_241118.csv'  
    FCTableFileNames = r'106_400_in_fcl_171118_241118.csv'  
    
    State_df = load_state_table_csv(inputPath=inputPath,fileName=StateTableFileNames)
    Child_df = load_child_table_csv(inputPath=inputPath,fileName=childTableFileNames)
    PreventionPlan_df = load_plan_table_csv(inputPath=inputPath,fileName=PPTableFileNames)
    Services_df = load_service_table_csv(inputPath=inputPath,fileName=ServiceTableFileNames)
    Fostercare_df = load_fcentry_table_csv(inputPath=inputPath,fileName=FCTableFileNames)
    
    #print(Child_df['calc_child_race_ethnicity'].value_counts())
    #print(Child_df['f4_sex'].value_counts())
    #print(Child_df)
    #print(State_df.info())
    #print(Child_df.info())



# %%
