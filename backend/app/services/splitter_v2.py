
from dataclasses import dataclass

@dataclass
class Split:
    founder: float = 0.20
    contributors: float = 0.10
    partner: float = 0.05
    owner: float = 0.65
    # reseller is taken from partner share by default, not additional inflation
    reseller_from_partner: float = 0.40  # 40% of partner share goes to reseller when reseller exists

def split_with_reseller(amount: float, has_reseller: bool) -> dict:
    a = float(amount)
    founder = a * Split.founder
    contributors = a * Split.contributors
    partner_total = a * Split.partner
    owner = a * Split.owner

    if has_reseller:
        reseller = partner_total * Split.reseller_from_partner
        partner = partner_total - reseller
    else:
        reseller = 0.0
        partner = partner_total

    return {
        "founder": round(founder, 6),
        "contributors": round(contributors, 6),
        "partner": round(partner, 6),
        "reseller": round(reseller, 6),
        "owner": round(owner, 6),
    }
