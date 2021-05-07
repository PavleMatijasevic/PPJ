#include "kvaternioni.hpp"

Kvaternion::Kvaternion(double s, double i, double j, double k) {
	_s = s;
	_i = i;
	_j = j;
	_k = k;
	_init = DEF_S|DEF_I|DEF_J|DEF_K;
}

Kvaternion::Kvaternion(const Kvaternion& kv) {
	
	_s = kv._s;
	_i = kv._i;
	_j = kv._j;
	_k = kv._k;
	_init = kv._init;
}

void Kvaternion::show(ostream& s) const {
	
	s<<_s;
	if (_i < 0)
		s<<" - ";
	else 
		s<<" + ";
	s<<fabs(_i)<<"i";
	
	if (_j < 0)
		s<<" - ";
	else 
		s<<" + ";
	s<<fabs(_j)<<"j";
	
	if (_k < 0)
		s<<" - ";
	else 
		s<<" + ";
	s<<fabs(_k)<<"k";
}

double Kvaternion::norm() const {
	
	double n = _s*_s + _i*_i + _j*_j + _k*_k;
	
	return sqrt(n);
}

Kvaternion* Kvaternion::operator +(const Kvaternion& kv) const {
	
	Kvaternion* novi = new Kvaternion();
	
	novi->set_s(_s + kv._s);
	novi->set_i(_i + kv._i);
	novi->set_j(_j + kv._j);
	novi->set_i(_k + kv._k);
	
	return novi;
}
Kvaternion* Kvaternion::operator -(const Kvaternion& kv) const {

	Kvaternion* novi = new Kvaternion();
	
	novi->set_s(_s - kv._s);
	novi->set_i(_i - kv._i);
	novi->set_j(_j - kv._j);
	novi->set_i(_k - kv._k);
	
	return novi;
}

Kvaternion* Kvaternion::operator *(const Kvaternion& kv) const {
	
	Kvaternion* novi = new Kvaternion();
	
	novi->set_s(_s + kv._s);
	novi->set_i(_i + kv._i);
	novi->set_j(_j + kv._j);
	novi->set_i(_k + kv._k);
	
	return novi;
}

Kvaternion* Kvaternion::operator /(const Kvaternion& kv) const {
	
	Kvaternion* novi = new Kvaternion();
	
	novi->set_s(_s + kv._s);
	novi->set_i(_i + kv._i);
	novi->set_j(_j + kv._j);
	novi->set_i(_k + kv._k);
	
	return novi;
}

Kvaternion* Kvaternion::operator -() const {
	
	Kvaternion* novi = new Kvaternion();
	
	novi->set_s(-_s);
	novi->set_i(-_i);
	novi->set_j(-_j);
	novi->set_i(-_k);
	
	return novi;
}

bool Kvaternion::set_s(double v) {
	
	if (_init & DEF_S)
		return false;
	
	_s = v;
	_init |= DEF_S;
	
	return true;
}
bool Kvaternion::set_i(double v){
	if (_init & DEF_I)
		return false;
	
	_i = v;
	_init |= DEF_I;
	
	return true;
}
bool Kvaternion::set_j(double v){
	if (_init & DEF_J)
		return false;
	
	_j = v;
	_init |= DEF_J;
	
	return true;
}
bool Kvaternion::set_k(double v){
	if (_init & DEF_K)
		return false;
	
	_k = v;
	_init |= DEF_K;
	
	return true;
}

double Kvaternion::get_s() {
	return _s;
}
double Kvaternion::get_i(){
	return _i;
}
double Kvaternion::get_j(){
	return _j;
}
double Kvaternion::get_k(){
	return _k;
}

bool Kvaternion::dodaj(element_t e) {
	
	if (_init & e.el) {
		return false;
	}
	
	_init |= e.el;
	if (e.el & DEF_S)
		_s = e.v;
	else if (e.el & DEF_I)
		_i = e.v;
	else if (e.el & DEF_J)
		_j = e.v;
	else if (e.el & DEF_K)
		_k = e.v;
		
	return true;
}

ostream& operator <<(ostream& s, const Kvaternion& kv) {
	
	kv.show(s);
	return s;
}