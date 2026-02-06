
import { useEffect, useState } from 'react';

export default function AdminAudits(){
  const [items, setItems] = useState([]);

  useEffect(()=>{
    fetch('http://localhost:8000/admin/audits?limit=50')
      .then(r=>r.json()).then(d=>setItems(d.items||[]))
      .catch(()=>setItems([]));
  },[]);

  return (
    <div className="card">
      <div className="cardTitle">Admin: Audit Logs</div>
      <div className="metric">Shows latest audit.log entries (founder-only endpoint).</div>
      <pre className="mono">{items.join('\n')}</pre>
    </div>
  )
}
