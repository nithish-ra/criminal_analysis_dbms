import database

collections = {
            "Criminals": database.criminals,
            "Crimes": database.crimes,
            "Stations": database.stations,
            "Prisons": database.prisons,
            "CrimeRecords": database.crime_records,
            "Investigators": database.investigator,
            "Victims": database.victims,
            "Witnesses": database.witnesses,
            "CourtCases": database.court_cases,
            "CourtTrials": database.court_trials
}

data= {
  "Criminals": [
    {
      "_id": "CRIML1",
      "name": "Criminal 1",
      "gender": "Female",
      "dob": "1981-02-15",
      "address": "1 Dark Alley, City"
    },
    {
      "_id": "CRIML2",
      "name": "Criminal 2",
      "gender": "Male",
      "dob": "1982-03-15",
      "address": "2 Dark Alley, City"
    },
    {
      "_id": "CRIML3",
      "name": "Criminal 3",
      "gender": "Female",
      "dob": "1983-04-15",
      "address": "3 Dark Alley, City"
    },
    {
      "_id": "CRIML4",
      "name": "Criminal 4",
      "gender": "Male",
      "dob": "1984-05-15",
      "address": "4 Dark Alley, City"
    },
    {
      "_id": "CRIML5",
      "name": "Criminal 5",
      "gender": "Female",
      "dob": "1985-06-15",
      "address": "5 Dark Alley, City"
    },
    {
      "_id": "CRIML6",
      "name": "Criminal 6",
      "gender": "Male",
      "dob": "1986-07-15",
      "address": "6 Dark Alley, City"
    },
    {
      "_id": "CRIML7",
      "name": "Criminal 7",
      "gender": "Female",
      "dob": "1987-08-15",
      "address": "7 Dark Alley, City"
    },
    {
      "_id": "CRIML8",
      "name": "Criminal 8",
      "gender": "Male",
      "dob": "1988-09-15",
      "address": "8 Dark Alley, City"
    },
    {
      "_id": "CRIML9",
      "name": "Criminal 9",
      "gender": "Female",
      "dob": "1989-01-15",
      "address": "9 Dark Alley, City"
    },
    {
      "_id": "CRIML10",
      "name": "Criminal 10",
      "gender": "Male",
      "dob": "1980-02-15",
      "address": "10 Dark Alley, City"
    }
  ],
  "Crimes": [
    {
      "_id": "CRM1",
      "crime_type": "Type 1",
      "section_of_law": "IPC 123"
    },
    {
      "_id": "CRM2",
      "crime_type": "Type 2",
      "section_of_law": "IPC 223"
    },
    {
      "_id": "CRM3",
      "crime_type": "Type 3",
      "section_of_law": "IPC 323"
    },
    {
      "_id": "CRM4",
      "crime_type": "Type 4",
      "section_of_law": "IPC 423"
    },
    {
      "_id": "CRM5",
      "crime_type": "Type 5",
      "section_of_law": "IPC 523"
    },
    {
      "_id": "CRM6",
      "crime_type": "Type 6",
      "section_of_law": "IPC 623"
    },
    {
      "_id": "CRM7",
      "crime_type": "Type 7",
      "section_of_law": "IPC 723"
    },
    {
      "_id": "CRM8",
      "crime_type": "Type 8",
      "section_of_law": "IPC 823"
    },
    {
      "_id": "CRM9",
      "crime_type": "Type 9",
      "section_of_law": "IPC 923"
    },
    {
      "_id": "CRM10",
      "crime_type": "Type 10",
      "section_of_law": "IPC 1023"
    }
  ],
  "Stations": [
    {
      "_id": "STN1",
      "station_name": "Station 1",
      "location": "Area B"
    },
    {
      "_id": "STN2",
      "station_name": "Station 2",
      "location": "Area C"
    },
    {
      "_id": "STN3",
      "station_name": "Station 3",
      "location": "Area D"
    },
    {
      "_id": "STN4",
      "station_name": "Station 4",
      "location": "Area E"
    },
    {
      "_id": "STN5",
      "station_name": "Station 5",
      "location": "Area F"
    },
    {
      "_id": "STN6",
      "station_name": "Station 6",
      "location": "Area G"
    },
    {
      "_id": "STN7",
      "station_name": "Station 7",
      "location": "Area H"
    },
    {
      "_id": "STN8",
      "station_name": "Station 8",
      "location": "Area I"
    },
    {
      "_id": "STN9",
      "station_name": "Station 9",
      "location": "Area J"
    },
    {
      "_id": "STN10",
      "station_name": "Station 10",
      "location": "Area K"
    }
  ],
  "Prisons": [
    {
      "_id": "PRSN1",
      "prison_name": "Prison 1",
      "location": "Zone B"
    },
    {
      "_id": "PRSN2",
      "prison_name": "Prison 2",
      "location": "Zone C"
    },
    {
      "_id": "PRSN3",
      "prison_name": "Prison 3",
      "location": "Zone D"
    },
    {
      "_id": "PRSN4",
      "prison_name": "Prison 4",
      "location": "Zone E"
    },
    {
      "_id": "PRSN5",
      "prison_name": "Prison 5",
      "location": "Zone F"
    },
    {
      "_id": "PRSN6",
      "prison_name": "Prison 6",
      "location": "Zone G"
    },
    {
      "_id": "PRSN7",
      "prison_name": "Prison 7",
      "location": "Zone H"
    },
    {
      "_id": "PRSN8",
      "prison_name": "Prison 8",
      "location": "Zone I"
    },
    {
      "_id": "PRSN9",
      "prison_name": "Prison 9",
      "location": "Zone J"
    },
    {
      "_id": "PRSN10",
      "prison_name": "Prison 10",
      "location": "Zone K"
    }
  ],
  "Investigators": [
    {
      "_id": "INV1",
      "name": "Investigator 1",
      "rank": "Rank 1",
      "station_id": "STN1"
    },
    {
      "_id": "INV2",
      "name": "Investigator 2",
      "rank": "Rank 2",
      "station_id": "STN2"
    },
    {
      "_id": "INV3",
      "name": "Investigator 3",
      "rank": "Rank 3",
      "station_id": "STN3"
    },
    {
      "_id": "INV4",
      "name": "Investigator 4",
      "rank": "Rank 4",
      "station_id": "STN4"
    },
    {
      "_id": "INV5",
      "name": "Investigator 5",
      "rank": "Rank 5",
      "station_id": "STN5"
    },
    {
      "_id": "INV6",
      "name": "Investigator 6",
      "rank": "Rank 6",
      "station_id": "STN6"
    },
    {
      "_id": "INV7",
      "name": "Investigator 7",
      "rank": "Rank 7",
      "station_id": "STN7"
    },
    {
      "_id": "INV8",
      "name": "Investigator 8",
      "rank": "Rank 8",
      "station_id": "STN8"
    },
    {
      "_id": "INV9",
      "name": "Investigator 9",
      "rank": "Rank 9",
      "station_id": "STN9"
    },
    {
      "_id": "INV10",
      "name": "Investigator 10",
      "rank": "Rank 10",
      "station_id": "STN10"
    }
  ],
  "CrimeRecords": [
    {
      "_id": "RECD1",
      "criminal_id": "CRIML1",
      "crime_id": "CRM1",
      "station_id": "STN1",
      "case_id": "CASE1",
      "entry_date": "2022-02-10"
    },
    {
      "_id": "RECD2",
      "criminal_id": "CRIML2",
      "crime_id": "CRM2",
      "station_id": "STN2",
      "case_id": "CASE2",
      "entry_date": "2022-03-10"
    },
    {
      "_id": "RECD3",
      "criminal_id": "CRIML3",
      "crime_id": "CRM3",
      "station_id": "STN3",
      "case_id": "CASE3",
      "entry_date": "2022-04-10"
    },
    {
      "_id": "RECD4",
      "criminal_id": "CRIML4",
      "crime_id": "CRM4",
      "station_id": "STN4",
      "case_id": "CASE4",
      "entry_date": "2022-05-10"
    },
    {
      "_id": "RECD5",
      "criminal_id": "CRIML5",
      "crime_id": "CRM5",
      "station_id": "STN5",
      "case_id": "CASE5",
      "entry_date": "2022-06-10"
    },
    {
      "_id": "RECD6",
      "criminal_id": "CRIML6",
      "crime_id": "CRM6",
      "station_id": "STN6",
      "case_id": "CASE6",
      "entry_date": "2022-07-10"
    },
    {
      "_id": "RECD7",
      "criminal_id": "CRIML7",
      "crime_id": "CRM7",
      "station_id": "STN7",
      "case_id": "CASE7",
      "entry_date": "2022-08-10"
    },
    {
      "_id": "RECD8",
      "criminal_id": "CRIML8",
      "crime_id": "CRM8",
      "station_id": "STN8",
      "case_id": "CASE8",
      "entry_date": "2022-09-10"
    },
    {
      "_id": "RECD9",
      "criminal_id": "CRIML9",
      "crime_id": "CRM9",
      "station_id": "STN9",
      "case_id": "CASE9",
      "entry_date": "2022-01-10"
    },
    {
      "_id": "RECD10",
      "criminal_id": "CRIML10",
      "crime_id": "CRM10",
      "station_id": "STN10",
      "case_id": "CASE10",
      "entry_date": "2022-02-10"
    }
  ],
  "Victims": [
    {
      "_id": "VIC1",
      "name": "Victim 1",
      "gender": "Male",
      "dob": "1991-02-20",
      "address": "1 Victim Street, City"
    },
    {
      "_id": "VIC2",
      "name": "Victim 2",
      "gender": "Female",
      "dob": "1992-03-20",
      "address": "2 Victim Street, City"
    },
    {
      "_id": "VIC3",
      "name": "Victim 3",
      "gender": "Male",
      "dob": "1993-04-20",
      "address": "3 Victim Street, City"
    },
    {
      "_id": "VIC4",
      "name": "Victim 4",
      "gender": "Female",
      "dob": "1994-05-20",
      "address": "4 Victim Street, City"
    },
    {
      "_id": "VIC5",
      "name": "Victim 5",
      "gender": "Male",
      "dob": "1995-06-20",
      "address": "5 Victim Street, City"
    },
    {
      "_id": "VIC6",
      "name": "Victim 6",
      "gender": "Female",
      "dob": "1996-07-20",
      "address": "6 Victim Street, City"
    },
    {
      "_id": "VIC7",
      "name": "Victim 7",
      "gender": "Male",
      "dob": "1997-08-20",
      "address": "7 Victim Street, City"
    },
    {
      "_id": "VIC8",
      "name": "Victim 8",
      "gender": "Female",
      "dob": "1998-09-20",
      "address": "8 Victim Street, City"
    },
    {
      "_id": "VIC9",
      "name": "Victim 9",
      "gender": "Male",
      "dob": "1999-01-20",
      "address": "9 Victim Street, City"
    },
    {
      "_id": "VIC10",
      "name": "Victim 10",
      "gender": "Female",
      "dob": "1990-02-20",
      "address": "10 Victim Street, City"
    }
  ],
  "Witnesses": [
    {
      "_id": "WIT1",
      "name": "Witness 1",
      "gender": "Female",
      "dob": "1991-02-25",
      "address": "1 Witness Avenue, City"
    },
    {
      "_id": "WIT2",
      "name": "Witness 2",
      "gender": "Male",
      "dob": "1992-03-25",
      "address": "2 Witness Avenue, City"
    },
    {
      "_id": "WIT3",
      "name": "Witness 3",
      "gender": "Female",
      "dob": "1993-04-25",
      "address": "3 Witness Avenue, City"
    },
    {
      "_id": "WIT4",
      "name": "Witness 4",
      "gender": "Male",
      "dob": "1994-05-25",
      "address": "4 Witness Avenue, City"
    },
    {
      "_id": "WIT5",
      "name": "Witness 5",
      "gender": "Female",
      "dob": "1995-06-25",
      "address": "5 Witness Avenue, City"
    },
    {
      "_id": "WIT6",
      "name": "Witness 6",
      "gender": "Male",
      "dob": "1996-07-25",
      "address": "6 Witness Avenue, City"
    },
    {
      "_id": "WIT7",
      "name": "Witness 7",
      "gender": "Female",
      "dob": "1997-08-25",
      "address": "7 Witness Avenue, City"
    },
    {
      "_id": "WIT8",
      "name": "Witness 8",
      "gender": "Male",
      "dob": "1998-09-25",
      "address": "8 Witness Avenue, City"
    },
    {
      "_id": "WIT9",
      "name": "Witness 9",
      "gender": "Female",
      "dob": "1999-01-25",
      "address": "9 Witness Avenue, City"
    },
    {
      "_id": "WIT10",
      "name": "Witness 10",
      "gender": "Male",
      "dob": "1990-02-25",
      "address": "10 Witness Avenue, City"
    }
  ],
  "CourtCases": [
    {
      "_id": "CASE1",
      "record_id": "RECD1",
      "trial_id": "TRL1",
      "case_status": "Closed",
      "victims": [
        "VIC1"
      ],
      "witnesses": [
        "WIT1"
      ],
      "evidences": [
        "Evidence1"
      ],
      "case_description": "Case 1 description",
      "inv_id": "INV1"
    },
    {
      "_id": "CASE2",
      "record_id": "RECD2",
      "trial_id": "TRL2",
      "case_status": "Open",
      "victims": [
        "VIC2"
      ],
      "witnesses": [
        "WIT2"
      ],
      "evidences": [
        "Evidence2"
      ],
      "case_description": "Case 2 description",
      "inv_id": "INV2"
    },
    {
      "_id": "CASE3",
      "record_id": "RECD3",
      "trial_id": "TRL3",
      "case_status": "Closed",
      "victims": [
        "VIC3"
      ],
      "witnesses": [
        "WIT3"
      ],
      "evidences": [
        "Evidence3"
      ],
      "case_description": "Case 3 description",
      "inv_id": "INV3"
    },
    {
      "_id": "CASE4",
      "record_id": "RECD4",
      "trial_id": "TRL4",
      "case_status": "Open",
      "victims": [
        "VIC4"
      ],
      "witnesses": [
        "WIT4"
      ],
      "evidences": [
        "Evidence4"
      ],
      "case_description": "Case 4 description",
      "inv_id": "INV4"
    },
    {
      "_id": "CASE5",
      "record_id": "RECD5",
      "trial_id": "TRL5",
      "case_status": "Closed",
      "victims": [
        "VIC5"
      ],
      "witnesses": [
        "WIT5"
      ],
      "evidences": [
        "Evidence5"
      ],
      "case_description": "Case 5 description",
      "inv_id": "INV5"
    },
    {
      "_id": "CASE6",
      "record_id": "RECD6",
      "trial_id": "TRL6",
      "case_status": "Open",
      "victims": [
        "VIC6"
      ],
      "witnesses": [
        "WIT6"
      ],
      "evidences": [
        "Evidence6"
      ],
      "case_description": "Case 6 description",
      "inv_id": "INV6"
    },
    {
      "_id": "CASE7",
      "record_id": "RECD7",
      "trial_id": "TRL7",
      "case_status": "Closed",
      "victims": [
        "VIC7"
      ],
      "witnesses": [
        "WIT7"
      ],
      "evidences": [
        "Evidence7"
      ],
      "case_description": "Case 7 description",
      "inv_id": "INV7"
    },
    {
      "_id": "CASE8",
      "record_id": "RECD8",
      "trial_id": "TRL8",
      "case_status": "Open",
      "victims": [
        "VIC8"
      ],
      "witnesses": [
        "WIT8"
      ],
      "evidences": [
        "Evidence8"
      ],
      "case_description": "Case 8 description",
      "inv_id": "INV8"
    },
    {
      "_id": "CASE9",
      "record_id": "RECD9",
      "trial_id": "TRL9",
      "case_status": "Closed",
      "victims": [
        "VIC9"
      ],
      "witnesses": [
        "WIT9"
      ],
      "evidences": [
        "Evidence9"
      ],
      "case_description": "Case 9 description",
      "inv_id": "INV9"
    },
    {
      "_id": "CASE10",
      "record_id": "RECD10",
      "trial_id": "TRL10",
      "case_status": "Open",
      "victims": [
        "VIC10"
      ],
      "witnesses": [
        "WIT10"
      ],
      "evidences": [
        "Evidence10"
      ],
      "case_description": "Case 10 description",
      "inv_id": "INV10"
    }
  ],
  "CourtTrials": [
    {
      "_id": "TRL1",
      "case_id": "CASE1",
      "verdict": "Not Guilty",
      "sentence_years": 2,
      "trial_date": "2023-02-15",
      "prison_id": "PRSN1"
    },
    {
      "_id": "TRL2",
      "case_id": "CASE2",
      "verdict": "Guilty",
      "sentence_years": 3,
      "trial_date": "2023-03-15",
      "prison_id": "PRSN2"
    },
    {
      "_id": "TRL3",
      "case_id": "CASE3",
      "verdict": "Not Guilty",
      "sentence_years": 4,
      "trial_date": "2023-04-15",
      "prison_id": "PRSN3"
    },
    {
      "_id": "TRL4",
      "case_id": "CASE4",
      "verdict": "Guilty",
      "sentence_years": 5,
      "trial_date": "2023-05-15",
      "prison_id": "PRSN4"
    },
    {
      "_id": "TRL5",
      "case_id": "CASE5",
      "verdict": "Not Guilty",
      "sentence_years": 6,
      "trial_date": "2023-06-15",
      "prison_id": "PRSN5"
    },
    {
      "_id": "TRL6",
      "case_id": "CASE6",
      "verdict": "Guilty",
      "sentence_years": 7,
      "trial_date": "2023-07-15",
      "prison_id": "PRSN6"
    },
    {
      "_id": "TRL7",
      "case_id": "CASE7",
      "verdict": "Not Guilty",
      "sentence_years": 8,
      "trial_date": "2023-08-15",
      "prison_id": "PRSN7"
    },
    {
      "_id": "TRL8",
      "case_id": "CASE8",
      "verdict": "Guilty",
      "sentence_years": 9,
      "trial_date": "2023-09-15",
      "prison_id": "PRSN8"
    },
    {
      "_id": "TRL9",
      "case_id": "CASE9",
      "verdict": "Not Guilty",
      "sentence_years": 10,
      "trial_date": "2023-01-15",
      "prison_id": "PRSN9"
    },
    {
      "_id": "TRL10",
      "case_id": "CASE10",
      "verdict": "Guilty",
      "sentence_years": 11,
      "trial_date": "2023-02-15",
      "prison_id": "PRSN10"
    }
  ]
}

for docs in data.keys():
    for doc in data[docs]:
        result = database.create_document(collections[docs],doc)
        print(result)

