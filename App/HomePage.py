import tkinter as tk
from tkinter import messagebox, ttk
import database 
from report_generator import generate_pdf_report 
import datetime
import main

class HomePage:
    def __init__(self, root, user):
        self.root = root
        self.user = user
        self.root.title("Criminal Records System - Home")
        self.root.geometry("1000x600")
        self.root.configure(bg="#f0f2f5")

        self.topbar()
        self.sidebar()
        self.main_frame = tk.Frame(self.root, bg="white")
        self.main_frame.pack(side="right", expand=True, fill="both")

    def topbar(self):
        top = tk.Frame(self.root, bg="#2e3f4f", height=50)
        top.pack(fill="x", side="top")

        tk.Label(top, text="Criminal Records Dashboard", font=("Helvetica", 16), bg="#2e3f4f", fg="white").pack(side="left", padx=20)
        tk.Button(top, text=f"{self.user}", command= self.show_profile_or_logout ).pack(side="right", padx=20)

    def sidebar(self):
        side = tk.Frame(self.root, bg="#3b4c5a", width=200)
        side.pack(side="left", fill="y")

        buttons = [
            ("View Database", self.see_database),
            ("Update Case Status", self.update_case_status),
            ("Criminals by Crime", self.criminals_by_crime),
            ("Cases by Station", self.cases_by_station),
            ("Cases Handled by Investigator", self.cases_handled_by_investigator),
            ("Repeat Offenders", self.repeat_offenders),
            ("Ongoing Trials", self.ongoing_trials),
            ("Victims in a Case", self.victims_in_case),
            ("Generate Case Report (PDF)", self.generate_report),
            ("Get Full Case Timeline", self.get_case_timeline)
        ]

        for (label, cmd) in buttons:
            tk.Button(side, text=label, command=cmd, bg="#3b4c5a", fg="white", relief="flat").pack(fill="x", pady=2, padx=5)

    def clear_main(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_profile(self):
        self.clear_main()
        # Assume 'current_user' is stored globally or passed
        profile = database.read_documents(database.users, {"username": f"{self.user}"})[0]
        tk.Label(self.main_frame, text="Your Profile", font=("Arial", 16), bg="white").pack(pady=10)
        for key, value in profile.items():
            tk.Label(self.main_frame, text=f"{key}: {value}", bg="white").pack(anchor="w", padx=20)

    # Each function below should be defined with appropriate database queries

    def see_database(self):
        # Clear current frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        notebook = ttk.Notebook(self.main_frame)
        notebook.pack(fill="both", expand=True)

        # Define your collections and labels
        collections = {
            "Criminals": database.criminals,
            "Crimes": database.crimes,
            "Stations": database.stations,
            "Prisons": database.prisons,
            "Crime Records": database.crime_records,
            "Investigators": database.investigator,
            "Victims": database.victims,
            "Witnesses": database.witnesses,
            "Court Cases": database.court_cases,
            "Court Trials": database.court_trials
        }
        self.collections = collections

        for tab_name, collection in collections.items():
            tab_frame = ttk.Frame(notebook)
            notebook.add(tab_frame, text=tab_name)
            self.populate_tab(tab_frame, collection)

    def update_case_status(self):
        popup = tk.Toplevel(self.root)
        popup.title("Update Case Status")
        popup.geometry("400x400")

        tk.Label(popup, text="Enter Case ID:", font=('Arial', 12)).pack(pady=5)
        case_id_entry = tk.Entry(popup, width=30)
        case_id_entry.pack(pady=5)

        status_options = ["In Trial", "Closed", "Awaiting Evidence", "Pending Investigation", "Under Review"]
        tk.Label(popup, text="Select New Status:", font=('Arial', 12)).pack(pady=5)
        status_var = tk.StringVar(popup)
        status_var.set(status_options[0])
        status_dropdown = tk.OptionMenu(popup, status_var, *status_options)
        status_dropdown.pack(pady=5)

        output_frame = tk.Frame(popup)
        output_frame.pack(pady=10, fill='both', expand=True)

        def fetch_case_data():
            for widget in output_frame.winfo_children():
                widget.destroy()

            case_id = case_id_entry.get()
            case = database.read_documents(database.court_cases, {"_id": case_id})
            if not case:
                tk.Label(output_frame, text="No case found with this ID.", fg='red').pack()
                return

            case = case[0]
            for key, value in case.items():
                tk.Label(output_frame, text=f"{key}: {value}", anchor='w').pack(fill='x')

        def update_status():
            case_id = case_id_entry.get()
            new_status = status_var.get()

            result = database.update_document(
                database.court_cases,
                {"_id": case_id},
                {"$set": {"case_status": new_status}}
            )

            if result.modified_count > 0:
                messagebox.showinfo("Success", f"Status updated to '{new_status}' for case {case_id}.")
                fetch_case_data()
            else:
                messagebox.showerror("Error", f"Update failed or no change for case {case_id}.")

        tk.Button(popup, text="View Case Details", command=fetch_case_data).pack(pady=5)
        tk.Button(popup, text="Update Status", command=update_status, bg='green', fg='white').pack(pady=10)

    def criminals_by_crime(self):
        popup = tk.Toplevel(self.root)
        popup.title("Criminals by Crime")
        popup.geometry("600x500")

        tk.Label(popup, text="Enter Crime ID:", font=('Arial', 12)).pack(pady=5)
        crime_id_entry = tk.Entry(popup, width=30)
        crime_id_entry.pack(pady=5)

        # === Scrollable result frame ===
        container = tk.Frame(popup)
        canvas = tk.Canvas(container, borderwidth=0)
        scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        container.pack(fill="both", expand=True)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        def fetch_criminals():
            for widget in scrollable_frame.winfo_children():
                widget.destroy()

            crime_id = crime_id_entry.get().strip()
            
            # Fetch and display crime details
            crime = database.read_documents(database.crimes, {"_id": crime_id})
            if not crime:
                tk.Label(scrollable_frame, text="No crime found with this ID.", fg='red').pack(pady=5)
                return
            
            tk.Label(scrollable_frame, text="Crime Details", font=('Arial', 12, 'bold')).pack(pady=5)
            for key, val in crime[0].items():
                tk.Label(scrollable_frame, text=f"{key}: {val}", anchor='w').pack(fill='x')

            # Fetch crime_records with that crime_id
            records = database.read_documents(database.crime_records, {"crime_id": crime_id})
            if not records:
                tk.Label(scrollable_frame, text="No crime records found for this crime.", fg='red').pack(pady=5)
                return
            
            criminal_ids = [r["criminal_id"] for r in records]

            # Fetch and display criminal details
            criminals = database.read_documents(database.criminals, {"_id": {"$in": criminal_ids}})
            if not criminals:
                tk.Label(scrollable_frame, text="No criminals found for this crime.", fg='red').pack(pady=5)
                return

            tk.Label(scrollable_frame, text="\nCriminals Involved", font=('Arial', 12, 'bold')).pack(pady=5)
            for c in criminals:
                frame = tk.LabelFrame(scrollable_frame, text=f"Criminal ID: {c.get('_id', 'N/A')}", padx=10, pady=5)
                frame.pack(fill="x", padx=10, pady=5)
                for key, val in c.items():
                    tk.Label(frame, text=f"{key}: {val}", anchor='w').pack(fill='x')

        tk.Button(popup, text="Search", command=fetch_criminals).pack(pady=10)


    def cases_by_station(self):
        def fetch_cases():
            station_id = entry.get()
            station = database.read_documents(database.stations, {"_id": station_id})
            if not station:
                messagebox.showerror("Error", "Station not found.")
                return

            station = station[0]

            for widget in output_frame.winfo_children():
                widget.destroy()

            # Display Station Info
            tk.Label(output_frame, text="Station Details", font=("Arial", 12, "bold")).pack(anchor='w')
            tk.Label(output_frame, text=f"ID: {station['_id']}").pack(anchor='w')
            tk.Label(output_frame, text=f"Name: {station['station_name']}").pack(anchor='w')
            tk.Label(output_frame, text=f"Location: {station['location']}").pack(anchor='w')
            ttk.Separator(output_frame, orient='horizontal').pack(fill='x', pady=5)

            # Get all case_ids from crime_records linked to this station
            records = database.read_documents(database.crime_records, {"station_id": station_id})
            if not records:
                tk.Label(output_frame, text="No crime records found for this station.").pack()
                return

            case_ids = [r["case_id"] for r in records]
            cases = database.read_documents(database.court_cases, {"_id": {"$in": case_ids}})

            if not cases:
                tk.Label(output_frame, text="No court cases found for this station.").pack()
                return

            tk.Label(output_frame, text="Cases Filed in This Station:", font=("Arial", 12, "bold")).pack(anchor='w')

            for case in cases:
                frame = tk.Frame(output_frame, bd=1, relief="solid", padx=5, pady=5)
                frame.pack(fill='x', padx=5, pady=3)

                tk.Label(frame, text=f"Case ID: {case['_id']}").pack(anchor='w')
                tk.Label(frame, text=f"Status: {case['case_status']}").pack(anchor='w')
                tk.Label(frame, text=f"Victims: {', '.join(case.get('victims', []))}").pack(anchor='w')
                tk.Label(frame, text=f"Witnesses: {', '.join(case.get('witnesses', []))}").pack(anchor='w')
                tk.Label(frame, text=f"Description: {case.get('case_description', 'N/A')}").pack(anchor='w')

        # Popup setup
        popup = tk.Toplevel()
        popup.title("Cases by Police Station")
        popup.geometry("500x500")

        tk.Label(popup, text="Enter Station ID:").pack(pady=5)
        entry = tk.Entry(popup)
        entry.pack(pady=5)
        tk.Button(popup, text="Search", command=fetch_cases).pack(pady=5)

        # Scrollable frame
        canvas = tk.Canvas(popup)
        scrollbar = ttk.Scrollbar(popup, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        output_frame = scrollable_frame

    def cases_handled_by_investigator(self):
        popup = tk.Toplevel(self.root)
        popup.title("Cases by Investigator")
        popup.geometry("650x500")

        tk.Label(popup, text="Enter Investigator ID:", font=('Arial', 12)).pack(pady=5)
        investigator_entry = tk.Entry(popup, width=30)
        investigator_entry.pack(pady=5)

        # === Scrollable view ===
        container = tk.Frame(popup)
        canvas = tk.Canvas(container)
        scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        container.pack(fill="both", expand=True)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        def fetch_cases():
            for widget in scrollable_frame.winfo_children():
                widget.destroy()

            inv_id = investigator_entry.get().strip()

            investigator = database.read_documents(database.investigator, {"_id": inv_id})
            if not investigator:
                tk.Label(scrollable_frame, text="No investigator found with this ID.", fg='red').pack()
                return

            tk.Label(scrollable_frame, text="Investigator Details", font=('Arial', 12, 'bold')).pack(pady=5)
            for key, val in investigator[0].items():
                tk.Label(scrollable_frame, text=f"{key}: {val}", anchor='w').pack(fill='x')

            # === Fetch cases handled by investigator ===
            cases = database.read_documents(database.court_cases, {"inv_id": inv_id})
            if not cases:
                tk.Label(scrollable_frame, text="No cases handled by this investigator.", fg='red').pack(pady=10)
                return

            tk.Label(scrollable_frame, text="\nCases Handled", font=('Arial', 12, 'bold')).pack(pady=5)
            for case in cases:
                case_box = tk.LabelFrame(scrollable_frame, text=f"Case ID: {case.get('_id', 'N/A')}", padx=10, pady=5)
                case_box.pack(fill="x", padx=10, pady=5)
                for key, val in case.items():
                    tk.Label(case_box, text=f"{key}: {val}", anchor='w').pack(fill='x')

        tk.Button(popup, text="Search", command=fetch_cases).pack(pady=10)


    def repeat_offenders(self):
        def show_repeat_offenders():
            for widget in output_frame.winfo_children():
                widget.destroy()

            # Aggregate count of crimes per criminal
            pipeline = [
                {"$group": {"_id": "$criminal_id", "crime_count": {"$sum": 1}}},
                {"$match": {"crime_count": {"$gt": 1}}}
            ]
            repeated_criminals = list(database.crime_records.aggregate(pipeline))

            if not repeated_criminals:
                tk.Label(output_frame, text="No repeat offenders found.").pack()
                return

            tk.Label(output_frame, text="Repeat Offenders", font=("Arial", 12, "bold")).pack(anchor='w', pady=5)

            for item in repeated_criminals:
                criminal_id = item['_id']
                crime_count = item['crime_count']
                criminal = database.read_documents(database.criminals, {"_id": criminal_id})
                if not criminal:
                    continue
                criminal = criminal[0]

                frame = tk.Frame(output_frame, bd=1, relief="solid", padx=5, pady=5)
                frame.pack(fill='x', padx=5, pady=5)

                tk.Label(frame, text=f"Name: {criminal['name']}", font=("Arial", 10, "bold")).pack(anchor='w')
                tk.Label(frame, text=f"ID: {criminal['_id']}").pack(anchor='w')
                tk.Label(frame, text=f"Gender: {criminal['gender']}").pack(anchor='w')
                tk.Label(frame, text=f"DOB: {str(criminal['dob'])[:10]}").pack(anchor='w')
                tk.Label(frame, text=f"Address: {criminal['address']}").pack(anchor='w')
                tk.Label(frame, text=f"Number of Crimes: {crime_count}", fg="red").pack(anchor='w')

                tk.Label(frame, text="Crimes Committed:", font=("Arial", 9, "bold")).pack(anchor='w', pady=(5, 0))

                records = database.read_documents(database.crime_records, {"criminal_id": criminal_id})
                for rec in records:
                    crime = database.read_documents(database.crimes, {"_id": rec["crime_id"]})
                    if crime:
                        crime = crime[0]
                        tk.Label(frame, text=f"• {crime['crime_type']} ({crime['section_of_law']})").pack(anchor='w')

        # Popup UI
        popup = tk.Toplevel()
        popup.title("Repeat Offenders")
        popup.geometry("550x600")

        # Scrollable output
        canvas = tk.Canvas(popup)
        scrollbar = ttk.Scrollbar(popup, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        output_frame = scrollable_frame
        show_repeat_offenders()

    def ongoing_trials(self):
        popup = tk.Toplevel(self.root)
        popup.title("Ongoing Trials")
        popup.geometry("700x500")

        container = tk.Frame(popup)
        canvas = tk.Canvas(container)
        scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        container.pack(fill="both", expand=True)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        ongoing_status = ["Pending", "Ongoing"] 
        trials = database.read_documents(database.court_trials, {"verdict": {"$in": ongoing_status}})

        if not trials:
            tk.Label(scrollable_frame, text="No ongoing trials found.", fg='red').pack(pady=10)
            return

        tk.Label(scrollable_frame, text="Ongoing Trials", font=('Arial', 14, 'bold')).pack(pady=10)

        for trial in trials:
            trial_box = tk.LabelFrame(scrollable_frame, text=f"Trial ID: {trial.get('_id', 'N/A')}", padx=10, pady=5)
            trial_box.pack(fill="x", padx=10, pady=5)

            for key, val in trial.items():
                tk.Label(trial_box, text=f"{key}: {val}", anchor='w').pack(fill='x')

            linked_cases = database.read_documents(database.court_cases, {"trial_id": trial["_id"]})
            if linked_cases:
                case = linked_cases[0]
                tk.Label(trial_box, text="\nRelated Case Info", font=('Arial', 10, 'bold')).pack(anchor='w')
                for k, v in case.items():
                    tk.Label(trial_box, text=f"{k}: {v}", anchor='w').pack(fill='x')


    
    def victims_in_case(self):
        popup = tk.Toplevel(self.root)
        popup.title("Victims in a Case")
        popup.geometry("700x500")

        tk.Label(popup, text="Enter Case ID:", font=("Arial", 12)).pack(pady=10)
        case_id_entry = tk.Entry(popup, width=40)
        case_id_entry.pack(pady=5)

        result_container = tk.Frame(popup)
        result_container.pack(fill="both", expand=True)

        def fetch_victims():
            case_id = case_id_entry.get().strip()
            if not case_id:
                messagebox.showwarning("Input Error", "Please enter a valid Case ID.")
                return

            # Clear previous results
            for widget in result_container.winfo_children():
                widget.destroy()

            try:
                case = database.read_documents(database.court_cases, {"_id": case_id})[0]
                victim_ids = case.get("victims", [])
            except (IndexError, KeyError):
                messagebox.showerror("Not Found", "No data found for the given Case ID.")
                return

            # === Case Summary ===
            summary_frame = tk.Frame(result_container)
            summary_frame.pack(pady=10, fill="x")

            tk.Label(summary_frame, text=f"Case ID: {case_id}", font=("Arial", 10, "bold")).pack(anchor="w")
            tk.Label(summary_frame, text=f"Status: {case.get('case_status', 'N/A')}", anchor="w").pack(anchor="w")
            tk.Label(summary_frame, text=f"Description: {case.get('case_description', 'N/A')}", anchor="w", wraplength=600).pack(anchor="w")

            # === Scrollable Victim List ===
            canvas = tk.Canvas(result_container)
            scrollbar = ttk.Scrollbar(result_container, orient="vertical", command=canvas.yview)
            scroll_frame = tk.Frame(canvas)

            scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
            canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)

            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")

            if not victim_ids:
                tk.Label(scroll_frame, text="No victims linked to this case.").pack(pady=10)
                return

            for vid in victim_ids:
                try:
                    victim = database.read_documents(database.victims, {"_id": vid})[0]
                    frame = tk.LabelFrame(scroll_frame, text=f"Victim ID: {vid}", padx=10, pady=5)
                    frame.pack(fill="x", padx=10, pady=5)
                    for key, val in victim.items():
                        tk.Label(frame, text=f"{key}: {val}", anchor="w", justify="left").pack(fill="x")
                except IndexError:
                    continue

        tk.Button(popup, text="Fetch Victims", command=fetch_victims).pack(pady=10)


    
    def generate_report(self):
        self.clear_main()
        tk.Label(self.main_frame, text="Generate Case Report", font=("Arial", 16), bg="white").pack(pady=10)

        tk.Label(self.main_frame, text="Enter Case ID:", bg="white").pack()
        case_id_entry = tk.Entry(self.main_frame)
        case_id_entry.pack()

        def generate():
            case_id = case_id_entry.get()
            if not case_id:
                messagebox.showerror("Error", "Case ID is required.")
                return
            generate_pdf_report(case_id)
            messagebox.showinfo("Success", "PDF Report Generated.")

        tk.Button(self.main_frame, text="Generate", command=generate).pack(pady=10)

    def get_case_timeline(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        tk.Label(self.main_frame, text="Enter Case ID:", font=("Arial", 12)).pack(pady=10)
        case_id_entry = tk.Entry(self.main_frame, width=40)
        case_id_entry.pack(pady=5)

        def fetch_timeline():
            # Clear previous timeline if any
            for widget in self.main_frame.winfo_children():
                if isinstance(widget, tk.Frame) or isinstance(widget, tk.Canvas):
                    widget.destroy()

            case_id = case_id_entry.get().strip()
            if not case_id:
                messagebox.showwarning("Input Error", "Please enter a Case ID.")
                return

            try:
                record = database.read_documents(database.crime_records, {"case_id": case_id})[0]
                case = database.read_documents(database.court_cases, {"_id": case_id})[0]
                trial = database.read_documents(database.court_trials, {"_id": case["trial_id"]})[0]

                station = record.get("station_id", "Unknown")
                station = database.read_documents(database.stations, {"_id": station})[0]
                station = station.get("station_name","Unknown")
                entry_date = record.get("entry_date", "Unknown")
                if isinstance(entry_date, dict) and "$date" in entry_date:
                    entry_date = entry_date["$date"].split("T")[0]
                elif isinstance(entry_date, datetime.datetime):
                    entry_date = entry_date.strftime("%Y-%m-%d")

                trial_date = trial.get("trial_date", "Unknown")
                if isinstance(trial_date, dict) and "$date" in trial_date:
                    trial_date = trial_date["$date"].split("T")[0]
                elif isinstance(trial_date, datetime.datetime):
                    trial_date = trial_date.strftime("%Y-%m-%d")

            except IndexError:
                messagebox.showerror("Not Found", "No records found for this Case ID.")
                return

            # Scrollable Frame Setup
            timeline_canvas = tk.Canvas(self.main_frame, height=400)
            timeline_scrollbar = ttk.Scrollbar(self.main_frame, orient="vertical", command=timeline_canvas.yview)
            scrollable_timeline = tk.Frame(timeline_canvas)

            scrollable_timeline.bind(
                "<Configure>",
                lambda e: timeline_canvas.configure(scrollregion=timeline_canvas.bbox("all"))
            )

            timeline_canvas.create_window((0, 0), window=scrollable_timeline, anchor="nw")
            timeline_canvas.configure(yscrollcommand=timeline_scrollbar.set)

            timeline_canvas.pack(side="left", fill="both", expand=True)
            timeline_scrollbar.pack(side="right", fill="y")

            # Timeline Content
            steps = [
                ("Crime Reported", f"Station: {station}\nEntry Date: {entry_date}"),
                ("Arrest & Case Registered", f"Status: {case.get('case_status', 'N/A')}\nDescription: {case.get('case_description', 'N/A')}"),
                ("Court Proceedings", f"Evidence: {case.get('evidences', 'N/A')}"),
                ("Verdict", f"Verdict: {trial.get('verdict', 'N/A')}\nSentence: {trial.get('sentence_years', 'N/A')} years\nTrial Date: {trial_date}")
            ]

            for step, detail in steps:
                box = tk.LabelFrame(scrollable_timeline, text=step, padx=10, pady=10, font=("Arial", 10, "bold"))
                box.pack(fill="x", pady=5, padx=10)
                tk.Label(box, text=detail, anchor="w", justify="left").pack(fill="x")

        tk.Button(self.main_frame, text="Get Timeline", command=fetch_timeline).pack(pady=10)


    def populate_tab(self, tab_frame, collection):
        documents = database.read_documents(collection)

        if not documents:
            tk.Label(tab_frame, text="No records found.").pack()
            return

        columns = list(documents[0].keys())

        # Button Frame
        button_frame = tk.Frame(tab_frame)
        button_frame.pack(pady=5)

        # Add Record Button
        tk.Button(button_frame, text="Add Record", command=lambda: self.add_record_popup(collection, columns)).pack(side="left", padx=5)

        # Delete Record Button
        tk.Button(button_frame, text="Delete Selected", command=lambda: self.delete_selected_record(tree, collection, columns)).pack(side="left", padx=5)

        # Update Record Button
        tk.Button(button_frame, text="Update Selected", command=lambda: self.update_selected_record(tree, collection, columns)).pack(side="left", padx=5)

        # Treeview
        tree = ttk.Treeview(tab_frame, columns=columns, show="headings", height=15)
        tree.pack(fill="both", expand=True)

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor='center')

        for doc in documents:
            values = []
            for col in columns:
                val = doc.get(col, "")
                if isinstance(val, datetime.datetime):
                    val = val.strftime("%Y-%m-%d")
                elif isinstance(val, dict) and "$date" in val:
                    val = val["$date"].split("T")[0]
                values.append(str(val))
            tree.insert("", "end", values=values)


    def add_record_popup(self, collection, fields):
        popup = tk.Toplevel(self.root)
        popup.title("Add Record")
        popup.geometry("400x500")

        entries = {}

        for field in fields:

            tk.Label(popup, text=field).pack(pady=2)
            entry = tk.Entry(popup, width=40)
            entry.pack(pady=2)
            entries[field] = entry

        def submit():
            new_doc = {}
            for field, entry in entries.items():
                value = entry.get().strip()
                if value == "":
                    continue
                # Basic type conversion for known fields
                if "date" in field.lower():   
                    try:
                        value = datetime.datetime.strptime(value, "%Y-%m-%d")
                    except ValueError:
                        messagebox.showerror("Invalid Date", f"Please enter a valid date in YYYY-MM-DD format for '{field}'.")
                        return
                new_doc[field] = value

            # Insert into DB
            database.create_document(collection, new_doc)
            messagebox.showinfo("Success", "Record added successfully!")
            popup.destroy()
            self.see_database()  # Refresh view

        tk.Button(popup, text="Submit", command=submit).pack(pady=20)

    def delete_selected_record(self, tree, collection, columns):
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a record to delete.")
            return

        values = tree.item(selected_item)['values']
        record_id = values[columns.index("_id")]

        if messagebox.askyesno("Confirm", f"Are you sure you want to delete record with _id = {record_id}?"):
            result = database.delete_document(collection, record_id)
            print(result)
            messagebox.showinfo("Deleted", "Record deleted successfully!")
            self.see_database()

    def update_selected_record(self, tree, collection, columns):
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a record to update.")
            return

        values = tree.item(selected_item)['values']
        current_data = dict(zip(columns, values))
        record_id = current_data["_id"]

        popup = tk.Toplevel(self.root)
        popup.title("Update Record")
        popup.geometry("400x500")

        entries = {}

        for field in columns:
            tk.Label(popup, text=field).pack(pady=2)
            entry = tk.Entry(popup, width=40)
            entry.insert(0, current_data[field])
            entry.pack(pady=2)
            entries[field] = entry

        def submit_update():
            updated_doc = {}
            for field, entry in entries.items():
                value = entry.get().strip()
                if value == "":
                    continue
                if "date" in field.lower():
                    try:
                        value = datetime.datetime.strptime(value, "%Y-%m-%d")
                    except ValueError:
                        messagebox.showerror("Invalid Date", f"Please enter a valid date in YYYY-MM-DD format for '{field}'.")
                        return
                updated_doc[field] = value

            database.update_document(collection, {"_id": record_id}, {"$set": updated_doc})
            messagebox.showinfo("Success", "Record updated successfully!")
            popup.destroy()
            self.see_database()

        tk.Button(popup, text="Submit", command=submit_update).pack(pady=20)


    def show_profile_or_logout(self):
        confirm = messagebox.askyesno("Logout Confirmation", "Do you want to logout?")
        if confirm:
            self.root.destroy()  # Close the current home page window

            # Reopen the login window
            import main  # assuming your AuthApp is in main.py
            root = tk.Tk()
            app = main.AuthApp(root)
            root.mainloop()



