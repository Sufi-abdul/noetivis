
def resolve_payees(attribution_row):
    # attribution_row can be None
    if not attribution_row:
        return {"owner_user_id": None, "partner_user_id": None, "reseller_user_id": None}
    return {
        "owner_user_id": getattr(attribution_row, "owner_user_id", None),
        "partner_user_id": getattr(attribution_row, "partner_user_id", None),
        "reseller_user_id": getattr(attribution_row, "reseller_user_id", None),
    }
