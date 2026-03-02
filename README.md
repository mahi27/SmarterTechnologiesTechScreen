📦 Package Sorting <br />
This module contains the sort(width, height, length, mass) function used to classify packages in a robotic automation system.

Rules:
1) Bulky → Volume ≥ 1,000,000 cm³ OR any dimension ≥ 150 cm
2) Heavy → Mass ≥ 20 kg
   
Stack Assignment
 - STANDARD → Not bulky and not heavy
 - SPECIAL → Bulky OR heavy
 - REJECTED → Bulky AND heavy

Validation
 - All inputs must be numeric (int or float)
 - Dimensions must be > 0
 - Mass must be ≥ 0

Example <br />
result = sort(100, 100, 100, 10)
print(result)  # STANDARD
