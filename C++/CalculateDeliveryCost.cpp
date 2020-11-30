// Author: Alex Grams
// Calculates delivery charge for items of different types using polymorphism

#include "pch.h"
#include <iostream>
#include <iomanip>

using namespace std;

class Item
{
public:
	Item(const int &amt);
	virtual float calcCost() const = 0;
	virtual float calcDelivery() const = 0;

protected:
	int amount;
};

Item::Item(const int &amt)
	: amount(amt)
{

}

class Weight : public Item
{
public:
	Weight(const int &amt);
	virtual float calcCost() const;
	virtual float calcDelivery() const;
};

Weight::Weight(const int &amt)
	: Item(amt)
{

}

float Weight::calcCost() const
{
	return 0.05 * amount;
}

float Weight::calcDelivery() const
{
	return 100.00 + 10 * ceil(float(amount) / 1000);
}

class Volume : public Item
{
public:
	Volume(const int &amt);
	virtual float calcCost() const;
	virtual float calcDelivery() const;
};

Volume::Volume(const int &amt)
	: Item(amt)
{

}

float Volume::calcCost() const
{
	return 0.12 * amount;
}

float Volume::calcDelivery() const
{
	return 50 + ceil(float(amount) / 750) * 8;
}

class Quantity : public Item
{
public:
	Quantity(const int &amt);
	virtual float calcCost() const;
	virtual float calcDelivery() const;
};

Quantity::Quantity(const int &amt)
	: Item(amt)
{

}

float Quantity::calcCost() const
{
	if (amount > 0 && amount <= 10)
		return 0.11 * amount;
	else if (amount >= 11 && amount <= 50)
		return 0.09 * amount;
	else
		return 0.06 * amount;
}

float Quantity::calcDelivery() const
{
	return 50;
}

// Prototypes
float getCost(const Item &item);
float getDelivery(const Item &item);

int main()
{
	Weight weight(2345);
	Volume volume(6550);
	Quantity quantity(343);
	float weightCost = getDelivery(weight), volumeCost = getDelivery(volume), quantityCost = getDelivery(quantity);

	cout << fixed << setprecision(2) << "Weight: " << weightCost << endl
		<< "Volume: " << volumeCost << endl
		<< "Quantity: " << quantityCost << endl;
}

// Gets cost of an item using polymorphism
float getCost(const Item &item)
{
	return item.calcCost();
}

// Gets delivery cost of item using polymorphism
float getDelivery(const Item &item)
{
	return item.calcDelivery();
}