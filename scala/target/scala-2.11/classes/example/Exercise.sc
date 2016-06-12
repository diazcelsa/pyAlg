import math.abs

object exercise {
  val tolerance = 0.0001
  def isCloseEnough(x:Double, y:Double) =
    abs((x-y)/x)/x < tolerance
  def fixedPoint(f:Double => Double)(FirstGuess: Double) = {
    def iterate(guess: Double): Double = {
      val next = f(guess)
      if(isCloseEnough(guess,next)) next
      else iterate(next)
    }
    iterate(FirstGuess)
  }
  def fixPointOneOverTwo(FirstGuess: Double) = fixedPoint(x => 1 + x/2)
  fixedPoint(x => 1 + x/2)(1)
  fixPointOneOverTwo(1)
  def sqrt(x:Double) = fixedPoint(y => x/y)(1)
  sqrt(2)
}