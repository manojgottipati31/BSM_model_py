from option import Option

if __name__ == '__main__':
    s = input("Stock Price (S): ")
    k = input("Strike Price (K): ")
    r = input("Rate in decimals (r): ")
    t = input("Time (T): ")
    vol = input("Volatility (sigma): ")
    option_type = input("Option (C/P): ")
    if option_type.upper()=='C':
        option_type = "call"
    else:
        option_type = "put"

    option = Option(float(s), float(k), float(r), float(t), float(vol), option_type)

    print("Option price:", option.price)
    print("Delta:", option.delta)
    print("Gamma:", option.gamma)
    print("Vega:", option.vega)
    print("Theta:", option.theta)
    print("Rho:", option.rho)
