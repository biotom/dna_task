import unittest
import mutations

class TestMutationFunctions(unittest.TestCase):

    def test_insertion(self):
        original_sequence = "atgcctag"
        position_to_insert = 0
        mutated_sequence = mutations.insertion(original_sequence, position_to_insert)
        try:
            self.assertEqual(len(mutated_sequence), len(original_sequence) + 1)
        except AssertionError as e:
            print("mutant sequence: ", mutated_sequence)
            print("original sequence: ", original_sequence)
            print(e)
            self.fail(e)

    def test_insertion(self):
        original_sequence = "atgcctag"
        position_to_delete = 0
        mutated_sequence = mutations.deletion(original_sequence, position_to_delete)
        try:
            self.assertEqual(len(mutated_sequence), len(original_sequence) - 1)
        except AssertionError as e:
            print("mutant sequence: ", mutated_sequence)
            print("original sequence: ", original_sequence)
            print(e)
            self.fail(e)
    
    def test_mismatch(self):
        original_sequence = "atgcctag"
        position_to_mismatch = 0
        mutated_sequence = mutations.mismatch(original_sequence, position_to_mismatch)
        try:
            self.assertEqual(len(mutated_sequence), len(original_sequence))
            self.assertNotEqual(mutated_sequence[position_to_mismatch], original_sequence[position_to_mismatch])
        except AssertionError as e:
            print("mutant sequence: ", mutated_sequence)
            print("original sequence: ", original_sequence)
            print(e)
            self.fail(e)






    # def test_deletion(self):
    #     original_sequence = "atgcctag"
    #     position_to_insert = 4
    #     mutated_sequence = insertion(original_sequence, position_to_insert)
    #     self.assertEqual(mutated_sequence, "atggcctag")

if __name__ == '__main__':
    unittest.main()
