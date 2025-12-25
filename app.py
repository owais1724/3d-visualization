import streamlit as st
import pandas as pd

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="3D In-Vitro Lead Qualification Dashboard",
    layout="wide"
)

# -----------------------------
# Custom Dark Styling
# -----------------------------
st.markdown("""
<style>
    .block-container {
        padding-top: 2rem;
    }
    h1 {
        font-size: 42px;
        font-weight: 800;
    }
    .subtitle {
        font-size: 16px;
        color: #b3b3b3;
        margin-bottom: 25px;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Title
# -----------------------------
st.title("3D In-Vitro Lead Qualification Dashboard")
st.markdown(
    '<div class="subtitle">'
    'This dashboard identifies, enriches, and ranks life-science professionals '
    'based on their probability of working with 3D in-vitro models.'
    '</div>',
    unsafe_allow_html=True
)

# -----------------------------
# Mock Final Output Data
# -----------------------------
data = [
    [1, 100, "Dr John Smith", "Director of Toxicology", "ABC Biotech", "Boston", "Cambridge MA", "Remote", "dr.john@abcbiotech.com"],
    [2, 100, "Dr Michael Brown", "VP Preclinical Safety", "OncoNova", "Bay Area", "Bay Area", "Onsite", "dr.michael@onconova.com"],
    [3, 100, "Dr Priya Nair", "Head of Translational Safety", "GenovaBio", "Cambridge MA", "Cambridge MA", "Onsite", "dr.priya@genovabio.com"],
    [4, 100, "Dr Andreas Müller", "Director of Investigative Toxicology", "BioHelix", "Munich", "Basel", "Remote", "dr.andreas@biohelix.eu"],
    [5, 100, "Dr Robert Wilson", "Director of Safety Pharmacology", "CardioLife", "Boston", "Boston", "Onsite", "dr.robert@cardiolife.com"],
    [6, 65, "Dr Emily Chen", "Head of Safety Assessment", "NeoPharma", "Basel", "Basel", "Onsite", "dr.emily@neopharma.com"],
    [7, 35, "Dr Laura Martinez", "Senior Toxicologist", "HepatoTech", "San Diego", "San Diego", "Onsite", "dr.laura@hepatotech.com"],
    [8, 15, "Dr Sarah Patel", "Principal Scientist", "TheraGen", "London", "UK Golden Triangle", "Remote", "dr.sarah@theragen.co"],
    [9, 0, "Jane Doe", "Junior Scientist", "StartupX", "Texas", "San Diego", "Remote", "jane.doe@startupx.io"],
    [10, 0, "Dr Kevin Lee", "Scientist", "EarlyBio", "Toronto", "Toronto", "Onsite", "dr.kevin@earlybio.ai"],
]

columns = [
    "rank",
    "probability_score",
    "name",
    "title",
    "company",
    "person_location",
    "company_hq",
    "work_mode",
    "email"
]

df = pd.DataFrame(data, columns=columns)

# -----------------------------
# Display Table
# -----------------------------
st.dataframe(
    df,
    use_container_width=True,
    hide_index=True,
    height=420
)

# -----------------------------
# Download Button
# -----------------------------
st.download_button(
    label="📥 Download Qualified Leads (CSV)",
    data=df.to_csv(index=False),
    file_name="qualified_3d_invitro_leads.csv",
    mime="text/csv"
)
