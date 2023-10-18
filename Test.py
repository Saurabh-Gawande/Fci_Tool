import pandas as pd
from pulp import *
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

fetched_data = {'TEFD': '', 'origin_state': 'default', 'org_rhcode': 'FCP', 'destination_state': 'default', 'dest_rhcode': 'MDP', 'block_data': [{'origin_state': 'Haryana', 'origin_railhead': 'FCP', 'destination_state': 'Jharkhand', 'destination_railhead': 'MDP', 'id': 1697618835233}], 'Scenerio': '', 'confirmed_data': [{'origin_state': 'Karnataka', 'origin_railhead': 'FIH', 'destination_state': 'Kerala', 'destination_railhead': 'MVKF', 'commodity': 'RICE', 'value': '', 'id': 1697618851412}], 'rice_origin': [{'origin_state': 'Andhra Pradesh', 'origin_railhead': 'ADB', 'origin_value': '1', 'id': 1697618756837}], 'rice_destination': [{'origin_state': 'Bihar', 'origin_railhead': 'BBU', 'origin_value': '1', 'id': 1697618764807}], 'rice_inline': [{'origin_state': 'Chattisgarh', 'origin_railhead': 'BLSN', 'destination_state': 'Goa', 'destination_railhead': 'VSG', 'id': 1697618786753}], 'rice_dest_inline': [{'origin_state': 'Gujarat', 'origin_railhead': 'CHM', 'destination_state': 'Jammu & Kashmir', 'destination_railhead': 'BBMN', 'id': 1697618804054}], 'rice_dest_inline_value': '1000', 'rice_inline_value': '100', 'wheat_origin': [{'origin_state': 'MP', 'origin_railhead': 'BINA', 'origin_value': '1', 'id': 1697618870463}], 'wheat_destination': [{'origin_state': 'Maharashtra', 'origin_railhead': 'BAP', 'origin_value': '1', 'id': 1697618886691}], 'wheat_inline': [{'origin_state': 'NE', 'origin_railhead': 'BPRD', 'destination_state': 'Odisha', 'destination_railhead': 'DJX', 'id': 1697618904744}], 'wheat_inline_value': '100', 'wheat_dest_inline': [{'origin_state': 'Rajasthan', 'origin_railhead': 'CNA', 'destination_state': 'Tamil Nadu', 'destination_railhead': 'CBFB', 'id': 1697618927030}], 'wheat_dest_inline_value': '10000'}

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
# surplus_wheat=pd.read_excel(data,sheet_name="Surplus_wheat",index_col=1)
# deficit_wheat=pd.read_excel(data,sheet_name="Deficit_wheat",index_col=1)
# surplus_rra=pd.read_excel(data,sheet_name="Surplus_RRA",index_col=1)
# deficit_rra=pd.read_excel(data,sheet_name="Deficit_RRA",index_col=1)
# # surplus_frk_rra=pd.read_excel(data,sheet_name="Surplus_FRK_RRA",index_col=1)
# # deficit_frk_rra=pd.read_excel(data,sheet_name="Deficit_FRK_RRA",index_col=1)
# # surplus_frk_br=pd.read_excel(data,sheet_name="Surplus_FRK_BR",index_col=1)
# # deficit_frk_br=pd.read_excel(data,sheet_name="Deficit_FRK_BR",index_col=1)
# # surplus_coarse=pd.read_excel(data,sheet_name="Surplus_Coarse_GR",index_col=1)
# # deficit_coarse=pd.read_excel(data,sheet_name="Deficit_Coarse_GR",index_col=1)
# # surplus_comm_mix=pd.read_excel(data,sheet_name="Surplus_Comm_mix",index_col=1)
# # deficit_comm_mix=pd.read_excel(data,sheet_name="Deficit_Comm_mix",index_col=1)
# rail_cost=pd.read_excel(data,sheet_name="Railhead_cost_matrix_1rake",index_col=0)
rail_cost = pd.read_excel(matrices_data, sheet_name="Railhead_cost_matrix", index_col=0)
distance_rh = pd.read_excel(matrices_data, sheet_name="Railhead_dist_matrix", index_col=0)
# # states_alloc=pd.read_excel(data,sheet_name="States_allocation",index_col=0)
# # states_supply=pd.read_excel(data,sheet_name="States_supply",index_col=0)

prob = LpProblem("FCI_monthly_model_allocation_rr", LpMinimize)

source_wheat = {}
for i in range(len(wheat_origin)):
    if int(wheat_origin[i]["origin_value"]) > 0:
        source_wheat[wheat_origin[i]["origin_railhead"]] = int(wheat_origin[i]["origin_value"])

source_rra = {}
for i in range(len(rra_origin)):
    if int(rra_origin[i]["origin_value"]) > 0:
        source_rra[rra_origin[i]["origin_railhead"]] = int(rra_origin[i]["origin_value"])

source_wheat_inline = {}
for i in range(len(wheat_origin_inline)):
    source_wheat_inline[wheat_origin_inline[i]["origin_railhead"]] = rra_origin_inline[i]["destination_railhead"]

source_rra_inline = {}
for i in range(len(rra_origin_inline)):
    source_rra_inline[rra_origin_inline[i]["origin_railhead"]] = rra_origin_inline[i]["destination_railhead"]

dest_wheat = {}
for i in range(len(wheat_dest)):
    if int(wheat_dest[i]["origin_value"]) > 0:
        dest_wheat[wheat_dest[i]["origin_railhead"]] = int(wheat_dest[i]["origin_value"])

