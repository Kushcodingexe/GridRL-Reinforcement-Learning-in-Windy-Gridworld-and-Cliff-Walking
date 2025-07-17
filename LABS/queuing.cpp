#include <iostream>
#include <cmath>
using namespace std;
int main(){
    int clock=0;
    int state=0; 
    int timeToNextCompletion=INT_MAX;
    int timeToNextArrival=0;
    int array[1000];
    while(clock<1000)
{
    timeToNextArrival = rand() % 10 + 1;
    timeToNextCompletion = rand() % 10 + 1;
    
    if(timeToNextArrival<timeToNextCompletion)
    {
        clock+=timeToNextArrival;
        state++;
    }
    else
    {
        clock+=timeToNextCompletion;
        state--;
    }
    array[clock]=state;
}}