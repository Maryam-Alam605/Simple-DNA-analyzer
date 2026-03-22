dna = input("Enter DNA sequence: ").upper()

countA=dna.count("A");
countC=dna.count("C");
countT=dna.count("T");
countG=dna.count("G");

print("Adenine: ", countA);
print("Cytosine: ", countC);
print("Thymine: ", countT);
print("Guanine: ", countG);

dnaLength = len(dna);

countCG = ((countC + countG)/dnaLength)*100;
countAT = ((countA + countT)/dnaLength)*100;

print("total bases: ", dnaLength);
print("CG content: ", countCG);
print("AT content: ", countAT);

for char in dna:
    if char not in "ACTG":
        print("invalid base")
        break;




