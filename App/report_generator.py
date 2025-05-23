from fpdf import FPDF
import database

def generate_pdf_report(case_id):
    case = database.read_documents(database.court_cases, {"_id": case_id})[0]
    trial = database.read_documents(database.court_trials, {"_id": case["trial_id"]})[0]
    record = database.read_documents(database.crime_records, {"case_id": case_id})[0]
    criminal = database.read_documents(database.criminals, {"_id": record["criminal_id"]})[0]
    crime = database.read_documents(database.crimes, {"_id": record["crime_id"]})[0]
    prison = database.read_documents(database.prisons, {"_id": trial["prison_id"]})[0]

    # Fetch all victims and witnesses
    victims = [database.read_documents(database.victims, {"_id": vid})[0] for vid in case["victims"]]
    witnesses = [database.read_documents(database.witnesses, {"_id": wid})[0] for wid in case["witnesses"]]

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Case Report", ln=True, align='C')
    pdf.ln(5)

    # Basic Info
    pdf.cell(200, 10, txt=f"Case ID: {case_id}", ln=True)
    pdf.cell(200, 10, txt=f"Crime Type: {crime['crime_type']} ({crime['section_of_law']})", ln=True)
    pdf.cell(200, 10, txt=f"Status: {case['case_status']}", ln=True)
    pdf.cell(200, 10, txt=f"Verdict: {trial['verdict']}, Sentence: {trial['sentence_years']} years", ln=True)
    pdf.cell(200, 10, txt=f"Trial Date: {trial['trial_date']}", ln=True)
    pdf.cell(200, 10, txt=f"Prison: {prison['prison_name']} ({prison['location']})", ln=True)
    pdf.ln(5)

    # Criminal Info
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, txt="Criminal Details:", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.cell(200, 10, txt=f"Name: {criminal['name']}, Gender: {criminal['gender']}, DOB: {criminal['dob']}, Address: {criminal['address']}", ln=True)
    pdf.ln(5)

    # Victims Info
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, txt="Victims Involved:", ln=True)
    pdf.set_font("Arial", "", 12)
    for v in victims:
        pdf.cell(200, 10, txt=f"- {v['name']} | Gender: {v['gender']} | DOB: {v['dob']} | Address: {v['address']}", ln=True)
    pdf.ln(5)

    # Witnesses Info
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, txt="Witnesses Involved:", ln=True)
    pdf.set_font("Arial", "", 12)
    for w in witnesses:
        pdf.cell(200, 10, txt=f"- {w['name']} | Gender: {w['gender']} | DOB: {w['dob']} | Address: {w['address']}", ln=True)
    pdf.ln(5)

    # Description and Evidence
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, txt="Case Description:", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10, txt=case.get("case_description", "No description provided."))
    pdf.ln(5)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, txt="Evidences:", ln=True)
    pdf.set_font("Arial", "", 12)
    for ev in case.get("evidences", []):
        pdf.cell(200, 10, txt=f"- {ev}", ln=True)

    # Save the PDF
    pdf.output(f"{case_id}_report.pdf")
    print(f"{case_id}_report.pdf generated successfully.")
