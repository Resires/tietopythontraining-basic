ALICE_SET = {1, 2, 3, 4}
BOB_SET = {1, 2, 10000000}

print("Numerical colors of cubes in both sets:",
      ALICE_SET & BOB_SET)
print("Numerical colors of cubes only in Alice's set",
      ALICE_SET - BOB_SET)
print("Numerical colors of cubes only in Bob's set",
      BOB_SET - ALICE_SET)
