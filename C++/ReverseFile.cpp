// Author: Alex Grams
// Gets the number of lines in a file and writes the contents of the file in reverse order to another file

#include "pch.h"
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

// Prototypes
int getNumLines(ifstream &in);
void readFile(ifstream &in, string lines[]);
void reverseFile(const string lines[], ofstream &out, const int &numLines);

int main()
{
	ifstream in("Lab_HW9_1_Input.txt");
	if (!in.is_open())
	{
		cerr << "File not open" << endl;
		exit(1);
	}

	int numLines = getNumLines(in);
	string *lines = new string[numLines];
	in.seekg(0, ios::beg);
	readFile(in, lines);

	ofstream out("reverse_output.txt");
	if (!out.is_open())
	{
		cerr << "File not open" << endl;
		exit(1);
	}
	reverseFile(lines, out, numLines);

	delete[] lines;
}

// Find and returns the number of lines in a file
int getNumLines(ifstream &in) 
{
	int total = 0;
	string input;

	while (in.good())
	{
		getline(in, input);
		if (input != "")
			total++;
	}

	return total;
}

// Puts a file's stored data into an array
void readFile(ifstream &in, string lines[])
{
	string input;
	int i = 0;

	while (in.good())
	{
		getline(in, input);
		lines[i] = input;
		i++;
	}
}

// Prints out the contents of a string array in reverse order
void reverseFile(const string lines[], ofstream &out, const int &numLines)
{
	for (int i = numLines - 1; i >= 0; i--)
	{
		out << lines[i] << endl;
	}
}
