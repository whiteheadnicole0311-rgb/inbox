"""Texas Personal Property Rental-Purchase (RTO) early purchase option calculator."""


def texas_rto_calculator(
    cash_price,
    rental_payment,
    total_terms,
    terms_paid,
    payment_frequency="weekly",
    epo_factor=0.60,
):
    """
    Calculates the Texas Personal Property Rental-Purchase early purchase (EPO) payoff.

    payment_frequency: "weekly" or "monthly" — determines the 90-day cutoff in terms.
        The 90-day window is ~13 terms for weekly plans, ~3 terms for monthly plans.
        This must be passed explicitly: inferring it from total_terms is unreliable
        (e.g. a 20-week weekly plan would be misread as monthly, cutting the 90-day
        "same as cash" window down to 3 weeks instead of ~13).
    epo_factor: The multiplier applied to remaining payments after 90 days (commonly 50% to 70%).
    """
    if payment_frequency not in ("weekly", "monthly"):
        raise ValueError("payment_frequency must be 'weekly' or 'monthly'")
    if cash_price <= 0 or rental_payment <= 0:
        raise ValueError("cash_price and rental_payment must be positive")
    if total_terms <= 0 or not (0 <= terms_paid <= total_terms):
        raise ValueError("terms_paid must be between 0 and total_terms")

    total_scheduled_cost = rental_payment * total_terms
    total_paid_so_far = rental_payment * terms_paid
    remaining_scheduled_balance = total_scheduled_cost - total_paid_so_far

    # 90-day window: ~13 weekly terms or ~3 monthly terms
    ninety_day_term_cutoff = 13 if payment_frequency == "weekly" else 3
    is_within_90_days = terms_paid <= ninety_day_term_cutoff

    if is_within_90_days:
        # Standard Texas 90-day buyout: Cash price minus base rent applied (or flat cash price)
        early_purchase_price = max(cash_price - (total_paid_so_far * 0.75), cash_price * 0.2)
        stage = "Within 90-Day 'Same as Cash' Period"
    else:
        # Standard post-90 day formula
        early_purchase_price = remaining_scheduled_balance * epo_factor
        stage = "Standard Early Purchase Option (Post-90 Days)"

    # Cap total cost to ensure it never exceeds the total scheduled payments
    if total_paid_so_far + early_purchase_price > total_scheduled_cost:
        early_purchase_price = remaining_scheduled_balance

    results = {
        "stage": stage,
        "total_scheduled_cost": total_scheduled_cost,
        "total_paid_so_far": total_paid_so_far,
        "remaining_scheduled_balance": remaining_scheduled_balance,
        "early_purchase_price": early_purchase_price,
        "total_combined_cost": total_paid_so_far + early_purchase_price,
    }

    print(f"--- Texas RTO Calculator Results ({stage}) ---")
    print(f"Total Cost if Rented to Term: ${results['total_scheduled_cost']:,.2f}")
    print(f"Total Amount Paid to Date:    ${results['total_paid_so_far']:,.2f}")
    print(f"Remaining Scheduled Balance:  ${results['remaining_scheduled_balance']:,.2f}")
    print("==================================================")
    print(f"ESTIMATED EPO BUYOUT PRICE:   ${results['early_purchase_price']:,.2f}")
    print(f"Total Combined Cost if Bought Now: ${results['total_combined_cost']:,.2f}")

    return results


if __name__ == "__main__":
    # $1,000 cash price item, $25/week for 104 weeks, buying out at week 20
    texas_rto_calculator(
        cash_price=1000,
        rental_payment=25,
        total_terms=104,
        terms_paid=20,
        payment_frequency="weekly",
        epo_factor=0.60,
    )
