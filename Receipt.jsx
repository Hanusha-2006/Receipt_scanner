

function Receipt({ data }) {
    return (
        <div className="receipt-container">
            <h2 className="receipt-title"> Receipt Summary</h2>
            <table className="receipt-table" width="100%" border="1" style={{ borderCollapse: 'collapse' }} >

                <tr><td className="receipt-label"><b>Store_Name</b></td> <td className="receipt-price">{data.store_name} </td></tr>
                <tr><td className="receipt-label"><b>Date</b></td><td className="receipt-price">{data.date} </td></tr>
                <tr><td className="receipt-label"><b>Time</b></td><td className="receipt-price">{data.time} </td></tr>
                <tr><td className="receipt-label"><b>Tax</b></td><td className="receipt-price"> {data.tax} </td></tr>
                <tr><td className="receipt-label"><b>Sub-total</b></td><td className="receipt-price">{data.subtotal} </td></tr>
                <tr><td className="receipt-label"><b>Total</b></td><td className="receipt-price">{data.total} </td></tr>

            </table>
            <h3 className="receipt-items-title">Items Purchased </h3>
            {data.items.length > 0 ? (
                <table className="receipt-items-table" width="100%" border="1" cellPadding="8">
                    <thead>
                        <tr><th>Item</th><th>Price</th></tr>
                    </thead>
                    <tbody>
                        {data.items.map((item, i) => (
                            <tr key = {i}>
                                <td className="receipt-label">{item.name}</td>
                                <td className="receipt-price">{item.price}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            ) : (
                <p>No items found </p>
            )}
            </div>
    );
}            

export default Receipt;