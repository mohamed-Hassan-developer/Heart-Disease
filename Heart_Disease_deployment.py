
import streamlit as st
import pandas as pd
import plotly.express as px

html_title = """<h1 style="color:white;text-align:center;"> <span style="color:red">Heart Disease </span> Risk Factor Exploratory Data Analysis </h1>"""
st.markdown(html_title, unsafe_allow_html=True)
    # Set Title 
st.set_page_config(layout='wide', page_title= 'Heart Disease Risk Factor EDA',page_icon='💔')

page = st.sidebar.radio('Page', ['Home','Dash Board', 'Statistics', 'Dynamic Reports'])

df = pd.read_csv('cleaned_df.csv', index_col= 0)

if page == 'Home':



    # Insert Image
    col1, col2, col3 = st.columns([1,2,1])

    
    col2.image(width=1000,image='https://www.riversidehealthcare.org/sites/default/files/healthcurrents/GettyImages-1344030014.jpg')


    st.header('Dataset Overview')
    col1, col2 = st.columns([2,1])

    col1.dataframe(df,height=1100)

        # Create table of column descriptions
    data = {
        "Column Name": [
            "Gender", "Age", "Age_Segment", "Blood Pressure",
            "Blood_Pressure_Ranges", "High Blood Pressure", "Stress Level",
            "Cholesterol Level", "Low HDL Cholesterol", "High LDL Cholesterol","Exercise Habits","Smoking","Diabetes","Sugar Consumption",
            "Fasting Blood Sugar", "BMI", "BMI categories", "Alcohol Consumption",
            "Sleep Hours", "Sleep_Type", "Triglyceride Level", "trigly_level",
            "CRP Level", "CRP_Group", "Homocysteine Level",
            "Homocysteine_Category", "Family Heart Disease",
            "Heart Disease Status", "Heart Disease Binary"
        ],
        "Description": [
            "Biological sex of the individual",
            "Age in years",
            "Categorized age segment",
            "Systolic blood pressure (mm/Hg)",
            "Blood pressure classification",
            "Whether the person has high BP",
            "Self-reported stress level",
            "Total cholesterol (mg/dL)",
            "Indicates low HDL cholesterol",
            "Indicates High HDL cholesterol",
            "Exercise habits (Low, Medium, High)",
            "Smoker or not (Yes or No)",
            "Diabetes or not (Yes or No)",
            "Daily sugar intake level",
            "Fasting blood glucose level",
            "Body Mass Index",
            "BMI classification",
            "Alcohol consumption level",
            "Average daily sleep duration",
            "Sleep quality category",
            "Triglyceride level (mg/dL)",
            "Triglyceride range classification",
            "C-Reactive Protein level",
            "CRP classification",
            "Homocysteine level",
            "Homocysteine category",
            "Family history of heart disease",
            "Heart disease type/status",
            "Binary heart disease indicator"
        ]
    }

    desc_df = pd.DataFrame(data)

    # Display table
    col2.subheader("📝 Column Descriptions")
    col2.table(desc_df)

elif page == 'Statistics':

    #col1, col2 = st.columns([1,1])

    #with col1:
    cat_col = [
        'Heart Disease Status','Gender','Age_Segment','Blood_Pressure_Ranges',
        'High Blood Pressure','Stress Level','Low HDL Cholesterol','High LDL Cholesterol',
        'Exercise Habits','Smoking','Diabetes','Sugar Consumption','BMI categories',
        'Alcohol Consumption','Sleep_Type','trigly_level','CRP_Group',
        'Homocysteine_Category','Family Heart Disease'
    ]

    st.title("Categorical Analysis for Heart Disease")

    for col in cat_col:
        result = df[df['Heart Disease Status'] == 'Yes'].groupby(col)['Per'].sum().round(2).reset_index().sort_values('Per', ascending=False)
        
        with st.expander(f"📊 {col}"):
            col1, col2 = st.columns([1,1])

            #st.dataframe(result)
            col1.dataframe(result)
            Chart_Type=col1.radio('Chart Type :',options=['Histrogram','Pie'],key=col)
            if Chart_Type=='Histrogram':

                col2.plotly_chart(px.histogram(result, x=col, y='Per',text_auto= True, title=f"{col}"))
            else :
                col2.plotly_chart(px.pie(result, names=col, values='Per', title=f"{col}"))


