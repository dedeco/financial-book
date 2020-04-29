schema_files_csv = {
    "stewardshipbh.stewardship_bh.Tb_LF_Timecards_Historic":
        {"action": "append",
         "file_name": "Timecards",
         "fields":
             [
                 "Timecard_Id",
                 "Timecard_Split",
                 "Project",
                 "Sub_Project",
                 "Project_Manager",
                 "Assignment",
                 "Timecard_Owner_Name",
                 "Start_Date",
                 "End_Date",
                 "Billable",
                 "Status",
                 "Monday_Hours",
                 "Tuesday_Hours",
                 "Wednesday_Hours",
                 "Thursday_Hours",
                 "Friday_Hours",
                 "Saturday_Hours",
                 "Sunday_Hours",
                 "Total_Hours",
                 "Total_Days_Worked",
                 "Currency",
                 "Total_Billable_Amount_Currency",
                 "Total_Billable_Amount",
                 "Bill_Rate_from_Timecard_Currency",
                 "Bill_Rate_from_Timecard"
             ],
         "numeric_fields":
             ["Monday_Hours",
              "Tuesday_Hours",
              "Wednesday_Hours",
              "Thursday_Hours",
              "Friday_Hours",
              "Saturday_Hours",
              "Sunday_Hours",
              "Total_Hours",
              "Total_Days_Worked",
              "Total_Billable_Amount",
              "Bill_Rate_from_Timecard"],
         "sep": ";",
         "decimal": ".",
         "thousands": ","
         },
    "stewardshipbh.stewardship_bh.Tb_LF_AccountProjects":
        {"action": "replace",
         "file_name": "Account_Projects",
         "fields":
             [
                 "Account_Name",
                 "Account_Client_Code",
                 "Account_Region",
                 "ClientProj_Code",
                 "Project_Name",
                 "Project_Manager",
                 "Region",
                 "Location",
                 "Active",
                 "Billable",
                 "Start_Date",
                 "End_Date",
                 "Financial_Status",
                 "Stage",
                 "Project_ID"
                 "Account_ID",
                 "Project_ID",
                 "Project_ID_18_Characters",
                 "Project_ID_2",
                 "Account_ID_18_Characters",
                 "Project_Code"
             ],
         "numeric_fields":
             [],
         "sep": ";",
         "decimal": ".",
         "thousands": ","
         },
    "stewardshipbh.stewardship_bh.Tb_LF_ResourceAssignments":
        {"action": "replace",
         "file_name": "Resource_Assignments",
         "fields":
             [
                 "Resource_Request",
                 "Resource_Full_Name",
                 "Resource_Email",
                 "Project",
                 "Assignment_Assignment_Name",
                 "Assignment_ID",
                 "API_Assignment_Correlation_ID",
                 "Resource_Account_ID",
                 "Resource_Employee_ID",
                 "Resource_Account_ID_18_Characters",
                 "Resource_Client_Code",
                 "Start_Date",
                 "End_Date",
                 "Status"
             ],
         "numeric_fields":
             [
                 "API_Assignment_Correlation_ID",
                 "Resource_Client_Code"
             ],
         "sep": ";",
         "decimal": ".",
         "thousands": ","
         },
    "stewardshipbh.stewardship_bh.Tb_LF_ResourceRequest":
        {"action": "replace",
         "file_name": "Resource_Request",
         "fields":
             [
                 "Project",
                 "Assignment_Name",
                 "Request_Id",
                 "Jigsaw_Id",
                 "Resource_Grade",
                 "Resource_Role",
                 "Record_ID",
                 "Assignment_ID",
                 "Resource_Request_Account_Id",
             ],
         "numeric_fields":
             [],
         "sep": ";",
         "decimal": ".",
         "thousands": ","
         },
    "stewardshipbh.stewardship_bh.Tb_MN_CGM_Historic":
        {"action": "replace",
         "file_name": "CGM",
         "fields":
             [
                 "DATA_REF",
                 "COD_PROJECT",
                 "PROJECT",
                 "VLR_PROF_SERV_REVENUE",
                 "VLR_REVENUE_NET",
                 "VLR_TOTAL_COSTS",
                 "PERC_CLIENT_GROSS_MARGIN_PERC"
             ],
         "numeric_fields":
             [
                 "VLR_PROF_SERV_REVENUE",
                 "VLR_REVENUE_NET",
                 "VLR_TOTAL_COSTS",
                 "PERC_CLIENT_GROSS_MARGIN_PERC"
             ],
         "sep": ",",
         "decimal": ",",
         "thousands": "."
         },
    "stewardshipbh.stewardship_bh.Tb_MN_Dolar_Historic":
        {"action": "replace",
         "file_name": "Dolar",
         "fields":
             [
                 "Date",
                 "Rate",
             ],
         "numeric_fields":
             [
                 "Rate",
             ],
         "sep": ",",
         "decimal": ",",
         "thousands": "."
         },
    "stewardshipbh.stewardship_bh.Tb_LF_AccountsProjectsTimecards":
        {"action": "replace",
         "file_name": "Accounts_Projects_Time",
         "fields":
             [
                 "Account_Id",
                 "Account_Name",
                 "Project_ID",
                 "Project_Code",
                 "Project_Name",
                 "Timecard_Id",
                 "Timecard_Split_Id",
                 "End_Date",
             ],
         "numeric_fields":
             [
             ],
         "sep": ";",
         "decimal": ".",
         "thousands": ","
         },
    "stewardshipbh.stewardship_bh.Tb_JG_AssignmentBeach":
        {"action": "replace",
         "file_name": "Assignment_Beach",
         "fields":
             [
                 "Employee_ID",
                 "Consultant",
                 "Gender",
                 "Role",
                 "Grade",
                 "Skills",
                 "Assignment_Start_Date",
                 "End_Date",
                 "Effort",
                 "Probability",
                 "Staffing_Office",
                 "Working_Office",
                 "Project",
                 "Account",
                 "Sales_Region",
                 "Opportunity_Owner",
                 "Parent_Account",
                 "Industry",
                 "Contract_Type",
                 "Sales_Stage",
                 "Opportunity_Probability",
                 "Close_Date",
                 "Primary_Service",
                 "Forecast_Categor",
                 "Project_Start_Date",
                 "Duration",
                 "Location_Of_Work",
                 "Project_Description",
                 "Notes_For_RM",
                 "Unnamed_29"
             ],
         "numeric_fields":
             [
                 "Effort",
                 "Probability",
                 "Opportunity_Probability",
                 "Notes_For_RM",
                 "Unnamed_29"
             ],
         "sep": ",",
         "decimal": ",",
         "thousands": "."
         }
}

