import pandas as pd


file="Data.xlsx"

profile_df=pd.read_excel(file,sheet_name="basic")
timeline_df=pd.read_excel(file,sheet_name="timeline")
skills_df=pd.read_excel(file,sheet_name="skills")
certification_df=pd.read_excel(file,sheet_name="certification")
tools_df=pd.read_excel(file,sheet_name="tools&frameworks")
activities_df=pd.read_excel(file,sheet_name="dailyactivities")


def list_to_dict(df,column1,column2):
    return dict(zip(df[column1].tolist(),df[column2].tolist()))

profile_info=list_to_dict(profile_df,"Entity","Values")
skills=list_to_dict(skills_df,"skill","rating")
tools=tools_df["toolname"].tolist()
activities=activities_df["activity"].tolist()
time_spent = [int(x * 60) for x in activities_df["hours"].tolist()]
timeline_info =list(zip(timeline_df["title"],timeline_df["description"]))
