
export default function AdminTenants(){
  return (
    <div className="card">
      <div className="cardTitle">Admin: Tenants</div>
      <div className="metric">Multi-tenant white-label configuration (founder-only).</div>
      <ul>
        <li>POST /tenants/create</li>
        <li>GET /tenants/list</li>
      </ul>
    </div>
  )
}
