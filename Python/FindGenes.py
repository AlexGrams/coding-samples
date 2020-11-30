# Author: Alex Grams
# Finds gene sequences in inputted genomes.
# A gene is a series of bases beginning with ATG and ending with TAG, TAA, or TGA.

def checkGenome(genome:str)->None:
    """Gets all genes in inputted genome"""
    index = 0
    allGenes = ""

    while index + 3 <= len(genome):
        if genome[index:index + 3] == "ATG":
            endIndex = index + 3

            while endIndex + 3 <= len(genome) and genome[endIndex:endIndex + 3] != "TAG" and genome[endIndex:endIndex + 3] != "TAA" and genome[endIndex:endIndex + 3] != "TGA" and genome[endIndex:endIndex + 3] != "ATG":
                endIndex += 3

            if endIndex + 3 <= len(genome)and genome[endIndex:endIndex + 3] != "ATG":
                allGenes += genome[index + 3:endIndex] + "\n"

            index = endIndex
        else:
            index += 1

    if allGenes == "":
        print("No genes found")
        print()
    else:
        print(allGenes)   


def main():
    times = int(input("Enter number of genomes: "))

    for index in range(times):
        genome = input("Enter a genome string: ")

        checkGenome(genome)


if __name__ == "__main__":
    main()
