
export default function AdminPayouts(){
  return (
    <div className="card">
      <div className="cardTitle">Admin: Payouts</div>
      <div className="metric">List pending payouts, batch them, lock and mark paid safely.</div>
      <ul>
        <li>GET /payouts/list?status=pending</li>
        <li>POST /batches/create</li>
        <li>POST /batches/lock?batch_id=...</li>
        <li>POST /safe/mark-paid?payout_id=...</li>
      </ul>
    </div>
  )
}
