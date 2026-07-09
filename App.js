import { useState } from "react";
import Upload from "./components/Uploads";
import Receipt from "./components/Receipt";
import './App.css';


export default function App() {
    const[ receipt, setReceipt] = useState(null);
    const[ loading, setLoading] = useState(false);
    const[ error, setError] = useState(null);

    const handleFileChange = async (file) => {
        setLoading(true);
        setError(null);
    

    const fmtdata = new FormData();
    fmtdata.append("image", file);

    try {
        const response = await fetch("http://localhost:5000/scan", {
            method: "POST",
            body: fmtdata,
        });

        const data = await response.json();
        setReceipt(data);
    } catch(err) {
        setError("Failed to scan receipt: Try again")
    } finally {
        setLoading(false);
    }
};


return (
    <div className="app-container">
        <h1 className="app-title">Receipt Summary</h1>
        <p className="app-subtitle"> Upload a receipt to extract details</p>
        <Upload onUpload={handleFileChange} />
        {loading && (
            <div className="loading-container">
                <div className="loading-spinner"></div>
                <p>Scanning receipt.....</p>
            </div>
        )}
        {error && <p style={{ color: "red"}}>{error}</p>}
        {receipt && <Receipt data={receipt} />}
    </div>

   );

}


