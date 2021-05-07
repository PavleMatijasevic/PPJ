#ifndef KVATERNION_HPP
#define KVATERNION_HPP

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>

using namespace std;

#define DEF_S (1)
#define DEF_I (2)
#define DEF_J (4)
#define DEF_K (8)

typedef struct{
	double v;
	char el;
} element_t;

class Kvaternion {
	
	private:
		double _s, _i, _j, _k;
		char _init;
		
	public:
		Kvaternion() {}
		Kvaternion(double s, double i, double j, double k);
		Kvaternion(const Kvaternion& kv);
		
		void show(ostream& s) const;
		
		double norm() const;
		
		Kvaternion* operator +(const Kvaternion& kv) const;
		Kvaternion* operator -(const Kvaternion& kv) const;
		Kvaternion* operator *(const Kvaternion& kv) const;
		Kvaternion* operator /(const Kvaternion& kv) const;
		Kvaternion* operator -() const;
		
		bool set_s(double v);
		bool set_i(double v);
		bool set_j(double v);
		bool set_k(double v);
		
		double get_s();
		double get_i();
		double get_j();
		double get_k();
		
		bool dodaj(element_t e);
};

ostream& operator <<(ostream& s, const Kvaternion& kv);

#endif