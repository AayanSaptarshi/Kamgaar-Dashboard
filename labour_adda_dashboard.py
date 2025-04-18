# Labour Adda Dashboard (Streamlit version)

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Sample datasets (replace with actual cleaned data)
demo_data = pd.DataFrame({
    'Age Group': ['18-25', '26-35', '36-45', '46-60', '60+'],
    'Male': [120, 150, 100, 70, 30],
    'Female': [80, 90, 60, 40, 20],
    'Married': [100, 130, 120, 100, 50]
})

skill_data = pd.DataFrame({
    'Skill': ['Mason', 'Electrician', 'Painter', 'Welder', 'Unskilled'],
    'Count': [45, 30, 25, 20, 80],
    'Formal Training': [10, 15, 5, 8, 0],
    'Informal Training': [35, 15, 20, 12, 80]
})

income_data = pd.DataFrame({
    'Bracket': ['<₹200', '₹200-400', '₹400-600', '₹600+'],
    'Count': [25, 40, 20, 15]
})

migration_data = pd.DataFrame({
    'City': ['Delhi', 'Mumbai', 'Bangalore', 'Hyderabad'],
    'Willing': [70, 50, 30, 20],
    'Capable': [60, 35, 25, 15]
})

assets_data = pd.DataFrame({
    'Category': ['Productive', 'Household', 'Liquid', 'Debt'],
    'Value': [40, 70, 20, 50]
})

def show_demographics():
    st.subheader("Demographic Snapshot")
    demo_melted = demo_data.melt(id_vars='Age Group', var_name='Category', value_name='Count')
    fig = px.bar(demo_melted, x='Age Group', y='Count', color='Category', barmode='group')
    st.plotly_chart(fig)
    st.write("### Education & Caste Distribution")
    edu_data = pd.DataFrame({'Education': ['None', 'Primary', 'Secondary', 'Graduate'], 'Count': [30, 70, 50, 20]})
    caste_data = pd.DataFrame({'Caste': ['SC', 'ST', 'OBC', 'General'], 'Count': [40, 20, 70, 40]})
    st.plotly_chart(px.pie(edu_data, names='Education', values='Count', title='Education'))
    st.plotly_chart(px.pie(caste_data, names='Caste', values='Count', title='Caste'))


def show_skills():
    st.subheader("Current Skill Mapping")
    fig = px.treemap(skill_data, path=['Skill'], values='Count')
    st.plotly_chart(fig)
    train_data = pd.DataFrame({
        'Type': ['Formal', 'Informal'],
        'Total': [skill_data['Formal Training'].sum(), skill_data['Informal Training'].sum()]
    })
    st.plotly_chart(px.bar(train_data, x='Type', y='Total', title='Training Type'))
    st.write("### Skill vs Income")
    scatter_data = pd.DataFrame({
        'Skill': skill_data['Skill'],
        'Income': [500, 600, 550, 650, 300]
    })
    st.plotly_chart(px.scatter(scatter_data, x='Skill', y='Income', title='Skill vs Income'))


def show_reskilling():
    st.subheader("Reskilling Opportunities")
    reskill = pd.DataFrame({
        'Domain': ['Electrician', 'Driving', 'Tailoring', 'Plumbing'],
        'Interest': [40, 30, 20, 10]
    })
    st.plotly_chart(px.bar(reskill, x='Domain', y='Interest', title='Reskilling Interest'))

    barrier_data = pd.DataFrame({
        'Barrier': ['Cost', 'Time', 'Family Duties', 'Access'],
        'Value': [30, 20, 25, 15]
    })
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(r=barrier_data['Value'], theta=barrier_data['Barrier'], fill='toself'))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True)), showlegend=False, title='Barriers to Reskilling')
    st.plotly_chart(fig)

    age_data = pd.DataFrame({'Age': [20, 30, 40, 50], 'Interest': [90, 60, 40, 20]})
    st.plotly_chart(px.line(age_data, x='Age', y='Interest', title='Age vs Reskilling Interest'))


def show_migration():
    st.subheader("Migration Readiness & Aspiration")
    st.plotly_chart(px.bar(migration_data, x='City', y=['Willing', 'Capable'], barmode='group', title='Willing vs Capable'))

    st.write("### Push/Pull Factors")
    fig = go.Figure(data=[go.Sankey(
        node=dict(label=['Low Income', 'Lack of Work', 'Better Wages', 'Urban Services']),
        link=dict(source=[0, 1], target=[2, 3], value=[60, 40])
    )])
    fig.update_layout(title='Migration Push/Pull Factors')
    st.plotly_chart(fig)


