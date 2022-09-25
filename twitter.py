x = input ("kata :").strip()

for huruf in "aiueoAIUEO" :
    x = x.replace(huruf, "").strip()

print(f'\n{x}')