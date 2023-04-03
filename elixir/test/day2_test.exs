defmodule Day2Test do
  use ExUnit.Case

  test "part 1" do
    assert Day2.solve("../puzzle-input/day2-example-input.txt") == 15
    assert Day2.solve("../puzzle-input/day2-input.txt") == 13_565
  end

  test "part 2" do
    assert Day2Part2.solve("../puzzle-input/day2-example-input.txt") == 12
    assert Day2Part2.solve("../puzzle-input/day2-input.txt") == 12_424
  end
end
