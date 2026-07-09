import fileIcon from './files_icon.png';

function Uploads({ onUpload }) {
    const handleFileChange = (event) => {
        const file = event.target.files[0];
        if (file) {
            onUpload(file);
        };
    };
    return (
        <div className="upload-container">
            {/* <div className="upload-icon">🧾</div> */}
            <p className="upload-title">Drag and drop your file here or click to select the file <img src={fileIcon} alt="File Icon" width="45px" height="48px" /></p>
            <div className="upload-dropzone">
            <input type ='file' accept='image/*' onChange={handleFileChange} className="upload-input" id="fileInput" />
            <label htmlFor="fileInput" className="upload-button">Choose File</label>
            </div>
        </div>
    );
};

export default Uploads;

