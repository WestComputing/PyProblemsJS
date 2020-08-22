from decimal import Decimal

COMPETITORS_SHIPPING = Decimal('0.78')
MY_SHIPPING = Decimal('0.99')

while True:
    competitors_price = input("\nCompetitor's price: ")
    if not len(competitors_price):
        exit(0)
    else:
        competitors_price = Decimal(competitors_price)
    matching_price = Decimal(competitors_price + COMPETITORS_SHIPPING - MY_SHIPPING)
    print(f"Matching price: {matching_price}")
