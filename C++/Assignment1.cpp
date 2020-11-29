//----------------------------------------------------------------------------//
//                                                                            //
// Name:   Alex Grams                                                         //
//                                                                            //
//----------------------------------------------------------------------------//

#include "pch.h"
#include <iostream>
#include <string>
#include <iomanip>

#define ACRES 1000;

using namespace std;

class Crop
{
private:
	string name;
	double cost, bushel, increase;
	int yield;
public:
	void setData(string nName, double nCost, double nBushel, double nIncrease, int nYield)
	{
		name = nName;
		cost = nCost;
		bushel = nBushel;
		increase = nIncrease;
		yield = nYield;
	}

	string getName()
	{
		return name;
	}

	double getCost()
	{
		return cost;
	}

	double getBushel()
	{
		return bushel;
	}

	double getIncrease()
	{
		return increase;
	}

	int getYield()
	{
		return yield;
	}
};

// Function prototypes.
void calculate(Crop crop, double &minProfit, double &maxProfit, double &avgProfit);
void inputData(Crop crops[]);
void printResults(Crop crop, double minProfit, double maxProfit, double avgProfit);

int main()
{
	Crop crops[4];
	double minProfit, maxProfit, avgProfit, bestProfit = 0;
	string bestCrop;

	inputData(crops);

	cout << left << setprecision(2) << fixed << setw(22) << "\nCrop" << setw(26) << "Minimum Profit" << setw(26) << "Maximum Profit" << "Average Profit" << endl;
	for (int i = 0; i < 4; i++)
	{
		calculate(crops[i], minProfit, maxProfit, avgProfit);
		printResults(crops[i], minProfit, maxProfit, avgProfit);
		if (avgProfit > bestProfit)
		{
			bestProfit = avgProfit;
			bestCrop = crops[i].getName();
		}
	}

	cout << endl << "Old MacDonald, you should plant " << bestCrop << endl << endl;
}

// Calculates the minimum, maximum, and average profit from data memebers within the inputted Crop object
void calculate(Crop crop, double &minProfit, double &maxProfit, double &avgProfit)
{
	double minGrossProfit = crop.getYield() * crop.getBushel() * ACRES;
	double totalCost = crop.getCost() * ACRES;

	minProfit = minGrossProfit - totalCost;
	maxProfit = minGrossProfit + (minGrossProfit * (crop.getIncrease() / 100)) - totalCost;
	avgProfit = (maxProfit + minProfit) / 2;
}

// Sets data member values of array of four crops
void inputData(Crop crops[])
{
	string name;
	double cost, bushel, increase;
	int yield;

	for (int i = 0; i < 4; i++)
	{
		cout << "Enter the crop name: ";
		getline(cin, name);
		cout << "Enter the cost, yield, price per bushel, and increase data: ";
		cin >> cost;
		cin >> yield;
		cin >> bushel;
		cin >> increase;
		cin.ignore();

		crops[i].setData(name, cost, bushel, increase, yield);
	}
}

// Displays minimum, maximum, and average profit of a given inputted crop
void printResults(Crop crop, double minProfit, double maxProfit, double avgProfit)
{
	cout << left << setw(25) << crop.getName() << "$" << setw(25) << minProfit << "$" << setw(25) << maxProfit << "$" << avgProfit << endl;
}

/*
Enter the crop name: Sweet corn
Enter the cost, yield, price per bushel, and increase data: 45.25 173 .54 4.7
Enter the crop name: Wheat
Enter the cost, yield, price per bushel, and increase data: 43 200 .43 3.1
Enter the crop name: Kale
Enter the cost, yield, price per bushel, and increase data: 43.5 157 .61 4.3
Enter the crop name: Green beans
Enter the cost, yield, price per bushel, and increase data: 40.8 118 .72 2.7

Crop                 Minimum Profit            Maximum Profit            Average Profit
Sweet corn               $48170.00                 $52560.74                 $50365.37
Wheat                    $43000.00                 $45666.00                 $44333.00
Kale                     $52270.00                 $56388.11                 $54329.06
Green beans              $44160.00                 $46453.92                 $45306.96

Old MacDonald, you should plant Kale
*/