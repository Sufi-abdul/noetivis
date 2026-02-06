
export default function AdminCompliance(){
  return (
    <div className="card">
      <div className="cardTitle">Admin: Compliance</div>
      <div className="metric">Declared transactions, exportable reports.</div>
      <ul>
        <li>GET /compliance/dashboard</li>
        <li>GET /compliance/exports/tax.csv</li>
      </ul>
    </div>
  )
}
