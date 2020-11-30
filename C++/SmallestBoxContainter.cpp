// Author: Alex Grams
// Takes 10 2D rectangular boxes as input from the user, then outputs the smallest 
// rectangle which fits all boxes. If the surrounding rectangle has at least 90% of
// its interior filled, then the boxes are considered to be efficiently arranged.
// The user inputs the size and position of each box using the coordinates of its four
// corners in the 2D plane.

#include "pch.h"
#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

// Box class 
class Box
{
public:
	Box();
	float getHeight() const;
	int getLength() const;
	int getWidth() const;
	int getMaxX() const;
	int getMaxY() const;
	int getMinX() const;
	int getMinY() const;
	float getVolume() const;
	string getName() const;
	void setData(const string &sName, const int &sMinX, const int &sMaxX, const int &sMinY, const int &sMaxY, const float &sHeight);

private:
	int minX, maxX, minY, maxY, length, width;
	float height;
	string name;
};

Box::Box()
{

}

int Box::getMaxX() const
{
	return maxX;
}

int Box::getMaxY() const
{
	return maxY;
}

int Box::getMinX() const
{
	return minX;
}

int Box::getMinY() const
{
	return minY;
}

float Box::getHeight() const
{
	return height;
}

int Box::getLength() const
{
	return length;
}

int Box::getWidth() const
{
	return width;
}

float Box::getVolume() const
{
	return length * width * height;
}

string Box::getName() const
{
	return name;
}

void Box::setData(const string &sName, const int &sMinX, const int &sMaxX, const int &sMinY, const int &sMaxY, const float &sHeight)
{
	name = sName;
	minX = sMinX;
	maxX = sMaxX;
	minY = sMinY;
	maxY = sMaxY;
	length = maxX - minX;
	width = maxY - minY;
	height = sHeight;
}

// Prototypes
void getBoxInput(Box *boxes);
float printBoxInformation(const Box *boxes);
float printMinimumContainer(Box *boxes);
istream& operator>>(istream &input, Box &box);
ostream& operator<<(ostream &output, const Box *boxes);
ostream& operator<<(ostream &output, const Box &box);

int main()
{
	Box boxes[10];
	float totalVolume, smallestContainerVolume, spaceUsed;

	getBoxInput(boxes);

	totalVolume = printBoxInformation(boxes);
	smallestContainerVolume = printMinimumContainer(boxes);
	spaceUsed = totalVolume / smallestContainerVolume;

	if (spaceUsed >= .9)
	{
		cout << "The layout is efficient, it uses " << spaceUsed * 100 << "% of the space." << endl;
	}
	else
	{
		cout << "The layout is not efficient, it wastes " << (1 - spaceUsed) * 100 << "% of the space." << endl;
	}

	return 0;
}

// Overloaded stream extraction operator to get information for one Box object
istream& operator>>(istream &input, Box &box)
{
	string name;
	int minX, maxX, minY, maxY, in;
	float height;

	getline(input, name);
	input >> minX >> minY;
	maxX = minX;
	maxY = minY;

	for (int i = 0; i < 3; i++)
	{
		input >> in;
		if (in < minX)
		{
			minX = in;
		}
		else if (in > maxX)
		{
			maxX = in;
		}

		input >> in;
		if (in < minY)
		{
			minY = in;
		}
		else if (in > maxY)
		{
			maxY = in;
		}
	}
	input >> height;

	box.setData(name, minX, maxX, minY, maxY, height);
	input.ignore();

	return input;
}

// Overloaded stream insertion operator to print index, description, and volume of ten boxes in an array
ostream& operator<<(ostream &output, const Box *boxes)
{
	for (int i = 0; i < 10; i++)
	{
		output << left << setw(20) << i + 1 << setw(20) << boxes[i].getName() << right << setw(20) << boxes[i].getVolume() << endl;
	}

	return output;
}

// Overloaded stream insertion operator to print information of one box
ostream& operator<<(ostream &output, const Box &box)
{
	output << "Length: " << (float)box.getLength() << " Width : " << (float)box.getWidth() << " Height : " << box.getHeight() << " Volume : " << box.getVolume() << " cu / units" << endl;
	return output;
}

// Gets input for box size
void getBoxInput(Box *boxes)
{
	for (int i = 0; i < 10; i++)
	{
		cin >> boxes[i];
	}
}

// Prints out the box number, description, and volume of each box, then prints and returns the total volume of all boxes
float printBoxInformation(const Box *boxes)
{
	float totalVolume = 0;

	cout << endl << left << setw(20) << "Box#" << setw(20) << "Description" << right << setw(20) << "Volume(cu/units)" << endl;
	cout << boxes;
	for (int i = 0; i < 10; i++)
	{
		totalVolume += boxes[i].getVolume();
	}
	
	cout << "\nThe total volume of the boxes is: " << setprecision(1) << fixed << totalVolume << " cu/units." << endl << endl;

	return totalVolume;
}

// Prints and returns the volume of the smallest container needed to fit all the boxes
float printMinimumContainer(Box *boxes)
{
	float minX = boxes[0].getMinX(), maxX = boxes[0].getMaxX(), minY = boxes[0].getMinY(), maxY = boxes[0].getMaxY(), maxHeight = boxes[0].getHeight();
	Box minBox;

	for (int i = 1; i < 10; i++)
	{
		if (boxes[i].getMinX() < minX)
			minX = boxes[i].getMinX();
		if (boxes[i].getMaxX() > maxX)
			maxX = boxes[i].getMaxX();
		if (boxes[i].getMinY() < minY)
			minY = boxes[i].getMinY();
		if (boxes[i].getMaxY() > maxY)
			maxY = boxes[i].getMaxY();
		if (boxes[i].getHeight() > maxHeight)
			maxHeight = boxes[i].getHeight();
	} 
	minBox.setData("", minX, maxX, minY, maxY, maxHeight);
	cout << "Minimum container specifications: " << endl << minBox << endl;

	return minBox.getVolume();
}

/*
SAMPLE OUTPUT:

Standard tools
0 0 0 5 14 5 14 0 5
Metric tools
0 10 5 10 5 5 0 5 5
Plastic parts
10 10 10 5 5 5 5 10 5
Steel parts
13 7 10 7 10 8 13 8 3.8
Aluminum parts
10 5 10 7 15 7 15 5 4.5
Rubber gaskets
0 14 4 10 0 10 4 14 4
Large bags
4 10 8 10 8 14 4 14 4
Small bags
8 10 8 14 12 14 12 10 4.5
Sealant
14 8 14 9 10 8 10 9 5
Liquid nitrogen
10 9 10 10 11 10 11 9 5

Box#                Description             Volume(cu/units)
1                   Standard tools                       350
2                   Metric tools                         125
3                   Plastic parts                        125
4                   Steel parts                         11.4
5                   Aluminum parts                        45
6                   Rubber gaskets                        64
7                   Large bags                            64
8                   Small bags                            72
9                   Sealant                               20
10                  Liquid nitrogen                        5

The total volume of the boxes is: 881.4 cu/units.

Minimum container specifications:
Length: 15.0 Width : 14.0 Height : 5.0 Volume : 1050.0 cu / units

The layout is not efficient, it wastes 16.1% of the space.

*/