elif page == 'Dash Board':

    cat_col = [
        'Heart Disease Status','Gender','Age_Segment','Blood_Pressure_Ranges',
        'High Blood Pressure','Stress Level','Low HDL Cholesterol','High LDL Cholesterol',
        'Exercise Habits','Smoking','Diabetes','Sugar Consumption','BMI categories',
        'Alcohol Consumption','Sleep_Type','trigly_level','CRP_Group',
        'Homocysteine_Category','Family Heart Disease'
    ]

    st.title("Categorical Analysis for Heart Disease")

    for col in cat_col:
        result = df[df['Heart Disease Status'] == 'Yes'].groupby(col)['Per'].sum().round(2).reset_index().sort_values('Per', ascending=False)
        
        col1, col2 = st.columns([1,1])
        
        col2.dataframe(result)
        Chart_Type=col2.radio('Chart Type :',options=['Histrogram','Pie'],key=col)

        if Chart_Type=='Histrogram':
            col1.plotly_chart(px.histogram(result, x=col, y='Per',text_auto= True, title=f"{col}"))
        else :
            col1.plotly_chart(px.pie(result, names=col, values='Per', title=f"{col}"))

        
        co1,col2,col3 =st.columns([1,2,1])

        col2.write(f"### 💗 ▂▃▅▇ {col.upper()} ANALYSIS ▇▅▃▂ 💗")
        st.write("-----")


