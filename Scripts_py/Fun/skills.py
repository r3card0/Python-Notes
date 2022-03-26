proficiency = {
    "1 ✅" : "3+ years working experience with Spatial Data",
    "2 ✅" : "Master's or Bachelor degree in GIS, Mathematics, Engineering",
    "3 ✅" : "Advanced working SQL knowledge and experience working with relational databases",
    "4 ✅" : "Intermediate programming skills in Python",
    "5 ✅" : "Knowledge of GIS tools (i.e. ArcGIS ,FME)",
    "6 ✅" : "Basic knowledge of UNIX/Linux",
    "7 🔜" : "Experience with AWS services (EMR, Lambda, Athena, EC2, RDS)",
    "8 🔜" : "GitLab, Tableau is a plus",
    "9 🔜" : "Knowledge of data mining and analytics methods",
    "10🔜" : "Ability to connect data using Web API or REST API"
}

for skill, description in proficiency.items():
    print(skill, ":", description)