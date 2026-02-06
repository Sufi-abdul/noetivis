
import { useEffect, useState } from 'react';
export default function Marketplace(){
  const [items, setItems] = useState([]);
  useEffect(()=>{
    fetch('http://localhost:8000/marketplace/browse').then(r=>r.json()).then(d=>setItems(d.items||[])).catch(()=>setItems([]));
  },[]);
  return (
    <div className="card">
      <div className="cardTitle">Marketplace</div>
      <pre className="mono">{JSON.stringify(items, null, 2)}</pre>
    </div>
  )
}
