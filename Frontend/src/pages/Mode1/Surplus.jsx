import React, { useEffect, useState } from "react";
import * as XLSX from "xlsx";
import config from "../../config";

function Surplus() {
  const ProjectIp = config.serverUrl;

  const [surplus, setSurplus] = useState([]);
  const [deficit, setDeficit] = useState([]);

  const [surplusState, setSurplusState] = useState();
  const [totalSurplusRailhead, setTotalSurplusRailhead] = useState([]);
  const [surplusRailhead, setSurplusRailhead] = useState();
  const [surplusValue, setSurplusValue] = useState(1);
  const [surplusCommodity, setSurplusCommodity] = useState();

  const [deficitState, setDeficitState] = useState();
  const [totalDeficitRailhead, setTotalDeficitRailhead] = useState([]);
  const [deficitRailhead, setDeficitRailhead] = useState();
  const [deficitValue, setDeficitValue] = useState(1);
  const [deficitCommodity, setDeficitCommodity] = useState();

  const [surplusInlineState, setSurplusInlineState] = useState();
  const [surplusInlineRailhead, setSurplusInlineRailhead] = useState();
  const [surplusInlineCommodity, setSurplusInlineCommodity] = useState();
  const [totalSurplusInlineRailhead, setTotalSurplusInlineRailhead] = useState(
    []
  );

  const [deficitInlineState, setDeficitInlineState] = useState();
  const [deficitInlineRailhead, setDeficitInlineRailhead] = useState();
  const [deficitInlineCommodity, setDeficitInlineCommodity] = useState();
  const [totalDeficitInlineRailhead, setTotalDeficitInlineRailhead] = useState(
    []
  );

  useEffect(() => {
    const excel = async () => {
      const response = await fetch("/data/FCI_Optimal_planner_template.xlsx");
      const arrayBuffer = await response.arrayBuffer();
      const data = new Uint8Array(arrayBuffer);
      const workbook = XLSX.read(data, { type: "array" });
      const surplusSheetIndices = [0, 2, 4, 6, 8, 10];
      const deficitSheetIndices = [1, 3, 5, 7, 9, 11];
      const surplusData = processSheetData(workbook, surplusSheetIndices);
      setSurplus(surplusData);
      const deficitData = processSheetData(workbook, deficitSheetIndices);
      setDeficit(deficitData);
    };
    excel();
  }, []);

  const processSheetData = (workbook, sheetIndices) => {
    const jsonData = [];
    sheetIndices.forEach((sheetIndex) => {
      const sheetName = workbook.SheetNames[sheetIndex];
      const sheet = workbook.Sheets[sheetName];
      const sheetData = XLSX.utils.sheet_to_json(sheet);
      sheetData.forEach((row) => {
        if (row.Value > 0) {
          let surplusCommodity = "";
          switch (sheetIndex) {
            case 0:
            case 1:
              surplusCommodity = "Wheat";
              break;
            case 2:
            case 3:
              surplusCommodity = "PRA";
              break;
            case 4:
            case 5:
              surplusCommodity = "FRK RRA";
              break;
            case 6:
            case 7:
              surplusCommodity = "FRK BR";
              break;
            case 8:
            case 9:
              surplusCommodity = "Coarse Grain";
              break;
            default:
              break;
          }

          row.Commodity = surplusCommodity;
          jsonData.push(row);
        }
      });
    });
    return jsonData;
  };

  const handleSurplusStateChange = async (e) => {
    const selectedValue = e.target.value;
    setSurplusState(selectedValue);
    const response = await fetch("/data/Updated_railhead_list.xlsx");
    const arrayBuffer = await response.arrayBuffer();
    const data = new Uint8Array(arrayBuffer);
    const workbook = XLSX.read(data, { type: "array" });
    const sheetName = workbook.SheetNames[0];
    const sheet = workbook.Sheets[sheetName];
    const jsonData = XLSX.utils.sheet_to_json(sheet, { header: 1 });
    let dropdownOptions = [];
    let dropdownOptions_default = {
      value: "",
      label: "Please select Railhead",
    };
    for (let i = 0; i < jsonData.length; i++) {
      if (
        jsonData[i][1] &&
        jsonData[i][1].trim().toLowerCase() ===
          selectedValue.trim().toLowerCase()
      ) {
        dropdownOptions.push({ value: jsonData[i][0], label: jsonData[i][0] });
      }
    }
    dropdownOptions.sort((a, b) => a.label.localeCompare(b.label));
    dropdownOptions.unshift(dropdownOptions_default);
    setTotalSurplusRailhead(dropdownOptions);
  };

  const handleDefictStateChange = async (e) => {
    const selectedValue = e.target.value;
    setDeficitState(selectedValue);
    const response = await fetch("/data/Updated_railhead_list.xlsx");
    const arrayBuffer = await response.arrayBuffer();
    const data = new Uint8Array(arrayBuffer);
    const workbook = XLSX.read(data, { type: "array" });
    const sheetName = workbook.SheetNames[0];
    const sheet = workbook.Sheets[sheetName];
    const jsonData = XLSX.utils.sheet_to_json(sheet, { header: 1 });
    let dropdownOptions = [];
    let dropdownOptions_default = {
      value: "",
      label: "Please select Railhead",
    };
    for (let i = 0; i < jsonData.length; i++) {
      if (
        jsonData[i][1] &&
        jsonData[i][1].trim().toLowerCase() ===
          selectedValue.trim().toLowerCase()
      ) {
        dropdownOptions.push({ value: jsonData[i][0], label: jsonData[i][0] });
      }
    }
    dropdownOptions.sort((a, b) => a.label.localeCompare(b.label));
    dropdownOptions.unshift(dropdownOptions_default);
    setTotalDeficitRailhead(dropdownOptions);
  };

  const handleSurplusInlineStateChange = async (e) => {
    const selectedValue = e.target.value;
    setSurplusInlineState(selectedValue);
    const response = await fetch("/data/Updated_railhead_list.xlsx");
    const arrayBuffer = await response.arrayBuffer();
    const data = new Uint8Array(arrayBuffer);
    const workbook = XLSX.read(data, { type: "array" });
    const sheetName = workbook.SheetNames[0];
    const sheet = workbook.Sheets[sheetName];
    const jsonData = XLSX.utils.sheet_to_json(sheet, { header: 1 });
    let dropdownOptions = [];
    let dropdownOptions_default = {
      value: "",
      label: "Please select Railhead",
    };
    for (let i = 0; i < jsonData.length; i++) {
      if (
        jsonData[i][1] &&
        jsonData[i][1].trim().toLowerCase() ===
          selectedValue.trim().toLowerCase()
      ) {
        dropdownOptions.push({ value: jsonData[i][0], label: jsonData[i][0] });
      }
    }
    dropdownOptions.sort((a, b) => a.label.localeCompare(b.label));
    dropdownOptions.unshift(dropdownOptions_default);
    setTotalSurplusInlineRailhead(dropdownOptions);
  };

  const AddSurplusInline = async (e) => {};

  const handleDefictInlineStateChange = async (e) => {
    const selectedValue = e.target.value;
    setDeficitInlineState(selectedValue);
    const response = await fetch("/data/Updated_railhead_list.xlsx");
    const arrayBuffer = await response.arrayBuffer();
    const data = new Uint8Array(arrayBuffer);
    const workbook = XLSX.read(data, { type: "array" });
    const sheetName = workbook.SheetNames[0];
    const sheet = workbook.Sheets[sheetName];
    const jsonData = XLSX.utils.sheet_to_json(sheet, { header: 1 });
    let dropdownOptions = [];
    let dropdownOptions_default = {
      value: "",
      label: "Please select Railhead",
    };
    for (let i = 0; i < jsonData.length; i++) {
      if (
        jsonData[i][1] &&
        jsonData[i][1].trim().toLowerCase() ===
          selectedValue.trim().toLowerCase()
      ) {
        dropdownOptions.push({ value: jsonData[i][0], label: jsonData[i][0] });
      }
    }
    dropdownOptions.sort((a, b) => a.label.localeCompare(b.label));
    dropdownOptions.unshift(dropdownOptions_default);
    setTotalDeficitInlineRailhead(dropdownOptions);
  };

  const AddSurplus = (e) => {
    e.preventDefault();
    const existingIndex = surplus.findIndex(
      (row) =>
        row.Railhead === surplusRailhead &&
        row.State === surplusState &&
        row.Commodity === surplusCommodity
    );

    if (existingIndex !== -1) {
      const updatedSurplus = [...surplus];
      updatedSurplus[existingIndex].Value = updatedSurplus[
        existingIndex
      ].Value =
        parseInt(updatedSurplus[existingIndex].Value) + parseInt(surplusValue);
      setSurplus(updatedSurplus);
    } else {
      setSurplus((prev) => [
        ...prev,
        {
          Railhead: surplusRailhead,
          State: surplusState,
          Value: surplusValue,
          Commodity: surplusCommodity,
        },
      ]);
    }
    setSurplusRailhead("");
    setSurplusValue(1);
    setSurplusCommodity("");
  };

  const AddDeficit = (e) => {
    e.preventDefault();
    const existingIndex = deficit.findIndex(
      (row) =>
        row.Railhead === deficitRailhead &&
        row.State === deficitState &&
        row.Commodity === deficitCommodity
    );

    if (existingIndex !== -1) {
      const updatedDeficit = [...deficit];
      updatedDeficit[existingIndex].Value =
        parseInt(updatedDeficit[existingIndex].Value) + parseInt(deficitValue);
      setDeficit(updatedDeficit);
    } else {
      setDeficit((prev) => [
        ...prev,
        {
          Railhead: deficitRailhead,
          State: deficitState,
          Value: deficitValue,
          Commodity: deficitCommodity,
        },
      ]);
    }
    setDeficitRailhead("");
    setDeficitValue(1);
    setDeficitCommodity("");
  };

  const handleOptimizePlan = async (e) => {
    e.preventDefault();
    const requestBody = {
      surplus: surplus,
      deficit: deficit,
    };

    try {
      const response = await fetch(ProjectIp + "/Daily_Planner", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        credentials: "include",
        body: JSON.stringify(requestBody),
      });

      if (response.status === 200) {
        const jsonResponse = await response.json();
        if (jsonResponse.status === 1) {
          alert("Data send to Backend");
        } else {
          console.log(jsonResponse);
          alert("Error uploading file");
        }
      } else {
        alert("Failed to send data. Please try again.");
      }
    } catch (error) {
      console.error("Error sending data:", error);
      alert("An error occurred. Please try again later.");
    }
  };

  return (
    <div>
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          width: "60vw",
        }}
      >
        <div style={{ display: "flex", flexDirection: "column" }}>
          <strong style={{ fontSize: "16px", padding: "5px" }}>
            Select Origin State
          </strong>
          <select
            style={{
              width: "200px",
              padding: "5px",
              marginRight: 25,
            }}
            onChange={handleSurplusStateChange}
            value={surplusState}
          >
            <option value="default">Select Origin State</option>
            <option value="Andhra Pradesh">Andhra Pradesh</option>
            <option value="Bihar">Bihar</option>
            <option value="Chattisgarh">Chattisgarh</option>
            <option value="Goa">Goa</option>
            <option value="Gujarat">Gujarat</option>
            <option value="Haryana">Haryana</option>
            <option value="Jammu & Kashmir">Jammu & Kashmir</option>
            <option value="Jharkhand">Jharkhand</option>
            <option value="Karnataka">Karnataka</option>
            <option value="Kerala">Kerala</option>
            <option value="MP">Madhya Pradesh</option>
            <option value="Maharashtra">Maharashtra</option>
            <option value="NE">North East</option>
            <option value="Odisha">Odisha</option>
            <option value="Punjab">Punjab</option>
            <option value="Rajasthan">Rajasthan</option>
            <option value="Tamil Nadu">Tamil Nadu</option>
            <option value="Telangana">Telangana</option>
            <option value="UP">Uttar Pradesh</option>
            <option value="Uttarakhand">Uttarakhand</option>
            <option value="West Bengal">West Bengal</option>
          </select>
        </div>
        <div style={{ display: "flex", flexDirection: "column" }}>
          <strong style={{ fontSize: "16px", padding: "5px" }}>
            Select Origin Railhead
          </strong>
          <select
            style={{
              width: "200px",
              padding: "5px",
            }}
            onChange={(e) => setSurplusRailhead(e.target.value)}
            value={surplusRailhead}
          >
            {totalSurplusRailhead.map((option) => (
              <option key={option.value} value={option.value}>
                {option.label}
              </option>
            ))}
          </select>
        </div>
        <div style={{ display: "flex", flexDirection: "column" }}>
          <strong
            style={{
              width: "200px",
              padding: "5px",
            }}
          >
            Select Commodity
          </strong>
          <select
            value={surplusCommodity}
            onChange={(e) => {
              setSurplusCommodity(e.target.value);
            }}
          >
            <option value="">Select Commodity</option>
            <option value="Rice">Rice</option>
            <option value="Wheat">Wheat</option>
            <option value="RRA">RRA</option>
            <option value="FRK RRA">FRK RRA</option>
            <option value="FRK BR">FRK BR</option>
            <option value="Coarse Grain">Coarse Grains</option>
            <option value="W+ CGR">W+ CGR</option>
            <option value="FRK+CGR">FRK+CGR</option>
          </select>
        </div>
        <div style={{ display: "flex", flexDirection: "column" }}>
          <strong style={{ fontSize: "16px", padding: "5px" }}>
            Enter Value:
          </strong>
          <input
            type="number"
            min={1}
            onChange={(e) => setSurplusValue(e.target.value)}
            value={surplusValue}
          />
        </div>
        <button
          onClick={AddSurplus}
          style={{
            backgroundColor: "orange",
            width: 70,
            height: 40,
          }}
        >
          Add
        </button>
      </div>
      <div>Surplus</div>
      <table>
        <thead>
          <tr>
            <th>Sno</th>
            <th>Railhead</th>
            <th>State</th>
            <th>Value</th>
            <th>Commodity</th>
          </tr>
        </thead>
        <tbody>
          {surplus.map((row, index) => (
            <tr key={index}>
              <td>{index}</td>
              <td>{row.Railhead}</td>
              <td>{row.State}</td>
              <td>{row.Value}</td>
              <td>{row.Commodity}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          width: "60vw",
        }}
      >
        <div style={{ display: "flex", flexDirection: "column" }}>
          <strong style={{ fontSize: "16px", padding: "5px" }}>
            Select Destination State
          </strong>
          <select
            style={{
              width: "200px",
              padding: "5px",
              marginRight: 25,
            }}
            onChange={handleDefictStateChange}
            value={deficitState}
          >
            <option value="default">Select Origin State</option>
            <option value="Andhra Pradesh">Andhra Pradesh</option>
            <option value="Bihar">Bihar</option>
            <option value="Chattisgarh">Chattisgarh</option>
            <option value="Goa">Goa</option>
            <option value="Gujarat">Gujarat</option>
            <option value="Haryana">Haryana</option>
            <option value="Jammu & Kashmir">Jammu & Kashmir</option>
            <option value="Jharkhand">Jharkhand</option>
            <option value="Karnataka">Karnataka</option>
            <option value="Kerala">Kerala</option>
            <option value="MP">Madhya Pradesh</option>
            <option value="Maharashtra">Maharashtra</option>
            <option value="NE">North East</option>
            <option value="Odisha">Odisha</option>
            <option value="Punjab">Punjab</option>
            <option value="Rajasthan">Rajasthan</option>
            <option value="Tamil Nadu">Tamil Nadu</option>
            <option value="Telangana">Telangana</option>
            <option value="UP">Uttar Pradesh</option>
            <option value="Uttarakhand">Uttarakhand</option>
            <option value="West Bengal">West Bengal</option>
          </select>
        </div>
        <div style={{ display: "flex", flexDirection: "column" }}>
          <strong style={{ fontSize: "16px", padding: "5px" }}>
            Select Destination Railhead
          </strong>
          <select
            style={{
              width: "200px",
              padding: "5px",
            }}
            onChange={(e) => setDeficitRailhead(e.target.value)}
            value={deficitRailhead}
          >
            {totalDeficitRailhead.map((option) => (
              <option key={option.value} value={option.value}>
                {option.label}
              </option>
            ))}
          </select>
        </div>
        <div style={{ display: "flex", flexDirection: "column" }}>
          <strong
            style={{
              width: "200px",
              padding: "5px",
            }}
          >
            Select Commodity
          </strong>
          <select
            value={deficitCommodity}
            onChange={(e) => {
              setDeficitCommodity(e.target.value);
            }}
          >
            <option value="">Select Commodity</option>
            <option value="Rice">Rice</option>
            <option value="Wheat">Wheat</option>
            <option value="RRA">RRA</option>
            <option value="FRK RRA">FRK RRA</option>
            <option value="FRK BR">FRK BR</option>
            <option value="Coarse Grains">Coarse Grains</option>
            <option value="W+ CGR">W+ CGR</option>
            <option value="FRK+CGR">FRK+CGR</option>
          </select>
        </div>
        <div style={{ display: "flex", flexDirection: "column" }}>
          <strong style={{ fontSize: "16px", padding: "5px" }}>
            Enter Value:
          </strong>
          <input
            type="number"
            min={1}
            onChange={(e) => setDeficitValue(e.target.value)}
            value={deficitValue}
          />
        </div>
        <button
          onClick={AddDeficit}
          style={{
            backgroundColor: "orange",
            width: 70,
            height: 40,
          }}
        >
          Add
        </button>
      </div>
      <div>Deficit</div>
      <table>
        <thead>
          <tr>
            <th>Sno</th>
            <th>Railhead</th>
            <th>State</th>
            <th>Value</th>
            <th>Commodity</th>
          </tr>
        </thead>
        <tbody>
          {deficit.map((row, index) => (
            <tr key={index}>
              <td>{index}</td>
              <td>{row.Railhead}</td>
              <td>{row.State}</td>
              <td>{row.Value}</td>
              <td>{row.Commodity}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          width: "60vw",
        }}
      >
        <div style={{ display: "flex", flexDirection: "column" }}>
          <strong style={{ fontSize: "16px", padding: "5px" }}>
            Select Inline State
          </strong>
          <select
            style={{ width: "200px", padding: "5px" }}
            onChange={handleSurplusInlineStateChange}
            value={surplusInlineState}
          >
            <option value="default">Select Destination Inline State</option>
            <option value="Andhra Pradesh">Andhra Pradesh</option>
            <option value="Bihar">Bihar</option>
            <option value="Chattisgarh">Chattisgarh</option>
            <option value="Goa">Goa</option>
            <option value="Gujarat">Gujarat</option>
            {/* <option value="Haryana">Haryana</option> */}
            <option value="Jammu & Kashmir">Jammu & Kashmir</option>
            <option value="Jharkhand">Jharkhand</option>
            <option value="Karnataka">Karnataka</option>
            <option value="Kerala">Kerala</option>
            {/* <option value="MP">Madhya Pradesh</option> */}
            <option value="Maharashtra">Maharashtra</option>
            <option value="NE">North East</option>
            <option value="Odisha">Odisha</option>
            {/* <option value="Punjab">Punjab</option> */}
            <option value="Rajasthan">Rajasthan</option>
            <option value="Tamil Nadu">Tamil Nadu</option>
            <option value="Telangana">Telangana</option>
            <option value="UP">Uttar Pradesh</option>
            <option value="Uttarakhand">Uttarakhand</option>
            <option value="West Bengal">West Bengal</option>
          </select>
        </div>
        <div style={{ display: "flex", flexDirection: "column" }}>
          <strong style={{ fontSize: "16px", padding: "5px" }}>
            Select Inline Railhead
          </strong>
          <select
            style={{ width: "200px", padding: "5px" }}
            onChange={(e) => setSurplusInlineRailhead(e.target.value)}
            value={surplusInlineRailhead}
          >
            {totalSurplusInlineRailhead.map((option) => (
              <option key={option.value} value={option.value}>
                {option.label}
              </option>
            ))}
          </select>
        </div>
        <div style={{ display: "flex", flexDirection: "column" }}>
          <strong style={{ fontSize: "16px", padding: "5px" }}>
            Select Inline State
          </strong>
          <select
            style={{ width: "200px", padding: "5px" }}
            onChange={handleDefictInlineStateChange}
            value={deficitInlineState}
          >
            <option value="default">Select Inline State</option>
            <option value="Andhra Pradesh">Andhra Pradesh</option>
            <option value="Bihar">Bihar</option>
            <option value="Chattisgarh">Chattisgarh</option>
            <option value="Goa">Goa</option>
            <option value="Gujarat">Gujarat</option>
            {/* <option value="Haryana">Haryana</option> */}
            <option value="Jammu & Kashmir">Jammu & Kashmir</option>
            <option value="Jharkhand">Jharkhand</option>
            <option value="Karnataka">Karnataka</option>
            <option value="Kerala">Kerala</option>
            {/* <option value="MP">Madhya Pradesh</option> */}
            <option value="Maharashtra">Maharashtra</option>
            <option value="NE">North East</option>
            <option value="Odisha">Odisha</option>
            {/* <option value="Punjab">Punjab</option> */}
            <option value="Rajasthan">Rajasthan</option>
            <option value="Tamil Nadu">Tamil Nadu</option>
            <option value="Telangana">Telangana</option>
            <option value="UP">Uttar Pradesh</option>
            <option value="Uttarakhand">Uttarakhand</option>
            <option value="West Bengal">West Bengal</option>
          </select>
        </div>
        <div style={{ display: "flex", flexDirection: "column" }}>
          <strong style={{ fontSize: "16px", padding: "5px" }}>
            Select Inline Railhead
          </strong>
          <select
            style={{ width: "200px", padding: "5px" }}
            onChange={(e) => setDeficitInlineRailhead(e.target.value)}
            value={deficitInlineRailhead}
          >
            {totalDeficitInlineRailhead.map((option) => (
              <option key={option.value} value={option.value}>
                {option.label}
              </option>
            ))}
          </select>
        </div>
        <button
          onClick={AddSurplusInline}
          style={{
            backgroundColor: "orange",
            width: 70,
            height: 40,
          }}
        >
          Add
        </button>
      </div>
      <button onClick={handleOptimizePlan}>Optimize solution </button>
    </div>
  );
}

export default Surplus;
