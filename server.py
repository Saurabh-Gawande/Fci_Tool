import pandas as pd
from pulp import *
from array import *
import json
from flask import Flask, request, session, jsonify, send_file
import pickle
from flask_cors import CORS
import ast



app = Flask(__name__)
app.secret_key = 'aqswdefrgt'
CORS(app, supports_credentials=True)


active_sessions = {}


@app.route('/login',methods = ["POST"])
def login():

    users = {
        "admin@iitd.com": "admin@321",
        "saurabh@iitd.com": "password1",
        "atul@iitd.com": "password2",
        "biharuser":"biharuser@123",
        "jharkhanduser":"jharkhanduser@123",
        "orissauser":"orissauser@123",
        "westbengaluser":"westbengaluser@123",
        "haryanauser":"haryanauser@123",
        "jkuser":"jkuser@123",
        "punjabuser":"punjabuser@123",
        "rajasthanuser":"rajasthanuser@123",
        "uttarpradeshuser":"uttarpradeshuser@123",
        "uttaranchaluser":"uttaranchaluser@123",
        "arunachalpradeshuser":"arunachalpradeshuser@123",
        "assamuser":"assamuser@123",
        "manipuruser":"manipuruser@123",
        "nagalanduser":"nagalanduser@123",
        "nefuser":"nefuser@123",
        "andhrapradeshuser":"andhrapradeshuser@123",
        "karnatakauser":"karnatakauser@123",
        "keralauser":"keralauser@123",
        "tamilnaduuser":"tamilnaduuser@123",
        "telanganauser":"telanganauser@123",
        "chhattisgarhuser":"chhattisgarhuser@123",
        "gujaratuser":"gujaratuser@123",
        "madhyapradeshuser":"madhyapradeshuser@123",
        "maharastrauser":"maharastrauser@123",
        "hpuser":"hpuser@123",

        # Add more users as needed
    }    

    data = {}
    if 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
    
        if username in users and password == users[username]:
            active_sessions[username] = session.get('sid')
            data['status'] = 1
            session['username'] = username
        else:
            data['status'] = 0
    else:
        data['status'] = 'Invalid request'

    json_data = json.dumps(data)
    json_object = json.loads(json_data)
    response = jsonify(json_object)
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Credentials', 'true') 
    return (json.dumps(json_object, indent = 1))


@app.route("/upload_Monthly_File_M01",methods = ["POST"])
def upload_Monthly_File_M01():
    data = {}
    try:
        file = request.files['uploadFile']
        file.save("Input//Monthly_Template_M1.xlsx")
        data['status'] = 1
    except:
        data['status'] = 0
    
    json_data = json.dumps(data)
    json_object = json.loads(json_data)

    return(json.dumps(json_object, indent = 1))

@app.route("/upload_Monthly_File_M02",methods = ["POST"])
def upload_Monthly_File_M02():
    data = {}
    try:
        file = request.files['uploadFile_M02']
        file.save("Input//Input_Template_M02.xlsx")
        data['status'] = 1
    except:
        data['status'] = 0
    
    json_data = json.dumps(data)
    json_object = json.loads(json_data)

    return(json.dumps(json_object, indent = 1))

@app.route("/uploadDailyFile_S2",methods = ["POST"])
def uploadDailyFile_S2():
    data = {}
    try:
        file = request.files['uploadFile']
        file.save("Input//Temp_balanced_DPT_scen2.xlsx")
        data['status'] = 1
    except:
        data['status'] = 0
    
    json_data = json.dumps(data)
    json_object = json.loads(json_data)

    return(json.dumps(json_object, indent = 1))

@app.route("/uploadDailyFile_S1",methods = ["POST"])
def uploadDailyFile_S1():
    data = {}
    try:
        file = request.files['uploadFile']
        file.save("Input//Temp_balanced_DPT_scen1.xlsx")
        data['status'] = 1
    except:
        data['status'] = 0
    
    json_data = json.dumps(data)
    json_object = json.loads(json_data)

    return(json.dumps(json_object, indent = 1))

@app.route("/uploadDailyFile",methods = ["POST"])
def uploadDailyFile():
    data = {}
    try:
        file = request.files['file']
        file.save("Input//Data_template.xlsx")
        data['status'] = 1
    except:
        data['status'] = 0
    
    json_data = json.dumps(data)
    json_object = json.loads(json_data)

    return(json.dumps(json_object, indent = 1))
    

@app.route("/read_Monthly_state_table",methods = ["POST","GET"])
def read_Monthly_state_table():
    if request.method == "POST":        
        try: 
            df1 = pd.read_excel('Output\\Monthly_State_To_State_Table.xlsx', sheet_name="Wheat")
            df2 = pd.read_excel('Output\\Monthly_State_To_State_Tablee.xlsx', sheet_name="Rice")    
            json_data1 = df1.to_json(orient='records', indent=1)
            json_data2 = df2.to_json(orient='records', indent=1)
            json_data = {"Wheat": json_data1, "Rice": json_data2}
        except:
            json_data = json.dumps({"Status": 0}, indent=1)

        json_object = json.dumps(json_data)
        return json_object
    else:
        return ("Error")
        

@app.route("/read_Relevant_Result",methods = ["POST","GET"])
def read_Relevant_Result():
    if request.method == "POST":        
        try: 
            df1 = pd.read_excel('Output\\Relevent_Results.xlsx', sheet_name="wheat")
            df2 = pd.read_excel('Output\\Relevent_Results.xlsx', sheet_name="rice")    
            json_data1 = df1.to_json(orient='records', indent=1)
            json_data2 = df2.to_json(orient='records', indent=1)
            json_data = {"wheat": json_data1, "rice": json_data2}
        except:
            json_data = json.dumps({"Status": 0}, indent=1)

        json_object = json.dumps(json_data)
        return json_object
    else:
        return ("error")
    
# @app.route("/read_Result_M02",methods = ["POST","GET"])
# def read_Result_M02():
#     if request.method == "POST":        
#         try: 
#             df1 = pd.read_excel('Output\\Results_tentative.xlsx', sheet_name="r_wheat")
#             df2 = pd.read_excel('Output\\Results_tentative.xlsx', sheet_name="r_rice")  
#             df3 = pd.read_excel('Output\\Results_tentative.xlsx', sheet_name="w_wheat")
#             df4 = pd.read_excel('Output\\Results_tentative.xlsx', sheet_name="w_rice")  
#             df5 = pd.read_excel('Output\\Results_tentative.xlsx', sheet_name="x_wr_wheat")
#             df6 = pd.read_excel('Output\\Results_tentative.xlsx', sheet_name="x_wr_rice")  
#             df7 = pd.read_excel('Output\\Results_tentative.xlsx', sheet_name="x_rw_wheat")
#             df8 = pd.read_excel('Output\\Results_tentative.xlsx', sheet_name="x_rw_rice")    
#             json_data1 = df1.to_json(orient='records', indent=1)
#             json_data2 = df2.to_json(orient='records', indent=1)
#             json_data3 = df3.to_json(orient='records', indent=1)
#             json_data4 = df4.to_json(orient='records', indent=1)
#             json_data5 = df5.to_json(orient='records', indent=1)
#             json_data6 = df6.to_json(orient='records', indent=1)
#             json_data7 = df7.to_json(orient='records', indent=1)
#             json_data8 = df8.to_json(orient='records', indent=1)
#             json_data = {"r_rice": json_data1, "r_wheat": json_data2, "w_rice": json_data3, "w_wheat": json_data4, "x_wr_rice": json_data5, "x_wr_wheat": json_data6, "x_rw_rice": json_data7, "x_rw_wheat": json_data8}
#         except:
#             json_data = json.dumps({"Status": 0}, indent=1)

#         json_object = json.dumps(json_data)
#         return json_object
#     else:
#         return ("error")
    
@app.route("/read_Daily_Planner_S2",methods = ["POST","GET"])
def read_Daily_Planner_S2():
    if request.method == "POST":        
        try: 
            df1 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="rra") 
            df2 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="wheat") 
            json_data1 = df1.to_json(orient='records', indent=1)
            json_data2 = df2.to_json(orient='records', indent=1)
            json_data = {"rra": json_data1, "wheat": json_data2}
        except:
            json_data = json.dumps({"Status": 0}, indent=1)

        json_object = json.dumps(json_data)
        return json_object
    else:
        return ("error")

@app.route("/read_Daily_Planner_S1",methods = ["POST","GET"])
def read_Daily_Planner_S1():
    if request.method == "GET":        
        try: 
            df1 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="rra")
            df2 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="wheat") 
            df3 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="coarse_grain") 
            df4 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="frk_rra") 
            df5 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="frk_br") 
            df6 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="frk") 
            df7 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="frkcgr")
            df8 = pd.read_excel('Output\\List_DPT.xlsx', sheet_name="wcgr")
            json_data1 = df1.to_json(orient='records', indent=1)
            json_data2 = df2.to_json(orient='records', indent=1)
            json_data3 = df3.to_json(orient='records', indent=1)
            json_data4 = df4.to_json(orient='records', indent=1)
            json_data5 = df5.to_json(orient='records', indent=1)
            json_data6 = df6.to_json(orient='records', indent=1)
            json_data7 = df7.to_json(orient='records', indent=1)
            json_data8 = df8.to_json(orient='records', indent=1)
            json_data = {"rra": json_data1, "wheat": json_data2, "coarse_grain": json_data3, "frk_rra":json_data4 , "frk_br": json_data5 , "frk": json_data6, "frkcgr":json_data7 , "wcgr": json_data8}
        except:
            json_data = json.dumps({"Status": 0}, indent=1)

        json_object = json.dumps(json_data)
        return json_object
    else:
        return ("error")
    
@app.route("/read_Monthly_Template_M1",methods = ["POST","GET"])
def read_Monthly_Template_M1():
    if request.method == "POST":        
        try: 
            df1 = pd.read_excel('Input\\Monthly_Template_M1.xlsx', sheet_name="Surplus_wheat") 
            df2 = pd.read_excel('Input\\Monthly_Template_M1.xlsx', sheet_name="Deficit_wheat")
            df3 = pd.read_excel('Input\\Monthly_Template_M1.xlsx', sheet_name="Surplus_rice")
            df4 = pd.read_excel('Input\\Monthly_Template_M1.xlsx', sheet_name="Deficit_rice")
            df5 = pd.read_excel('Input\\Monthly_Template_M1.xlsx', sheet_name="States_supply")
            df6 = pd.read_excel('Input\\Monthly_Template_M1.xlsx', sheet_name="States_allocation")
            df7 = pd.read_excel('Input\\Monthly_Template_M1.xlsx', sheet_name="Rail_cost_chart")
            json_data1 = df1.to_json(orient='records', indent=1)
            json_data2 = df2.to_json(orient='records', indent=1)
            json_data3 = df3.to_json(orient='records', indent=1)
            json_data4 = df4.to_json(orient='records', indent=1)
            json_data5 = df5.to_json(orient='records', indent=1)
            json_data6 = df6.to_json(orient='records', indent=1)
            json_data7 = df7.to_json(orient='records', indent=1)
            json_data = {"Surplus_wheat": json_data1, "Deficit_wheat": json_data2, "Surplus_rice": json_data3, "Deficit_rice": json_data4, "States_supply": json_data5, "States_allocation": json_data6, "Rail_cost_chart": json_data7}
        except:
            json_data = json.dumps({"Status": 0}, indent=1)

        json_object = json.dumps(json_data)
        return json_object
    else:
        return ("error")
    
