object rationals {
  val x = new Rational(1,2)
  val y = new Rational(5,7)
  val z = new Rational(3,2)
  x.denom
  x.numer
  x.sub(y).sub(z)


  class Rational(x: Int, y: Int) {
    def numer = x
    def denom = y
    def add(that: Rational) =
      new Rational(
        numer * that.denom + that.numer * denom, denom * that.denom)
    def neg(that: Rational) =
      new Rational(-that.numer,denom)
    def sub(that: Rational) = add(that.neg)
  }

}