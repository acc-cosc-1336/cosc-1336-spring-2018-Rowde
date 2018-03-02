import unittest
#write the import for function for assignment7 sum_list_values
from assignment7 import sum_list_values

class Test_Assign7(unittest.TestCase):

    def sample_test(self):
        self.assertEqual(1,1)

    #create a test for the sum_list_values function with list elements:
    # bill 23 16 19 22
    def test_sum_list_values_joe_10_15_20_30_40(self):
        self.assertEqual(115, sum_list_values(['joe','10','15','20','30','40']))

    def test_sum_list_values_bill_23_16_19_22(self):
        self.assertEqual(80, sum_list_values(['bill','23','16','19','22']))

    def test_sum_list_values_sue_8_22_17_14_32_17_24_21_2_9_11_17(self):
        self.assertEqual(194, sum_list_values(['sue','8','22','17','14','32','17','24','21','2','9','11','17']))

    def test_sum_list_values_grace_12_28_21_45_26_10(self):
        self.assertEqual(142, sum_list_values(['grace','12','28','21','45','26','10']))

    def test_sum_list_values_john_14_32_25_16_89(self):
        self.assertEqual(176, sum_list_values(['john','14','32','25','16','89']))

unittest.main(verbosity=2)    