@app.route("/read_Daily_Template_S1",methods = ["POST","GET"])
def read_Daily_Template_S1():
    if request.method == "POST":        
        try: 
            df1 = pd.read_excel('Input\\Daily_Template_Scene1.xlsx', sheet_name="Surplus_wheat") 
            df2 = pd.read_excel('Input\\Daily_Template_Scene1.xlsx', sheet_name="Deficit_wheat")
            df3 = pd.read_excel('Input\\Daily_Template_Scene1.xlsx', sheet_name="Surplus_rice")
            df4 = pd.read_excel('Input\\Daily_Template_Scene1.xlsx', sheet_name="Deficit_rice")
            df5 = pd.read_excel('Input\\Daily_Template_Scene1.xlsx', sheet_name="States_supply")
            df6 = pd.read_excel('Input\\Daily_Template_Scene1.xlsx', sheet_name="States_allocation")
            df7 = pd.read_excel('Input\\Daily_Template_Scene1.xlsx', sheet_name="Rail_cost_chart")
            json_data1 = df1.to_json(orient='records', indent=1)
            json_data2 = df2.to_json(orient='records', indent=1)
            json_data3 = df3.to_json(orient='records', indent=1)
            json_data4 = df4.to_json(orient='records', indent=1)
            json_data5 = df5.to_json(orient='records', indent=1)
            json_data6 = df6.to_json(orient='records', indent=1)
            json_data7 = df7.to_json(orient='records', indent=1)
            json_data = {"Surplus_wheat": json_data1, "Deficit_wheat": json_data2, "Surplus_rice": json_data3, "Deficit_rice": json_data4, "States_supply": json_data5, "States_allocation": json_data6, "Rail_cost_chart": json_data7}
        except:
            json_data = json.dumps({"Status": 0}, indent=1)

        json_object = json.dumps(json_data)
        return json_object
    else:
        return ("error")
    
@app.route("/read_Daily_Template_S2",methods = ["POST","GET"])
def read_Daily_Template_S2():
    if request.method == "POST":        
        try: 
            df1 = pd.read_excel('Input\\Daily_Template_Scene2.xlsx', sheet_name="Surplus_wheat") 
            df2 = pd.read_excel('Input\\Daily_Template_Scene2.xlsx', sheet_name="Deficit_wheat")
            df3 = pd.read_excel('Input\\Daily_Template_Scene2.xlsx', sheet_name="Surplus_rice")
            df4 = pd.read_excel('Input\\Daily_Template_Scene2.xlsx', sheet_name="Deficit_rice")
            df5 = pd.read_excel('Input\\Daily_Template_Scene2.xlsx', sheet_name="States_supply")
            df6 = pd.read_excel('Input\\Daily_Template_Scene2.xlsx', sheet_name="States_allocation")
            df7 = pd.read_excel('Input\\Daily_Template_Scene2.xlsx', sheet_name="Rail_cost_chart")
            json_data1 = df1.to_json(orient='records', indent=1)
            json_data2 = df2.to_json(orient='records', indent=1)
            json_data3 = df3.to_json(orient='records', indent=1)
            json_data4 = df4.to_json(orient='records', indent=1)
            json_data5 = df5.to_json(orient='records', indent=1)
            json_data6 = df6.to_json(orient='records', indent=1)
            json_data7 = df7.to_json(orient='records', indent=1)
            json_data = {"Surplus_wheat": json_data1, "Deficit_wheat": json_data2, "Surplus_rice": json_data3, "Deficit_rice": json_data4, "States_supply": json_data5, "States_allocation": json_data6, "Rail_cost_chart": json_data7}
        except:
            json_data = json.dumps({"Status": 0}, indent=1)

        json_object = json.dumps(json_data)
        return json_object
    else:
        return ("error")
    
@app.route("/Download_Template_to_add", methods=["POST", "GET"])
def Download_Template_to_add():
    if request.method == "POST":
        try:
            df1 = pd.read_excel('Input\\Non-TEFD.xlsx', sheet_name="Railhead_cost_matrix_1rake", index_col=0) 
            df2 = pd.read_excel('Frontend\\public\\data\\Updated_railhead_list.xlsx', sheet_name="RH_Sheet") 

            prev_col = list(df1.columns)
            present_col = list(df2["RH_code"])

            prev_st = set(prev_col)

            add_rh = []
            for rh in present_col:
                if rh not in prev_st:
                    add_rh.append(rh)

            # Create a dictionary with "Railhead" as the first column
            data = {"": add_rh}

            # Add other columns
            for col in present_col:
                data[col] = [""] * len(add_rh)

            Excel_data = pd.DataFrame(data)

            json_data1 = Excel_data.to_json(orient='records', indent=1)

            json_data = {
                "Railhead_cost_matrix_1rake": json_data1,
                "Railhead_dist_matrix": json_data1,
                "Cost_matrix_Non_TEFD": json_data1,
                "Cost_matrix_TEFD": json_data1,
                "Cost_matrix_Non_TEFD+TC": json_data1,
                "Cost_matrix_TEFD+TC": json_data1
            }
        except Exception as e:
            json_data = {"Status": 0, "Error": str(e)}
        json_object = json.dumps(json_data, indent=1)
        return json_object
    else:
        return "error"



    
@app.route("/Monthly_readPickle",methods = ["POST","GET"])
def Monthly_readPickle():
    try:
        dbfile = open('Output\\OutputPickle.pkl', 'rb')     
        db = pickle.load(dbfile)
        dbfile.close()
    except:
        db = {}
        db["status"] = 0
    return(json.dumps(db, indent = 1))


@app.route("/Update_matrices",methods = ["POST"])
def Update_matrices():
    data = {}
    try:
        file = request.files['uploadFile']
        file.save("Input//Update_matrices.xlsx")
        Railhead_cost_matrix_1rake_U_data = pd.read_excel("Input/Update_matrices.xlsx", sheet_name="Railhead_cost_matrix_1rake", index_col=0)
        Railhead_cost_matrix_U_data_Non_TEFD = pd.read_excel("Input/Update_matrices.xlsx", sheet_name="Cost_matrix_Non_TEFD", index_col=0)
        Railhead_cost_matrix_U_data_TEFD = pd.read_excel("Input/Update_matrices.xlsx", sheet_name="Cost_matrix_TEFD", index_col=0)
        Railhead_cost_matrix_U_data_Non_TEFD_TC = pd.read_excel("Input/Update_matrices.xlsx", sheet_name="Cost_matrix_Non_TEFD+TC", index_col=0)
        Railhead_cost_matrix_U_data_TEFD_TC = pd.read_excel("Input/Update_matrices.xlsx", sheet_name="Cost_matrix_TEFD+TC", index_col=0)
        Railhead_dist_matrix_U_data = pd.read_excel("Input/Update_matrices.xlsx", sheet_name="Railhead_dist_matrix", index_col=0)
        Railhead_cost_matrix_1rake_M_data = pd.read_excel("Input/Non-TEFD.xlsx", sheet_name="Railhead_cost_matrix_1rake", index_col=0)
        Railhead_cost_matrix_M_data = pd.read_excel("Input/Non-TEFD.xlsx", sheet_name="Railhead_cost_matrix", index_col=0)
        Railhead_dist_matrix_M_data = pd.read_excel("Input/Non-TEFD.xlsx", sheet_name="Railhead_dist_matrix", index_col=0)

        for row in Railhead_cost_matrix_1rake_U_data.index:
            for col in Railhead_cost_matrix_1rake_U_data.columns:
                value = Railhead_cost_matrix_1rake_U_data.loc[row, col]
                Railhead_cost_matrix_1rake_M_data.at[row, col] = value
                Railhead_cost_matrix_1rake_M_data.at[col, row] = value

        for row in Railhead_cost_matrix_U_data_Non_TEFD.index:
            for col in Railhead_cost_matrix_U_data_Non_TEFD.columns:
                value = Railhead_cost_matrix_U_data_Non_TEFD.loc[row, col]
                Railhead_cost_matrix_M_data.at[row, col] = value
                Railhead_cost_matrix_M_data.at[col, row] = value

        for row in Railhead_dist_matrix_U_data.index:
            for col in Railhead_dist_matrix_U_data.columns:
                value = Railhead_dist_matrix_U_data.loc[row, col]
                Railhead_dist_matrix_M_data.at[row, col] = value
                Railhead_dist_matrix_M_data.at[col, row] = value

        with pd.ExcelWriter("Input/Non-TEFD.xlsx",mode='a',engine='openpyxl', if_sheet_exists='replace') as writer:
            Railhead_cost_matrix_1rake_M_data.to_excel(writer,sheet_name="Railhead_cost_matrix_1rake", index=True)
            Railhead_cost_matrix_M_data.to_excel(writer,sheet_name="Railhead_cost_matrix", index=True)
            Railhead_dist_matrix_M_data.to_excel(writer,sheet_name="Railhead_dist_matrix", index=True)

        for row in Railhead_cost_matrix_1rake_U_data.index:
            for col in Railhead_cost_matrix_1rake_U_data.columns:
                value = Railhead_cost_matrix_1rake_U_data.loc[row, col]
                Railhead_cost_matrix_1rake_M_data.at[row, col] = value
                Railhead_cost_matrix_1rake_M_data.at[col, row] = value

        for row in Railhead_cost_matrix_U_data_TEFD.index:
            for col in Railhead_cost_matrix_U_data_TEFD.columns:
                value = Railhead_cost_matrix_U_data_TEFD.loc[row, col]
                Railhead_cost_matrix_M_data.at[row, col] = value
                Railhead_cost_matrix_M_data.at[col, row] = value

        for row in Railhead_dist_matrix_U_data.index:
            for col in Railhead_dist_matrix_U_data.columns:
                value = Railhead_dist_matrix_U_data.loc[row, col]
                Railhead_dist_matrix_M_data.at[row, col] = value
                Railhead_dist_matrix_M_data.at[col, row] = value

        with pd.ExcelWriter("Input/TEFD.xlsx",mode='a',engine='openpyxl', if_sheet_exists='replace') as writer:
            Railhead_cost_matrix_1rake_M_data.to_excel(writer,sheet_name="Railhead_cost_matrix_1rake", index=True)
            Railhead_cost_matrix_M_data.to_excel(writer,sheet_name="Railhead_cost_matrix", index=True)
            Railhead_dist_matrix_M_data.to_excel(writer,sheet_name="Railhead_dist_matrix", index=True)

        for row in Railhead_cost_matrix_1rake_U_data.index:
            for col in Railhead_cost_matrix_1rake_U_data.columns:
                value = Railhead_cost_matrix_1rake_U_data.loc[row, col]
                Railhead_cost_matrix_1rake_M_data.at[row, col] = value
                Railhead_cost_matrix_1rake_M_data.at[col, row] = value

        for row in Railhead_cost_matrix_U_data_Non_TEFD_TC.index:
            for col in Railhead_cost_matrix_U_data_Non_TEFD_TC.columns:
                value = Railhead_cost_matrix_U_data_Non_TEFD_TC.loc[row, col]
                Railhead_cost_matrix_M_data.at[row, col] = value
                Railhead_cost_matrix_M_data.at[col, row] = value

        for row in Railhead_dist_matrix_U_data.index:
            for col in Railhead_dist_matrix_U_data.columns:
                value = Railhead_dist_matrix_U_data.loc[row, col]
                Railhead_dist_matrix_M_data.at[row, col] = value
                Railhead_dist_matrix_M_data.at[col, row] = value

        with pd.ExcelWriter("Input/Non_TEFD_TC.xlsx",mode='a',engine='openpyxl', if_sheet_exists='replace') as writer:
            Railhead_cost_matrix_1rake_M_data.to_excel(writer,sheet_name="Railhead_cost_matrix_1rake", index=True)
            Railhead_cost_matrix_M_data.to_excel(writer,sheet_name="Railhead_cost_matrix", index=True)
            Railhead_dist_matrix_M_data.to_excel(writer,sheet_name="Railhead_dist_matrix", index=True)

        for row in Railhead_cost_matrix_1rake_U_data.index:
            for col in Railhead_cost_matrix_1rake_U_data.columns:
                value = Railhead_cost_matrix_1rake_U_data.loc[row, col]
                Railhead_cost_matrix_1rake_M_data.at[row, col] = value
                Railhead_cost_matrix_1rake_M_data.at[col, row] = value

        for row in Railhead_cost_matrix_U_data_TEFD_TC.index:
            for col in Railhead_cost_matrix_U_data_TEFD_TC.columns:
                value = Railhead_cost_matrix_U_data_TEFD_TC.loc[row, col]
                Railhead_cost_matrix_M_data.at[row, col] = value
                Railhead_cost_matrix_M_data.at[col, row] = value

        for row in Railhead_dist_matrix_U_data.index:
            for col in Railhead_dist_matrix_U_data.columns:
                value = Railhead_dist_matrix_U_data.loc[row, col]
                Railhead_dist_matrix_M_data.at[row, col] = value
                Railhead_dist_matrix_M_data.at[col, row] = value

        with pd.ExcelWriter("Input/TEFD_TC.xlsx",mode='a',engine='openpyxl', if_sheet_exists='replace') as writer:
            Railhead_cost_matrix_1rake_M_data.to_excel(writer,sheet_name="Railhead_cost_matrix_1rake", index=True)
            Railhead_cost_matrix_M_data.to_excel(writer,sheet_name="Railhead_cost_matrix", index=True)
            Railhead_dist_matrix_M_data.to_excel(writer,sheet_name="Railhead_dist_matrix", index=True)

        data['status'] = 1
    except:
        data['status'] = 0
    
    json_data = json.dumps(data)
    json_object = json.loads(json_data)

    return(json.dumps(json_object, indent = 1))


