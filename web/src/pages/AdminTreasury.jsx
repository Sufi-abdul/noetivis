
import { useState } from 'react';

export default function AdminTreasury(){
  const [pool, setPool] = useState('contributors_pool');
  const [amount, setAmount] = useState(50);

  return (
    <div className="card">
      <div className="cardTitle">Admin: Treasury</div>
      <div className="metric">Manage platform pools (founder/contributors/ops)</div>
      <div style={{display:'flex', gap:10, flexWrap:'wrap'}}>
        <input value={pool} onChange={e=>setPool(e.target.value)} />
        <input type="number" value={amount} onChange={e=>setAmount(Number(e.target.value))} />
      </div>
      <div className="mono" style={{marginTop:10}}>
        Call backend:
        <div>POST /treasury/add?pool={pool}&amount={amount}</div>
      </div>
    </div>
  )
}