def show_schemes():
    st.subheader("Government Schemes Awareness")
    schemes = pd.DataFrame({
        'Scheme': ['PM-SYM', 'PMRPY', 'Ayushman Bharat', 'Old Age Pension'],
        'Aware': [60, 40, 55, 35],
        'Enrolled': [30, 20, 25, 15],
        'Accessed': [15, 10, 20, 5]
    })
    st.plotly_chart(px.bar(schemes.melt(id_vars='Scheme'), x='Scheme', y='value', color='variable', barmode='group'))
    st.write("### Most Valued Schemes")
    valued = pd.DataFrame({'Scheme': ['Ayushman', 'PM-SYM', 'Pension'], 'Votes': [30, 25, 20]})
    st.plotly_chart(px.bar(valued, x='Scheme', y='Votes', title='Most Valued Schemes'))


def show_facilities():
    st.subheader("Facilities at Labour Addas")
    facilities = pd.DataFrame({
        'Facility': ['Toilets', 'Water', 'Shelter', 'Medical', 'Security'],
        'Availability (%)': [60, 75, 30, 45, 50]
    })
    st.plotly_chart(px.bar(facilities, x='Facility', y='Availability (%)', title='Civic Facilities'))


def show_income():
    st.subheader("Income & Productivity")
    income = pd.DataFrame({
        'Source': ['Wages', 'Agriculture', 'Self-business'],
        'Monthly': [8500, 4500, 7000]
    })
    st.plotly_chart(px.bar(income, x='Source', y='Monthly', title='Income by Source'))

    product = pd.DataFrame({
        'Skill': ['Mason', 'Electrician', 'Painter'],
        'Productivity Score': [70, 80, 65]
    })
    st.plotly_chart(px.bar(product, x='Skill', y='Productivity Score', title='Productivity by Skill'))

    mult_income = pd.DataFrame({
        'Source': ['Wages', 'Wages+Agri', 'Wages+Biz'],
        'Monthly': [8500, 9500, 10000],
        'Diversity Score': [1, 2, 2]
    })
    fig = px.bar(mult_income, x='Source', y='Monthly', title='Income vs Diversification')
    fig.add_scatter(x=mult_income['Source'], y=mult_income['Diversity Score'], mode='lines+markers', name='Diversity')
    st.plotly_chart(fig)


def show_assets():
    st.subheader("Assets & Liabilities Overview")
    st.plotly_chart(px.treemap(assets_data, path=['Category'], values='Value', title='Assets Overview'))
    st.write("### Liabilities")
    liabilities = pd.DataFrame({
        'Type': ['Health', 'Education', 'Housing', 'Social'],
        'Count': [20, 15, 30, 10]
    })
    st.plotly_chart(px.bar(liabilities, x='Type', y='Count', title='Liability Reasons'))
    gauge = go.Figure(go.Indicator(mode="gauge+number", value=65, title={"text": "% Households with Debt"}, gauge={"axis": {"range": [0, 100]}}))
    st.plotly_chart(gauge)


def show_vulnerability():
    st.subheader("Livelihood Vulnerability Scoreboard")
    radar = go.Figure()
    radar.add_trace(go.Scatterpolar(r=[65, 70, 55, 60, 50], theta=['Skill', 'Assets', 'Income', 'Migration', 'Schemes'], fill='toself'))
    radar.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0,100])), showlegend=False)
    st.plotly_chart(radar)

# UI setup
st.title("🧩 Labour Adda Unified Dashboard - Uttar Pradesh")
st.sidebar.title("Dashboard Sections")
section = st.sidebar.radio("Select a section:", [
    "Demographics", "Skill Mapping", "Reskilling", "Migration", "Scheme Awareness",
    "Facilities", "Income & Productivity", "Assets & Liabilities", "Vulnerability Score"
])

if section == "Demographics":
    show_demographics()
elif section == "Skill Mapping":
    show_skills()
elif section == "Reskilling":
    show_reskilling()
elif section == "Migration":
    show_migration()
elif section == "Scheme Awareness":
    show_schemes()
elif section == "Facilities":
    show_facilities()
elif section == "Income & Productivity":
    show_income()
elif section == "Assets & Liabilities":
    show_assets()
elif section == "Vulnerability Score":
    show_vulnerability()
