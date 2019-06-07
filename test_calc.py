import unittest
import calc #テストされる側の～.py
 
class TestCalc(unittest.TestCase):

    #　四則演算（＋、－、×、÷）
  def test_add_num(self):
    self.assertEqual(10, calc.add_num(6, 4)) 
 
  def test_sub_num(self):
    self.assertEqual(2, calc.sub_num(6, 4))

  def test_mul_num(self):
    self.assertEqual(24, calc.mul_num(6, 4))

  def test_div_num(self):
    self.assertEqual(1.5, calc.div_num(6, 4))

   # 小数点の四則演算（＋、－、×、÷）
  def test_add_num_float(self):
    self.assertEqual(6, calc.add_num(4.8, 1.2)) 
 
  def test_sub_num_float(self):
    self.assertEqual(3.6, calc.sub_num(4.8, 1.2))

  def test_mul_num_float(self):
    self.assertEqual(5.76, calc.mul_num(4.8, 1.2))

  def test_div_num_float(self):
    self.assertEqual(4, calc.div_num(4.8, 1.2))
   
   
    # ％機能
  def test_per_num(self):
    self.assertEqual(0.57, calc.per_num(57))
 
    # √機能をもつ。
  def test_sqrt_num(self):
    self.assertEqual(3, calc.sqrt_num(9))