elif page =='Dynamic Reports' :

    col1, col2 = st.columns([3,1])

    All_gender =  ['Choose'] + df.Gender.unique().tolist() 
    Gender = st.sidebar.selectbox('Gender', All_gender)

    age_group=st.sidebar.selectbox('Age Group', ['All Age Groups','Teenager', 'Young Adult','Adult', 'Middle-Aged','Senior'])

    Boold_pressure_ranges =  ['All Ranges'] + ['Normal  [80-120]','Elevated  [120-129]','Stage 1 Hypertension  [130-139]','Stage 2 Hypertension [140 & above]'] 
    
    Boold_pressure_ranges = st.sidebar.selectbox('Blood Pressure Ranges', Boold_pressure_ranges)

    Alcohol_Consumption =  ['All'] +  ['Most likly Never','Low','Medium','High']
    
    Alcohol_Consumption = st.sidebar.selectbox('Alcohol Consumption', Alcohol_Consumption)

    BMI_categories =  ['All Categories'] + ['Underweight','Normal weight','Overweight','Obesity'] 
    
    BMI_categories = st.sidebar.selectbox('BMI categories', BMI_categories)

    CRP_Group =  ['All Groups'] + ['Normal/Low', 'Marked Elevation','Moderate Elevation']
    
    CRP_Group = st.sidebar.selectbox('CRP Group', CRP_Group)    
    
    Homocysteine_Category =  ['All Categories'] + ['Marked Elevation', 'Moderate Elevation','Severe Elevation'] 
    
    Homocysteine_Category = st.sidebar.selectbox('Homocysteine categories', Homocysteine_Category)

    Stress=st.sidebar.radio('Stess Level', options=['All'] + ['Low','Medium','High'],horizontal=True )

    Exercise_Habits=st.sidebar.radio('Exercise Habits', options=['All'] +  ['Low','Medium','High'],horizontal=True )

    Smoker=st.sidebar.radio('Smoker',options=['All','Yes','No'],horizontal=True)

    LDL_Cholesterol=st.sidebar.radio('Cholesterol',options=['All','Yes','No'],horizontal=True)

    Diabetes=st.sidebar.radio('Diabetes',options=['All','Yes','No'],horizontal=True)

    Family_Heart_Disease=st.sidebar.radio('Family Heart History',options=['All','Yes','No'],horizontal=True)

    Sleep=st.sidebar.radio('Sleep Type',options=['Any','Normal', 'Light', 'Deep'],horizontal=True)

    trigly_level = st.sidebar.radio('Triglyceride Level', ['All'] + ['Normal','High','Borderline'],horizontal=True)




    dF_select=col2.multiselect('Data Frame',df.drop(columns=['Per','Heart Disease Status'],axis=1).columns,max_selections=26,default=df.drop(columns=['Per','Heart Disease Status'],axis=1).columns)

    if dF_select != '':

        df_filtered_col = ['Heart Disease Status'] + dF_select

        df_filtered=df[df['Heart Disease Status']=='Yes'].groupby(df_filtered_col)['Per'].sum()
        df_filtered=df_filtered.reset_index().sort_values(by='Per',ascending=False)

    
    if Gender != 'Choose' and 'Gender' in df_filtered_col:

        df_filtered = df_filtered[df_filtered['Gender'] == Gender]

    if Smoker != 'All' and 'Smoking' in df_filtered_col:

        df_filtered = df_filtered[df_filtered['Smoking'] == Smoker]

    if age_group != 'All Age Groups' and 'Age_Segment' in df_filtered_col:

        df_filtered = df_filtered[df_filtered['Age_Segment'] == age_group]

    if Boold_pressure_ranges != 'All Ranges' and 'Blood_Pressure_Ranges' in df_filtered_col:

        df_filtered = df_filtered[df_filtered['Blood_Pressure_Ranges'] == Boold_pressure_ranges]


    if Alcohol_Consumption != 'All' and 'Alcohol Consumption' in df_filtered_col:

        df_filtered = df_filtered[df_filtered['Alcohol Consumption'] == Alcohol_Consumption]       


    if BMI_categories != 'All Categories' and 'BMI categories' in df_filtered_col:

        df_filtered = df_filtered[df_filtered['BMI categories'] == BMI_categories]  

    if CRP_Group != 'All Groups' and 'CRP_Group' in df_filtered_col:

        df_filtered = df_filtered[df_filtered['CRP_Group'] == CRP_Group]  

    if Homocysteine_Category != 'All Categories' and 'Homocysteine_Category' in df_filtered_col:

        df_filtered = df_filtered[df_filtered['Homocysteine_Category'] == Homocysteine_Category]  

    if Stress != 'All' and 'Stress Level' in df_filtered_col:

        df_filtered = df_filtered[df_filtered['Stress Level'] == Stress]  
 
    if Exercise_Habits != 'All' and 'Exercise Habits' in df_filtered_col:

        df_filtered = df_filtered[df_filtered['Exercise Habits'] == Exercise_Habits]     

    if Diabetes != 'All' and 'Diabetes' in df_filtered_col:

        df_filtered = df_filtered[df_filtered['Diabetes'] == Diabetes]  

    if Sleep != 'Any' and 'Sleep_Type' in df_filtered_col:

        df_filtered = df_filtered[df_filtered['Sleep_Type'] == Sleep]  

    if trigly_level != 'All' and 'trigly_level' in df_filtered_col:

        df_filtered = df_filtered[df_filtered['trigly_level'] == trigly_level] 


    if Family_Heart_Disease != 'All' and 'Family Heart Disease' in df_filtered_col:

        df_filtered = df_filtered[df_filtered['Family Heart Disease'] == Family_Heart_Disease] 

    if LDL_Cholesterol != 'All' and 'High LDL Cholesterol' in df_filtered_col:

        df_filtered = df_filtered[df_filtered['High LDL Cholesterol'] == LDL_Cholesterol] 


    if dF_select != '':
        col1.dataframe(df_filtered)
        st.plotly_chart(px.histogram(df_filtered, x=dF_select, y='Per',barmode='overlay',height=600,text_auto= True))
            
    else :
        col1.dataframe(df)



