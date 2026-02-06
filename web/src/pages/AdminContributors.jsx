
export default function AdminContributors(){
  return (
    <div className="card">
      <div className="cardTitle">Admin: Contributors Pool</div>
      <div className="metric">Set contributor weights and distribute the contributors_pool into payouts.</div>
      <ul>
        <li>POST /contributors/set</li>
        <li>GET /contributors/list</li>
        <li>POST /distribute/contributors</li>
      </ul>
    </div>
  )
}
