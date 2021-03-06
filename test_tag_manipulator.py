from tag_manipulator import TagManipulator

def test_split_empty_string_result_empty_array():
    # arrange
    stringToSplit = ""
    expResult = []
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit)

    # assert
    assert result == expResult

def test_split_comma_empty_string_result_empty_array():
    # arrange
    stringToSplit = ","
    expResult = []
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit)

    # assert
    assert result == expResult

def test_split_one_string_result_array_of_one():
    # arrange
    stringToSplit = "java"
    regex = ","
    expResult = ["java"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)

    # assert
    assert result == expResult

def test_split_one_string_with_white_space_before_result_array_of_one():
    # arrange
    stringToSplit = " java"
    regex = ","
    expResult = ["java"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)

    # assert
    assert result == expResult

def test_split_two_strings_with_white_space_before_second_word_result_array_of_one():
    # arrange
    stringToSplit = "java, python"
    regex = ","
    expResult = ["java", "python"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)

    # assert
    assert result == expResult

def test_split_one_string_with_comma_before_result_array_of_one():
    # arrange
    stringToSplit = ",java"
    regex = ","
    expResult = ["java"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)

    # assert
    assert result == expResult

def test_split_one_string_with_comma_after_result_array_of_one():
    # arrange
    stringToSplit = "java,"
    regex = ","
    expResult = ["java"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)

    # assert
    assert result == expResult

def test_split_more_strings_with_comma_between_result_array_of_two():
    # arrange
    stringToSplit = "java byte code, python"
    regex = ","
    expResult = ["java byte code", "python"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)

    # assert
    assert result == expResult