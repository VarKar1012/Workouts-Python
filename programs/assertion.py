# assert<cond>
# assert<cond><msg>

# assert 6>3
# print("condition success")

# assert 6>30
# print("assertion err")

assert 6>30, "condition failed" #msg will be displayed along assertion error
print("assertion err: execution stopped")