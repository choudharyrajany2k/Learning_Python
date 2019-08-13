#!/usr/bin/python
"""
Purpose: Demo for Set
"""
BANNER = 5*"*"
a= {1,2,3,4,56,6,7,1}

def GetBanner(message):
    print(BANNER+message+BANNER)

# set orders are random so the indexing is not possible

GetBanner("Print Set Demo")
print(f" a {a}")

GetBanner("Iteratable for set")
for item in a:
    print(f"itemsIn Set {item}")

GetBanner("Unique ports for a machine")
listofall_ports = {12,8080,23,234,2345,56}
print(f"listofall_ports {listofall_ports}")
print(f"sorted ports {sorted(listofall_ports,reverse=False)}")

GetBanner("SetOperation")
set_of_ports = {123,24,34,23,24,123}
print(f"dir(set_of_ports) {dir(set_of_ports)}")

for each_item in dir(set_of_ports):
    print(f"{print(each_item)if (not each_item.startswith('__')) else print()}")

