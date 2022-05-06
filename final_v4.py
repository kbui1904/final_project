#Kiet Bui and Jack Katene
import pandas as pd
import sqlite3
import streamlit as st

st.header("Final project")

#FR-2.13: Connect to the database and extract list of countries in a dataframe

con = sqlite3.connect('ecsel_database.db')
df_countries = pd.read_sql('''SELECT Country, Acronym
FROM countries''', con)

#FR-2.14 + FR-2.15: input country acronym and validate selection

'''country_selected = str(input("Please select your desired country: "))
while country_selected not in df_countries.loc[:,'Acronym'].tolist():
    print("Invalid country")
    country_selected = str(input("Please select your desired country: "))
'''
    
country_selected = st.selectbox('Please choose the country acronym:', df_countries.loc[:,'Acronym'].tolist())


#FR-2.16: Connect to the database and create grants_per_participants dataframe
#FR-2.17: Display the dataframe

con = sqlite3.connect('ecsel_database.db')
df_participants = pd.read_sql('''SELECT shortName, name, activityType, organizationURL, ecContribution, country 
FROM participants
INNER JOIN projects
ON participants.projectID = projects.projectID''', con)

df_filtered = df_participants[df_participants["country"] == country_selected]

df_grants_per_partner = df_filtered.groupby(['country', 'shortName', 'name', 'activityType', 'organizationURL'], as_index=False).agg({'ecContribution': ['count', 'sum']})
df_grants_per_partner = df_grants_per_partner.sort_values([("ecContribution", "sum")], ascending=False)
st.write(df_grants_per_partner)

#FR-2.18: Generate Dataframe with project coordinators from the selected country

con = sqlite3.connect('ecsel_database.db')
df_project_coordinators = pd.read_sql('''SELECT country, shortName, name, activityType, projectAcronym 
FROM participants
WHERE role = 'coordinator'
''', con)

df_project_coordinators = df_project_coordinators[df_project_coordinators["country"] == country_selected]
df_project_coordinators = df_project_coordinators.sort_values(by=['shortName'], ascending=True)
'''df_project_coordinators'''
