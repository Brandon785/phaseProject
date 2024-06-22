
#include "ascent/Ascent.h"
#include <cmath>
#include <iomanip> 
#include <iostream>
//myPhysicsLab
using namespace asc;
struct phaseProfile{
   // x[0] = theta 
   // x[1] = omega w
   // x[2] = Torque
   void operator()(const state_t& x, state_t& xd, const double){
      static constexpr double a = .25; // was .1
      static constexpr double K = 1;
      //static constexpr double T = .5;
      double T = x[2];
      //std::cout<<"T is : "<<T<<std::endl;
      xd[0] = x[1];
      xd[1] = -(a*x[1]) + T - (K*sin(x[0]));
   }
};

int main()
{
   // Adding a third field for Torque
   double T = .5;
   
   //state_t x = { 10.0, 1.0, 1.0 };
   double t = 0.0;
   double dt = 0.01;
   double t_end = 100.0;
   /*
   RK4 integrator;
   phaseProfile system;

   Recorder recorder;
   state_t x = {0,-20,T};
   while (t < t_end)
   {
      recorder({ t, x[0], x[1],x[2] });
      integrator(system, x, t, dt);
   }
   recorder.csv("pendulumT=1", { "t", "theta", "w"});
   */
   
   for(double i = 0;i <= 4;i+=.5 ){
      //state_t x = {0,-20,T};
      RK4 integrator;
      phaseProfile system;

      Recorder recorder;
      t = 0.0;
      T = i;
      std::cout<<"T is: "<<T<<std::endl;
      state_t x = {0,-20,T}; // Theta,Omega
      while (t < t_end)
      {
         recorder({ t, x[0], x[1],x[2] });
         integrator(system, x, t, dt);
      }
      std::ostringstream streamObj;
      streamObj << std::fixed;
      streamObj << std::setprecision(1);
      streamObj << T;
      std::string tValue = streamObj.str();
      std::string pendulumT = "pendulumT=" + tValue;
      recorder.csv(pendulumT, { "t", "theta", "w","torque"});

   }


   return 0;
}