from google.cloud import bigquery

schema_files_bq = {"stewardshipbh.stewardship_bh.timecard": [
    bigquery.SchemaField("Timecard_Id", "STRING"),
    bigquery.SchemaField("Timecard_Split", "STRING"),
    bigquery.SchemaField("Project", "STRING"),
    bigquery.SchemaField("Sub_Project", "STRING"),
    bigquery.SchemaField("Project_Manager", "STRING"),
    bigquery.SchemaField("Assignment", "STRING"),
    bigquery.SchemaField("Timecard_Owner_Name", "STRING"),
    bigquery.SchemaField("Start_Date", "DATE"),
    bigquery.SchemaField("End_Date", "DATE"),
    bigquery.SchemaField("Billable", "STRING"),
    bigquery.SchemaField("Status", "STRING"),
    bigquery.SchemaField("Monday_Hours", "NUMERIC"),
    bigquery.SchemaField("Tuesday_Hours", "NUMERIC"),
    bigquery.SchemaField("Wednesday_Hours", "NUMERIC"),
    bigquery.SchemaField("Thursday_Hours", "NUMERIC"),
    bigquery.SchemaField("Friday_Hours", "NUMERIC"),
    bigquery.SchemaField("Saturday_Hours", "NUMERIC"),
    bigquery.SchemaField("Sunday_Hours", "NUMERIC"),
    bigquery.SchemaField("Total_Hours", "NUMERIC"),
    bigquery.SchemaField("Total_Days_Worked", "NUMERIC"),
    bigquery.SchemaField("Currency", "STRING"),
    bigquery.SchemaField("Total_Billable_Amount_Currency", "STRING"),
    bigquery.SchemaField("Total_Billable_Amount", "NUMERIC"),
    bigquery.SchemaField("Bill_Rate_from_Timecard_Currency", "STRING"),
    bigquery.SchemaField("Bill_Rate_from_Timecard", "NUMERIC"),
],
    "stewardshipbh.stewardship_bh.account_projects": [
        bigquery.SchemaField("Account_Name", "STRING"),
        bigquery.SchemaField("Client_Code", "STRING"),
        bigquery.SchemaField("Account_Region", "STRING"),
        bigquery.SchemaField("ClientProj_Code", "STRING"),
        bigquery.SchemaField("Project_Name", "STRING"),
        bigquery.SchemaField("Project_Manager", "STRING"),
        bigquery.SchemaField("Margin_Percentage", "STRING"),
        bigquery.SchemaField("Region", "STRING"),
        bigquery.SchemaField("Location", "STRING"),
        bigquery.SchemaField("Active", "STRING"),
        bigquery.SchemaField("Billable", "STRING"),
        bigquery.SchemaField("Start_Date", "STRING"),
        bigquery.SchemaField("End_Date", "STRING"),
        bigquery.SchemaField("Financial_Status", "STRING"),
        bigquery.SchemaField("Stage", "STRING"),
    ],
    "stewardshipbh.stewardship_bh.assignments": [
        bigquery.SchemaField("Resource_Request", "STRING"),
        bigquery.SchemaField("Resource_Full_Name", "STRING"),
        bigquery.SchemaField("Resource_Email", "STRING"),
        bigquery.SchemaField("Project", "STRING"),
        bigquery.SchemaField("Assignment_Assignment_Name", "STRING"),
        bigquery.SchemaField("Assignment_ID", "STRING"),
    ],
    "stewardshipbh.stewardship_bh.requests": [
        bigquery.SchemaField("Project", "STRING"),
        bigquery.SchemaField("Assignment_Name", "STRING"),
        bigquery.SchemaField("Request_Id", "STRING"),
        bigquery.SchemaField("Jigsaw_Id", "STRING"),
        bigquery.SchemaField("Resource_Grade", "STRING"),
        bigquery.SchemaField("Resource_Role", "STRING"),
    ],
    "stewardshipbh.stewardship_bh.cgm": [
        bigquery.SchemaField("DATA_REF", "DATE"),
        bigquery.SchemaField("COD_PROJECT", "STRING"),
        bigquery.SchemaField("PROJECT", "STRING"),
        bigquery.SchemaField("VLR_PROF_SERV_REVENUE", "NUMERIC"),
        bigquery.SchemaField("VLR_REVENUE_NET", "NUMERIC"),
        bigquery.SchemaField("VLR_TOTAL_COSTS", "NUMERIC"),
        bigquery.SchemaField("PERC_CLIENT_GROSS_MARGIN_PERC", "NUMERIC"),
    ],
    "stewardshipbh.stewardship_bh.tb_dolar": [
        bigquery.SchemaField("Date", "DATE"),
        bigquery.SchemaField("Rate", "NUMERIC"),
    ]
}
