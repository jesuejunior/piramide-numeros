from unittest import TestCase
from main import clear_and_convert_to_int, _get_bigger_path
from main import get_bigger_neighbor

class MainTest(TestCase):
    def test_clear_and_return_list(self):
        data_input = '7 4 13\n'
        output = clear_and_convert_to_int(data_input)
        self.assertEquals(len(output), 3)
        self.assertEquals(output[0], 7)
        self.assertEquals(output[1], 4)
        self.assertEquals(output[2], 13)

    def test_type_is_array(self):
        data_input = '07 47 13\n'
        output = clear_and_convert_to_int(data_input)
        self.assertTrue(isinstance(output, list))

    def test_result_16(self):
        nodes = [[3], [2, 4], [7, 5, 3], [1, 2, 8, 11]]
        result = _get_bigger_path(nodes)
        self.assertEquals(result, 16)

    def test_result_23(self):
        nodes = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
        result = _get_bigger_path(nodes)
        self.assertEquals(result, 23)

    def test_get_neighbor_initial(self):
        input_list = [ 4, 7, 1, 3] #, [ 2, 4, 6]]
        result, index = get_bigger_neighbor(input_list)
        self.assertEquals(result, 7)
        self.assertEquals(index, 1)

    def test_get_neighbor_next_array(self):
        input_list = [ 2, 4, 6]
        result, index = get_bigger_neighbor(input_list, 0 )
        self.assertEquals(result, 4)
        self.assertEquals(index, 1)

    def test_get_neighbor_next_lt(self):
        input_list = [ 7, 4, 6]
        result, index = get_bigger_neighbor(input_list, 1 )
        self.assertEquals(result, 7)
        self.assertEquals(index, 0)

    def test_get_neighbor_lt_3(self):
        input_list = [3, 6]
        result, index = get_bigger_neighbor(input_list, 0 )
        self.assertEquals(result, 6)
        self.assertEquals(index, 1)

    def test_get_neighbor_lt_3_with_index(self):
        input_list = [3, 6]
        result, index = get_bigger_neighbor(input_list, 1 )
        self.assertEquals(result, 6)
        self.assertEquals(index, 1)