@app.route("/Alternate_Railhead_readPickle",methods = ["POST","GET"])
def Alternate_Railhead_readPickle():
    try:
        dbfile = open('Output\\Alternate_Railhead.pkl', 'rb')     
        db = pickle.load(dbfile)
        dbfile.close()
        blank_data = []
        with open('Output\\Alternate_Railhead.pkl', 'wb') as f:
            pickle.dump(blank_data, f)
    except:
        db = {}
        db["status"] = 0
    return jsonify(db)


@app.route("/Add_Railhead", methods=["POST", "GET"])
def Add_Railhead():
    try:
        Railhead_name = []
        Railhead_State = []
        fetched_data = request.get_json()  # Make sure to handle request properly in your Flask app
        Railhead_name.append(fetched_data["railhead"].upper())
        Railhead_State.append(fetched_data['state'])

        Monthly_Template_M1 = 'Input\\Monthly_Template_M1.xlsx'
        Daily_Template_S1 = 'Input\\Temp_balanced_DPT_scen1.xlsx'
        Daily_Template_S2 = 'Input\\Temp_balanced_DPT_scen2.xlsx'
        Data_sheet = 'Frontend/public/data/Updated_railhead_list.xlsx'

        # Sheets
        Monthly_Sheets = ["Surplus_wheat", "Deficit_wheat", "Surplus_rice", "Deficit_rice"]
        Daily_Sheets_S1 = ["Surplus_wheat", "Deficit_wheat", "Surplus_rice", "Deficit_rice"]
        Daily_Sheets_S2 = ["Surplus_wheat", "Deficit_wheat", "Surplus_rice", "Deficit_rice"]

        # Initialize lists for DataFrames
        Monthly_df = []
        Daily_S1_df = []
        Daily_S2_df = []
        Data_sheets = pd.read_excel(Data_sheet, sheet_name="RH_Sheet")

        # Read data from Excel files and store in lists
        for sheets in Monthly_Sheets:
            x = pd.read_excel(Monthly_Template_M1, sheet_name=sheets)
            Monthly_df.append(x)

        for sheets in Daily_Sheets_S1:
            x = pd.read_excel(Daily_Template_S1, sheet_name=sheets)
            Daily_S1_df.append(x)

        for sheets in Daily_Sheets_S2:
            x = pd.read_excel(Daily_Template_S2, sheet_name=sheets)
            Daily_S2_df.append(x)

        for i in range(len(Railhead_name)):
            Data_sheets = pd.concat([Data_sheets, pd.DataFrame({"RH_code": [Railhead_name[i]], "State": [Railhead_State[i]]})])

        # Append data to the DataFrames
        for i in range(len(Monthly_Sheets)):
            for j in range(len(Railhead_name)):
                Monthly_df[i] = pd.concat([Monthly_df[i], pd.DataFrame({"Railhead": [Railhead_name[j]], "State": [Railhead_State[j]]})])
                for col in Monthly_df[i].columns:
                    if col not in ["Railhead", "State"]:
                        Monthly_df[i][col] = 0  # Set all values to zero

        for i in range(len(Daily_Sheets_S1)):
            for j in range(len(Railhead_name)):
                Daily_S1_df[i] = pd.concat([Daily_S1_df[i], pd.DataFrame({"Railhead": [Railhead_name[j]], "State": [Railhead_State[j]]})])
                for col in Daily_S1_df[i].columns:
                    if col not in ["Railhead", "State"]:
                        Daily_S1_df[i][col] = 0  # Set all values to zero

        for i in range(len(Daily_Sheets_S2)):
            for j in range(len(Railhead_name)):
                Daily_S2_df[i] = pd.concat([Daily_S2_df[i], pd.DataFrame({"Railhead": [Railhead_name[j]], "State": [Railhead_State[j]]})])
                for col in Daily_S2_df[i].columns:
                    if col not in ["Railhead", "State"]:
                        Daily_S2_df[i][col] = 0  # Set all values to zero

        # Write modified DataFrames back to Excel files
        with pd.ExcelWriter("Input\\Monthly_Template_M1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
            for i in range(len(Monthly_Sheets)):
                Monthly_df[i].to_excel(writer, sheet_name=Monthly_Sheets[i], index=False)

        with pd.ExcelWriter("Input\\Temp_balanced_DPT_scen1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
            for i in range(len(Daily_Sheets_S1)):
                Daily_S1_df[i].to_excel(writer, sheet_name=Daily_Sheets_S1[i], index=False)

        with pd.ExcelWriter("Input\\Temp_balanced_DPT_scen2.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
            for i in range(len(Daily_Sheets_S2)):
                Daily_S2_df[i].to_excel(writer, sheet_name=Daily_Sheets_S2[i], index=False)

        with pd.ExcelWriter("Frontend\\public\\data\\Updated_railhead_list.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
            Data_sheets.to_excel(writer, sheet_name="RH_Sheet", index=False)


        db = {"status": 1, "message": "Railhead names and states added successfully"}
    except Exception as e:
        db = {"status": 0, "message": str(e)}

    return json.dumps(db, indent=1)

@app.route('/getMonthlyExcelData')
def get_monthly_excel_data():
    Monthly_Template_M1 = 'Input\\Monthly_Template_M1.xlsx'
    excel_path = os.path.join(os.path.dirname(__file__), Monthly_Template_M1)
    return send_file(excel_path, as_attachment=True)

@app.route('/getDaily1ExcelData')
def get_daily_scen1_excel_data():
    Monthly_Template_M1 = 'Input\\Temp_balanced_DPT_scen1.xlsx'
    excel_path = os.path.join(os.path.dirname(__file__), Monthly_Template_M1)
    return send_file(excel_path, as_attachment=True)

@app.route('/getDaily2ExcelData')
def get_daily_scen2_excel_data():
    Monthly_Template_M1 = 'Input\\Temp_balanced_DPT_scen2.xlsx'
    excel_path = os.path.join(os.path.dirname(__file__), Monthly_Template_M1)
    return send_file(excel_path, as_attachment=True)

@app.route('/getDataTemplate')
def data_template():
    Monthly_Template_M1 = 'Input\\Data_template.xlsx'
    excel_path = os.path.join(os.path.dirname(__file__), Monthly_Template_M1)
    return send_file(excel_path, as_attachment=True)

@app.route("/Modify_Monthly_Template_M01", methods=["POST", "GET"])
def Modify_Monthly_Template_M01():
    try:
        def try_float(value):
            try:
                return float(value)
            except (ValueError, TypeError):
                return value
        fetched_data = request.get_json()
        sheets = fetched_data['SheetNames']
       

        for sht in sheets:
            if sht == 'Surplus_wheat':
                columns = ['Railhead', 'State', 'Supply']
                sht_data = fetched_data['Sheets'][sht]
                length = len(sht_data) // len(columns)
                Railhead = [sht_data[f'A{i}']['v'] for i in range(3, length + 1)]
                state = [sht_data[f'B{i}']['v'] for i in range(3, length + 1)]
                supply = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                df = pd.DataFrame({'Railhead': Railhead, 'State': state, 'Supply': supply})
                with pd.ExcelWriter("Input/Monthly_Template_M1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name="Surplus_wheat", index=False)

            elif sht == 'Deficit_wheat':
                columns = ['Railhead', 'State', 'Demand', 'Capacity']
                sht_data = fetched_data['Sheets'][sht]
                length = len(sht_data) // len(columns)
                Railhead = [sht_data[f'A{i}']['v'] for i in range(3, length + 1)]
                state = [sht_data[f'B{i}']['v'] for i in range(3, length + 1)]
                Demand = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                Capacity = [try_float(sht_data[f'D{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                df = pd.DataFrame({'Railhead': Railhead, 'State': state, 'Demand': Demand, 'Capacity': Capacity})
                with pd.ExcelWriter("Input/Monthly_Template_M1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name="Deficit_wheat", index=False)

            elif sht == 'Surplus_rice':
                columns = ['Railhead', 'State', 'Supply']
                sht_data = fetched_data['Sheets'][sht]
                length = len(sht_data) // len(columns)
                Railhead = [sht_data[f'A{i}']['v'] for i in range(3, length + 1)]
                state = [sht_data[f'B{i}']['v'] for i in range(3, length + 1)]
                supply = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                df = pd.DataFrame({'Railhead': Railhead, 'State': state, 'Supply': supply})
                with pd.ExcelWriter("Input/Monthly_Template_M1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name="Surplus_rice", index=False)

            elif sht == 'Deficit_rice':
                columns = ['Railhead', 'State', 'Demand']
                sht_data = fetched_data['Sheets'][sht]
                length = len(sht_data) // len(columns)
                Railhead = [sht_data[f'A{i}']['v'] for i in range(3, length + 1)]
                state = [sht_data[f'B{i}']['v'] for i in range(3, length + 1)]
                demand = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                df = pd.DataFrame({'Railhead': Railhead, 'State': state, 'Demand': demand})
                with pd.ExcelWriter("Input/Monthly_Template_M1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name="Deficit_rice", index=False)

            elif sht == 'States_supply':
                columns = ['State', 'Supply_wheat', 'Supply_rice']
                sht_data = fetched_data['Sheets'][sht]
                length = len(sht_data) // len(columns)
                State = [sht_data[f'A{i}']['v'] for i in range(3, length + 1)]
                Supply_wheat = [try_float(sht_data[f'B{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                Supply_rice = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                df = pd.DataFrame({'State': State, 'Supply_wheat': Supply_wheat, 'Supply_rice': Supply_rice})
                with pd.ExcelWriter("Input/Monthly_Template_M1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name="States_supply", index=False)

            elif sht == 'States_allocation':
                columns = ['States', 'Alloc_wheat', 'Alloc_rice', 'Capacity']
                sht_data = fetched_data['Sheets'][sht]
                length = len(sht_data) // len(columns)
                States = [sht_data[f'A{i}']['v'] for i in range(3, length + 1)]
                Alloc_wheat = [try_float(sht_data[f'B{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                Alloc_rice = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                Capacity = [try_float(sht_data[f'D{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                df = pd.DataFrame({'States': States, 'Alloc_wheat': Alloc_wheat, 'Alloc_rice': Alloc_rice, 'Capacity': Capacity})
                with pd.ExcelWriter("Input/Monthly_Template_M1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name="States_allocation", index=False)

            # elif sht == 'Rail_cost_chart':
            #     columns = ['From', 'To', 'Rate per Ton']
            #     sht_data = fetched_data['Sheets'][sht]
            #     length = len(sht_data) // len(columns)
            #     From = [try_float(sht_data[f'A{i}']['v']) for i in range(3, length + 1)]
            #     To = [try_float(sht_data[f'B{i}']['v']) for i in range(3, length + 1)]
            #     Rate_per_Ton = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
            #     df = pd.DataFrame({'From': From, 'To': To, 'Rate per Ton': Rate_per_Ton})
            #     with pd.ExcelWriter("Input/Monthly_Template_M1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
            #         df.to_excel(writer, sheet_name="Rail_cost_chart", index=False)

        db = {"status": 1, "message": "Railhead names and states added successfully"}
    except Exception as e:
        db = {"status": 0, "message": str(e)}

    return json.dumps(db, indent=1)

@app.route("/Modify_Daily_Template_S01", methods=["POST", "GET"])
def Modify_Daily_Template_S01():
    try:
        def try_float(value):
            try:
                return float(value)
            except (ValueError, TypeError):
                return value
        fetched_data = request.get_json()
        sheets = fetched_data['SheetNames']

        for sht in sheets:
            if sht == 'Surplus_wheat':
                columns = ['Railhead', 'State', 'Supply']
                sht_data = fetched_data['Sheets'][sht]
                length = len(sht_data) // len(columns)
                Railhead = [sht_data[f'A{i}']['v'] for i in range(3, length + 1)]
                state = [sht_data[f'B{i}']['v'] for i in range(3, length + 1)]
                supply = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                df = pd.DataFrame({'Railhead': Railhead, 'State': state, 'Supply': supply})
                with pd.ExcelWriter("Input/Temp_balanced_DPT_scen1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name="Surplus_wheat", index=False)

            elif sht == 'Deficit_wheat':
                columns = ['Railhead', 'State', 'Demand']
                sht_data = fetched_data['Sheets'][sht]
                length = len(sht_data) // len(columns)
                Railhead = [sht_data[f'A{i}']['v'] for i in range(3, length + 1)]
                state = [sht_data[f'B{i}']['v'] for i in range(3, length + 1)]
                Demand = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                df = pd.DataFrame({'Railhead': Railhead, 'State': state, 'Demand': Demand})
                with pd.ExcelWriter("Input/Temp_balanced_DPT_scen1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name="Deficit_wheat", index=False)

            elif sht == 'Surplus_rice':
                columns = ['Railhead', 'State', 'Supply']
                sht_data = fetched_data['Sheets'][sht]
                length = len(sht_data) // len(columns)
                Railhead = [sht_data[f'A{i}']['v'] for i in range(3, length + 1)]
                state = [sht_data[f'B{i}']['v'] for i in range(3, length + 1)]
                supply = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                df = pd.DataFrame({'Railhead': Railhead, 'State': state, 'Supply': supply})
                with pd.ExcelWriter("Input/Temp_balanced_DPT_scen1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name="Surplus_rice", index=False)

            elif sht == 'Deficit_rice':
                columns = ['Railhead', 'State', 'Demand']
                sht_data = fetched_data['Sheets'][sht]
                length = len(sht_data) // len(columns)
                Railhead = [sht_data[f'A{i}']['v'] for i in range(3, length + 1)]
                state = [sht_data[f'B{i}']['v'] for i in range(3, length + 1)]
                demand = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                df = pd.DataFrame({'Railhead': Railhead, 'State': state, 'Demand': demand})
                with pd.ExcelWriter("Input/Temp_balanced_DPT_scen1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name="Deficit_rice", index=False)

            elif sht == 'States_supply':
                columns = ['State', 'Supply_wheat', 'Supply_rice']
                sht_data = fetched_data['Sheets'][sht]
                length = len(sht_data) // len(columns)
                State = [sht_data[f'A{i}']['v'] for i in range(3, length + 1)]
                Supply_wheat = [try_float(sht_data[f'B{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                Supply_rice = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                df = pd.DataFrame({'State': State, 'Supply_wheat': Supply_wheat, 'Supply_rice': Supply_rice})
                with pd.ExcelWriter("Input/Temp_balanced_DPT_scen1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name="States_supply", index=False)

            elif sht == 'States_allocation':
                columns = ['States', 'Alloc_wheat', 'Alloc_rice']
                sht_data = fetched_data['Sheets'][sht]
                length = len(sht_data) // len(columns)
                States = [sht_data[f'A{i}']['v'] for i in range(3, length + 1)]
                Alloc_wheat = [try_float(sht_data[f'B{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                Alloc_rice = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                df = pd.DataFrame({'States': States, 'Alloc_wheat': Alloc_wheat, 'Alloc_rice': Alloc_rice})
                with pd.ExcelWriter("Input/Temp_balanced_DPT_scen1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name="States_allocation", index=False)

            # elif sht == 'Rail_cost_chart':
            #     columns = ['From', 'To', 'Rate per Ton']
            #     sht_data = fetched_data['Sheets'][sht]
            #     length = len(sht_data) // len(columns)
            #     From = [try_float(sht_data[f'A{i}']['v']) for i in range(3, length + 1)]
            #     To = [try_float(sht_data[f'B{i}']['v']) for i in range(3, length + 1)]
            #     Rate_per_Ton = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
            #     df = pd.DataFrame({'From': From, 'To': To, 'Rate per Ton': Rate_per_Ton})
            #     with pd.ExcelWriter("Input/Daily_Template_Scene1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
            #         df.to_excel(writer, sheet_name="Rail_cost_chart", index=False)

        db = {"status": 1, "message": "Railhead names and states added successfully"}
    except Exception as e:
        db = {"status": 0, "message": str(e)}

    return json.dumps(db, indent=1)

@app.route("/Modify_Daily_Template_S02", methods=["POST", "GET"])
def Modify_Daily_Template_S02():
    try:
        def try_float(value):
            try:
                return float(value)
            except (ValueError, TypeError):
                return value
        fetched_data = request.get_json()
        sheets = fetched_data['SheetNames']
       
        for sht in sheets:
            if sht == 'Surplus_wheat':
                columns = ['Railhead', 'State', 'Supply']
                sht_data = fetched_data['Sheets'][sht]
                length = len(sht_data) // len(columns)
                Railhead = [sht_data[f'A{i}']['v'] for i in range(3, length + 1)]
                state = [sht_data[f'B{i}']['v'] for i in range(3, length + 1)]
                supply = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                df = pd.DataFrame({'Railhead': Railhead, 'State': state, 'Supply': supply})
                with pd.ExcelWriter("Input/Temp_balanced_DPT_scen2.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name="Surplus_wheat", index=False)

            elif sht == 'Deficit_wheat':
                columns = ['Railhead', 'State', 'Demand']
                sht_data = fetched_data['Sheets'][sht]
                length = len(sht_data) // len(columns)
                Railhead = [sht_data[f'A{i}']['v'] for i in range(3, length + 1)]
                state = [sht_data[f'B{i}']['v'] for i in range(3, length + 1)]
                Demand = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                Capacity = [try_float(sht_data[f'D{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                df = pd.DataFrame({'Railhead': Railhead, 'State': state, 'Demand': Demand, 'Capacity': Capacity})
                with pd.ExcelWriter("Input/Temp_balanced_DPT_scen2.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name="Deficit_wheat", index=False)

            elif sht == 'Surplus_rice':
                columns = ['Railhead', 'State', 'Supply']
                sht_data = fetched_data['Sheets'][sht]
                length = len(sht_data) // len(columns)
                Railhead = [sht_data[f'A{i}']['v'] for i in range(3, length + 1)]
                state = [sht_data[f'B{i}']['v'] for i in range(3, length + 1)]
                supply = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                df = pd.DataFrame({'Railhead': Railhead, 'State': state, 'Supply': supply})
                with pd.ExcelWriter("Input/Temp_balanced_DPT_scen2.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name="Surplus_rice", index=False)

            elif sht == 'Deficit_rice':
                columns = ['Railhead', 'State', 'Demand']
                sht_data = fetched_data['Sheets'][sht]
                length = len(sht_data) // len(columns)
                Railhead = [sht_data[f'A{i}']['v'] for i in range(3, length + 1)]
                state = [sht_data[f'B{i}']['v'] for i in range(3, length + 1)]
                demand = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                Capacity = [try_float(sht_data[f'D{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                df = pd.DataFrame({'Railhead': Railhead, 'State': state, 'Demand': demand, 'Capacity': Capacity})
                with pd.ExcelWriter("Input/Temp_balanced_DPT_scen2.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name="Deficit_rice", index=False)

            elif sht == 'States_supply':
                columns = ['State', 'Supply_wheat', 'Supply_rice']
                sht_data = fetched_data['Sheets'][sht]
                length = len(sht_data) // len(columns)
                State = [sht_data[f'A{i}']['v'] for i in range(3, length + 1)]
                Supply_wheat = [try_float(sht_data[f'B{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                Supply_rice = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                df = pd.DataFrame({'State': State, 'Supply_wheat': Supply_wheat, 'Supply_rice': Supply_rice})
                with pd.ExcelWriter("Input/Temp_balanced_DPT_scen2.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name="States_supply", index=False)

            elif sht == 'States_allocation':
                columns = ['States', 'Alloc_wheat', 'Alloc_rice']
                sht_data = fetched_data['Sheets'][sht]
                length = len(sht_data) // len(columns)
                States = [sht_data[f'A{i}']['v'] for i in range(3, length + 1)]
                Alloc_wheat = [try_float(sht_data[f'B{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                Alloc_rice = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
                df = pd.DataFrame({'States': States, 'Alloc_wheat': Alloc_wheat, 'Alloc_rice': Alloc_rice})
                with pd.ExcelWriter("Input/Temp_balanced_DPT_scen2.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                    df.to_excel(writer, sheet_name="States_allocation", index=False)

            # elif sht == 'Rail_cost_chart':
            #     columns = ['From', 'To', 'Rate per Ton']
            #     sht_data = fetched_data['Sheets'][sht]
            #     length = len(sht_data) // len(columns)
            #     From = [try_float(sht_data[f'A{i}']['v']) for i in range(3, length + 1)]
            #     To = [try_float(sht_data[f'B{i}']['v']) for i in range(3, length + 1)]
            #     Rate_per_Ton = [try_float(sht_data[f'C{i}']['v']) for i in range(3, length + 1)]  # Convert to float
            #     df = pd.DataFrame({'From': From, 'To': To, 'Rate per Ton': Rate_per_Ton})
            #     with pd.ExcelWriter("Input/Daily_Template_Scene1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
            #         df.to_excel(writer, sheet_name="Rail_cost_chart", index=False)

        db = {"status": 1, "message": "Railhead names and states added successfully"}
    except Exception as e:
        db = {"status": 0, "message": str(e)}

    return json.dumps(db, indent=1)




@app.route("/Remove_Railhead", methods=["POST", "GET"])
def Remove_Railhead():
    try:
        Railhead_name = []
        Railhead_State = []
        fetched_data = request.get_json()
        Railhead_name.append(fetched_data["railhead"].upper())
        Railhead_State.append(fetched_data['state'])
        Monthly_Template_M1 = 'Input\\Monthly_Template_M1.xlsx'
        Daily_Template_S1 = 'Input\\Daily_Template_Scene1.xlsx'
        Daily_Template_S2 = 'Input\\Daily_Template_Scene1.xlsx'
        Data_sheet = 'Frontend\\public\\data\\Updated_railhead_list.xlsx'

        Monthly_Sheets = ["Surplus_wheat", "Deficit_wheat", "Surplus_rice", "Deficit_rice"]
        Daily_Sheets_S1 = ["Surplus_wheat", "Deficit_wheat", "Surplus_rice", "Deficit_rice"]
        Daily_Sheets_S2 = ["Surplus_wheat", "Deficit_wheat", "Surplus_rice", "Deficit_rice"]

        Monthly_df = []
        Daily_S1_df = []
        Daily_S2_df = []
        Data_sheets = pd.read_excel(Data_sheet, sheet_name="RH_Sheet")

        for sheets in Monthly_Sheets:
            x = pd.read_excel(Monthly_Template_M1, sheet_name=sheets)
            Monthly_df.append(x)
        for sheets in Daily_Sheets_S1:
            x = pd.read_excel(Daily_Template_S1, sheet_name=sheets)
            Daily_S1_df.append(x)
        for sheets in Daily_Sheets_S2:
            x = pd.read_excel(Daily_Template_S2, sheet_name=sheets)
            Daily_S2_df.append(x)

        for i in range(len(Monthly_Sheets)):
            for j in range(len(Railhead_name)):
                for df in [Monthly_df[i], Daily_S1_df[i], Daily_S2_df[i]]:
                        df.drop(df[df["Railhead"] == Railhead_name[j]].index, inplace=True)
                        
        for i in range(len(Railhead_name)):
            Data_sheets.drop(Data_sheets[Data_sheets["RH_code"] == Railhead_name[i]].index, inplace=True)

        with pd.ExcelWriter("Input\\Monthly_Template_M1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
            for i in range(len(Monthly_Sheets)):
                Monthly_df[i].to_excel(writer, sheet_name=Monthly_Sheets[i], index=False)
        with pd.ExcelWriter("Input\\Daily_Template_Scene1.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
            for i in range(len(Daily_Sheets_S1)):
                Daily_S1_df[i].to_excel(writer, sheet_name=Daily_Sheets_S1[i], index=False)
        with pd.ExcelWriter("Input\\Daily_Template_Scene2.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
            for i in range(len(Daily_Sheets_S2)):
                Daily_S2_df[i].to_excel(writer, sheet_name=Daily_Sheets_S2[i], index=False)
        with pd.ExcelWriter("Frontend\\public\\data\\Updated_railhead_list.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
            Data_sheets.to_excel(writer, sheet_name="RH_Sheet", index=False)


        db = {"status": 1, "message": "Railhead names and states added successfully"}
    except Exception as e:
        db = {"status": 0, "message": str(e)}

    return json.dumps(db, indent=1)



@app.route("/Monthly_Solution",methods = ["POST","GET"])
def Monthly_Solution():
    data1 = {}
    if request.method == "POST":
        try:
            r_s = 25
            r_d = 25

            fetched_data = request.get_json()
            r_s_fetched = fetched_data['r_s']
            r_d_fetched = fetched_data['r_d']
            TEFD_fetched = fetched_data['TEFD']

            if (r_s_fetched != ''):
                r_s = int(r_s_fetched)
            if r_d_fetched != '':
                r_d = int(r_d_fetched)


            data=pd.ExcelFile("Input\\Monthly_Template_M1.xlsx")
            surplus_wheat=pd.read_excel(data,sheet_name="Surplus_wheat",index_col=0)
            deficit_wheat=pd.read_excel(data,sheet_name="Deficit_wheat",index_col=0)
            surplus_rice=pd.read_excel(data,sheet_name="Surplus_rice",index_col=0)
            deficit_rice=pd.read_excel(data,sheet_name="Deficit_rice",index_col=0)
            states_alloc=pd.read_excel(data,sheet_name="States_allocation",index_col=0)
            rail_cost = None
            if TEFD_fetched == 'NON-TEFD':
                rail_cost=pd.read_excel("Input\\Non-TEFD.xlsx",sheet_name="Railhead_cost_matrix",index_col=0)
            elif TEFD_fetched == 'TEFD':
                rail_cost=pd.read_excel("Input\\TEFD.xlsx",sheet_name="Railhead_cost_matrix",index_col=0)
            elif TEFD_fetched == 'Non-TEFD+TC':
                rail_cost=pd.read_excel("Input\\Non_TEFD_TC.xlsx",sheet_name="Railhead_cost_matrix",index_col=0)
            else:
                rail_cost=pd.read_excel("Input\\TEFD_TC.xlsx",sheet_name="Railhead_cost_matrix",index_col=0)
            


            prob = LpProblem("Output\\FCI_monthly_model_allocation_rr",LpMinimize)
            x_ij_wheat=LpVariable.dicts("x_wheat",[(i,j) for i in surplus_wheat.index for j in deficit_wheat.index],0)
            x_ij_rice=LpVariable.dicts("x_rice",[(i,j) for i in surplus_rice.index for j in deficit_rice.index],0)
            b_ij_wheat = LpVariable.dicts("b_wheat",[(i,j) for i in surplus_wheat.index for j in deficit_wheat.index],cat="Binary")
            b_ij_rice = LpVariable.dicts("b_rice",[(i,j) for i in surplus_rice.index for j in deficit_rice.index],cat="Binary")

            prob+=lpSum(x_ij_wheat[(i,j)]*rail_cost.loc[i][j] for i in surplus_wheat.index for j in deficit_wheat.index)+lpSum(x_ij_rice[(i,j)]*rail_cost.loc[i][j] for i in surplus_rice.index for j in deficit_rice.index)            
            
            for i in surplus_wheat.index:
                for j in deficit_wheat.index:
                    if i==j:
                        prob+=x_ij_wheat[(i,j)]==0
                        
            for i in surplus_rice.index:
                for j in deficit_rice.index:
                    if i==j:
                        prob+=x_ij_rice[(i,j)]==0

            for i in surplus_wheat.index:
                for j in deficit_wheat.index:
                    prob+=x_ij_wheat[(i,j)]>=0.027*b_ij_wheat[(i,j)]
                    
            for i in surplus_wheat.index:
                for j in deficit_wheat.index:
                    prob+=x_ij_wheat[(i,j)]<=1000000*b_ij_wheat[(i,j)]
                    
            for i in surplus_rice.index:
                for j in deficit_rice.index:
                    prob+=x_ij_rice[(i,j)]>=0.027*b_ij_rice[(i,j)]
                    
            for i in surplus_rice.index:
                for j in deficit_rice.index:
                    prob+=x_ij_rice[(i,j)]<=1000000*b_ij_rice[(i,j)]
                        
            for i in surplus_wheat.index:
                prob+=lpSum(x_ij_wheat[(i,j)] for j in deficit_wheat.index)<=surplus_wheat["Supply"][i]
            for i in surplus_rice.index:
                prob+=lpSum(x_ij_rice[(i,j)] for j in deficit_rice.index)<=surplus_rice["Supply"][i]
                
            for i in surplus_wheat.index:
                prob+=lpSum(x_ij_wheat[(i,j)] for j in deficit_wheat.index)+lpSum(x_ij_rice[(i,j)] for j in deficit_rice.index)<=r_s

           
            
            for a in states_alloc.index:
                prob+=lpSum(x_ij_wheat[(i,j)] for i in surplus_wheat.index for j in deficit_wheat.index if deficit_wheat.loc[j]["State"]==a)>=states_alloc.loc[a]["Alloc_wheat"]
                prob+=lpSum(x_ij_wheat[(i,j)] for i in surplus_wheat.index for j in deficit_wheat.index if deficit_wheat.loc[j]["State"]==a)<=states_alloc.loc[a]["Alloc_wheat"]
            for a in states_alloc.index:
                prob+=lpSum(x_ij_rice[(i,j)] for i in surplus_rice.index for j in deficit_rice.index if deficit_rice.loc[j]["State"]==a)>=states_alloc.loc[a]["Alloc_rice"]
                prob+=lpSum(x_ij_rice[(i,j)] for i in surplus_rice.index for j in deficit_rice.index if deficit_rice.loc[j]["State"]==a)<=states_alloc.loc[a]["Alloc_rice"]
            for j in deficit_wheat.index:
                prob+=lpSum(x_ij_wheat[(i,j)] for i in surplus_wheat.index)+lpSum(x_ij_rice[(i,j)] for i in surplus_rice.index)<=deficit_wheat["Capacity"][j]
            for j in deficit_wheat.index:
                prob+=lpSum(x_ij_wheat[(i,j)] for i in surplus_wheat.index)+lpSum(x_ij_rice[(i,j)] for i in surplus_rice.index)<=r_d
            

            prob.writeLP("Output\\FCI_monthly_model_allocation_rr.lp")
            prob.solve()
            print("Status:", LpStatus[prob.status])
            print("Minimum Cost of Transportation = Rs.", value(prob.objective),"Lakh")
            print("Total Number of Variables:",len(prob.variables()))
            print("Total Number of Constraints:",len(prob.constraints)) 
            result_data = {"Minimum Cost of Transportation": value(prob.objective), "Total Number of Variables": len(prob.variables()),"Total Number of Constraints":len(prob.constraints)}
            with open('Output\\OutputPickle.pkl', 'wb') as f:
                pickle.dump(result_data, f)   
            r_wheat={}
            r_wheat=pd.DataFrame([],index=surplus_wheat.index,columns=deficit_wheat.index)
                
            for r in surplus_wheat.index:
                for j in deficit_wheat.index:
                    r_wheat.loc[r][j]=x_ij_wheat[(r,j)].value()
                        
            r_rice={}
            r_rice=pd.DataFrame([],index=surplus_rice.index,columns=deficit_rice.index)

            for r in surplus_rice.index:
                for j in deficit_rice.index:
                    r_rice.loc[r][j]=x_ij_rice[(r,j)].value()
                    
            with pd.ExcelWriter("Output//Total_Results.xlsx",mode='a',engine='openpyxl', if_sheet_exists='replace') as writer:
                r_wheat.to_excel(writer,sheet_name="r_wheat",float_format="%0.3f")
                r_rice.to_excel(writer,sheet_name="r_rice",float_format="%0.3f")
            
            relevant_data=pd.ExcelFile("Output//Total_Results.xlsx")
            relevant_r_wheat=pd.read_excel(relevant_data,sheet_name="r_wheat",index_col=0)
            relevant_r_rice=pd.read_excel(relevant_data,sheet_name="r_rice",index_col=0)
            relevant_Dict_wheat={}
            relevant_Dict_rice={}
            for i in range(len(relevant_r_wheat.index)):
                for j in range(len(relevant_r_wheat.columns)):
                    if relevant_r_wheat.iat[i,j]>0:
                        relevant_Dict_wheat[relevant_r_wheat.index[i],relevant_r_wheat.columns[j]]=relevant_r_wheat.iloc[i][relevant_r_wheat.columns[j]]
                        
            for i in range(len(relevant_r_rice.index)):
                for j in range(len(relevant_r_rice.columns)):
                    if relevant_r_rice.iat[i,j]>0:
                        relevant_Dict_rice[relevant_r_rice.index[i],relevant_r_rice.columns[j]]=relevant_r_rice.iloc[i][relevant_r_rice.columns[j]]
            
            L1=list(relevant_Dict_wheat.keys())
            L2=list(relevant_Dict_wheat.values())
            A=[]
            B=[]
            C=[]

            df_wheat=pd.DataFrame()

            for i in range(len(L1)):
                A.append(L1[i][0])
                B.append(L1[i][1])
                C.append(L2[i])
                

            df_wheat["From"]=A
            df_wheat["To"]=B
            df_wheat["Values"]=C

            From_state=[]
            To_state=[]
            Commodity=[]

            for i in range(len(L1)):
                for j in surplus_wheat.index:
                    if L1[i][0]==j:
                        From_state.append(surplus_wheat.loc[j]["State"])
                        
            for i in range(len(L1)):
                for j in surplus_wheat.index:
                    if L1[i][1]==j:
                        To_state.append(surplus_wheat.loc[j]["State"])
                        
            for i in range(len(L1)):
                Commodity.append("Wheat")
                
                
            df_wheat.insert(1,"From_state",From_state)
            df_wheat.insert(3,"To_state",To_state)
            df_wheat.insert(4,"Commodity",Commodity)

            L3=list(relevant_Dict_rice.keys())
            L4=list(relevant_Dict_rice.values())

            D=[]
            E=[]
            F=[]

            df_rice=pd.DataFrame()

            for i in range(len(L3)):
                D.append(L3[i][0])
                E.append(L3[i][1])
                F.append(L4[i])
                
            df_rice["From"]=D
            df_rice["To"]=E
            df_rice["Values"]=F

            From_state_rice=[]
            To_state_rice=[]
            Commodity_rice=[]

            for i in range(len(L3)):
                for j in surplus_wheat.index:
                    if L3[i][0]==j:
                        From_state_rice.append(surplus_wheat.loc[j]["State"])
                        
            for i in range(len(L3)):
                for j in surplus_wheat.index:
                    if L3[i][1]==j:
                        To_state_rice.append(surplus_wheat.loc[j]["State"])
                        
            for i in range(len(L3)):
                Commodity_rice.append("Rice")
                
            df_rice.insert(1,"From_state",From_state_rice)
            df_rice.insert(3,"To_state",To_state_rice)
            df_rice.insert(4,"Commodity",Commodity_rice)

            with pd.ExcelWriter("Output//Relevent_Results.xlsx",mode='a',engine='openpyxl', if_sheet_exists='replace') as writer:
                df_wheat.to_excel(writer,sheet_name="wheat")
                df_rice.to_excel(writer,sheet_name="rice")

            # List_data = pd.ExcelFile("Output//Relevent_Results.xlsx")
            # List_rice = pd.read_excel(List_data, sheet_name="rice", index_col=0)
            # List_wheat = pd.read_excel(List_data, sheet_name="wheat", index_col=0)

            # wheat_cost = []
            # rice_cost = []
                
            # for i in range(len(List_rice)):
            #     org = List_rice["From"][i]
            #     dest = List_rice["To"][i]
            #     price = rail_cost.loc[org][dest]*List_rice["Values"][i]
            #     rice_cost.append(price)

            # for i in range(len(List_wheat)):
            #     org = List_wheat["From"][i]
            #     dest = List_wheat["To"][i]
            #     price = rail_cost.loc[org][dest]*List_wheat["Values"][i]
            #     wheat_cost.append(price)

            # List_wheat["Cost"] = wheat_cost
            # List_rice["Cost"] = rice_cost

            # with pd.ExcelWriter("Output//Relevent_Results.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
            #     List_rice.to_excel(writer, sheet_name="rice")
            #     List_wheat.to_excel(writer, sheet_name="wheat")
            
            table = pd.ExcelFile("Output//Relevent_Results.xlsx")
            table_data_w = pd.read_excel(table,sheet_name="wheat",index_col=0)
            table_data_r = pd.read_excel(table,sheet_name="rice",index_col=0)
            tab_A_w = list(table_data_w["From_state"])
            tab_B_w = list(table_data_w["To_state"])
            tab_A_r = list(table_data_r["From_state"])
            tab_B_r = list(table_data_r["To_state"])
            A_main_w = []
            B_main_w = []
            C_main_w = []
            table_set_w = set()

            A_main_r = []
            B_main_r = []
            C_main_r = []
            table_set_r = set()

            for i in range(len(tab_A_w)):
                table_set_w.add((tab_A_w[i],tab_B_w[i]))
            for i in range(len(tab_A_r)):
                table_set_r.add((tab_A_r[i],tab_B_r[i]))

            for i in table_set_w:
                source = i[0]
                dest = i[1]
                val = 0
                for _, row in table_data_w.iterrows():
                    if (row["From_state"] == source) and (row["To_state"] == dest):
                        val += int(row["Values"])
                A_main_w.append(source)
                B_main_w.append(dest)
                C_main_w.append(val)

            for i in table_set_r:
                source = i[0]
                dest = i[1]
                val = 0
                for _, row in table_data_r.iterrows():
                    if (row["From_state"] == source) and (row["To_state"] == dest):
                        val += int(row["Values"])
                A_main_r.append(source)
                B_main_r.append(dest)
                C_main_r.append(val)

            df_table_w = pd.DataFrame()
            df_table_w["From_State"] = A_main_w
            df_table_w["To_State"] = B_main_w
            df_table_w["Values"] = C_main_w

            df_table_r = pd.DataFrame()
            df_table_r["From_State"] = A_main_r
            df_table_r["To_State"] = B_main_r
            df_table_r["Values"] = C_main_r

            pivot_table_w = df_table_w.pivot_table(index="From_State", columns="To_State", values="Values", fill_value=0)
            pivot_table_r = df_table_r.pivot_table(index="From_State", columns="To_State", values="Values", fill_value=0)

            with pd.ExcelWriter("Output//Monthly_State_To_State_Table.xlsx",mode='a',engine='openpyxl', if_sheet_exists='replace') as writer:
                pivot_table_w.to_excel(writer,sheet_name="Wheat")
                pivot_table_r.to_excel(writer,sheet_name="Rice")
            
            data1["status"] = 1
                  
        except Exception as e:
            print(e)
            data1["status"] = 0
        json_data = json.dumps(data1)
        json_object = json.loads(json_data)

        return(json.dumps(json_object, indent = 1))
    else:
        return ("error")

@app.route("/Daily_Planner_Check", methods = ["POST","GET"]) 
def Daily_Planner_Check():
    data = {}
    if request.method == "POST":
        try:
            matrices_data = pd.ExcelFile("Input\\Non-TEFD.xlsx")
            distance_rh=pd.read_excel(matrices_data,sheet_name="Railhead_dist_matrix",index_col=0)
            fetched_data = request.get_json()
            print(fetched_data)
            inline_data = fetched_data["rice_inline"] + fetched_data["wheat_inline"]
            inline_source = ""
            inline_dest = ""
          
            if fetched_data["rice_inline_value"] == '':
                fetched_data["rice_inline_value"] = 0
            if fetched_data["wheat_inline_value"] == '':
                fetched_data["wheat_inline_value"] = 0  
            Inline_dist = max(int(fetched_data["rice_inline_value"]), int(fetched_data["wheat_inline_value"]))
            for i in range(len(inline_data)):
                inline_source = inline_data[i]["origin_railhead"]

            for i in range(len(inline_data)):
                inline_dest = inline_data[i]["destination_railhead"]
        
            if distance_rh.loc[inline_source, inline_dest]<=Inline_dist:
                data["status"] = "YES"
            else:
                data["status"] = "NO"
        except Exception as e:
            print(e)
            data["status"] = 0
        json_data = json.dumps(data)
        json_object = json.loads(json_data)

        return(json.dumps(json_object, indent = 1))
    else:
        return ("error")
    

@app.route("/Consistency_Check", methods=["POST", "GET"])
def Consistency_Check():
    data = {"Total Wheat supply Check": "", "Total Rice supply Check": "", "Red State": "", "status": "OK"}
    if request.method == "POST" or request.method == "GET" :
        try:
            Wheat_supply = pd.read_excel("Input\\Monthly_Template_M1.xlsx", sheet_name="Surplus_wheat", index_col=0)
            Wheat_demand = pd.read_excel("Input\\Monthly_Template_M1.xlsx", sheet_name="Deficit_wheat", index_col=0)
            Rice_supply = pd.read_excel("Input\\Monthly_Template_M1.xlsx", sheet_name="Surplus_rice", index_col=0)
            Rice_demand = pd.read_excel("Input\\Monthly_Template_M1.xlsx", sheet_name="Deficit_rice", index_col=0)

            # Calculate total demand and supply for wheat and rice
            Total_demand_w = Wheat_demand["Demand"].sum()
            Total_supply_w = Wheat_supply["Supply"].sum()

            Total_demand_r = Rice_demand["Demand"].sum()
            Total_supply_r = Rice_supply["Supply"].sum()

            if Total_supply_w < Total_demand_w:
                data["Total Wheat supply Check"] = "Supply of Wheat is less than demand"

            if Total_supply_r < Total_demand_r:
                data["Total Rice supply Check"] = "Supply of Rice is less than demand"

            # Initialize dictionaries for state capacity and demand
            State_capacity = {}
            State_demand = {}

            # Calculate state capacity and demand for wheat
            for i in range(len(Wheat_demand)):
                state = Wheat_demand["State"][i]
                capacity = Wheat_demand["Capacity"][i]
                demand = Wheat_demand["Demand"][i]
                
                if state in State_capacity:
                    State_capacity[state] += capacity
                else:
                    State_capacity[state] = capacity
                    
                if state in State_demand:
                    State_demand[state] += demand
                else:
                    State_demand[state] = demand

            # Calculate state demand for rice
            for i in range(len(Rice_demand)):
                state = Rice_demand["State"][i]
                demand = Rice_demand["Demand"][i]
                
                if state in State_demand:
                    State_demand[state] += demand
                else:
                    State_demand[state] = demand

            # Identify states with insufficient capacity to meet demand
            red_state = []

            for state, value in State_capacity.items():
                if state in State_demand and State_demand[state] > value:
                    red_state.append(state)

            data["Red State"] = red_state

        except Exception as e:
            error_message = str(e)  # Convert the error to a string
            data["status"] = "error"  # Set status to indicate an error
            data["error_message"] = error_message  # Include the error message in the response

        return jsonify(data)
    else:
        data["status"] = "error"
        return jsonify(data)



@app.route("/Daily_Planner",methods = ["POST","GET"])
def Daily_Planner():
    data1 = {}
    if request.method == "POST":
        try:
            blocked_org_rhcode = []
            blocked_dest_rhcode = []
            blocked_org_state = []
            blocked_dest_state = []

            confirmed_org_rhcode = []
            confirmed_dest_rhcode = []
            confirmed_org_state = []
            confirmed_dest_state = []
            confirmed_railhead_value = []
            confirmed_railhead_commodities = []

            fetched_data = request.get_json()
            print(fetched_data)

            blocked_data = fetched_data['block_data']
            confirmed_data = fetched_data['confirmed_data']
            # Scenerio = fetched_data["Scenerio"]
            TEFD_fetched = fetched_data['TEFD']
            rra_origin = fetched_data["rice_origin"]
            rra_dest = fetched_data["rice_destination"]
            rra_origin_inline = fetched_data["rice_inline"]
            rra_dest_inline = fetched_data["rice_dest_inline"]
            # rice_src_inline = fetched_data["rice_inline"]
            # rice_dest_inline = fetched_data["rice_dest_inline"]
            wheat_origin = fetched_data["wheat_origin"]
            wheat_dest = fetched_data["wheat_destination"]
            wheat_origin_inline = fetched_data["wheat_inline"]
            wheat_dest_inline = fetched_data["wheat_dest_inline"]
            coarseGrain_origin = fetched_data["coarseGrain_origin"]
            coarseGrain_dest = fetched_data["coarseGrain_destination"]
            frkrra_origin = fetched_data["frkrra_origin"]
            frkrra_dest = fetched_data["frkrra_destination"]
            frkbr_origin = fetched_data["frkbr_origin"]
            frkbr_dest = fetched_data["frkbr_destination"]
            frk_origin = fetched_data["frk_origin"]
            frk_dest = fetched_data["frk_destination"]
            frkcgr_origin = fetched_data["frkcgr_origin"]
            frkcgr_dest = fetched_data["frkcgr_destination"]
            wcgr_origin = fetched_data["wcgr_origin"]
            wcgr_dest = fetched_data["wcgr_destination"]

            for i in range(len(blocked_data)):
                blocked_org_rhcode.append(blocked_data[i]["origin_railhead"])
                blocked_dest_rhcode.append(blocked_data[i]["destination_railhead"])
                blocked_org_state.append(blocked_data[i]["origin_state"])
                blocked_dest_state.append(blocked_data[i]["destination_state"])

            for i in range(len(confirmed_data)):
                confirmed_org_rhcode.append(confirmed_data[i]["origin_railhead"])
                confirmed_dest_rhcode.append(confirmed_data[i]["destination_railhead"])
                confirmed_org_state.append(confirmed_data[i]["origin_state"])
                confirmed_dest_state.append(confirmed_data[i]["destination_state"])
                confirmed_railhead_value.append(confirmed_data[i]["value"])
                confirmed_railhead_commodities.append(confirmed_data[i]["commodity"])
            matrices_data = pd.ExcelFile("Input\\Non-TEFD.xlsx")
            
            rail_cost = pd.read_excel(matrices_data, sheet_name="Railhead_cost_matrix", index_col=0)
            distance_rh = pd.read_excel(matrices_data, sheet_name="Railhead_dist_matrix", index_col=0)
            # # states_alloc=pd.read_excel(data,sheet_name="States_allocation",index_col=0)
            # # states_supply=pd.read_excel(data,sheet_name="States_supply",index_col=0)

            prob = LpProblem("FCI_monthly_model_allocation_rr", LpMinimize)

            source_wheat = {}
            for wheat in wheat_origin:
                if wheat["Value"] > 0:
                    source_wheat[wheat["origin_railhead"]] = wheat["Value"]

            dest_wheat = {}
            for i in range(len(wheat_dest)):
                if int(wheat_dest[i]["Value"]) > 0:
                    dest_wheat[wheat_dest[i]["origin_railhead"]] = int(wheat_dest[i]["Value"])

            source_wheat_inline = {}
            for i in range(len(wheat_origin_inline)):
                source_wheat_inline[wheat_origin_inline[i]["origin_railhead"]] = rra_origin_inline[i]["destination_railhead"]
                
            dest_wheat_inline = {}
            for i in range(len(wheat_dest_inline)):
                dest_wheat_inline[wheat_dest_inline[i]["origin_railhead"]] = wheat_dest_inline[i]["destination_railhead"]

            source_rra = {}
            for rra in rra_origin:
                if rra["Value"] > 0:
                    source_rra[rra["origin_railhead"]] = rra["Value"]

            dest_rra = {}
            for i in range(len(rra_dest)):
                if int(rra_dest[i]["Value"]) > 0:
                    dest_rra[rra_dest[i]["origin_railhead"]] = int(rra_dest[i]["Value"]) 

            source_rra_inline = {}
            for i in range(len(rra_origin_inline)):
                source_rra_inline[rra_origin_inline[i]["origin_railhead"]] = rra_origin_inline[i]["destination_railhead"]

            dest_rra_inline = {}
            for i in range(len(rra_dest_inline)):
                dest_rra_inline[rra_dest_inline[i]["origin_railhead"]] = rra_dest_inline[i]["destination_railhead"]

            source_coarseGrain = {}
            for coarseGrain in coarseGrain_origin:
                if coarseGrain["Value"] > 0:
                    source_coarseGrain[coarseGrain["origin_railhead"]] = coarseGrain["Value"]

            dest_coarseGrain = {}
            for coarseGrain in coarseGrain_dest:
                if coarseGrain["Value"] > 0:
                    dest_coarseGrain[coarseGrain["origin_railhead"]] = coarseGrain["Value"]
                    
            source_frkrra = {}
            for frkrra in frkrra_origin:
                if frkrra["Value"] > 0:
                    source_frkrra[frkrra["origin_railhead"]] = frkrra["Value"]

            dest_frkrra = {}
            for frkrra in frkrra_dest:
                if frkrra["Value"] > 0:
                    dest_frkrra[frkrra["origin_railhead"]] = frkrra["Value"]

            source_frkbr = {}
            for frkbr in frkbr_origin:
                if frkbr["Value"] > 0:
                    source_frkbr[frkbr["origin_railhead"]] = frkbr["Value"]

            dest_frkbr = {}
            for frkbr in  frkbr_dest:
                if frkbr["Value"] > 0:
                    dest_frkbr[frkbr["origin_railhead"]] = frkbr["Value"]

            source_frk = {}
            for frk in frk_origin:
                if frk["Value"] > 0:
                    source_frk[frk["origin_railhead"]] = frk["Value"]

            dest_frk = {}
            for frk in  frk_dest:
                if frk["Value"] > 0:
                    dest_frk[frk["origin_railhead"]] = frk["Value"]

            source_frkcgr = {}
            for frkcgr in frkcgr_origin:
                if frkcgr["Value"] > 0:
                    source_frkcgr[frkcgr["origin_railhead"]] = frkcgr["Value"]

            dest_frkcgr = {}
            for frkcgr in  frkcgr_dest:
                if frkcgr["Value"] > 0:
                    dest_frkcgr[frkcgr["origin_railhead"]] = frkcgr["Value"]

            source_wcgr = {}
            for wcgr in wcgr_origin:
                if wcgr["Value"] > 0:
                    source_wcgr[wcgr["origin_railhead"]] = wcgr["Value"]

            dest_wcgr = {}
            for wcgr in  wcgr_dest:
                if wcgr["Value"] > 0:
                    dest_wcgr[wcgr["origin_railhead"]] = wcgr["Value"]
            
            L1 = list(source_wheat_inline.keys())
            L2 = list(source_rra_inline.keys())
            # L3=list(source_frk_rra_inline.keys())
            # L4=list(source_frk_br_inline.keys())
            # L5=list(source_coarse_gr_inline.keys())
            # L6=list(source_comm_mix_inline.keys())
            L7 = list(dest_wheat_inline.keys())
            L8 = list(dest_rra_inline.keys())

            list_src_wheat = []
            for i in L1:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_wheat.keys():
                    List_A.append(i)
                    List_A.append(source_wheat_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_wheat_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]
                list_src_wheat.append(Value[max(List_B)])

            for i in list_src_wheat:
                source_wheat[i] = 1

            list_src_rra = []
            for i in L2:
                Value = {}
                List_A = []
                List_B = []
                for j in dest_rra.keys():
                    List_A.append(i)
                    List_A.append(source_rra_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[source_rra_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_src_rra.append(Value[max(List_B)])

            for i in list_src_rra:
                source_rra[i] = 1

            list_dest_wheat = []
            for i in L7:
                Value = {}
                List_A = []
                List_B = []
                for j in source_wheat.keys():
                    List_A.append(i)
                    List_A.append(dest_wheat_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_wheat_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]

                list_dest_wheat.append(Value[max(List_B)])

            for i in list_dest_wheat:
                dest_wheat[i] = 1

            list_dest_rra = []

            for i in L8:
                Value = {}
                List_A = []
                List_B = []
                for j in source_rra.keys():
                    List_A.append(i)
                    List_A.append(dest_rra_inline[i])
                    List_B.append(distance_rh[i][j])
                    List_B.append(distance_rh[dest_rra_inline[i]][j])

                for i in range(len(List_A)):
                    Value[List_B[i]] = List_A[i]
                list_dest_rra.append(Value[max(List_B)])

            for i in list_dest_rra:
                dest_rra[i] = 1
           
            x_ij_wheat = LpVariable.dicts("x_wheat", [(i, j) for i in source_wheat.keys() for j in dest_wheat.keys()], cat="Integer")
            x_ij_rra = LpVariable.dicts("x_rra", [(i, j) for i in source_rra.keys() for j in dest_rra.keys()], cat="Integer")
            x_ij_coarseGrain = LpVariable.dicts("x_coarsegrain", [(i, j) for i in source_coarseGrain.keys() for j in dest_coarseGrain.keys()], cat="Integer")
            x_ij_frkrra = LpVariable.dicts("x_frkrra", [(i, j) for i in source_frkrra.keys() for j in dest_frkrra.keys()], cat="Integer")
            x_ij_frk_br=LpVariable.dicts("x_frk_br",[(i,j) for i in source_frkbr.keys() for j in dest_frkbr.keys()],cat="Integer")
            x_ij_frk=LpVariable.dicts("x_frk",[(i,j) for i in source_frk.keys() for j in dest_frk.keys()],cat="Integer")
            x_ij_frkcgr=LpVariable.dicts("x_frkcgr",[(i,j) for i in source_frkcgr.keys() for j in dest_frkcgr.keys()],cat="Integer")
            x_ij_wcgr=LpVariable.dicts("x_wcgr",[(i,j) for i in source_wcgr.keys() for j in dest_wcgr.keys()],cat="Integer")

            prob += (
                lpSum(x_ij_wheat[(i, j)] * rail_cost.loc[i][j] for i in source_wheat.keys() for j in dest_wheat.keys()) +
                lpSum(x_ij_rra[(i, j)] * rail_cost.loc[i][j] for i in source_rra.keys() for j in dest_rra.keys()) +
                lpSum(x_ij_coarseGrain[(i, j)] * rail_cost.loc[i][j] for i in source_coarseGrain.keys() for j in dest_coarseGrain.keys()) +
                lpSum(x_ij_frkrra[(i, j)] * rail_cost.loc[i][j] for i in source_frkrra.keys() for j in dest_frkrra.keys()) +
                lpSum(x_ij_frk_br[(i, j)] * rail_cost.loc[i][j] for i in source_frkbr.keys() for j in dest_frkbr.keys()) +
                lpSum(x_ij_frk[(i, j)] * rail_cost.loc[i][j] for i in source_frk.keys() for j in dest_frk.keys()) +
                lpSum(x_ij_frkcgr[(i, j)] * rail_cost.loc[i][j] for i in source_frkcgr.keys() for j in dest_frkcgr.keys()) +
                lpSum(x_ij_wcgr[(i, j)] * rail_cost.loc[i][j] for i in source_wcgr.keys() for j in dest_wcgr.keys())
            )

            for i in source_wheat.keys():
                prob += lpSum(x_ij_wheat[(i, j)] for j in dest_wheat.keys()) <= source_wheat[i]

            for i in dest_wheat.keys():
                prob += lpSum(x_ij_wheat[(j, i)] for j in source_wheat.keys()) >= dest_wheat[i]

            for i in source_rra.keys():
                prob += lpSum(x_ij_rra[(i, j)] for j in dest_rra.keys()) <= source_rra[i]

            for i in dest_rra.keys():
                prob += lpSum(x_ij_rra[(j, i)] for j in source_rra.keys()) >= dest_rra[i]

            for i in source_coarseGrain.keys():
                prob += lpSum(x_ij_coarseGrain[(i, j)] for j in dest_coarseGrain.keys()) <= source_coarseGrain[i]

            for i in dest_coarseGrain.keys():
                prob += lpSum(x_ij_coarseGrain[(j, i)] for j in source_coarseGrain.keys()) >= dest_coarseGrain[i]
            
            for i in source_frkrra.keys():
                prob += lpSum(x_ij_frkrra[(i, j)] for j in dest_frkrra.keys()) <= source_frkrra[i]
            
            for i in dest_frkrra.keys():
                prob += lpSum(x_ij_frkrra[(j, i)] for j in source_frkrra.keys()) >= dest_frkrra[i]

            for i in source_frkbr.keys():
                prob += lpSum(x_ij_frk_br[(i, j)] for j in dest_frkbr.keys()) <= source_frkbr[i]

            for i in dest_frkbr.keys():
                prob += lpSum(x_ij_frk_br[(j, i)] for j in source_frkbr.keys()) >= dest_frkbr[i] 

            for i in source_frk.keys():
                prob += lpSum(x_ij_frk[(i, j)] for j in dest_frk.keys()) <= source_frk[i]

            for i in dest_frk.keys():
                prob += lpSum(x_ij_frk[(j, i)] for j in source_frk.keys()) >= dest_frk[i] 

            for i in source_frkcgr.keys():
                prob += lpSum(x_ij_frkcgr[(i, j)] for j in dest_frkcgr.keys()) <= source_frkcgr[i]

            for i in dest_frkcgr.keys():
                prob += lpSum(x_ij_frkcgr[(j, i)] for j in source_frkcgr.keys()) >= dest_frkcgr[i] 

            for i in source_wcgr.keys():
                prob += lpSum(x_ij_wcgr[(i, j)] for j in dest_wcgr.keys()) <= source_wcgr[i]

            for i in dest_wcgr.keys():
                prob += lpSum(x_ij_wcgr[(j, i)] for j in source_wcgr.keys()) >= dest_wcgr[i] 

            prob.writeLP("FCI_monthly_model_allocation_rr.lp")
            prob.solve()
            print("Status:", LpStatus[prob.status])
            print("Minimum Cost of Transportation = Rs.", prob.objective.value(), "Lakh")
            print("Total Number of Variables:", len(prob.variables()))
            print("Total Number of Constraints:", len(prob.constraints))

            df_wheat = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []

            for i in source_wheat:
                for j in dest_wheat:
                    if int(x_ij_wheat[(i, j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_wheat[(i, j)].value())
                        commodity.append("Wheat")
                        
            for i in range(len(From)):
                for wheat in wheat_origin:
                    if From[i] == wheat["origin_railhead"]:
                        From_state.append(wheat["origin_state"])
                       
            for i in range (len(To)): 
                for wheat in wheat_dest: 
                    if To[i] == wheat["origin_railhead"]:
                        To_state.append(wheat["origin_state"])
            
            # for i in range(len(confirmed_org_rhcode)):
            #     org = str(confirmed_org_rhcode[i])
            #     org_state = str(confirmed_org_state[i])
            #     dest = str(confirmed_dest_rhcode[i])
            #     dest_state = str(confirmed_dest_state[i])
            #     Commodity = confirmed_railhead_commodities[i]
            #     # val = confirmed_railhead_value[i]
            #     if Commodity == 'WHEAT':
            #         From.append(org)
            #         # From_state.append(org_state)
            #         To.append(dest)
            #         # To_state.append(dest_state)
            #         commodity.append("Wheat")
            #         # values.append(val)

            df_wheat["From"] = From
            df_wheat["From State"] = From_state
            df_wheat["To"] = To
            df_wheat["To State"] = To_state
            df_wheat["Commodity"] = commodity
            df_wheat["Values"] = values
            
            for i in dest_wheat_inline.keys():
                for j in range(len(df_wheat["To"])):
                    if (i == df_wheat.iloc[j]["To"] or dest_wheat_inline[i] == df_wheat.iloc[j]["To"]):
                        df_wheat.loc[j, 'To'] = (i + '+' + dest_wheat_inline[i])

           
            df_rra = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state_rra = []
            To_state_rra = []

            for i in source_rra:
                for j in dest_rra:
                    if int(x_ij_rra[(i, j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_rra[(i, j)].value())
                        commodity.append("RRA")
            print(values)
            for i in range(len(From)):
                for rra in rra_origin:
                    if From[i] == rra["origin_railhead"]:
                        From_state_rra.append(rra["origin_state"])

            for i in range (len(To)): 
                for rra in rra_dest: 
                    if To[i] == rra["origin_railhead"]:
                        To_state_rra.append(rra["origin_state"]) 
            # for i in range(len(confirmed_org_rhcode)):
            #     org = str(confirmed_org_rhcode[i])
            #     org_state = str(confirmed_org_state[i])
            #     dest = str(confirmed_dest_rhcode[i])
            #     dest_state = str(confirmed_dest_state[i])
            #     Commodity = confirmed_railhead_commodities[i]
            #     # val = float(confirmed_railhead_value[i])
            #     if Commodity == 'RICE':
            #         From.append(org)
            #         # From_state_rra.append(org_state)
            #         To.append(dest)
            #         # To_state_rra.append(dest_state)
            #         commodity.append("Rice")
            #         # values.append(val)

            df_rra["From"] = From
            df_rra["From State"] = From_state_rra
            df_rra["To"] = To
            df_rra["To State"] = To_state_rra
            df_rra["Commodity"] = commodity
            df_rra["Values"] = values
            for i in dest_rra_inline.keys():
                for j in range(len(df_rra["To"])):
                    if (i == df_rra.iloc[j]["To"] or dest_rra_inline[i] == df_rra.iloc[j]["To"]):
                        df_rra.loc[j, 'To'] = (i + '+' + dest_rra_inline[i])

            df_CoarseGrain = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            
            for i in source_coarseGrain:
                for j in dest_coarseGrain:
                    if int(x_ij_coarseGrain[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_coarseGrain[(i,j)].value())
                        commodity.append("Coarse Grain")

            for i in range(len(From)):
                for coarseGrain in coarseGrain_origin:
                    if From[i] == coarseGrain["origin_railhead"]:
                        From_state.append(coarseGrain["origin_state"])

            for i in range (len(To)): 
                for coarseGrain in coarseGrain_dest: 
                    if To[i] == coarseGrain["origin_railhead"]:
                        To_state.append(coarseGrain["origin_state"])

            df_CoarseGrain["From"] = From
            df_CoarseGrain["From State"] = From_state
            df_CoarseGrain["To"] = To
            df_CoarseGrain["To State"] = To_state
            df_CoarseGrain["Commodity"] = commodity
            df_CoarseGrain["Values"] = values
          
            df_frkrra = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            
            for i in source_frkrra:
                for j in dest_frkrra:
                    if int(x_ij_frkrra[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_frkrra[(i,j)].value())
                        commodity.append("FRK RRA")

            for i in range(len(From)):
                for frkrra in frkrra_origin:
                    if From[i] == frkrra["origin_railhead"]:
                        From_state.append(frkrra["origin_state"])

            for i in range (len(To)): 
                for frkrra in frkrra_dest: 
                    if To[i] == frkrra["origin_railhead"]:
                        To_state.append(frkrra["origin_state"])
             
            df_frkrra["From"] = From
            df_frkrra["From State"] = From_state
            df_frkrra["To"] = To
            df_frkrra["To State"] = To_state
            df_frkrra["Commodity"] = commodity
            df_frkrra["Values"] = values

            df_frkbr = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            
            for i in source_frkbr:
                for j in dest_frkbr:
                    if int(x_ij_frk_br[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_frk_br[(i,j)].value())
                        commodity.append("FRK BR")

            for i in range(len(From)):
                for frkbr in frkbr_origin:
                    if From[i] == frkbr["origin_railhead"]:
                        From_state.append(frkbr["origin_state"])

            for i in range (len(To)): 
                for frkbr in frkbr_dest: 
                    if To[i] == frkbr["origin_railhead"]:
                        To_state.append(frkbr["origin_state"])

            df_frkbr["From"] = From
            df_frkbr["From State"] = From_state
            df_frkbr["To"] = To
            df_frkbr["To State"] = To_state
            df_frkbr["Commodity"] = commodity
            df_frkbr["Values"] = values

            df_frk = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            
            for i in source_frk:
                for j in dest_frk:
                    if int(x_ij_frk[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_frk[(i,j)].value())
                        commodity.append("FRK")

            for i in range(len(From)):
                for frk in frk_origin:
                    if From[i] == frk["origin_railhead"]:
                        From_state.append(frk["origin_state"])

            for i in range (len(To)): 
                for frk in frk_dest: 
                    if To[i] == frk["origin_railhead"]:
                        To_state.append(frk["origin_state"])

            df_frk["From"] = From
            df_frk["From State"] = From_state
            df_frk["To"] = To
            df_frk["To State"] = To_state
            df_frk["Commodity"] = commodity
            df_frk["Values"] = values
            
            df_frkcgr = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            
            for i in source_frkcgr:
                for j in dest_frkcgr:
                    if int(x_ij_frkcgr[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_frkcgr[(i,j)].value())
                        commodity.append("FRK+CGR")

            for i in range(len(From)):
                for frkcgr in frkcgr_origin:
                    if From[i] == frkcgr["origin_railhead"]:
                        From_state.append(frkcgr["origin_state"])

            for i in range (len(To)): 
                for frkcgr in frkcgr_dest: 
                    if To[i] == frkcgr["origin_railhead"]:
                        To_state.append(frkcgr["origin_state"])

            df_frkcgr["From"] = From
            df_frkcgr["From State"] = From_state
            df_frkcgr["To"] = To
            df_frkcgr["To State"] = To_state
            df_frkcgr["Commodity"] = commodity
            df_frkcgr["Values"] = values

            df_wcgr = pd.DataFrame()
            From = []
            To = []
            values = []
            commodity = []
            From_state = []
            To_state = []
            
            for i in source_wcgr:
                for j in dest_wcgr:
                    if int(x_ij_wcgr[(i,j)].value()) > 0:
                        From.append(i)
                        To.append(j)
                        values.append(x_ij_wcgr[(i,j)].value())
                        commodity.append("W+CGR")

            for i in range(len(From)):
                for wcgr in wcgr_origin:
                    if From[i] == wcgr["origin_railhead"]:
                        From_state.append(wcgr["origin_state"])

            for i in range (len(To)): 
                for wcgr in wcgr_dest: 
                    if To[i] == wcgr["origin_railhead"]:
                        To_state.append(wcgr["origin_state"])

            df_wcgr["From"] = From
            df_wcgr["From State"] = From_state
            df_wcgr["To"] = To
            df_wcgr["To State"] = To_state
            df_wcgr["Commodity"] = commodity
            df_wcgr["Values"] = values
            print(df_wheat)
            data1["rra"] = df_rra
            data1["wheat"] = df_wheat
            data1["coarse grain"] = df_CoarseGrain
            data1["FRK RRA"] = df_frkrra
            data1["FRK BR"] = df_frkbr
            data1["FRK"] = df_frk
            data1["FRK+CGR"] = df_frkcgr
            data1["W+CGR"] = df_wcgr

            with pd.ExcelWriter("Output//List_DPT.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                df_wheat.to_excel(writer, sheet_name="wheat", index=False)
                df_rra.to_excel(writer, sheet_name="rra", index=False)
                df_CoarseGrain.to_excel(writer, sheet_name="coarse_grain", index=False)
                df_frkrra.to_excel(writer, sheet_name="frk_rra", index=False)
                df_frkbr.to_excel(writer, sheet_name="frk_br", index=False)
                df_frk.to_excel(writer, sheet_name="frk", index=False)
                df_frkcgr.to_excel(writer, sheet_name="frkcgr", index=False)
                df_wcgr.to_excel(writer, sheet_name="wcgr", index=False)
    
        except Exception as e:
            print(e)
            data1["status"] = 0

        json_data = json.dumps(data1, default=lambda x: x.to_dict() if isinstance(x, pd.DataFrame) else x)
        json_object = json.loads(json_data)

        return(json.dumps(json_object, indent = 1))
    else:
        return ("error")

@app.route("/Alternate_Railhead_Solve",methods = ["POST","GET"])
def Alternate_Railhead_Solve():
    data = request.get_json()
    rh_source = data['rh_source']
    rh_dest = data['rh_dest']
    # zone = data['zone']
    # n = data['n']
    Alternate_Railhead_source = rh_source.upper()
    Alternate_Railhead_Destination = rh_dest.upper()
    # Alternate_Railhead_zone = zone
    # Alternate_Railhead_increment = 0.8
    data1 = {}
    if request.method == "POST":
        try:
            file = pd.ExcelFile("Input\\Temp_balanced_DPT_scen1.xlsx")
            matrices_data = pd.ExcelFile("Input\\Non-TEFD.xlsx")
            surplus_wheat = pd.read_excel(file, sheet_name="Surplus_wheat", index_col=0)
            rail_cost = pd.read_excel(matrices_data, sheet_name="Railhead_cost_matrix", index_col=0)
            alt_rh_state = surplus_wheat.loc[Alternate_Railhead_Destination]["State"]

            lst1 = []

            for index, row in surplus_wheat.iterrows():
                if row["State"] == alt_rh_state:
                    lst1.append(index)

            lst2 = []

            for j in lst1:
                lst2.append(rail_cost.loc[Alternate_Railhead_source, j])

            keys = lst1
            values = lst2

            dict_altrh = dict(zip(keys, values))

            threshold = rail_cost.loc[Alternate_Railhead_source, Alternate_Railhead_Destination]
            filt_dict_altrh = {k: v for k, v in dict_altrh.items() if k != Alternate_Railhead_Destination and v >= threshold}
            sort_dict_altrh = dict(sorted(filt_dict_altrh.items(), key=lambda item: item[1]))
            top_3_elements = list(sort_dict_altrh.items())[:3]
            result_altrh = []

            for i in range(len(top_3_elements)):
                result_altrh.append(top_3_elements[i][0])

            with open('Output\\Alternate_Railhead.pkl', 'wb') as f:
                pickle.dump(result_altrh, f)
                        
            data1["status"] = 1
                  
        except Exception as e:
            print(e)
            data1["status"] = 0
        json_data = json.dumps(data1)
        json_object = json.loads(json_data)

        return(json.dumps(json_object, indent = 1))
    else:
        return ("error")




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000 , debug=True)
