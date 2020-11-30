// Author: Alex Grams
// Allows user to input a time in hours, minutes, and seconds, 
// then outputs the time in both 12-hour and 24-hour format.

#include "pch.h"
#include <iostream>
#include <iomanip>

using namespace std;

class Time
{
private:
	int hours, minutes, seconds;
public:
	Time();
	void setHours(int h);
	void setMinutes(int m);
	void setSeconds(int s);
	void dspTime24();
	void dspTime12();
};

Time::Time()
{

}

void Time::setHours(int h)
{
	hours = h;
}

void Time::setMinutes(int m)
{
	minutes = m;
}

void Time::setSeconds(int s)
{
	seconds = s;
}

// Displays the current time in 24-hour format
void Time::dspTime24()
{
	cout << setfill(' ') << setw(2) << hours << ":" << setw(2) << setfill('0') << minutes << ":" << setw(2) << seconds << endl;
}

// Displays the current time in 12-hour format
void Time::dspTime12()
{
	int tempHours = hours;
	if (hours >= 12)
	{
		if (hours > 12)
			tempHours -= 12;
		cout << setfill(' ') << setw(2) << tempHours << ":" << setw(2) << setfill('0') << minutes << ":" << setw(2) << seconds << " PM" << endl;
		return;
	}
	else if (hours == 0)
	{
		tempHours = 12;
	}
	cout << setfill(' ') << setw(2) << tempHours << ":" << setw(2) << setfill('0') << minutes << ":" << setw(2) << seconds << " AM" << endl;
}

int main()
{
	Time time;
	int input;

	cout << "Enter hours: ";
	cin >> input;
	time.setHours(input);
	cout << "Enter  minutes: ";
	cin >> input;
	time.setMinutes(input);
	cout << "Enter seconds: ";
	cin >> input;
	time.setSeconds(input);

	time.dspTime24();
	time.dspTime12();

	return 0;
}
