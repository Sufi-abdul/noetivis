
export default function AdminPlugins(){
  return (
    <div className="card">
      <div className="cardTitle">Admin: Plugins</div>
      <div className="metric">Register and list plugins per tenant.</div>
      <ul>
        <li>POST /plugins/register</li>
        <li>GET /plugins/list?tenant_slug=public</li>
      </ul>
    </div>
  )
}
