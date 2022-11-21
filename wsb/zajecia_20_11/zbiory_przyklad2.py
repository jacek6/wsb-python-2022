A = {1, 2, 3, 4}
B = {1, 2, 30, 40}

print("Suma:", A.union(B))  # wszystkie elementy zbiorów A i B
print("Część wspólna:", A.intersection(B))  # część wspólna zbiorów A i B
print("Różnica A-B:", A.difference(B))
print("Różnica B-A:", B.difference(A))
print("Różnica symetryczna:", A.symmetric_difference(B))

print("Zbior A ma długość ", len(A), " - zbior A: ", A)
