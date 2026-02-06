
import React, { useEffect, useState } from 'react'
import './styles.css'

function Card({title, children}){
  return (
    <div className="card">
      <div className="cardTitle">{title}</div>
      <div>{children}</div>
    </div>
  )
}

export default function App(){
  const [health, setHealth] = useState(null)

  useEffect(()=>{
    fetch('http://localhost:8000/health')
      .then(r=>r.json())
      .then(setHealth)
      .catch(()=>setHealth({status:'API offline (start backend)'}))
  },[])

  return (
    <div className="wrap">
      <header className="header">
        <div className="brand">NOETIVIS</div>
        <div className="tag">Infinite Intelligence & Value OS</div>
      </header>
      <div className="grid">
        <Card title="System Status"><pre className="mono">{JSON.stringify(health, null, 2)}</pre></Card>
        <Card title="Earnings"><div className="metric">Founder 20% · Contributors 10% · Partners 5% · Owners 65%</div></Card>
        <Card title="Creator Economy"><div className="metric">Music · Video · Photo · Writing</div></Card>
        <Card title="Monetization"><div className="metric">Ads · Affiliates · Commerce</div></Card>
      </div>
    </div>
  )
}
