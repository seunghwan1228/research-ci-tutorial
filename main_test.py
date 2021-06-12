import unittest
import main


class MainTest(unittest.TestCase):
    def test_helloworld(self):
        ret = main.helloworld("Test")
        self.assertEqual(ret, "Hellow world! Test!")


if __name__ == "__main__":
    unittest.main()
