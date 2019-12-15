#!/usr/bin/env python
# -*- coding: utf-8 -*-

bill_amount = int(input("What is the bill amount?"))
tip_rate = int(input("What is the tip rate?"))

tip = round(bill_amount * (tip_rate / 100), 2)
total = bill_amount + tip

print("Tip: $", tip)
print("Total: $", total)
