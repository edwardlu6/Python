while True:
    orders = int(input('How many orders of Swedish Fish will you be processing today?'))
    if orders <= 0:
        print('Invalid entry, you must process at least one order')
    else:
        break
total = 0
for i in range(1, orders+1):
    print('Order #', i, sep = '')
    while True:
        fish = int(input('How many Swedish Fish will this client be ordering?'))
        if fish <= 0:
            print('Invalid entry, clients must order at least one Swedish Fish')
            continue
        else:
            total += fish
            break
print('In total your clients are ordering', total, 'Swedish Fish')
print('If you were to purchase these fish at the base-cost per fish ($0.05) this order would cost $', format(total * 0.05, '.2f'), sep = '')
if total < 100:
    print('This is the lowest price you can pay for this number of fish')
elif total >= 100:
    single = total - ((total - (total // 14400) * 14400) // 100) * 100 - (total // 14400) * 14400
    packs = (total - (total // 14400) * 14400) // 100
    cases = total // 14400
    print('This purchase qualifies for a bulk discount due to the number of fish being purchased')
    print('The lowest cost you can pay for this purchase is as follows:')
    print('* ', single, ' single fish @ $0.05 each = $', format(single * 0.05, '.2f'), sep = '')
    print('* ', packs, ' packs of 100 fish @ $4.00 per pack = $', format(packs * 4.00, '.2f'), sep = '')
    print('* ', cases, ' cases of 100 packs of fish (14,400 fish per case) @ $460.00 per case = $', format(cases * 460.00, '.2f'), sep = '')
    print('Total cost with bulk discount: $', format(single * 0.05 + packs * 4.00 + cases * 460.00, '.2f'), sep = '')
    print('Savings: $', format(total * 0.05 - (single * 0.05 + packs * 4.00 + cases * 460.00), '.2f'), sep = '')