dest_rra = {}
for i in range(len(rra_dest)):
    if int(rra_dest[i]["origin_value"]) > 0:
        dest_rra[rra_dest[i]["origin_railhead"]] = int(rra_dest[i]["origin_value"])

dest_wheat_inline = {}
for i in range(len(wheat_dest_inline)):
    dest_wheat_inline[wheat_dest_inline[i]["origin_railhead"]] = wheat_dest_inline[i]["destination_railhead"]

dest_rra_inline = {}
for i in range(len(rra_dest_inline)):
    dest_rra_inline[rra_dest_inline[i]["origin_railhead"]] = rra_dest_inline[i]["destination_railhead"]

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
    print(list_src_wheat)

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
# x_ij_frk_rra=LpVariable.dicts("x_frk_rra",[(i,j) for i in source_frk_rra.keys() for j in dest_frk_rra.keys()],cat="Integer")
# x_ij_frk_br=LpVariable.dicts("x_frk_br",[(i,j) for i in source_frk_br.keys() for j in dest_frk_br.keys()],cat="Integer")
# x_ij_cgr=LpVariable.dicts("x_cgr",[(i,j) for i in source_coarse_gr.keys() for j in dest_coarse_gr.keys()],cat="Integer")
# x_ij_mix=LpVariable.dicts("x_mix",[(i,j) for i in source_comm_mix.keys() for j in dest_comm_mix.keys()],cat="Integer")

prob += lpSum(x_ij_wheat[(i, j)] * rail_cost.loc[i][j] for i in source_wheat.keys() for j in dest_wheat.keys()) + lpSum(x_ij_rra[(i, j)] * rail_cost.loc[i][j] for i in source_rra.keys() for j in dest_rra.keys())

for i in source_wheat.keys():
    prob += lpSum(x_ij_wheat[(i, j)] for j in dest_wheat.keys()) <= source_wheat[i]

for i in source_rra.keys():
    prob += lpSum(x_ij_rra[(i, j)] for j in dest_rra.keys()) <= source_rra[i]

for i in dest_wheat.keys():
    prob += lpSum(x_ij_wheat[(j, i)] for j in source_wheat.keys()) >= dest_wheat[i]
    print(lpSum(x_ij_wheat[(j, i)] for j in source_wheat.keys()) >= dest_wheat[i])

# 2. RRA

for i in dest_rra.keys():
    prob += lpSum(x_ij_rra[(j, i)] for j in source_rra.keys()) >= dest_rra[i]
    print(lpSum(x_ij_rra[(j, i)] for j in source_rra.keys()) >= dest_rra[i])

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
        if x_ij_wheat[(i, j)].value() > 0:
            From.append(i)
            To.append(j)
            values.append(x_ij_wheat[(i, j)].value())
            commodity.append("Wheat")

for i in range(len(confirmed_org_rhcode)):
    org = str(confirmed_org_rhcode[i])
    org_state = str(confirmed_org_state[i])
    dest = str(confirmed_dest_rhcode[i])
    dest_state = str(confirmed_dest_state[i])
    Commodity = confirmed_railhead_commodities[i]
    # val = confirmed_railhead_value[i]
    if Commodity == 'WHEAT':
        From.append(org)
        # From_state.append(org_state)
        To.append(dest)
        # To_state.append(dest_state)
        commodity.append("Wheat")
        # values.append(val)

df_wheat["From"] = From
# df_wheat["From State"] = From_state
df_wheat["To"] = To
# df_wheat["To State"] = To_state
df_wheat["Commodity"] = commodity

for i in dest_wheat_inline.keys():
    for j in range(len(df_wheat["To"])):
        if (i == df_wheat.iloc[j]["To"] or dest_wheat_inline[i] == df_wheat.iloc[j]["To"]):
            df_wheat.loc[j, 'To'] = (i + '+' + dest_wheat_inline[i])

D = []
E = []
F = []

df_rra = pd.DataFrame()

From = []
To = []
values = []
commodity = []
From_state_rra = []
To_state_rra = []

for i in source_rra:
    for j in dest_rra:
        if x_ij_rra[(i, j)].value() > 0:
            From.append(i)
            To.append(j)
            values.append(x_ij_rra[(i, j)].value())
            commodity.append("RRA")

for i in range(len(confirmed_org_rhcode)):
    org = str(confirmed_org_rhcode[i])
    org_state = str(confirmed_org_state[i])
    dest = str(confirmed_dest_rhcode[i])
    dest_state = str(confirmed_dest_state[i])
    Commodity = confirmed_railhead_commodities[i]
    # val = float(confirmed_railhead_value[i])
    if Commodity == 'RICE':
        From.append(org)
        # From_state_rra.append(org_state)
        To.append(dest)
        # To_state_rra.append(dest_state)
        commodity.append("Rice")
        # values.append(val)

df_rra["From"] = From
# df_rra["From State"] = From_state_rice
df_rra["To"] = To
# df_rra["To State"] = To_state_rice
df_rra["Commodity"] = commodity

for i in dest_rra_inline.keys():
    for j in range(len(df_rra["To"])):
        if (i == df_rra.iloc[j]["To"] or dest_rra_inline[i] == df_rra.iloc[j]["To"]):
            df_rra.loc[j, 'To'] = (i + '+' + dest_rra_inline[i])

# data1["rra"] = df_rra
# data1["wheat"] = df_wheat

with pd.ExcelWriter("Output//List_DPT.xlsx", mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
    df_wheat.to_excel(writer, sheet_name="wheat", index=False)
    df_rra.to_excel(writer, sheet_name="rra", index=False)
