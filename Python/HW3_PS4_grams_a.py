# Alex Grams
# 1163814
# Finds genes in inputted genomes

def checkGenome(genome:str)->None:
    # Gets all genes in inputted genome
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
    

# Output
##>>> Test case 1
##==== RESTART: C:/Users/Alex/Documents/IVC/CS 10 HW/HW3/HW3_PS4_grams_a.py ====
##Enter number of genomes: 6
##Enter a genome string: TTATGTTTTAAGGATGGGGCGTTAGTT
##TTT
##GGGCGT
##
##Enter a genome string: TGTGTGTATAT
##No genes found
##
##Enter a genome string: TGATGCTCTAAGGATGCGCCGTTGATT
##CTC
##CGCCGT
##
##Enter a genome string: TGATGCTCTAGAGATGCGCCGTTGAATAT
##CTC
##CGCCGT
##
##Enter a genome string: TGATGCGTCTAAGAGACTGCTCGCCGGTTGAATAT
##No genes found
##
##Enter a genome string: TGATGGCTCCTATGAGAATGGCGCCCGTTTCGAAATAT
##No genes found
##
##>>> Test case 2
##==== RESTART: C:/Users/Alex/Documents/IVC/CS 10 HW/HW3/HW3_PS4_grams_a.py ====
##Enter number of genomes: 0
##>>> Test case 3
##==== RESTART: C:\Users\Alex\Documents\IVC\CS 10 HW\HW3\HW3_PS4_grams_a.py ====
##Enter number of genomes: 1
##Enter a genome string: ACTGGGTTTCAAATTTGGGAAACCTTTAGACTAGCTAG
##No genes found
##>>> Test case 4
##==== RESTART: C:\Users\Alex\Documents\IVC\CS 10 HW\HW3\HW3_PS4_grams_a.py ====
##Enter number of genomes: 3
##Enter a genome string: ACTGACTTTAGGGGTTTTCCCGGGAAAACCCGGTTT
##No genes found
##
##Enter a genome string: TGATGCTCTAAGGTGATGCTCTAAGGTGATGCTCTAAGG
##CTC
##CTC
##CTC
##
##Enter a genome string: TGATGCTCTAAGGAGTGATGCTCT
##CTC
##
##>>> Test case 5
##==== RESTART: C:\Users\Alex\Documents\IVC\CS 10 HW\HW3\HW3_PS4_grams_a.py ====
##Enter number of genomes: 1
##Enter a genome string: TTAGGGGTTTTCCCGGGAAAATTAGGGGTTTTCCCGGGAAAATTAGGGGTTTTCCCGGGAAAA
##No genes found
