"""Print out all the melons in our inventory."""


from melons import melon_names, melon_seedlessness, melon_prices,melon_flesh,melon_rind,melon_weigh


def print_melon(name, seedless, price, flesh, rind, weight ):
    """Print each melon with corresponding attribute information."""

    # have_or_have_not = 'have'
    # if seedless:
    #     have_or_have_not = 'do not have'


    # print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')

    print(name)
    print("     seedless: {}".format(seedless))
    print("     price: {}".format(price))
    print("     melon_flesh: {}".format(flesh))
    print("     melon_weigh: {}".format(weight))
    print("     melon_rind: {}".format(rind))

for i in melon_names:
    print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i], melon_flesh[i], melon_rind[i],melon_weigh[i])
    melons_dict = {}

# seedless: False
#     price: 2.5
#     flesh_color: None
#     weight: None
#     rind_color: None