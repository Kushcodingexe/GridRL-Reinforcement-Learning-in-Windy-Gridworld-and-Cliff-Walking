#include <iostream>
#include <cmath>
using namespace std;
int main(){
    int xb,yb;
    int xa=0,ya=0;
    int va=20;
    int vb=sqrt(xb^2+yb^2);
    int t=0;

    cout << "Enter the Initial x and y coordinates of the bomber: ";
    cin >> xb >> yb;
    cout << "Enter the Initial x and y coordinates of the Attacker Plane are : "<< xa <<","<<xb<<endl;
    cout << "Enter the speed of the Attacker Plane: ";
    cin >> va;

    cout << "Initial coordinates of the bomber: xb = " << xb << ", yb = " << yb << endl;

    // Random number generator
    #include <cstdlib>
    #include <ctime>


    while(1){
        t++;
    srand(time(0)); // Seed the random number generator
    int vx = rand() % 10 + 1; // Random x velocity between 1 and 10
    int vy = rand() % 10 + 1; // Random y velocity between 1 and 10

    cout << "Current velocities of the bomber: vx = " << vx << ", vy = " << vy << "t = "<< t << endl;
        xb += vx;
        yb += vy;
    
    int distance = sqrt((xb-xa)^2 + (yb-ya)^2);

    }
    srand(time(0)); // Seed the random number generator
    int vx = rand() % 10 + 1; // Random x velocity between 1 and 10
    int vy = rand() % 10 + 1; // Random y velocity between 1 and 10

    cout << "Initial velocities of the bomber: vx = " << vx << ", vy = " << vy << endl;

    // while (vb > va) {
    //     t++;
    //     vb = sqrt(xb * xb + yb * yb);
    //     xb -= 1;
    //     yb -= 1;
    // }
    // cout << "Time taken to catch the bomber: " << t << " units" << endl;
}